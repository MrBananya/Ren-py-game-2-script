
image enemy_attack_goblin = Movie(play="battlescreens/goblin1_attack.webm", size = (1920,1080), channel = "movie")

define enemy_list = [
    {"id": 1, "enemy_name": "гоблин", "enemy_alive": True, "image_life": "battlescreens/goblin1_calm.png", "image_death": "battlescreens/goblin1_death.png", "dmg": 3, "arm": 0, "hp": 25, "max_hp": 25, "id_reward": 4, "xp_reward": 1 },
    {"id": 2, "enemy_name": "гоблин", "enemy_alive": True, "image_life": "battlescreens/goblin1_calm.png", "image_death": "battlescreens/goblin1_death.png", "dmg": 3, "arm": 0, "hp": 25, "max_hp": 25, "id_reward": 4, "xp_reward": 1}

]

default enemy_in_battle = []
default selected_enemy_id = None

#Смерть игрока
label player_death:
    "-Это конец вашего пути.-"
    "-Загрузитесь или смиритесь со своей судьбой.-"
    return

# Перед битвой куда прыгать и кого призывать --------------------------------------------------------------------------------------------------------------------------------------
label before_battle:
    if Player_pos_cell_name == "forest":
        $ new_enemy_1 = {
                    "id": enemy_list[0]["id"],
                    "enemy_name": enemy_list[0]["enemy_name"],
                    "enemy_alive": enemy_list[0]["enemy_alive"],
                    "image_life": enemy_list[0]["image_life"],
                    "image_death": enemy_list[0]["image_death"],
                    "dmg": enemy_list[0]["dmg"],
                    "arm": enemy_list[0]["arm"],
                    "hp": enemy_list[0]["hp"],
                    "max_hp": enemy_list[0]["max_hp"],
                    "id_reward": enemy_list[0]["id_reward"],
                    "xp_reward": enemy_list[0]["xp_reward"]
                    }
        $ enemy_in_battle.append(new_enemy_1)

        $ random_number = renpy.random.random()
        if random_number > 0.2:
            $ new_enemy_2 = {
                "id": enemy_list[1]["id"],
                "enemy_name": enemy_list[1]["enemy_name"],
                "enemy_alive": enemy_list[1]["enemy_alive"],
                "image_life": enemy_list[1]["image_life"],
                "image_death": enemy_list[0]["image_death"],
                "dmg": enemy_list[1]["dmg"],
                "arm": enemy_list[1]["arm"],
                "hp": enemy_list[1]["hp"],
                "max_hp": enemy_list[1]["max_hp"],
                "id_reward": enemy_list[1]["id_reward"],
                "xp_reward": enemy_list[1]["xp_reward"]
            }
            $ enemy_in_battle.append(new_enemy_2)
        show screen battle_forest_screen
        call screen battle_forest_screen 

# Игрок ходит --------------------------------------------------------------------------------------------------------------------------------------
label plyer_attack:
    $ tmp_damage = 0
    $ tmp_death = 0
    python:
        for enemy in enemy_in_battle:
            if enemy["id"] == SetVariableItemId and enemy["enemy_alive"] == True:
                if Player_combat_indicators[0] - enemy["arm"] <= 0:
                        enemy["hp"] -= 1
                        tmp_damage+=1
                        if enemy["hp"] <= 0:
                            enemy["enemy_alive"] = False
                            #renpy.say('', "Враг " +enemy["enemy_name"] +" был побежден", interact=True) 
                            #renpy.jump(label='after_battle')
                else:
                        enemy["hp"] -= (Player_combat_indicators[0] - enemy["arm"])
                        tmp_damage += Player_combat_indicators[0] - enemy["arm"]
                        if enemy["hp"] <= 0:
                            enemy["enemy_alive"] = False
                            #renpy.say('', "Враг " +enemy["enemy_name"] +" был побежден", interact=True) 
                            #renpy.jump(label='after_battle')
        for enemy in enemy_in_battle:
            if enemy["enemy_alive"] == False:
                tmp_death += 1
            if len(enemy_in_battle) == tmp_death:
                renpy.show_screen(_screen_name='battle_forest_screen')
                renpy.say('', "Враги были побеждены", interact=True) 
                renpy.jump(label='after_battle')
                
    $ renpy.notify("Нанесено " +str(tmp_damage) +" урона")
    #$ renpy.pause(0.5)
    $ tmp_damage = 0
    jump enemy_attack

