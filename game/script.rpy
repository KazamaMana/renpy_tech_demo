# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
default hidden_story=False

define pov = Character("[povname]")

define mineo = Character("Mineo",image='mineo',color="#e06666")
define aiji = Character("Aiji",image='aiji',color="#999999")

# The game starts here.

label start:
    camera:
        perspective True
    #command prompt to ask the player's name 
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Kindred"
    pov "My name is [povname]!"

    scene bg outside with fade

    show mineo neutralopensoft with dissolve:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    # Text styling module

    mineo "This is a demo to showcase the features of Ren'py for future reference, I recommend you to not speed through this demo, as some effects depend on the wait times and such"
    mineo "So be patient while reading this demo project"
    mineo "Some descriptions of this features mention coding terms, ask your programming staff for more info or you can read the Ren'Py documentation & tutorial resources"
    mineo "What do you wanna learn?"

    hide mineo 
    show mineo neutralopensoft:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.7)*SaturationMatrix(0.7)*BrightnessMatrix(-0.2)*HueMatrix(0.0)

    menu:
        "Text style":
            jump text_styles
        "Image manipulation":
            jump image_manipulation
        "Music and sfx":
            jump audio_sfx
        "Translation features":
            jump translation_feature
        "Menus and choosing options":
            jump menu_options

label text_styles:
    window auto hide
    scene bg classroom with dissolve
    pause
    "Text style:"
    show mineo neutralclosedeyes:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    mineo "The first thing I would like to talk about is the input command, a lot of VNs out there let the player name their character,is good to know it exists"
    mineo "If I wanted to address the player I only need to define the {b}playername{/b} variable and then call it on the dialogue, do you understand {b}[pov]{/b}?"

    hide mineo 
    show mineo neutralopensoft:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.7)*SaturationMatrix(0.7)*BrightnessMatrix(-0.2)*HueMatrix(0.0)

    pov "{b}*Nods*{/b}"

    hide mineo
    show mineo neutralopensoft:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    mineo "Good, now I'll showcase some styling/tags options for the dialogue."

    mineo "This -normal text-, {b}-Bold Text- {i}-Bold Italic Text-{/i}{/b}, {u}-underlined text-{/u}, all of this are identical to what we use on emails/websites/discord, just a matter of placing double brackets at the start and end of a line."
    mineo "There is more styles out there, like alpha,{alpha=0.2}This text is barely readable for example.{/alpha}"
    mineo "{alpha=*0.5}This text is half as opaque as the default{/alpha}, and so on, we do this by using the alpha tag and defining a number between 0.0 and 1.0."
    mineo "Added to that there's line breaks.{space=30}Which can be used.{space=30}Like this."
    mineo "There's also this type of break {p}Which can be delivered{p=2.0}Like this"
    mineo "We can even fine tune these dialogue delivery by using a wait tag,{w} so you only can see this after clicking(and wait for it, don't click now), {w=3.0}or a determined time."
    mineo "These wait tags are needed if we need to make the auto option on the dialogue {alpha=0.3}or so it seems{/alpha}"
    mineo "Colors are used in this way, by adding the same brackets we mentioned before but add a color code like {color=#f00}this,{/color} {color=#fbbd01}we can add more{/color} {color=#08e8de}character to the text.{/color}"
    mineo "The color should be in #rgb, {i}#rgba, #rrggbb, or #rrggbbaa{/i}, you can use any hexcolor website for checking those values."
    mineo "Same thing for names on the dialogue, you can see my name on the text windows has an specific color"
    mineo "Next thing is: speed."
    mineo "{cps=10}You can dictate the speed of whatever dialogue goes on the screen, perfect for representing people who are taking it's time to talk{/cps}"
    mineo "{cps=160}or they're full panik trying to explain what the fuck it's going on!{/cps}"
    #Add translation fonts for this part
    mineo "What do you wanna learn now?"
    hide mineo 
    show mineo neutralopensoft:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.7)*SaturationMatrix(0.7)*BrightnessMatrix(-0.2)*HueMatrix(0.0)

    #Image manipulation module
    menu:
        "Can you explain me this again?":
            mineo "Sure thing"
            jump text_styles
        "Image manipulation":
            jump image_manipulation
        "Music and sfx":
            jump audio_sfx
        "Translation features":
            jump translation_feature
        "Menus and choosing options":
            jump menu_options

