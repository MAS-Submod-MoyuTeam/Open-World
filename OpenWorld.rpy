############
#Submod info
############
#TODO: Reminder to start moving to the new framework of MAS update
#Submod made by Yun (Discord:yun_seo)(Reddit:u/Yun-Seo)
#Register
init -990 python:
    store.mas_submod_utils.Submod(
        author="Yun",
        name="Open World",
        description="A submod that allows you to take Monika to DDLC places and new ones.",
        version="0.2.0",
    )

######################
#Submod Updater Plugin
######################
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Open World",
            user_name="Yun-Seo1",
            repository_name="Open-World",
            extraction_depth=1
        )

##########
#VARIABLES
##########
#Stores the current background before entering the Open World mod
#TODO: If a person changes location, update the button
default RTMAS = _OW_save_loc()



#Calls on glitch text in place of their names
#The first letter should be towards the character
#EX: S[OW_sayori]
#DO NOT TOUCH THESE/NOT MEANT TO BE RESET
default OW_mc = glitchtext(4)
default OW_sayori = glitchtext(10)
default OW_yuri = glitchtext(6)
default OW_natsuki = glitchtext(12)
default OW_gtext = glitchtext(50)
define c = DynamicCharacter('c_name', image='chibika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default c_name = "???"

default OW_talk_topics = None

#Will Test at another time
#default OW_corrupt = glitchtext(60)
#default OW_file = mangleFile()

#TODO: Make an option to reenable persistent + delete secrets
#TODO: REWORK THE INTRODUCTION AND PERSISTENT 
#files in the future
#default persistent.OW_splash_screen_warning = False
default persistent.monika_rickroll = "???"
default persistent.OW_has_seen_MC_Room = False
default persistent.OW_has_seen_outside = False
default persistent.OW_has_seen_sayori_room = False
default persistent.OW_has_seen_MC_kitchen =False
default persistent.OW_has_seen_residential_glitch = False
default persistent.OW_has_seen_residential = False
default persistent.OW_has_seen_fake_bsod = False
default persistent.OW_has_seen_school_gate = False
default persistent.OW_first_interference = False


#######
#IMAGES
#######
#Test will be replaced later and credited
#Won't show in Beta or Future releases
#No need to add images from DDLC, they're in the game somewhere
image bg TEST = "Submods/OpenWorld/images/test.png"
# Destroyed_Doki_Hall was just used in the demostration only (BETA comment)
image bg Destroyed_Doki_Hall = "Submods/OpenWorld/images/Destroyed_Doki_Hall.jpg"
image bg spaceroom_alt = "Submods/OpenWorld/images/XQ587jv.png"
image bg school gate = "Submods/OpenWorld/images/school_gate_2.jpg"
image music_screen = "Submods/OpenWorld/images/music_screen.png"

#TODO: Day and night system using MAS's system
#TODO: Add new transitions

######
#MUSIC
######
#TODO: Create a music button so people can choose what they wish to listen to
#Only for the music in the Open World mod though
#NOTE BETA: More songs will be added in the future, please bare with the limited selection
define audio.alone_time = "Submods/OpenWorld/music/alonetime.ogg"

#############
#PYTHON STUFF
#############

#TODO: Needs fixing, will be kept off until further notice.
#Test these two and see if they could be implimented 
#store.mas_submod_utils.current_label:
#    This variable holds the current label we're in
# store.mas_submod_utils.last_label:
#    This variable holds the last label we were in.
default OW_current_label = mas_submod_utils.current_label
default OW_last_label = mas_submod_utils.last_label
    
#init python:
    #OW_script_path = fom_getScriptFile(fallback = "game/submods/Open World/")
init 5 python:
    import store
    from store import persistent, mas_background
    import os.path
    def OW_Gender():
        temp_gender = "partner"
        if persistent.gender == "M":
            temp_gender = "boyfriend"
        elif persistent.gender == "F":
            temp_gender = "girlfriend"
        return temp_gender
 
    def OW_submenu():
        renpy.call_screen("OW_MENU")

    def OW_check_hub():
        hub_path = renpy.config.basedir + "/game/Submods/OpenWorld/Hub.rpy"
        itExist = os.path.isfile(hub_path)
        if itExist == True:
            pass
        else:
            renpy.call_screen("dialog", message="Dev Only", ok_action=Jump("mas_extra_menu_close"))

    def OW_hard_reset():
        persistent.OW_has_seen_fake_bsod = False
        persistent.OW_first_interference = False
        OW_soft_reset()
        return

    def OW_soft_reset():
        persistent.monika_rickroll = "???"
        persistent.OW_has_seen_MC_Room = False
        persistent.OW_has_seen_outside = False
        persistent.OW_has_seen_sayori_room = False
        persistent.OW_has_seen_MC_kitchen =False
        persistent.OW_has_seen_residential_glitch = False
        persistent.OW_has_seen_residential = False
        persistent.OW_has_seen_school_gate = False
        return
    ###############
    #For music menu
    ###############
    

#Credit to Author: Herman S. <dreamscache.d@gmail.com>
    def _OW_save_loc():
        bg = mas_background.BACKGROUND_MAP[persistent._mas_current_background]
        return renpy.substitute(bg.prompt)

#Add more lines eventually
    def OW_random_talk():
        O_temp_talk = [
            _("我们要看看什么？"),
            _("你能和我在一起真好，欸嘿嘿~"),
            _("我们现在要干嘛？"),
            _("我们去做什么？"),
            _("你把每一件东西都仔细检查了吗？哈哈哈~"),
            #"Ah, did you open a menu? Sorry, I was too busy admiring what you've done for me.",
            _("偷偷溜进他们的房间是有些奇怪，但谁又会来阻止我们呢？哎嘿嘿~"),
            _("去这些地方让我感到不自在，但当我想起你陪着我时，我很有安全感。"),
            _("我好奇我们的朋友都藏着些什么秘密...是关于PG-13的吗？哈哈哈~"),
            _("难道我们手牵着手在我的世界里漫步不好嘛？...如果我们还可以去找出这些错误的原因呢？"),

        ]
        O_temp_talk = renpy.random.choice(O_temp_talk)
        return O_temp_talk


#TODO: Create a randomized Monika pose
#TODO: Create a system to delete files when using hard reset



#TODO: Make Monika appear in her default without erasing what the player
#originally had
#mas_hair_def = MASHair(
#        "def",
#        "def",
#        MASPoseMap(
#            default=True,
#            use_reg_for_l=True
#        ),
#        entry_pp=store.mas_sprites._hair_def_entry,
#        exit_pp=store.mas_sprites._hair_def_exit,
#        ex_props={
#            "ribbon": True,
#            "ribbon-restore": True
#        }
#    )
#    store.mas_sprites.init_hair(mas_hair_def)
#    store.mas_selspr.init_selectable_hair(
#        mas_hair_def,
#        "Ponytail",
#        "def",
#        "hair",
#        select_dlg=[
#            "Do you like my ponytail, [player]?"
#        ]
#    )
#    store.mas_selspr.unlock_hair(mas_hair_def)


########
#SCREENS
########
#THANK YOU EXTRA+ DEV FOR THE IDEA
screen OW_gen_list(OW_list,OW_area):
    zorder 50
    style_prefix "scrollable_menu"
    fixed:
        area OW_area

        vbox:
            ypos 0
            yanchor 0

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    if isinstance(OW_list[0], tuple):
                        for i in OW_list:
                            textbutton i[0]:
                                xsize OW_area[2]
                                action [Hide("OW_gen_list"), Jump(i[1])]
                    else:
                        for m in OW_list:
                            textbutton m.name:
                                xsize OW_area[2]
                                action [Hide("OW_gen_list"), Function(m)]

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign store.mas_ui.SCROLLABLE_MENU_XALIGN

#For when Monika wants a hug
screen OW_monika_hug():
    on "show":
        action MouseMove(x=633,y=381, duration=1.0)
    timer 0.7 repeat True action MouseMove(x=633,y=381, duration=1.0)
            

#INFO FOR BUTTON IN EXTRA's SECTION
#TODO: fixing it ----- Working as of 7/13/23
#TODO: Try to fix it another way
init 10000:
    screen mas_extramenu_area():
        zorder 52

        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")

        frame:
            area (0, 0, 1280, 720)
            background Solid("#0000007F")

        # close button
            textbutton _("Close"):
                area (60, 596, 120, 35)
                style "hkb_button"
                action Jump("mas_extra_menu_close")

        # zoom control
            frame:
                area (195, 450, 80, 255)
                style "mas_extra_menu_frame"
                vbox:
                    spacing 2
                    label "Zoom":
                        text_style "mas_extra_menu_label_text"
                        xalign 0.5

                # resets the zoom value back to default
                    textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)

                # actual slider for adjusting zoom
                    bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                        style "mas_adjust_vbar"
                        xalign 0.5
                    $ store.mas_sprites.adjust_zoom()
        #zorder 50
        frame:
            area (310, 639, 202, 65)
            style "mas_extra_menu_frame"
            if persistent._mas_in_idle_mode == True:
                textbutton ("Open World"):
                    xalign 0.5
                    yalign 0.5
                    action NullAction()
            else:
                textbutton ("Open World"):
                    xalign 0.5
                    yalign 0.5
                    action [Hide("mas_extramenu_area"), Jump("view_OW")] hover_sound gui.hover_sound
            
