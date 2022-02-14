# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")

define mineo = Character("Mineo",image='mineo')
define aiji = Character("Aiji",image='aiji')

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside with fade

    #For image display you can either use at center, left, right tags or at Position and the respective arguments for it



    show mineo neutralopensoft with dissolve:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    # Text styling module

    mineo "This is a demo to showcase the features of Ren'py for future reference, I recommend you to not rush click the text to read, as some effects depend on the speed and such" #SCENE 01

    mineo "So be patient while reading this demo project"

    mineo "Some descriptions of this features mention coding terms, ask your programming staff for more info or you can read the Ren'Py documentation & tutorial resources"

    mineo "I'll demonstrate text style first."

    mineo "The first thing I would like to talk about is the input command, a lot of VNs out there let the player name their character,is good to know it exists"

    mineo "If I wanted to address the player I only need to define the {b}playername{/b} variable and then call it on the dialogue, do you understand {b}[pov]{/b}?"

    pov "{b}*Nods*{/b}"

    mineo "Good, now I'll showcase some styling/tags options for the dialogue."

    mineo "This -normal text-, {b}-Bold Text- {i}-Bold Italic Text-{/i}{/b}, {u}-underlined text-{/u}, all of this are identical to what we use on emails/websites/discord, just a matter of placing double brackets at the start and end of a line."

    mineo "There is more styles out there, like alpha,{alpha=0.2}This text is barely readable for example.{/alpha}"

    mineo "{alpha=*0.5}This text is half as opaque as the default{/alpha}, and so on, we do this by using the alpha tag and defining a number between 0.0 and 1.0."

    mineo "Added to that there's line breaks.{space=30}Which can be used.{space=30}Like this."

    mineo "There's also this type of break {p}Which can be delivered{p=2.0}Like this"

    mineo "We can even fine tune these dialogue delivery by using a wait tag,{w} so you only can see this after clicking, {w=3.0}or a determined time."

    mineo "These wait tags are needed if we need to make the auto option on the dialogue {alpha=0.3}or so it seems{/alpha}"

    mineo "Colors are used in this way, by adding the same brackets we mentioned before but add a color code like {color=#f00}this,{/color} {color=#fbbd01}we can add more{/color} {color=#08e8de}character to the text.{/color}"

    mineo "The color should be in #rgb, {i}#rgba, #rrggbb, or #rrggbbaa{/i}, you can use any hexcolor website for checking those values."

    mineo "Next thing is: speed."

    mineo "{cps=10}You can dictate the speed of whatever dialogue goes on the screen, perfect for representing people who are taking it's time to talk{/cps}"

    mineo "{cps=160}or they're full panik trying to explain what the fuck it's going on!{/cps}"
    #Add translation fonts for this part

    #Image manipulation module

    scene bg office with dissolve

    show aiji closedeyes with dissolve:
        subpixel True 
        zoom 0.7
        xpos 270
        ypos 12

    aiji "Ren'py also can manipulate images, you can change their size, position, layer position and special effects for every scene."  #SCENE 02

    aiji "We will start with scale and position"

    show aiji closedeyeseyebrowup at center

    aiji "This should be center position"

    show aiji closedeyeseyebrowup at left

    aiji "Left position"

    show aiji closedeyeseyebrowup at right

    aiji "Right position"

    aiji "More specific positions can be determined with the Position method and defining x & y coordinates"

    hide aiji 

    show mineo neutral2 with dissolve:
        subpixel True 
        zoom 0.7
        xpos 90
        ypos 12

    mineo "Of course you can display several characters and non-character images on the screen by using the {u}show{/u} method, depending on the order of the code, the last show method on the code will be over everyone elseon the screen"


    window auto hide
    show aiji smirk:
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

    aiji "This code snippet show that mineo was called first on the script, and then aiji, by default it means aiji will display over mineo on the screen"


    return