label image_manipulation:
    window auto hide
    scene bg office with dissolve
    pause
    show aiji closedeyes with dissolve:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12

    aiji "On Ren'py you can change the image's size, position, display order and special effects,{w} on this instance we're using the action editor to streamline the work, so think of image manipulation as timeline with keys, just like a video editor"  #SCENE 02
    aiji "We will start with default positions"

    show aiji closedeyeseyebrowup at center

    aiji "This should be center position"

    show aiji closedeyeseyebrowup at left

    aiji "Left position"

    show aiji closedeyeseyebrowup at right

    aiji "Right position"
    aiji "More specific positions can be determined with the Position method and defining x & y coordinates, scale goes the same way so there's no much to explain on that regard"

    hide aiji 

    show mineo neutral2 with dissolve:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    mineo "Of course you can display several characters and non-character images on the screen by using the {u}show{/u} method, the code will display them in the screen just like they were described in the code"
    aiji "What if you wanna overlap characters then and swap display when talking?"

    window auto hide
    show aiji smirk behind mineo:
        subpixel True 
        zoom 0.7
        parallel:
            xpos 600 
            linear 0.3 xpos 600 
            linear 0.9 xpos 240 
        parallel:
            alpha 0.0 
            linear 0.3 alpha 1.0 
    with Pause(1.2)
    show aiji smirk:
        xpos 240
        alpha 1.0
    window auto show

    show code_sample_1 with dissolve:
        subpixel True 
        pos (0.63, 0.17)

    aiji "This code snippet can let us know that aiji was displayed in the script but respecting the behind argument despite being called later"

    hide code_sample_1
    hide aiji

    show aiji smirk:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    show code_sample_2 with dissolve:
        subpixel True
        zoom 1.5
        pos (0.63, 0.17)

    mineo "By calling aiji again on the script but without the behind word on his statement, it displays on top of it now"

    mineo "This could be used to focus on one character from a group while they are talking"

    hide mineo 
    hide code_sample_2
    show aiji closedeyes with dissolve:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12
    aiji "With basic position figured out, we can move to the rest of the image manipulation features"

    window auto hide
    show aiji concernedopenmouth:
        subpixel True 
        xpos 270 
        linear 0.5 xpos 600 
    with Pause(0.5)
    show aiji concernedopenmouth:
        xpos 600
    window auto show

    mineo "Image movement across the screen can be used to represent character movement across an scene, this can be in any direction and with any desirable speed"

    show mineo neutral2:
        subpixel True 
        xzoom 1.0
        zoom 0.9
        parallel:
            ypos 666 
            linear 0.4 ypos -60 
        parallel:
            alpha 0.4 
            linear 0.4 alpha 1.0 
    with Pause(0.4)
    show mineo neutral2:
        ypos -60
        alpha 1.0
    window auto show

    mineo "Simulating getting closer to the main pov (by telling the sprite to move vertically and scaling up it's size)."

    hide aiji
    show aiji closedeyeseyebrowup:
        default subpixel True 
        ypos 1.0
        zoom 0.7
        parallel:
            xpos 0.75 
            linear 0.45 xpos 1.2 
        parallel:
            alpha 1.0 
            linear 0.47 alpha 0.5 
    with Pause(0.50)
    show aiji closedeyeseyebrowup:
        pos (1.2, 1.0)
        alpha 0.5
    window auto show

    aiji "Leaving the scene."

    image blink:
        "yanagi aiji/aiji closedeyes.png"
        0.05
        "yanagi aiji/aiji concerned.png"
        5.0
        repeat

    show blink:
        subpixel True 
        zoom 0.7
        xpos 580
        ypos 12

    aiji "Cycling over sprites to simulate blinking behavior (wait for it), etc"

    hide mineo
    show mineo nikoniko:
        subpixel True 
        ypos -60
        xpos 0
        zoom 0.9

    mineo "Background images do have their own set of effects as well, native to the ren'py engine for classic visual novel effects"

    hide mineo
    hide aiji 
    hide blink

    show bg hallway with fade

    "Fade effect"

    show bg office with dissolve

    "Dissolve effect"

    show bg outside with pixellate

    "Pixellate effect, this one can be fine tuned even more for speed and transition behavior"

    show bg stairs with blinds

    "Blinds effect"

    show bg train with squares

    "Squares in effect"

    show bg cabin with wipeleft

    "Wipe effect (can be up, down, left and right)"

    show bg outside with pushright

    "Push away effect (can be up, down, left and right)"

    show bg hallway with slideawayleft

    "Slide effect (can be up, down, left and right)"

    show bg office with irisin

    "Iris effect (either IN or OUT)"

    show aiji surprisedmouthagape:
        subpixel True 
        ypos -60
        xpos 0
        zoom 0.9

    show bg office with vpunch

    "Shaking backgrounds are also available, to add dramatism in a high tension moment"

    show bg office with hpunch

    "They can either shake horizontally or vertically (mind you, to avoid displaying blank space behind the screen, the background image should be a little bigger than the intended game resolution)"

    hide aiji 

    "What do you wanna learn now?"
    menu:        
        "Can you explain me this again?":
            aiji "Sure thing"
            jump image_manipulation
        "Text style":
            jump text_styles
        "Music and sfx":
            jump audio_sfx
        "Translation features":
            jump translation_feature
        "Menus and choosing options":
            jump menu_options

