
default Player_stats = [1, 0, 10, 5, 1, 50]
# 1 - Уровень
# 2 - Текущее кол-во опыта
# 3 - Нужно опыта для лвл апа
# 4 - Кол-во очков для прокачки
# 5 - Множитель опыта
# 6 - Max уровень игрока

default Player_health = [50, 50]
# 1 - Текущее кол-во здоровья
# 2 - Мах здоровья

default Player_weight = [0, 75]
# 1 - Текущий вес игрока
# 2 - Мах допустимый вес

default Player_stamina = [50, 100]
# 1 - Текущий запас энергии игрока
# 2 - Мах допустимый запас

default Player_mana = [10, 10]
# 1 - Текущий запас маны
# 2 - Мах допустимый запас 

default Player_money = [2,0,0,0]
# 1 - Медная монета
# 2 - Серебрянная 
# 3 - Золотая
# 4 - Платиновая

default Player_satiety_food = [50, 100]
default Player_satiety_water = [50, 100]
# Сытьсть игрока
# 1 - Еда
# 2 - вода

default Player_combat_indicators = [1, 0, 10, 5, 5]
# Показатели боя
# 1 - Урон игрока
# 2 - Броня игрока 
# 3 - Шанс увернуться 
# 4 - Крит шанс
# 5 - Крит урон


default guild_rep = [150, "F"]
# Репутация гильдии = ранг гильдии
# от 0 до 100 F
# от 101 до 200 E
# от 201 до 301 D
# от 301 до 400 C
# от 401 до 500 B
# от 501 до 600 A


# Атрибуты игрока. Сила ловкость и т.д
default player_attribute = [
    {"id": 1, "name": "Сила",           "image": "icon/skills/muscle.png",         "description": "Позволяет таскать больше вещей",                "current_level": 0},
    {"id": 2, "name": "Ловкость",       "image": "icon/skills/sprint.png",         "description": "Увеличивает max количество энергии",          "current_level": 0},
    {"id": 3, "name": "Интелект",       "image": "icon/skills/brain.png",          "description": "Увеличивает количество маны",                   "current_level": 0},
    {"id": 4, "name": "Выживаемость",   "image": "icon/skills/fat.png",            "description": "Увеличивает количество здоровья",               "current_level": 0},
    {"id": 5, "name": "Харизма",        "image": "icon/skills/discussion.png",     "description": "Позволяет быть более убедительным в диалогах",  "current_level": 0},
    {"id": 6, "name": "Удача",          "image": "icon/skills/clover.png",         "description": "Есть шанс что вам повезет",                     "current_level": 0}
]

# Пассивные навыки игрока
default player_passive_skills = [
    {"id":1, "name": "Травничество",    "image": "icon/skills/fruiting.png",    "description": "Влияет на шанс и количество собраных трав", "current_level": 0, "current_level_point": 0, "for_lvlup": 5, "max_lvl": 10},
    {"id":2, "name": "Торговля",        "image": "icon/skills/balance.png",     "description": "Влияет на навык торговли",                  "current_level": 0, "current_level_point": 0, "for_lvlup": 5, "max_lvl": 10},
]

