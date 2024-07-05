
default trader_items_default = [
    {"id": 1,      "name": "Топор",                "quest_item": False,    "quantity": 1,  "description": "Предмет для рубки дерева",                      "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/axe.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 5  },
    {"id": 2,      "name": "Кирка",                "quest_item": False,    "quantity": 1,  "description": "Предмет для добычи руды",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/pick.png",                       "weight": 1.5,  "sell_price": 1, "buy_price": 5  },
    {"id": 5,      "name": "Пустая бутылка",       "quest_item": False,    "quantity": 1,  "description": "Нужна для готовки зелий",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/empty_bottle.png",               "weight": 0.5,  "sell_price": 1, "buy_price": 10  },
    {"id": 202,      "name": "Бутылка с водой",     "quest_item": False,    "quantity": 1,  "description": "Обычная бутылка с водой. Немного утоляет жажду",   "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": False, "may_be_drink":True, "food_restoration": 15,       "image": "icon/food/water_bottle.png",                 "weight": 1.5,  "sell_price": 1, "buy_price": 15  },
    {"id": 203,      "name": "Хлеб",                "quest_item": False,    "quantity": 1,  "description": "Обычный хлеб. Немного утоляет голод",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/food/bread.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 20  },
    
]

default trader_items = [
    {"id": 1,      "name": "Топор",                "quest_item": False,    "quantity": 1,  "description": "Предмет для рубки дерева",                      "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/axe.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 5  },
    {"id": 2,      "name": "Кирка",                "quest_item": False,    "quantity": 1,  "description": "Предмет для добычи руды",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/pick.png",                       "weight": 1.5,  "sell_price": 1, "buy_price": 5  },
    {"id": 5,      "name": "Пустая бутылка",       "quest_item": False,    "quantity": 1,  "description": "Нужна для готовки зелий",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/empty_bottle.png",               "weight": 0.5,  "sell_price": 1, "buy_price": 10  },
    {"id": 202,      "name": "Бутылка с водой",     "quest_item": False,    "quantity": 1,  "description": "Обычная бутылка с водой. Немного утоляет жажду",   "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": False, "may_be_drink":True, "food_restoration": 15,       "image": "icon/food/water_bottle.png",                 "weight": 1.5,  "sell_price": 1, "buy_price": 15  },
    {"id": 203,      "name": "Хлеб",                "quest_item": False,    "quantity": 1,  "description": "Обычный хлеб. Немного утоляет голод",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/food/bread.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 20  },
              

]

image trader_shop = Movie(play="shop/shop.webm", size = (1920,1080), channel = "movie")

# Прагаем в action_item_menu_screen_buy для показа что купить -------------------------------------------------------------------
label action_item_menu_screen_label_in_shop_buy:
    show screen shop
    call screen action_item_menu_screen_buy

# Прагаем в action_item_menu_screen_sell для показа что продать -------------------------------------------------------------------
label action_item_menu_screen_label_in_shop_sell:
    show screen shop
    call screen action_item_menu_screen_sell


# Продажа в магазине--------------------------------------------------------------------------------------------------------------------------------------
label action_sell_item_menu:
    show screen shop
    python:
        for item in items:
            if item["id"] == SetVariableItemId:
                item_exists_in_shop = False
                # Проверяем, есть ли уже такой предмет в магазине
                for shop_item in trader_items:
                    if shop_item["id"] == SetVariableItemId:
                        # Увеличиваем количество предмета в магазине и обновляем цену
                        shop_item["quantity"] += 1
                        item_exists_in_shop = True
                        break

                # Если предмета нет в магазине, добавляем его
                if not item_exists_in_shop:
                    new_shop_item = {
                        "id": item["id"],
                        "name": item["name"],
                        "quest_item": item["quest_item"],
                        "quantity": 1,
                        "description": item["description"],
                        "cbeqiped": item["cbeqiped"],
                        "slot": item["slot"],
                        "dmg": item["dmg"],
                        "arm": item["arm"],
                        "may_be_eaten": item["may_be_eaten"],
                        "may_be_drink": item["may_be_drink"],
                        "food_restoration": item["food_restoration"],
                        "image": item["image"],
                        "weight": item["weight"],
                        "sell_price": item["sell_price"],
                        "buy_price": item["buy_price"]
                    }
                    trader_items.append(new_shop_item)

                # Уменьшаем количество предметов в инвентаре и добавляем деньги к игроку
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    items.remove(item)
                player_passive_skills[1]["current_level_point"] += 0.5
                Player_stats[1] += 0.1
                Player_money[0] += item["sell_price"]

    call update_skills_label
    call update_inventory_weight
    call screen shop

# Покупка в магазине--------------------------------------------------------------------------------------------------------------------------------------
label action_buy_item_menu:
    show screen shop
    python:
        for item in trader_items:
            if item["id"] == SetVariableItemId:
                if item["buy_price"] > Player_money[0]:
                    renpy.jump(label='if_less_money')
                item_exists = False
                # Проверяем, есть ли уже такой предмет в инвентаре
                for inv_item in items:
                    if inv_item["id"] == SetVariableItemId:
                        # Увеличиваем количество предмета на 1
                        inv_item["quantity"] += 1
                        item_exists = True
                        break
        
                # Если предмета нет в инвентаре, добавляем его
                if not item_exists:
                    new_item = {
                        "id": item["id"],
                        "name": item["name"],
                        "quest_item": item["quest_item"],
                        "quantity": 1,
                        "description": item["description"],
                        "cbeqiped": item["cbeqiped"],
                        "slot": item["slot"],
                        "dmg": item["dmg"],
                        "arm": item["arm"],
                        "may_be_eaten": item["may_be_eaten"],
                        "may_be_drink": item["may_be_drink"],
                        "food_restoration": item["food_restoration"],
                        "image": item["image"],
                        "weight": item["weight"],
                        "sell_price": item["sell_price"],
                        "buy_price": item["buy_price"]
                    }
                    items.append(new_item)

                # Уменьшаем количество предметов в магазине и вычитаем цену из денег игрока
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    trader_items.remove(item)
                player_passive_skills[1]["current_level_point"] += 0.5
                Player_stats[1] += 0.1
                Player_money[0] -= item["buy_price"]

    call update_skills_label
    call update_inventory_weight
    call screen shop

# просто пишет что недостаточно денег)--------------------------------------------------------------------------------------------------------------------------------------
label if_less_money:
    $ renpy.notify("Недостаточно денег для покупки")
    call update_inventory_weight
    call screen shop

# Разговор с торговцем --------------------------------------------------------------------------------------------------------------------------------------
label talk_with_trader:
    scene shop_anim
    scene shop1

    $ filtered_tasks = list(filter(lambda task: task['id'] == 5, tasks_in_game))

    if filtered_tasks[0]["quest_progress"] == 1:
        menu:
            "Как дела в магазине?":
                scene shop2
                Lusius_trader "Все как обычно"
                scene shop1
                jump talk_with_trader
        
            "Доставить посылку":
                scene shop1
                Player_name "У меня тут для тебя посылка есть."
                scene shop2
                Lusius_trader "Спасибо что доставил ее."
                scene shop1
                Player_name "Слушай, зачем тебе доставка если ты находишься рядом с гильдией?"
                scene shop2
                Lusius_trader "Тебе нужны деньги, а мне лень выходить из магазина. Все получают то что хотят."
                scene shop1
                $ filtered_tasks[0]["quest_progress"] = 2
                jump talk_with_trader

            "Ничего":
                $ current_screen = "main_trade_screen"
                hide shop1
                hide shop2
                call screen shop
    else:
        menu:
            "Как дела в магазине?":
                scene shop2
                Lusius_trader "Все как обычно"
                scene shop1
                jump talk_with_trader

            "Ничего":
                $ current_screen = "main_trade_screen"
                hide shop1
                hide shop2
                call screen shop

# Показывет кнопку для продажи предмета--------------------------------------------------------------------------------------------------------------------------------------
screen action_item_menu_screen_sell:
    for item in items:
        if item["id"] == SetVariableItemId:
            add im.Scale(item["image"], 100, 100) xpos 200 ypos 800
            text "%s" %item["name"] xpos 300 ypos 800
            text "%s" %item["description"] xpos 300 ypos 840
            text "Цена продажи %i " %item["sell_price"] xpos 300 ypos 880
            add im.Scale("icon/copper_coin.png", 50, 50) xpos 620 ypos 880

    hbox xalign 0.1 yalign 0.12 :
        textbutton "{color=#262829}{size=32} Продать  {/size}{/color}" xpos 0 ypos 800:
            action Jump("action_sell_item_menu")


# Показывет кнопку для покупки предмета--------------------------------------------------------------------------------------------------------------------------------------
screen action_item_menu_screen_buy:
    for item in trader_items:
        if item["id"] == SetVariableItemId:
            add im.Scale(item["image"], 100, 100) xpos 200 ypos 800
            text "%s" %item["name"] xpos 300 ypos 800
            text "%s" %item["description"] xpos 300 ypos 840
            text "Цена покупки %i " %item["buy_price"] xpos 300 ypos 880
            add im.Scale("icon/copper_coin.png", 50, 50) xpos 620 ypos 880

    hbox xalign 0.9 yalign 0.1 :
        textbutton "{color=#262829}{size=32} Купить  {/size}{/color}" xpos 0 ypos 800:
            action Jump("action_buy_item_menu")


# Магазин--------------------------------------------------------------------------------------------------------------------------------------
screen shop:
    imagemap:
        idle "shop_anim"
    imagemap:
        idle "trader_shop"
        #add im.Alpha(im.Scale('gui/frame.png', 400, 250), 0.5) xpos 1450 ypos 0
        text "{size=32}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=32}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1500 ypos 15

    if current_screen == "move_trade_screen":
        imagebutton:
                idle im.Scale('icon/go_back.png', 75, 75) 
                hover im.Alpha(im.Scale('icon/go_back.png', 75, 75), 0.5)
                action SetVariable("current_screen", "shop"), Jump('screen_in_city_jump')
        transform:
            add im.Alpha(im.Scale("backpack_bg.png", 1600, 900), 0.8) at truecenter 
            add im.Scale("gui/notify.png", 50, 500) xalign 0.5 yalign 0.2

        vbox xalign 0.15 yalign 0.3 spacing 5:
            for i in range(0, len(items), 4):
                hbox:
                    for item in items[i:i+4]:
                        imagebutton:
                            idle im.Scale(item["image"], 100, 100)
                            hover im.Alpha(im.Scale(item["image"], 100, 100),0.5)
                            action SetVariable("SetVariableItemId", item["id"]), Jump("action_item_menu_screen_label_in_shop_sell")  #продать
                        text "{color=#262829}{size=24}%i {/size}{/color}" %item['quantity'] xpos -100 ypos 0
                        text "{color=#262829}{size=24}%.1f  {/size}{/color}" %item["weight"] xpos -50 ypos 80

        vbox xalign 0.82 yalign 0.3 spacing 5:
            for i in range(0, len(trader_items), 4):
                hbox:
                    for item in trader_items[i:i+4]:
                        imagebutton:
                            idle im.Scale(item["image"], 100, 100)
                            hover im.Alpha(im.Scale(item["image"], 100, 100),0.5)
                            action SetVariable("SetVariableItemId", item["id"]), Jump("action_item_menu_screen_label_in_shop_buy")  #купить
                        text "{color=#262829}{size=24}%i {/size}{/color}" %item['quantity'] xpos -100 ypos 0
                        text "{color=#262829}{size=24}%.1f  {/size}{/color}" %item["weight"] xpos -50 ypos 80

        use coin_screen

    if current_screen == "main_trade_screen":
        vbox xalign 0.08 yalign 0.3 spacing 25:
            imagebutton:
                idle im.Scale('gui/button/frame5.png', 250, 100) 
                hover im.Alpha(im.Scale('gui/button/frame5.png', 250, 100), 0.5)
                action SetVariable("current_screen", "move_trade_screen")
            imagebutton:
                idle im.Scale('gui/button/talk_button.png', 250, 100) 
                hover im.Alpha(im.Scale('gui/button/talk_button.png', 250, 100), 0.5)
                action SetVariable("current_screen", "move_trade_screen"), Jump("talk_with_trader")

        hbox spacing 5:
            imagebutton:
                idle im.Scale('icon/go_back.png', 75, 75) 
                hover im.Alpha(im.Scale('icon/go_back.png', 75, 75), 0.5)
                action SetVariable("current_screen", "move_screen_city"), Jump('screen_in_city_jump')  
            imagebutton:
                idle im.Scale('icon/backpack.webp', 85, 85) 
                hover im.Alpha(im.Scale('icon/backpack.webp', 85, 85), 0.5)
                action SetVariable("current_screen", "backpack_screen"), SetVariable("current_screen_back", "shop"), Jump('screen_in_city_jump')
        use coin_screen


            