label audio_sfx:
    window auto hide
    scene bg sunset with fade
    pause
    show mineo neutral2 with dissolve:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12
    
    mineo "Music on the ren'py engine can be easily compared to a group of audio channels of any music mixer software,{w} every channel do have their specific purposes although."
    mineo "Ren'py natively allows you to play music, sounds and voices simultaneously,{w} let me try explaining the available options for every each of them and how can we also define our own."

    play music "audio/05. Tanteitachi No Kyusoku.mp3" volume 0.3 fadeout 2.0 fadein 2.0

    mineo "Hear something?"
    python:
        track = renpy.music.get_playing()

    mineo "If you hear this track ([track]), we successfully told ren'py to play such track right now, using the music channel."

    play sound "audio/neighborhood.mp3" volume 0.7 fadein 1.0 fadeout 1.0

    mineo "What about some ambience?"

    hide mineo
    show mineo smilingclosedeyes:
        subpixel True 
        xpos 270
        zoom 0.7
        ypos 12
    pause
    hide mineo
    show mineo smile:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12

    mineo "Now it feels like I'm in actual neighborhood, right?"

    voice "audio/enomoto_1.ogg" 

    mineo "And an audible voice?"
    mineo "For obvious reasons there's no fully voiced lines for this Tech demo, but we managed to slap some simple words to decorate the dialogue for this module"

    hide mineo
    show mineo lookingawayblush2:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12
    voice "audio/enomoto_4.ogg"
    mineo "Sorry"
    hide mineo
    show mineo concernedclosedeyes:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12

    mineo "Anyway, going back to the music, if not given any special instruction it will naturally play the song again"
    window auto hide
    show mineo neutral2:
        subpixel True 
        xpos 270 
        linear 0.4 xpos 0 
    show code_sample_3 with dissolve:
        subpixel True crop_relative True 
        pos (0.45, 0.54)
        crop (0.3, 0.0, 1.0, 1.0)
    with Pause(0.4)
    show mineo neutral2:
        xpos 0
    window auto show
    mineo "But in this case we're telling ren'py to play the song with a 2 seconds fade in, 2 seconds fade out, and it's playing at a 20 percent volume" 
    
    hide code_sample_3

    mineo "In general aspects, ren'py can do the following with audio:{p}Several layers of audio?(even more the ones I mentioned): Check{p}Can we loop music?: Check{p}Play portions of an audio?: Check{p}Queue Audio?:Check"
    "What do you wanna learn now?"
    show mineo neutral2:
        subpixel True 
        xpos 270 
        xpos 0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.7)*SaturationMatrix(0.7)*BrightnessMatrix(-0.2)*HueMatrix(0.0)
    menu:        
        "Can you explain me this again?":
            mineo "No problem"
            jump audio_sfx
        "Text style":
            jump text_styles
        "Image manipulation":
            jump image_manipulation
        "Translation features":
            jump translation_feature
        "Menus and choosing options":
            jump menu_options