# Инвентарь игрока
default items = [
        {"id": 1,      "name": "Топор",                "quest_item": False,    "quantity": 1,  "description": "Предмет для рубки дерева",                      "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/axe.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 2  },
        {"id": 2,      "name": "Кирка",                "quest_item": False,    "quantity": 1,  "description": "Предмет для добычи руды",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/pick.png",                       "weight": 1.5,  "sell_price": 1, "buy_price": 2  },
        
        {"id": 100,    "name": "Одноручный меч",       "quest_item": False,    "quantity": 2,  "description": "Обычный меч",                                   "cbeqiped": True,       "slot": "hand",  "dmg": 5, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/body/one_handed_sword.png",        "weight": 3,    "sell_price": 5, "buy_price": 8  },
        {"id": 101,    "name": "Кожаный нагрудник",    "quest_item": False,    "quantity": 1,  "description": "Обычный Кожаный нагрудник",                     "cbeqiped": True,       "slot": "chest", "dmg": 0, "arm":3,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_torso.png",          "weight": 4,    "sell_price": 8, "buy_price": 15  },
        {"id": 102,    "name": "Кожаные штаны",        "quest_item": False,    "quantity": 1,  "description": "Обычные Кожаные штаны",                         "cbeqiped": True,       "slot": "pants", "dmg": 0, "arm":2,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_pants.png",          "weight": 3,    "sell_price": 5, "buy_price": 10  },
        {"id": 103,    "name": "Кожаные ботинки",      "quest_item": False,    "quantity": 2,  "description": "Обычные Кожаные ботинки",                       "cbeqiped": True,       "slot": "leg",   "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_boot.png",           "weight": 2,    "sell_price": 3, "buy_price": 8  },
        {"id": 104,    "name": "Шлем",                 "quest_item": False,    "quantity": 2,  "description": "Обычный Кожаные Шлем",                          "cbeqiped": True,       "slot": "head",  "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,          "image": "icon/body/helmet.png",                 "weight": 1,    "sell_price": 3, "buy_price": 5  },
        {"id": 105,    "name": "Шлем с рогами",                 "quest_item": False,    "quantity": 2,  "description": "Обычный Кожаные Шлем. Только с рогами",                          "cbeqiped": True,       "slot": "head",  "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,           "image": "icon/body/viking_helmet.png",                 "weight": 1,    "sell_price": 3, "buy_price": 5  },
    
        {"id": 201,      "name": "Яблоко",              "quest_item": False,    "quantity": 2,  "description": "Обычное яблоко. Немного утоляет голод",            "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,         "image": "icon/food/apple.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 202,      "name": "Бутылка с водой",     "quest_item": False,    "quantity": 5,  "description": "Обычная бутылка с водой. Немного утоляет жажду",   "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": False, "may_be_drink":True, "food_restoration": 15,       "image": "icon/food/water_bottle.png",                 "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 203,      "name": "Хлеб",                "quest_item": False,    "quantity": 5,  "description": "Обычный хлеб. Немного утоляет голод",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/food/bread.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 204,      "name": "Малое зелье лечения", "quest_item": False,    "quantity": 1,  "description": "Немного востанавливает здоровье",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/heal_potion_color.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
    


]

# Экипированные вещи игрока
default player_equiped_items = [

]

# Части тела 
default display_of_equipped_items = [
    {"id": 1,   "slot": "head",  "image": "icon/body/head.png",      "item_equped_now": False },
    {"id": 2,  "slot": "chest",  "image": "icon/body/torso.png",     "item_equped_now": False },
    {"id": 3,   "slot": "hand",  "image": "icon/body/arm.png",        "item_equped_now": False },
    {"id": 4,  "slot": "pants",  "image": "icon/body/trousers.png",  "item_equped_now": False },
    {"id": 5,   "slot": "leg",   "image": "icon/body/legs.png",      "item_equped_now": False },
]

# Для обновление инвентаря----------------------------------------------------------------------------------------------
label update_inventory_weight:
    call tasks_update
    $ tmp_dmg = 0
    $ tmp_arm = 0
    $ total_weight = 0

    python:
        for item in items:
            total_weight += float(item["weight"]) * float(item["quantity"])

        for item2 in player_equiped_items:
            total_weight += float(item2["weight"]) * float(item2["quantity"])

        for item in player_equiped_items:
                tmp_dmg += item["dmg"] 
                tmp_arm += item["arm"]

        if tasks_in_game[1]["quest_progress"] == 1:
            for item in items:
                if item["id"] == 3:
                    tasks_in_game[1]["task_progr_have"] = item["quantity"] 

    $ Player_weight[0] = total_weight
    $ Player_combat_indicators[0] = tmp_dmg + 1
    $ Player_combat_indicators[1] = tmp_arm


    return

# Обновляем инф.ю о ранге ----------------------------------------------------------------------------------------------
label update_guild_rep_label:
    if guild_rep[0] <100:
        $ guild_rep[1] = "F" 
    if 100 < guild_rep[0] < 200:
        $ guild_rep[1] = "E"
    if 200 < guild_rep[0] < 300:
        $ guild_rep[1] = "D"
    if 300 < guild_rep[0] < 400:
        $ guild_rep[1] = "C"
    if 400 < guild_rep[0] < 500:
        $ guild_rep[1] = "B"
    if 500 < guild_rep[0] < 600:
        $ guild_rep[1] = "A"
    if 600 < guild_rep[0]:
        $ guild_rep[1] = "S"
    return
    #call screen backpack_screen


# Для обновления при переходе в рюкзак----------------------------------------------------------------------------------------------
label update_inventory_weight2:
    show screen backpack_screen
    call update_inventory_weight
    call screen backpack_screen

# Для удаления обновление инф.----------------------------------------------------------------------------------------------
label action_item_menu_screen_label:
    show screen backpack_screen
    call screen action_item_menu_screen

# Удаление предмета----------------------------------------------------------------------------------------------
label action_item_menu:
    show screen backpack_screen
    python:
        for item in items:
            if item["id"] == SetVariableItemId:
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    items.remove(item)
    call update_inventory_weight
    call screen backpack_screen



# Экипирование предмета----------------------------------------------------------------------------------------------
label action_equiped_item:
    show screen backpack_screen
    python:
        for item in items:
            if item["id"] == SetVariableItemId:
                if item["cbeqiped"] == True:
                    for item2 in display_of_equipped_items:
                        if item2["item_equped_now"] == False:
                            if item["slot"] == item2["slot"]:
                                item2["item_equped_now"] = True
                                if item["quantity"] > 1:
                                    item["quantity"] -= 1
                                    player_equiped_items.append(item)
                                else:
                                    player_equiped_items.append(item)
                                    items.remove(item)
                        #if item2["item_equped_now"] == False:
                            #if 

                else:
                    renpy.say("","Нельзя одеть", interact=True)
                    break

    call update_inventory_weight
    call screen backpack_screen   


label action_remove_equiped_item_menu_screen_label:
    show screen backpack_screen
    call screen takeoff_equiped_item_screen

# При снятии предмета----------------------------------------------------------------------------------------------
label action_remove_equiped_item:
    show screen backpack_screen
    python:
        for equiped_item in player_equiped_items:
            if equiped_item["id"] == SetVariableItemId:
                for player_item in items:
                    if player_item["id"] == equiped_item["id"]:
                        for item3 in display_of_equipped_items:
                            if equiped_item["slot"] == item3["slot"]:
                                item3["item_equped_now"] = False
                        if player_item["quantity"] >= 1:
                            player_item["quantity"] += 1
                        else:
                            items.append(equiped_item)
                        player_equiped_items.remove(equiped_item)
                        break  # Выходим из цикла после удаления
                else:
                    for item3 in display_of_equipped_items:
                        if equiped_item["slot"] == item3["slot"]:
                            item3["item_equped_now"] = False
                    items.append(equiped_item)
                    player_equiped_items.remove(equiped_item)
                
                        

    call update_inventory_weight
    call screen backpack_screen


# Обновление текущего кол-ва навыков----------------------------------------------------------------------------------------------
label update_skills_label:
    python:
        for skill in player_passive_skills:
            if skill["current_level_point"] >= skill["for_lvlup"]:
                skill["current_level"] += 1
                skill["current_level_point"] = 0
                skill["for_lvlup"] += 5
        if Player_stats[1] >= Player_stats[2]:
            Player_stats[0] += 1
            Player_stats[1] = 0
            Player_stats[2] += 5
            Player_stats[3] += 1

        discount = player_passive_skills[1]["current_level"] // 5
        for item in trader_items:
            #item["sell_price"] = max(1, trader_items_default[item["id"] - 1]["sell_price"] + discount)
            item["buy_price"] = item["buy_price"] - discount

    return

# Съедание еды ----------------------------------------------------------------------------------------------------------
label eat_food:
    python:
        for item in items:
            if item["id"] == SetVariableItemId:
                if item["may_be_eaten"] == True:
                    if item["id"] == 204:
                        Player_health[0] += 15
                        if Player_health[0] > Player_health[1]:
                            Player_health[0] = Player_health[1]
                    else:
                        Player_satiety_food[0] += item["food_restoration"]
                        if Player_satiety_food[0] > Player_satiety_food[1]:
                            Player_satiety_food[0] = Player_satiety_food[1]

                if item["may_be_drink"] == True:
                    Player_satiety_water[0] += item["food_restoration"]
                    if Player_satiety_water[0] > Player_satiety_water[1]:
                        Player_satiety_water[0] = Player_satiety_water[1]

                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    items.remove(item)
    call update_inventory_weight
    call screen backpack_screen 


# Показывет кнопку для удаления и экипировки предмета----------------------------------------------------------------------------------------------
screen action_item_menu_screen:
    if current_screen == "backpack_screen":
        for item in items:
            if item["id"] == SetVariableItemId:
                #text "%i" %item["id"] xpos 500 ypos 500
                add im.Scale(item["image"], 100, 100) xpos 200 ypos 800
                text "%s" %item["name"] xpos 300 ypos 800
                text "%s" %item["description"] xpos 300 ypos 840
                if item["cbeqiped"] == True:
                    text "Урон %.1f" %item["dmg"] xpos 310 ypos 880
                    text "Броня %.1f" %item["arm"] xpos 500 ypos 880

                hbox xalign 0.1 yalign 0.12 spacing 5:
                    textbutton "{color=#262829}{size=32} Выбросить  {/size}{/color}" xpos 0 ypos 800:
                        action Jump("action_item_menu")
                    
                    if item["cbeqiped"] == True:
                        textbutton "{color=#262829}{size=32} Экипировать  {/size}{/color}" xpos 0 ypos 800:
                            action Jump("action_equiped_item")
                    if item["may_be_eaten"] == True or item["may_be_drink"] == True:
                        textbutton "{color=#262829}{size=32} Съесть  {/size}{/color}" xpos 0 ypos 800:
                            action Jump("eat_food")


# Показывет кнопку для снятия вещей----------------------------------------------------------------------------------------------
screen takeoff_equiped_item_screen:
    for item in player_equiped_items:
        if item["id"] == SetVariableItemId:
            #text "%i" %item["id"] xpos 500 ypos 500
            add im.Scale(item["image"], 100, 100) xpos 200 ypos 800
            text "%s" %item["name"] xpos 300 ypos 800
            text "%s" %item["description"] xpos 300 ypos 840
            if item["cbeqiped"] == True:
                text "Урон %.1f" %item["dmg"] xpos 310 ypos 880
                text "Броня %.1f" %item["arm"] xpos 500 ypos 880

    hbox xalign 0.1 yalign 0.12 spacing 5:
        textbutton "{color=#262829}{size=32} Снять  {/size}{/color}" xpos 0 ypos 800:
            action Jump("action_remove_equiped_item")


# Здоровье ----------------------------------------------------------------------------------------------
screen healthbar_screen(xpos=140, ypos=800, xsize=300, ysize=40, show_text=True):
    zorder 10
    bar:
        xsize xsize
        ysize ysize
        xpos xpos
        ypos ypos
        value AnimatedValue(value = Player_health[0], range = Player_health[1], delay = 1)
        left_bar Frame("gui/bar/left_healthbar.png", 10,10)
        right_bar Frame("gui/bar/right_healthbar.png",10,10)
    if show_text == True:
        text "{size=30}{color=#000000}%i / %i {/color}{/size}"% (int(Player_health[0]), int(Player_health[1])) xpos xpos ypos ypos 

# Стамина\энергия ----------------------------------------------------------------------------------------------
screen staminabar_screen(xpos=140, ypos=850, xsize=300, ysize=40, show_text=True):
    zorder 10
    bar:
        xsize xsize
        ysize ysize
        xpos xpos
        ypos ypos
        value AnimatedValue(value = Player_stamina[0], range = Player_stamina[1], delay = 1)
        left_bar Frame("gui/bar/left_staminabar.png", 10,10)
        right_bar Frame("gui/bar/right_staminabar.png",10,10)
    if show_text == True:
        text "{size=30}{color=#000000} %i / [Player_stamina[1]] {/color}{/size}" %Player_stamina[0] xpos xpos ypos ypos

# Мана ----------------------------------------------------------------------------------------------
screen manabar_screen(xpos=140, ypos=900, xsize=300, ysize=40, show_text=True):
    zorder 10
    bar:
        xsize xsize
        ysize ysize
        xpos xpos
        ypos ypos
        value AnimatedValue(value = Player_mana[0], range = Player_mana[1], delay = 1)
        left_bar Frame("gui/bar/left_manabar.png", 10,10)
        right_bar Frame("gui/bar/right_manabar.png",10,10)
    if show_text == True:
        text "{size=30}{color=#000000}[Player_mana[0]] / [Player_mana[1]] {/color}{/size}" xpos xpos ypos ypos

# голод -------------------------------------------------------------------------------------------------
screen foodbar_screen(xpos=140, ypos=900, xsize=300, ysize=40, show_text=True):
    zorder 10
    bar:
        xsize xsize
        ysize ysize
        xpos xpos
        ypos ypos
        value AnimatedValue(value = Player_satiety_food[0], range = Player_satiety_food[1], delay = 1)
        left_bar Frame("gui/bar/left_foodbar.png", 10,10)
        right_bar Frame("gui/bar/right_foodbar.png",10,10)
    if show_text == True:
        text "{size=20}{color=#000000}[Player_satiety_food[0]] / [Player_satiety_food[1]] {/color}{/size}" xpos xpos ypos ypos 

# жажда -------------------------------------------------------------------------------------------------
screen waterbar_screen(xpos=140, ypos=900, xsize=300, ysize=40, show_text=True):
    zorder 10
    bar:
        xsize xsize
        ysize ysize
        xpos xpos
        ypos ypos
        value AnimatedValue(value = Player_satiety_water[0], range = Player_satiety_water[1], delay = 1)
        left_bar Frame("gui/bar/left_waterbar.png", 10,10)
        right_bar Frame("gui/bar/right_waterbar.png",10,10)
    if show_text == True:
        text "{size=20}{color=#000000}[Player_satiety_water[0]] / [Player_satiety_water[1]] {/color}{/size}" xpos xpos ypos ypos 

screen view_stats:
    use healthbar_screen
    use staminabar_screen
    use manabar_screen
    use foodbar_screen
    use waterbar_screen


#Показ денег ----------------------------------------------------------------------------------------------
screen coin_screen:
    vbox xpos 0.9 spacing 1:
        hbox :
            add im.Scale("icon/copper_coin.png", 45,45)
            text "{color=#FFFFFF}{size=30} %s  {/size}{/color}" % Player_money[0]  
        hbox:
            add im.Scale("icon/silver_coin.png", 45,45)
            text "{color=#FFFFFF}{size=30} %s  {/size}{/color}" % Player_money[1]
        hbox:
            add im.Scale("icon/gold_coin.png", 45,45)
            text "{color=#FFFFFF}{size=30} %s  {/size}{/color}" % Player_money[2]
        hbox:
            add im.Scale("icon/platina_coin.png", 45,45)
            text "{color=#FFFFFF}{size=30} %s  {/size}{/color}" % Player_money[3]

# Скилы ---------------------------------------------------------------------------------------------
label skill_info_screen_label:
    show screen backpack_screen
    call screen skill_info_screen

screen skill_info_screen:
    if current_screen == "Character_creen": 
        add im.Alpha(im.Scale('gui/frame.png', 1000, 100), 0.5) xalign 0.5 yalign 0.9 
        for skill in player_attribute:
            if skill["id"] == SetVariableItemId:
                text "%s" %skill["name"] xalign 0.5 yalign 0.85
                text "%s" %skill["description"] xalign 0.5 yalign 0.9

label skill_increas:
    python:
        for skill in player_attribute:
            if skill["id"] == SetVariableItemId:
                skill["current_level"] += 1
                Player_stats[3] -= 1

                if skill["name"] == "Сила":
                    Player_weight[1] += 5
                if skill["name"] == "Интелект":
                    Player_mana[1] += 1
                if skill["name"] == "Выживаемость":
                    Player_health[1] += 10
                if skill["name"] == "Ловкость":
                    Player_stamina[1] += 5


    call screen backpack_screen

# Показ инвентаря игрока ----------------------------------------------------------------------------------------------
screen backpack_screen:
    imagemap:
        idle "backpack_bg"

    # Показ инвентаря  
    if current_screen == "backpack_screen":
        imagemap:
            idle 'backpack_bg'
            if Player_weight[0] >= Player_weight[1]:
                text "Текущий вес \n{color=#910725}{size=30}%.1f / %i {/size}{/color} перевес" %(Player_weight[0], Player_weight[1]) xpos 25 ypos 110
            else:
                text "Текущий вес \n{color=#262829}{size=30}%.1f / %i {/size}{/color} " %(Player_weight[0], Player_weight[1]) xpos 25 ypos 110
            #text "{size=40}{color=#0f1b4d} %s {/color}{/size}" %  tt.value xpos 500 ypos 500
        
        imagebutton:
            idle im.Scale('icon/go_back.png', 100, 100) 
            hover im.Alpha(im.Scale('icon/go_back.png', 100, 100), 0.5)
            action Hide("backpack_screen"), Hide("action_item_menu_screen"), Jump('screen_in_city_jump_from_back')  #hovered tt.action("Назад")

        # Экипировать, выкинуть предмет
        vbox xalign 0.15 yalign 0.3 spacing 5:
            for i in range(0, len(items), 8):
                hbox:
                    for item in items[i:i+8]:
                        imagebutton:
                            idle im.Scale(item["image"], 100, 100)
                            hover im.Alpha(im.Scale(item["image"], 100, 100),0.5)
                            action SetVariable("SetVariableItemId", item["id"]), Jump("action_item_menu_screen_label")  #hovered tt.action(SetVariableItemId) 

                        text "{color=#262829}{size=24}%i {/size}{/color}" %item['quantity'] xpos -100 ypos 0
                        text "{color=#262829}{size=24}%.1f  {/size}{/color}" %item["weight"] xpos -50 ypos 80


        # Показ экипированых предметов  
        vbox xalign 0.1 yalign 0.28 spacing 5:
            for slot_info in display_of_equipped_items:
                if slot_info["item_equped_now"] == True:
                    for item in player_equiped_items:
                        if slot_info["slot"] == item["slot"]:
                            imagebutton:
                                idle im.Scale(item["image"], 100, 100) xpos 1500 ypos 200
                                hover im.Alpha(im.Scale(item["image"], 100, 100),0.5)
                                action SetVariable("SetVariableItemId", item["id"]), Jump("action_remove_equiped_item_menu_screen_label")  #hovered tt.action(SetVariableItemId)
                else:
                    add im.Alpha(im.Scale(slot_info["image"], 100, 100), 0.5) xpos 1500 ypos 200
        
        use coin_screen

    #Список заданий
    if current_screen == "task_screen":
        imagemap:
            idle 'backpack_bg'

        vbox xalign 0.10 yalign 0.1 spacing 5:
            text "{color=#FFFFFF}{size=30}Текущий список заданий {/size}{/color}"
        vbox xalign 0.15 yalign 0.3 spacing 5:
            for task in tasks_in_game:
                if task["quest_progress"] == 1:
                    text "{color=#FFFFFF}{size=30}%s {/size}{/color}" %task["name"]

                if task["quest_progress"] == 1:
                    if (task["task_progr_have"] != task["task_progr_need"]) and task["task_progr_need"] > 1:
                        text "{color=#FFFFFF}{size=30} В процесе %s / %s {/size}{/color}" % (task["task_progr_have"],task["task_progr_need"]) 
                    if (task["task_progr_have"] != task["task_progr_need"]) and task["task_progr_need"] <= 1:
                        text "{color=#FFFFFF}{size=30} В процесе {/size}{/color}"  
                if task["quest_progress"] == 2:
                    text "{color=#FFFFFF}{size=30}%s {/size}{/color}" %task["name"]
                    text "{color=#FFFFFF}{size=30} Выполнено {/size}{/color}" 

        imagebutton:
            idle im.Scale('icon/go_back.png', 100, 100) 
            hover im.Alpha(im.Scale('icon/go_back.png', 100, 100), 0.5)
            action Hide("backpack_screen"), Hide("action_item_menu_screen"), Jump('screen_in_city_jump_from_back')  #hovered tt.action("Назад")

    # Характеристики
    if current_screen == "Character_creen":
        imagemap:
            idle 'backpack_bg'
        vbox xalign 0.10 yalign 0.12 spacing 5:
            hbox spacing 5:
                text "Текущий уровень %i " % Player_stats[0]
                bar:
                    xsize 120  ysize 25
                    xpos 0   ypos 10
                    value AnimatedValue(value = Player_stats[1], range = Player_stats[2])
                    left_bar Frame("gui/bar/left_skillbar.png", 10,10)
                    right_bar Frame("gui/bar/right_skillbar.png",10,10)
            #text "%i"%Player_stats[1]
            text "Кол-во очков для прокачки %i " %Player_stats[3]
            text "Уровень в гильдии %i. Текщий ранг %s" %(guild_rep[0], guild_rep[1])
            text "Текущий урон %i, броня %i" %(Player_combat_indicators[0], Player_combat_indicators[1])

        imagebutton:
            idle im.Scale('icon/go_back.png', 100, 100) 
            hover im.Alpha(im.Scale('icon/go_back.png', 100, 100), 0.5)
            action Hide("backpack_screen"), Hide("action_item_menu_screen"), Jump('screen_in_city_jump_from_back')  #hovered tt.action("Назад")


        vbox xalign 0.8 yalign 0.5 spacing 35:
            for i in range(0, len(player_attribute), 2):
                hbox spacing 35:
                    for skill in player_attribute[i:i+2]:
                        text "%i" %skill["current_level"]
                        imagebutton:
                            idle im.Scale(skill["image"], 100, 100) 
                            hover im.Alpha(im.Scale(skill["image"], 100, 100),0.5)
                            action SetVariable("SetVariableItemId", skill["id"]), Jump("skill_info_screen_label")
                            tooltip "%s" %skill["name"]
                        if Player_stats[3] > 0:
                            textbutton "{color=#ffffff}{size=32} + {/size}{/color}" action SetVariable("SetVariableItemId", skill["id"]), Jump("skill_increas")


        $ tooltip = GetTooltip()
        $ x_mouse_pos, y_mouse_pos = renpy.get_mouse_pos()
        if tooltip:
            text "[tooltip]" xpos x_mouse_pos ypos y_mouse_pos

        use healthbar_screen (xpos=140, ypos=800, xsize=300, ysize=40, show_text=True)
        use staminabar_screen (xpos=140, ypos=850, xsize=300, ysize=40, show_text=True)
        use manabar_screen (xpos=140, ypos=900, xsize=300, ysize=40, show_text=True)
        use foodbar_screen (xpos=140, ypos=950, xsize=150, ysize=20, show_text=True)
        use waterbar_screen (xpos=300, ypos=950, xsize=150, ysize=20, show_text=True)

    # Скилы и пассивки
    if current_screen == "player_skills_screen":
        imagemap:
            idle 'backpack_bg' 

        imagebutton:
            idle im.Scale('icon/go_back.png', 100, 100) 
            hover im.Alpha(im.Scale('icon/go_back.png', 100, 100), 0.5)
            action Hide("backpack_screen"), Hide("action_item_menu_screen"), Jump('screen_in_city_jump_from_back')  #hovered tt.action("Назад")

        vbox xalign 0.10 yalign 0.2 spacing 5:
            for skill in player_passive_skills:
                imagebutton:
                    idle im.Scale(skill["image"], 100, 100)
                    hover im.Alpha(im.Scale(skill["image"], 100, 100),0.5)
                    #action SetVariable("SetVariableItemId", skill["id"]), Jump("action_skill_label")
                text "Текущий уровень %i" %(skill["current_level"])
                bar:
                    xsize 120  ysize 25
                    xpos 0   ypos 0
                    value AnimatedValue(value = skill["current_level_point"], range = skill["for_lvlup"])
                    left_bar Frame("gui/bar/left_skillbar.png", 10,10)
                    right_bar Frame("gui/bar/right_skillbar.png",10,10)
                #text "Текущее кол-во опыта %.1f / Нужно для нового уровня %i" %(skill["current_level_point"], skill["for_lvlup"])

    # Переход между вкладками в польз.интерф.
    hbox xalign 0.3  spacing 25:
            imagebutton:
                idle im.Scale("gui/button/frame4.png", 250, 100) #Характеристики
                action [SetVariable("SetVariableItemId", None), SetVariable("current_screen", "Character_creen"), Call("update_guild_rep_label")]
                hover im.Alpha(im.Scale('gui/button/frame4.png', 250, 100), 0.5)
            imagebutton:
                idle im.Scale("gui/button/frame1.png", 250, 100) #Инветнарь
                action [SetVariable("SetVariableItemId", None), SetVariable("current_screen", "backpack_screen"), Call("update_inventory_weight2")]
                hover im.Alpha(im.Scale('gui/button/frame1.png', 250, 100), 0.5)
            imagebutton:
                idle im.Scale("gui/button/frame2.png", 250, 100) #Задания
                action SetVariable("current_screen", "task_screen")
                hover im.Alpha(im.Scale('gui/button/frame2.png', 250, 100), 0.5)
            imagebutton: 
                idle im.Scale("gui/button/frame3.png", 250, 100) #Навыки
                action SetVariable("current_screen", "player_skills_screen")
                hover im.Alpha(im.Scale('gui/button/frame3.png', 250, 100), 0.5)