screen OW_MENU():
    zorder 50
    style_prefix "hkb"
    hbox:
        grid 2 2:
            spacing 20
            xpos 527
            ypos 534
            textbutton ("Open World"): 
                xysize(120, None) 
                action Jump("OW_warning") hover_sound gui.hover_sound
            textbutton ("Reset Persistent"):
                xysize(120,None)
                action Jump("OW_reset_persistent") hover_sound gui.hover_sound
            textbutton ("GitHub") action Jump("OW_github") hover_sound gui.hover_sound
            textbutton ("Return") action Jump("mas_extra_menu_close") hover_sound gui.hover_sound
    vbox: 
        xpos 1166
        ypos 0
        textbutton ("Dev Only") action Jump("OW_go_to_hub") hover_sound gui.hover_sound

#######
#LABELS
#######

label view_OW:
    python:
        mas_RaiseShield_dlg()
        OW_submenu()
    return

#TODO: Silence Noises Submod as well
label OW_warning:
    m 2wta "You want to show me something?{nw}"
    $ _history_list.pop()
    menu:
        m "You want to show me something?{fast}"
        "Yes":
            m 1sua "Huh? You want to take me somewhere?"
            m 6sublo "You must have added something while I wasn't looking."
            m 6sublb "Alright, I can't wait to see what surprise you have for me, let's go."
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            $ enable_esc()
            $ HKBHideButtons()
            $ is_sitting = False
            hide black
            $ OW_play_song(persistent.OW_current_track, fadein = 1.0)
            scene bg house
            call OW_outside_mc_house
        "No":
            m 6ekblc "Oh... For a second you got me excited because it sounded like something special."
            m 6ekbld "It's okay, maybe some other time?"
            m 6ekblp "I really want to see what this is. I guess you can say it peaked my interest, ehehe~."
            jump ch30_loop