# Враг ходит --------------------------------------------------------------------------------------------------------------------------------------
label enemy_attack:
    $ tmp_damage = 0
    python:
        for enemy in enemy_in_battle:
            if enemy["enemy_alive"] == True:
                if Player_combat_indicators[1] >= enemy["dmg"]:
                    Player_health[0] -= 1
                    tmp_damage +=1
                    #renpy.notify("Получено" +str(1) +" урона")
                else:
                    Player_health[0] -= abs(Player_combat_indicators[1] - enemy["dmg"])
                    tmp_damage += abs(Player_combat_indicators[1] - enemy["dmg"])
                if Player_health[0] <= 0:
                    renpy.say("", "Вы проиграли")
                    renpy.jump(label='player_death')

    $ renpy.notify("Получено " +str(tmp_damage) +" урона")
    $ tmp_damage = 0
    $ selected_enemy_id = None
    call screen battle_forest_screen


# После боя--------------------------------------------------------------------------------------------------------------------------------------
# Игроку дается награда и очищается список противников


label after_battle:
    python:
        for enemy in enemy_in_battle:
            Player_stats[1] += enemy["xp_reward"]
            for reward in global_items_in_the_game:
                if enemy["id_reward"] == reward["id"]:
                    if len(items) == 0:
                        new_item = reward.copy()
                        items.append(new_item)
                        break
                    else:
                        found = False
                        for item in items:
                            if item["id"] == enemy["id_reward"]:
                                item["quantity"] += 1
                                found = True
                        if not found:
                            new_item = reward.copy()
                            items.append(new_item)
            

        #for enemy in enemy_list:
            #enemy["hp"] = enemy["max_hp"]
    $ enemy_in_battle = []
    $ selected_enemy_id = None
    hide screen battle_forest_screen
    call screen globalmap_screen 

# Удрать с поля боя --------------------------------------------------------------------------------------------------------------------------------------
label escape_from_battle:
    show screen battle_forest_screen
    $ tmp = renpy.random.randint(0, 5)
    if tmp == 5:
        $ renpy.notify("Вы успешно убежали")
        $enemy_in_battle = []
        hide screen battle_forest_screen
        $ selected_enemy_id = None
        call screen globalmap_screen 
    else:
        $ renpy.notify("Побег не удался") 
        $ selected_enemy_id = None
        jump enemy_attack
        #call screen battle_forest_screen
    


# Варианты действий во время боя  --------------------------------------------------------------------------------------------------------------------------------------
screen battle_action_screen:
    if Player_health[0] > 0:
        add im.Scale("gui/frame.png", 480,200) xalign 0.9 yalign 1.0
        hbox xalign 0.2 yalign 0.12 spacing 5:
            textbutton "{color=#ffffff}{size=32} Атака  {/size}{/color}" xpos 1000 ypos 800:
                action Jump("plyer_attack")
            textbutton "{color=#ffffff}{size=32} Убежать  {/size}{/color}" xpos 1000 ypos 800:
                action Jump("escape_from_battle")
    else:
        modal False

# сам экран боя --------------------------------------------------------------------------------------------------------------------------------------
screen battle_forest_screen:
    imagemap:
        idle "battle_field1"
    #Знать сколько противников в бою
    #text "Кол-во в бою%s" %len(enemy_in_battle) xpos 100
    hbox xalign 0.5 :
        for enemy in enemy_in_battle:
            #text "Хп врага%i" %enemy["hp"] xpos 600   # Хп врага
            vbox:
                if enemy["enemy_alive"] == True:
                    bar xalign 0.5 ypos 250:
                        xsize 300  ysize 40
                        #xpos 140   ypos 800
                        value AnimatedValue(value = enemy["hp"], range = enemy["max_hp"], delay = 1)
                        left_bar Frame("gui/bar/left_healthbar.png", 10,10)
                        right_bar Frame("gui/bar/right_healthbar.png",10,10)
                        #text "{size=30}{color=#000000}%i / %i {/color}{/size}" % (int(enemy["hp"]), int(enemy["max_hp"]))
                if enemy["enemy_alive"] == True:
                    imagebutton:
                        ypos 250
                        idle im.Scale(enemy["image_life"], 380, 650)
                        hover im.Alpha(im.Scale(enemy["image_life"], 380, 650),0.8)
                        action SetVariable("SetVariableItemId", enemy["id"]), SetVariable("selected_enemy_id", enemy["id"])
                else:
                    imagebutton:
                        ypos 600
                        idle im.Scale(enemy["image_death"], 550, 300) 
                        hover im.Alpha(im.Scale(enemy["image_death"], 550, 300),0.8)
                        #action SetVariable("SetVariableItemId", enemy["id"]), SetVariable("selected_enemy_id", enemy["id"])

    use healthbar_screen 
    #use staminabar_screen
    use manabar_screen
    if selected_enemy_id is not None:
        use battle_action_screen
