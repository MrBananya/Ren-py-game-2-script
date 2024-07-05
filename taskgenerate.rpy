
image guild_worker = Movie(play="guild/guild_work_anim.webm", size = (1920,1080), channel = "movie")


default tasks_in_game = [
    #{"id": 0, "quest_progress": 0, "name": "Задание на зачистку подземелья", 
    #"reward": 2, "task_progr_need": 1, "task_progr_have": 0,         "show_task": True, 
    #"image": "guild/task.png", 
    #"explanation": "Требуеться авантюрист для зачистки подземелья.", 
    #"guild_master_expl": ["Нужно зачистить одно подземелье.", "Думаю у тебя хватит ума открыть карту и найти помеченое место."]},

    {"id": 1, "quest_progress": 0, "name": "Задание на поиск лечебной травы", 
    "reward": 12, "task_progr_need": 10, "task_progr_have": 0,       "show_task": True, 
    "image": "guild/task.png",
     "explanation": "Требуеться авантюрист для поиска и сбора лечебной травы. Эти травы пойдут на создание лечебных снадобий.",
     "guild_master_expl": ["Найди немного лечебной травы в лесу и просто приниси ее.", "И да, в лесу могут быть монстры."]},

    #{"id": 2, "quest_progress": 0, "name": "Задание на работу в шахте", 
    #"reward": 2, "task_progr_need": 1, "task_progr_have": 0,             "show_task": True, 
    #"image": "guild/task.png",
    #"explanation": "Требуеться авантюрист для работы в шахте.",
    #"guild_master_expl": ["Недалеко от города есть шахта в которой идет добыча разных руд.", "Из-за монстров в последнее время рабочих поубавилось. Метка будет на карте."]},

    #{"id": 3, "quest_progress": 0, "name": "Задание на добычу дерева", 
    #"reward": 2, "task_progr_need": 1, "task_progr_have": 0,              "show_task": True, 
    #"image": "guild/task.png",
    #"explanation": "Требуеться авантюрист для рубки дерева.",
    #"guild_master_expl": ["Тяжело быть лесорубом в месте где полно монстров.", "Просто пойди в лес и наруби дерева."]},

    {"id": 4, "quest_progress": 0, "name": "Задание на поиск домашнего животного", 
    "reward": 2, "task_progr_need": 1, "task_progr_have": 0,  "show_task": True, 
    "image": "guild/task.png",
     "explanation": "Потерялось домашнее животное. Требуеться помощь по его поиску",
     "guild_master_expl": ["Очередное задание по поиску животного. И ты решил его взять? Тебе действительно нечем заняться.", "Попробуй поискать в городе. Не думаю что ручное животное могло убежать далеко."]},

    {"id": 5, "quest_progress": 0, "name": "Задание на доставку", 
    "reward": 2, "task_progr_need": 1, "task_progr_have": 0,                   "show_task": True, 
    "image": "guild/task.png",
     "explanation": "Требуеться авантюрист для доставки сообщения.",
     "guild_master_expl": ["Тут рядом есть магазин Люциуса.", "Просто принеси ему это. И лучше не задавай лишних вопросов."]},

]
# quest_progress - прогресс по заданию 0 - Задание не взято/не активно. 1 - задание взято. 2 - задание выполнено.
# reward - награда за задание
# task_progr_need и task_progr_have. Сколько нужно сделать дел для выполнения задания


# Показ заданий
label task_board_label_1:
    #call show_task_on_board
    call screen task_board_screen

# Поговорить с гильдиео о задании
label talk_task_guild:
    scene guild_work_anim
    scene guild_worker
    menu:
        "Спросить о задании":
            jump ask_about_task
        "Сдать задание":
            jump complete_task
        "Ничего":
            call screen move_screen_guild

# Спросить про задание--------------------------------------------------------------------------------------------------------------------
label ask_about_task:
    python:
        ask_options = []
        for task in tasks_in_game:
            if task["quest_progress"] == 1:
                ask_options.append((task["name"], task))
        ask_options.append(("Назад", "back"))
        result = renpy.display_menu(ask_options, interact=True)

    if result == "back":
        jump talk_task_guild
    else:
        $ selected_task = result
        $ renpy.say(Player_name, f'Хочу спросить про "{selected_task["name"]}"', interact=True)
        scene gw2 with dissolve
        pause (0.5)
        scene gw5 with dissolve
        $ renpy.say(Kurumi_guild_worker, f'{selected_task["guild_master_expl"][0]}', interact=True)
        $ renpy.say(Kurumi_guild_worker, f'{selected_task["guild_master_expl"][1]}', interact=True)
        $ renpy.say(Kurumi_guild_worker, f'А теперь позволь мне вернуться к моей работе', interact=True)
        scene gw1 with dissolve
        jump talk_task_guild