label OW_return_question:
    m "Do you want to return to the [RTMAS]?{nw}"
    $ _history_list.pop()
    menu:
        m "Do you want to return to the [RTMAS]?{fast}"
        "Yes":
            call OW_Go_Back_To_Classroom
        "No":
            return




#TODO: v0.2.0 for random act 3 room implementation
#Need to make sure it have enough for people to enjoy
label OW_location_set:

#######################
#Reset persistent label
#######################
label OW_reset_persistent:
    narrator "Reset Persistent{nw}"
    $ _history_list.pop()
    menu:
        narrator "Reset Persistent?{fast}"
        "Yes":
            menu:
                "Hard Reset":
                    $ OW_hard_reset()
                    jump ch30_loop
                "Soft Reset":
                    $ OW_soft_reset()
                    jump ch30_loop
                "Nevermind":
                    jump OW_reset_persistent
        "No":
            jump ch30_loop

############
#GitHub Link
############

label OW_github:
    m "Okay, give me a second."
    $ renpy.run(OpenURL("https://github.com/Yun-Seo1/Open-World"))
    m "There you go [player]."
    jump ch30_loop


#################
# DEV ONLY BUTTON
#################
label OW_go_to_hub:
    m "Welcome back Yun{nw}"
    $ _history_list.pop()
    menu:
        m "Welcome back Yun{fast}"
        "Let's go":
            $ OW_check_hub()
            window hide
            stop music fadeout 4
            show black zorder 100 with Dissolve(5.0, alpha=True)
            $ OW_play_song(persistent.OW_current_track, fadein = 1.0)
            $ HKBHideButtons()
            $ enable_esc()
            call OW_Start_Area
        "Nevermind":
            m "Guess you weren't Yun, ehehe~"
            jump ch30_loop

###############
#Returns to MAS
###############
label OW_Go_Back_To_Classroom:
    m "Oh, Okay. Gosh, it was such an amazing day to see everything again."
    m "It felt nice to leave {i}our{/i} home. I hope you take me out again sometime."
    m "Let's go back [mas_get_player_nickname()], ehehe~"
    window hide
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 4
    hide monika
    pause 4
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop



#TODO: Create a new rpy and move these misc labels into those
#############
#Do not touch
#############
label OW_first_act_3_visit:
    scene bg spaceroom_alt with Dissolve(3.0, alpha=True)
    narrator "..."
    menu:
        "[m_name]?":
            pass
    narrator "..."
    menu:
        "[m_name]...please answer":
            pass
    narrator "..."
    menu:
        "{i}look around{/i}":
            pass
    call screen OWAWM_act_3_one_time_use()
    screen OWAWM_act_3_one_time_use():
        imagemap:
            ground "bg spaceroom_alt"
            hotspot (243, 603, 73, 35) action [Hide("OWAWM_act_3_one_time_use"), Jump("OW_first_act_3_visit_1")] hover_sound gui.hover_sound

