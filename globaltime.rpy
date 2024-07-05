###
#screen time_in_game:
#    timer 1 repeat True action If(interval_time < max_time, 
#        true=SetVariable('interval_time', interval_time + 1), 
#        false=SetVariable('interval_time', 1))
#    text "%s" %interval_time xpos 0 ypos 44
###

# определения переменных для счета времени/даты

default Year = 6035
default Mouth = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
                    "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
default MouthDays = [31, 28,31,30,31,30,31,31,30,31,30,31]
default MouthDaysNum = 3 # Номер месяца Mouth[MouthDaysNum] или MouthDays[MouthDaysNum]
default WeekDays = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Восресенье"]
default WeekDayNumber = 0 # Номер недели
default Days = 1 # Какой сечайс день
default Hours = 6 # сколько часов
default Minutes = 30 # сколько минут
default MinutesStr = "%d" % Minutes # полсьл вывод в виде 12:00 например. Иначе было бы 12:0
default Totaly_Days = 0 # Сколько прошло в сумме дней


label time_counter:
    # Считаем минуты
    if Minutes >= 60:
        $ Minutes -= 60
        $ Hours += 1

    if Minutes < 10:
        $ MinutesStr = "0%d" % Minutes
    else:
        $ MinutesStr = "%d" % Minutes

    if Hours > 23:
        $ Hours = 0
        $ Days += 1
        $ WeekDayNumber += 1
        $ Totaly_Days += 1 # Подсчет сколько дней всего прошло

        # Сбрасываем вещи торговца к дефолтным
        $ trader_items = []
        python:
            for item in trader_items_default:
                new_shop_item = {
                        "id": item["id"],
                        "name": item["name"],
                        "quest_item": item["quest_item"],
                        "quantity": item["quantity"],
                        "description": item["description"],
                        "cbeqiped": item["cbeqiped"],
                        "slot": item["slot"],
                        "dmg": item["dmg"],
                        "arm": item["arm"],
                        "image": item["image"],
                        "weight": item["weight"],
                        "sell_price": item["sell_price"],
                        "buy_price": item["buy_price"]
                    }
                trader_items.append(new_shop_item)

        # Обнавляем задания
        call new_task_generate


    if WeekDayNumber > 6:
        $ WeekDayNumber = 0
        if Days > MouthDays[MouthDaysNum]:
            $ MouthDaysNum += 1
            $ Days = 1
        if MouthDaysNum > 11:
            $ MouthDaysNum = 0
            $ Year += 1
        if Minutes < 10:
            $ MinutesStr = "0%d" % Minutes
        else:
            $ MinutesStr = "%d" % Minutes
    return

# Обновление заданий 
label new_task_generate:
    $tmp_task = 0
    python:
        for task in tasks_in_game:
            if task["show_task"] or task["quest_progress"] == 1:
                tmp_task +=1
    $ tmp = renpy.random.randint(0, len(tasks_in_game) - 1)
    if tasks_in_game[tmp]["show_task"] == False and tasks_in_game[tmp]["quest_progress"] == 0:
        $ tasks_in_game[tmp]["show_task"] = True
        return
    else:
        if tmp_task == len(tasks_in_game):
            return
        else:
            call new_task_generate

# Отдых персонажа
label player_rest_label: 
    $ Player_health[0] += 1
    $ Player_stamina[0] += 10

    if Player_satiety_food[0] <= 0:
        python:
            renpy.notify("Вам срочно нужно попить или поесть")
        $ Player_health[0] -= 1
        if Player_health[0] <= 0:
            jump player_death 
    else:
        $ Player_satiety_food[0] -= 1

    if Player_satiety_water[0] <=0:
        python:
            renpy.notify("Вам срочно нужно попить или поесть")
        $ Player_health[0] -= 1
        if Player_health[0] <= 0:
            jump player_death 
    else:
        $ Player_satiety_water[0] -= 1


    if Player_health[0] > Player_health[1]:
        $ Player_health[0] = Player_health[1]
    if  Player_stamina[0] > Player_stamina[1]:
        $ Player_stamina[0] = Player_stamina[1]
    $ Hours += 1
    call time_counter
    jump screen_in_city_jump