# Сдать задание--------------------------------------------------------------------------------------------------------------------
label complete_task:
    call tasks_update
    python:
        complete_options = []
        for task in tasks_in_game:
            if task["quest_progress"] == 2:
                complete_options.append((task["name"], task))
        complete_options.append(("Назад", "back"))
        result = renpy.display_menu(complete_options, interact=True)
    
    if result == "back":
        jump talk_task_guild
    else:
        $ selected_task = result
        $ renpy.say(Player_name, f'Хочу сдать "{selected_task["name"]}"', interact=True)
        $ renpy.say(Kurumi_guild_worker, f'Молодец. Вот награда, а теперь с глаз долой.', interact=True)

        $ item_for_task = list(filter(lambda item: item['id'] == 3, items))
        if selected_task["id"] == 1:
            if item_for_task[0]["quantity"] >= selected_task["task_progr_need"]:
                $ item_for_task[0]["quantity"] -= selected_task["task_progr_need"]

        $ selected_task["quest_progress"] = 0  # Обновляем состояние задания
        $ Player_money[0] += selected_task["reward"]
        $ guild_rep[0] += 1
        $ renpy.notify("Задание выполнено. Rep +1. Деньги +" +str(selected_task["reward"])) 
        jump talk_task_guild

# Задание на поиск домашнего животного--------------------------------------------------------------------------------------------------------------------
label cat_task:
    $ filtered_tasks = list(filter(lambda task: task['id'] == 4, tasks_in_game))
    $ filtered_tasks[0]["quest_progress"] = 2
    call screen move_screen_city

# Обновление инф. о текущем задании--------------------------------------------------------------------------------------------------------------------
label tasks_update:
    $ filtered_tasks = list(filter(lambda task: task['id'] == 1, tasks_in_game))
    python:
        for item in items:
            if item["id"] == 3:
                filtered_tasks[0]["task_progr_have"] = item["quantity"]
    if filtered_tasks[0]["quest_progress"] != 0:
        if filtered_tasks[0]["task_progr_need"] <= filtered_tasks[0]["task_progr_have"]:
            $ filtered_tasks[0]["quest_progress"] = 2
        else:
            $ filtered_tasks[0]["quest_progress"] = 1
    return


# Показ доски с заданиями в гильдии--------------------------------------------------------------------------------------------------------------------
screen task_board_screen:
    imagemap:
        idle 'task_board'

    imagebutton:
        idle im.Scale('icon/go_back.png', 75, 75) 
        hover im.Alpha(im.Scale('icon/go_back.png', 75, 75), 0.5)
        action  Jump('move_screen_guild_back')  #hovered tt.action("Назад")

    vbox xalign 0.4 yalign 0.3 spacing 30:
        for i in range(0, len(tasks_in_game), 5):
            hbox spacing 30:
                for task in tasks_in_game[i:i+5]:
                    if task["show_task"] == True and task["quest_progress"] == 0:
                        imagebutton:
                            idle im.Scale(task["image"], 150, 200)
                            action SetVariable("task_read_and_take", task["id"]), Jump("task_board_label_2")  
                            hover im.Alpha(im.Scale('guild/task.png', 150, 200), 0.5) 

label task_board_label_2:
    show screen task_board_screen
    call screen task_description

# Показ описания задания--------------------------------------------------------------------------------------------------------------------
screen task_description:
    add im.Alpha(im.Scale('gui/frame.png', 600, 1061), 0.5) xpos 1300 ypos 8 

    for task in tasks_in_game:
        if task["id"] == task_read_and_take:
            text "{color=#FFFFFF}{size=40} %s  {/size}{/color}" % task["name"] xpos 1350 ypos 50 xmaximum 500 
            text "{color=#FFFFFF}{size=32} %s  {/size}{/color}" % task["explanation"] xpos 1350 ypos 300 xmaximum 500

    textbutton "{color=#FFFFFF}{size=32} Принять задание  {/size}{/color}" xpos 1400 ypos 800:
        action Jump("task_update_label")


# Берем задание. Ставим quest_progress = 1 значит что задание взято и находится в стадии выполнения. show_task что задание не отображается на доске
label task_update_label:
    python:
        for task in tasks_in_game:
            if task["id"] == task_read_and_take:
                task["quest_progress"] = 1
                task["show_task"] = False
    call screen task_board_screen



label move_screen_guild_back:
    hide screen task_description
    hide screen task_board_screen
    call screen move_screen_guild


