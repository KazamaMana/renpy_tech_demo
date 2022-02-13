# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")

define Mineo = Character("Mineo")
image Mineo neutral = im.Scale("Enomoto Mineo/body (4).png",750,750) 
define Aiji = Character("Aiji")
image Aiji neutral = im.Scale("Yanagi Aiji/body (12).png",750,750) 
# The game starts here.

label start:
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

    show Mineo neutral at center with dissolve

    # Text styling module

    Mineo "This is a demo to showcase the features of Ren'py for future reference, I recommend you to not rush click the text to read, as some effects depend on the speed and such"

    Mineo "So be patient while reading this demo project"

    Mineo "Some descriptions of this features mention coding terms, ask your programming staff for more info or you can read the Ren'Py documentation & tutorial resources"

    Mineo "I'll demonstrate text style first."

    Mineo "The first thing I would like to talk about is the input command, a lot of VNs out there let the player name their character,is good to know it exists"

    Mineo "If I wanted to address the player I only need to define the {b}playername{/b} variable and then call it on the dialogue, do you understand {b}[pov]{/b}?"

    pov "{b}*Nods*{/b}"

    Mineo "Good, now I'll showcase some styling/tags options for the dialogue."

    Mineo "This -normal text-, {b}-Bold Text- {i}-Bold Italic Text-{/i}{/b}, {u}-underlined text-{/u}, all of this are identical to what we use on emails/websites/discord, just a matter of placing double brackets at the start and end of a line."

    Mineo "There is more styles out there, like alpha,{alpha=0.2}This text is barely readable for example.{/alpha}"

    Mineo "{alpha=*0.5}This text is half as opaque as the default{/alpha}, and so on, we do this by using the alpha tag and defining a number between 0.0 and 1.0."

    Mineo "Added to that there's line breaks.{space=30}Which can be used.{space=30}Like this."

    Mineo "There's also this type of break {p}Which can be delivered{p=2.0}Like this"

    Mineo "We can even fine tune these dialogue delivery by using a wait tag,{w} so you only can see this after clicking, {w=3.0}or a determined time."

    Mineo "These wait tags are needed if we need to make the auto option on the dialogue {alpha=0.3}or so it seems{/alpha}"

    Mineo "Colors are used in this way, by adding the same brackets we mentioned before but add a color code like {color=#f00}this,{/color} {color=#fbbd01}we can add more{/color} {color=#08e8de}character to the text.{/color}"

    Mineo "The color should be in #rgb, {i}#rgba, #rrggbb, or #rrggbbaa{/i}, you can use any hexcolor website for checking those values."

    Mineo "Next thing is: speed."

    Mineo "{cps=10}You can dictate the speed of whatever dialogue goes on the screen, perfect for representing people who are taking it's time to talk{/cps}"

    Mineo "{cps=160}or they're full panik trying to explain what the fuck it's going on!{/cps}"
    #Add translation fonts for this part

    #Image manipulation module

    scene bg office with dissolve

    show Aiji neutral at center with dissolve

    Aiji "Ren'py also can manipulate images, you can change their size, position, layer position and special effects for every scene."

    Aiji "We will start with scale and position"

    show Aiji neutral at center

    Aiji "This should be center position"

    show Aiji neutral at left

    Aiji "Left position"

    show Aiji neutral at right

    Aiji "Right position"

    hide Aiji neutral

    Aiji "More specific positions can be determined with the Position method and defininig x & y coordinates"

    Aiji "There's some clever tricks that can be used through this, specially with some plugins"

    show Aiji neutral at center 

    Aiji "For this tech demo we're using ActionEditor, a realtime image manipulation tool for creating animations and translating them into usable code"

    return