label menu_options:
    scene bg stairs with fade
    "In-game menus and story choices"
    show aiji eyebrowupclosedmouth with dissolve:
        subpixel True
        zoom 0.7

    aiji "Allowing a story to branch mostly relies in-game menus, and we're in good luck because ren'py's way to build an option menu is very straightforward (kinda)"
    aiji "But to allow us to understand how this works, I need to set some context on how Ren'py divides acts"

    show code_sample_4 with dissolve:
        subpixel True 
        pos (0.65, 0.17)

    aiji "Ren'py uses {i}labels{/i} to contain an a portion of the story, we can create as much labels per needed branches into the story we are telling."
    hide aiji
    show code_sample_5 with dissolve:
        subpixel True 
        pos (0.3, 0.17)

    aiji "When we tell ren'py we're making the player choose a path, we're actually making him {i}jump{/i} between labels"
    aiji "But what if you want to unlock certain branches of the story through conditions?{p}Let's try this:"
    hide code_sample_4
    hide code_sample_5

    menu hidden_path_activate:
        "???":
            $ hidden_story=True
            aiji "Now, wait for it"
        "Nothing happens":
            aiji "Nothing will happen indeed, you gotta pick the {b}???{/b}, you can click back on the options down below or keep going as you will be sent to the module menu."

    if hidden_story==True:
        aiji "Something should have happened now then"
        jump menu_options_2
    else:
        "What do you wanna learn now?"
        menu:        
            "Can you explain me this again?":
                aiji "No problem"
                jump menu_options
            "Text style":
                jump text_styles
            "Image manipulation":
                jump image_manipulation
            "Translation features":
                jump translation_feature
            "Audio and sfx":
                jump audio_sfx

label translation_feature:
    return

label menu_options_2:
    show aiji eyebrowupclosedmouth with dissolve:
        subpixel True
        zoom 0.7
    aiji "If you explored both options, you'll realize that actually {b}???{/b} unlocked something different, let's try breaking down what went through this process"
    show code_sample_6 with dissolve:
        subpixel True 
        pos (0.62, 0.04)
        zoom 1.50
    aiji "First, we need to tell ren'py there's a condition the player needs to meet in order to unlock an specific branch of the story"

    show code_sample_7 with dissolve:
        subpixel True 
        pos (0.59, 0.17)
        zoom 1.34

    aiji "Then we present the player the option to meet it, of course the player doesn't know, what you see on the menu it's only the text between quotes"

    show code_sample_8 with dissolve:
        subpixel True 
        pos (0.47, 0.49)
        zoom 1.19

    aiji "If the player successfully selected that option, the condition has been met and the player will continue through the branch as we wanted."
    aiji "What we did was very basic for now as I wanted to show you the direct consequence of meeting a requirement, we can accumulate any number of conditions to unlock a branch in reality"
    hide code_sample_6
    hide code_sample_7
    hide code_sample_8

    show code_sample_9 with dissolve:
        subpixel True 
        pos (0.58, 0.15)
        zoom 1.58
    show code_sample_10 with dissolve:
        subpixel True 
        pos (0.49, 0.4)
        zoom 1.36

    aiji "And these conditions can be anything that we can think for a story, increasing the affection of characters or asking if the player has items on their inventory"
    show aiji troubled with dissolve:
        subpixel True
        zoom 0.7
    aiji "These terms might a little more difficult to absorb so don't hesitate to ask staff for clarification."
    "What do you wanna learn now?"
    show aiji eyebrowupclosedmouth:
        subpixel True
        zoom 0.7
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.7)*SaturationMatrix(0.7)*BrightnessMatrix(-0.2)*HueMatrix(0.0)
    menu:        
        "Can you explain me this again?":
            aiji "Sure thing"
            jump menu_options
        "Text style":
            jump text_styles
        "Image manipulation":
            jump image_manipulation
        "Translation features":
            jump translation_feature
        "Audio and sfx":
            jump audio_sfx