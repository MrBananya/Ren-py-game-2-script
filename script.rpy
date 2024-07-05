 
define Player_name = Character('Казума', color="#c8ffc8")
define Lusius_trader = Character('Люциус', color="#c8ffc8")
define Kurumi_guild_worker = Character('Куруми', color="ff0000")

default tt = Tooltip("")
default tooltip = GetTooltip()


default  SetVariableItemId = 0
default  SelectItem = None

# Координаты 
default  Cell_x_pos = 0
default  Cell_y_pos = 0
default Cell_name_pos = ""
default Player_pos_cell_name = ""
default Player_pos = [8, 6]

default task_read_and_take = 0

# Время
default max_time = 10
default interval_time = 1
default time_start = 1

#Текущий экран
default current_screen = ""
default current_screen_back = ""


# Список предметов в игре 
define global_items_in_the_game = [
        #{"id": 0,      "Имя предмета": "",             "Предмет квестовый?"    "Кол-во": 0,    "Описание": "Нету",                             "Может быть экипирован - can be eqip", "Куда одеть": "голова и др.", "Урон предмета", "Броня предмета"                 "Изображение": "icon/axe.png",          "Вес": 1,5,       "Цена продажи": 1, "Цена покупки" 2  },

        {"id": 1,      "name": "Топор",                "quest_item": False,    "quantity": 1,  "description": "Предмет для рубки дерева",                      "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/axe.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 2  },
        {"id": 2,      "name": "Кирка",                "quest_item": False,    "quantity": 1,  "description": "Предмет для добычи руды",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/pick.png",                       "weight": 1.5,  "sell_price": 1, "buy_price": 2  },
        {"id": 3,      "name": "Цветок лечения",       "quest_item": False,    "quantity": 1,  "description": "Используется для создания исцеляющих снадобий", "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/flower1.png",                    "weight": 0.1,  "sell_price": 1, "buy_price": 2  }, 
        {"id": 4,      "name": "Ухо гоблина",          "quest_item": False,    "quantity": 1,  "description": "Часть тела монстра",                            "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/goblin_ear.png",                 "weight": 0.5,  "sell_price": 1, "buy_price": 2  },
        {"id": 5,      "name": "Пустая бутылка",       "quest_item": False,    "quantity": 1,  "description": "Нужна для готовки зелий",                       "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/empty_bottle.png",               "weight": 0.5,  "sell_price": 1, "buy_price": 2  },
        {"id": 6,      "name": "-----",                 "quest_item": False,    "quantity": 1,  "description": "-----",                                         "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,  "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,         "image": "-----",                        "weight": 1,    "sell_price": 1, "buy_price": 2  },
        {"id": 7,      "name": "-----",                 "quest_item": False,    "quantity": 1,  "description": "-----",                                         "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,  "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,         "image": "-----",                        "weight": 1,    "sell_price": 1, "buy_price": 2  },
        {"id": 8,      "name": "-----",                 "quest_item": False,    "quantity": 1,  "description": "-----",                                         "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,  "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,         "image": "-----",                        "weight": 1,    "sell_price": 1, "buy_price": 2  },
        {"id": 9,      "name": "-----",                 "quest_item": False,    "quantity": 1,  "description": "-----",                                         "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "-----",                        "weight": 1,    "sell_price": 1, "buy_price": 2  },
        
        {"id": 100,    "name": "Одноручный меч",       "quest_item": False,    "quantity": 1,  "description": "Обычный меч",                                   "cbeqiped": True,       "slot": "hand",  "dmg": 5, "arm":0,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,       "image": "icon/body/one_handed_sword.png",        "weight": 3,    "sell_price": 5, "buy_price": 8  },
        {"id": 101,    "name": "Кожаный нагрудник",    "quest_item": False,    "quantity": 1,  "description": "Обычный Кожаный нагрудник",                     "cbeqiped": True,       "slot": "chest", "dmg": 0, "arm":3,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_torso.png",          "weight": 4,    "sell_price": 8, "buy_price": 15  },
        {"id": 102,    "name": "Кожаные штаны",        "quest_item": False,    "quantity": 1,  "description": "Обычные Кожаные штаны",                         "cbeqiped": True,       "slot": "pants", "dmg": 0, "arm":2,   "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_pants.png",          "weight": 3,    "sell_price": 5, "buy_price": 10  },
        {"id": 103,    "name": "Кожаные ботинки",      "quest_item": False,    "quantity": 1,  "description": "Обычные Кожаные ботинки",                       "cbeqiped": True,       "slot": "leg",   "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,        "image": "icon/body/armored_boot.png",           "weight": 2,    "sell_price": 3, "buy_price": 8  },
        {"id": 104,    "name": "Шлем",                 "quest_item": False,    "quantity": 1,  "description": "Обычный Кожаные Шлем",                          "cbeqiped": True,       "slot": "head",  "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,          "image": "icon/body/helmet.png",                 "weight": 1,    "sell_price": 3, "buy_price": 5  },
        {"id": 105,    "name": "Шлем",                 "quest_item": False,    "quantity": 1,  "description": "Обычный Кожаные Шлем",                          "cbeqiped": True,       "slot": "head",  "dmg": 0, "arm":1.5, "may_be_eaten": False, "may_be_drink":False, "food_restoration": 0,           "image": "icon/body/viking_helmet.png",                 "weight": 1,    "sell_price": 3, "buy_price": 5  },
    
        {"id": 201,      "name": "Яблоко",              "quest_item": False,    "quantity": 1,  "description": "Обычное яблоко. Немного утоляет голод",            "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,         "image": "icon/food/apple.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 202,      "name": "Бутылка с водой",     "quest_item": False,    "quantity": 1,  "description": "Обычная бутылка с водой. Немного утоляет жажду",   "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": False, "may_be_drink":True, "food_restoration": 15,       "image": "icon/food/water_bottle.png",                 "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 203,      "name": "Хлеб",                "quest_item": False,    "quantity": 1,  "description": "Обычный хлеб. Немного утоляет голод",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/food/bread.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
        {"id": 204,      "name": "Малое зелье лечения", "quest_item": False,    "quantity": 1,  "description": "Немного востанавливает здоровье",              "cbeqiped": False,      "slot": "none",  "dmg": 0, "arm":0, "may_be_eaten": True, "may_be_drink":False, "food_restoration": 15,          "image": "icon/heal_potion_color.png",                        "weight": 1.5,  "sell_price": 1, "buy_price": 3  },
    
    ]                                                                                                                                                                                                                                                                                                           


label start:
    #show screen time_in_game
    scene bg_2
    call cell_update
    #jump move
    call screen move_screen_city
    return