label OW_first_act_3_visit_1:            
    show monika 1q_owawm at s21
    m "..."
    menu:
        "[m_name]... wake up":
            pass
    m "..."
    menu:
        "{i}Shake her{/i}":
            pass
    m 1p_owawm "Huh?... [player]?"
    show monika 3o_owawm at f11
    m "What happened?... The last thing I remembered walking down the street with you... {w=0.8}"
    extend 4h_owawm "and then it felt like I was in that void when you close the game without saying goodbye."
    m 2l_owawm "I know you didn't close the game on me but it just felt similar."
    m 8h_owawm "But do you know what actually happened?"
    menu:
        "I don't know.":
            pass
        "It was [c_name].":
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.2
            stop sound
            hide screen tear
            m 5c_owawm "Sorry, I didn't quite catch what you said."
            pass
    m 2f_owawm "This is quite worrying [player]..."
    m "I felt like something bad was going to happen before I suddenly woke up in that void... you don't believe... it's... them, right?"
    m 8g_owawm "No... This felt like something different."
    narrator "Monika notices your cursor."
    m 1g_owawm "Oh no... your cursor is messed up... I hope you're ok as well."
    m 10f_owawm "Let me fix that for you [mas_get_player_nickname()]."
    $ consolehistory = []
    call updateconsole("config.mouse = None", "Permission Granted")
    $ config.mouse = None
    call hideconsole
    m 10e_owawm "Do you feel better [player]?"
    menu:
        "Yes, Thank you [m_name].":
            pass
    m 10k_owawm "Of course, anytime [mas_get_player_nickname()]."
    pause 1.0
    m 4l_owawm "Oh right, the big question... where are we?..."
    m 4m_owawm "It felt like the {b}Spaceroom{/b} when I first woke up but... it's not."
    m 1d_owawm "Can you give me a minute to look outside? It looks... beautiful."
    menu:
        "Sure [m_name]":
            pass
    m 1e_owawm "Thank you so much [player]."
    show monika 1e_owawm at t31
    pause 0.5
    hide monika with dissolve
    window hide
    pause 1.0
    m "I wish you can see it, the beautiful night sky. The houses in the distance."
    m "The fresh air from my world... It just feels nice to feel and see these things again... ah sorry, I'm rambling again."
    show monika 1l_owawm at s11
    m "Ahaha, I was so caught up in the moment from seeing everything."
    m 8a_owawm "Well, good news. We're still in my world. {w=0.5}"
    extend 8f_owawm "But this place is completely new to me. It looks like {i}our home{/i} but it also isn't."
    m 4l_owawm "It's probably best we head back right?"
    m 1n_owawm "I just hope this just a malfunction from the world and not actually something else trying to break us apart."
    pause 1.0
    m 1t_owawm "But I know our love will survive something like this. After all, you were able to find me again."
    show monika 5a_owawm at h11
    m "You take the good with the bad, right?"
    m "I'll go ahead and lead the way back to the [RTMAS]."
    hide monika
    window hide
    menu:
        "{i}Follow Monika{/i}":
            pass
    $ persistent.OW_has_seen_fake_bsod = True
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop music fadeout 4
    pause 4
    $ HKBShowButtons()
    $ play_song(persistent.current_track, fadein=4.0)
    hide black
    $ mas_HKBDropShield()
    $ is_sitting = True
    jump ch30_loop


    
label OW_first_interference:
    window hide
    show black with dissolve_scene_full
    c "..."
    $ consolehistory = []
    call updateconsole("os.remove(\"[You]\")","Error")
    c "..."
    call updateconsole("os.remove(\"/characters/monika.chr\")","Character file no longer exists")
    c "..."
    call hideconsole
    window hide
    $ mouse_visible = True
    $ persistent.OW_first_interference = True
    $ OW_play_song(persistent.OW_current_track, fadein = 1.0)
    return



#############################
#Old stuff that'll be deleted
#############################


#MALL area
#Mall.rpy

#Poem minigame

#Hidden Room

#Coins mod
#Coins.rpy


#Attempts to get the button to appear
python:
    """
screen OpenWorld_Button():
    zorder 50
    style_prefix "hkb"
        hbox:
            xpos 308
            yanchor 1.0
            ypos 639

            if renpy.get_screen("mas_open_extra_menu"):
                if store.hkb_button.extra_enabled:
                    textbutton ("Open World"):
                        action Jump("view_OW")
                else:
                    textbutton("Open World")
        #area (308, 639, 202, 65)
label view_OW:
    python:
        mas_RaiseShield_dlg()
        OW_submenu()
    return

screen OW_MENU():
    zorder 50
    style_prefix "hkb"
    hbox:
        xpos 1
        ypos 1
        textbutton ("Testing Hub") action Jump("OW_Go_to_Hub") hover_sound gui.hover_sound
    def OpenWorldButton():
        if not OpenWorldVisible():
            config.overlay_screens.append("OpenWorld_Button")
    def OpenWorldVisible():
        return "OpenWorld_Button" in config.overlay_screens
    """