# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Loki")
define I = Character("Abel")
define t = Character("Chase")
define y = Character("Jordan")
define l = Character("Joe", color="c8a2c8")
define d = Character("Dean Withers", color="8b0000")

# The game starts here.

label start: 
    scene bedroom at truecenter:
        zoom 6
    show loki
    play music "newproj.mp3" fadein 1
    #she gets up from bed (draw that)
    "Loki" "I don't want to get up for school today"
    "Loki" "But Abel has been bothering me to come to debate club."

    scene house at truecenter:
        zoom 3
    show loki
    "Loki" "MOM! WHERE'S MY LAPTOP!"
    "Mom" "Idk girl"
    show loki:
        xzoom -1.0
    "bruh"

    scene schoolfront at truecenter:
        zoom 2
    show loki at right
    "Loki" "Is that abe-"

    show abel at truecenter:
        xoffset -90
    "Abel" "Hey Loki are you finally coming to debate club today?"
    "Loki" "Yea.."
    "Loki" "Why do you want to know?"
    show loki disgusted at right
    "Loki" "Are you coming??"
    show abel worried
    "Abel" "Why?"
    "Loki" "Because uhhh"
    "Loki" "Nevermind!"
    "Abel" "See you there then."
    #cuts to after school
    scene cassclass at truecenter:
        zoom 5.5
        yoffset -400
    show loki at left
    show abel at right
    "Loki"  "About time you pulled up homie me and the boys have been debating if water is wet"
    e " Is water wet?"

    menu:
        "uhh, water is wet":
            e "Good."

    show chase at center:
        xoffset -250
    show joe at center:
        xoffset -500
    show jordan at center:
        xoffset 500

    I "Well anyways say hello to my little friends Chase, Jordan and Joe"
    t "*puts on headphones*"
    y "Do you even lift bruh"
    l "What are you even doing here this is supposed to be bois only"
    I "Chill Joe before I get Joe mama"
    l "Whatever it's not like I care anyways"

    show dean withers at center:
        xoffset 150
        yoffset -50

    d "OKAY CLASS TODAY WE ARE GOING TO BE DEBATING, AND WE ARE GOING TO DEBATE IF LUFFY OR NARUTO WOULD WIN IN A FIGHT"
    y "Glances at loki"
    I "Bro youre saying that outloud"

    show loki disgusted

    y "Oh crap I'm sorry Loki. Can I take you to the gym later I lift 225"
    e "Fine."
    e "Meet me at La Fitness at 8 and don't forget to bring money for my guest pass"
    #cuts to an empty La Fitness
    scene lafitness:
        zoom 2
    show jordan at left
    y "Wow I've never seen the gym so empty"
    y "There aren't even workers at the front desk"
    show loki at right
    e "Hi Jordan"
    e "Honestly I've never really worked out before but I know you have a lot of experience."
    e "Can you show me how to do bench press?"
    y "Of course, just ask me anything."
    y "I know about a million things when it comes to working out"
    y "*lifts 225lb bar above his chest*"
    show jordan lifting bar
    show loki evil face at right
    y "What's going on..."
    y "The bar's getting heavier"
    y "HELP"
    hide jordan lifting bar
    show bar crushing jordan with fade:
        xoffset -130
        yoffset 400
    e "mwahaha I am actually the escaped subject eleven"
    e "I am"
    e "Evel"
    
    hide bar crushing jordan with fade
    play music "powerup.mp3" fadein 1
    stop music
    show jordan saiyan at truecenter:
        xoffset 0
        yoffset -20
    y "Nah I'D BOUNCE BACK!!!"
    y "So you see, you're not the only subject"
    y "After you escaped, four subjects were tasked with retrieving you"
    y "We've been waiting for you to make a wrong move and you've finally snapped"
    y "One of the doctors you killed in your escape was my father"
    y "There's no debate, you have to pay"
    y "Get em boys"
    show joe at truecenter:
        xoffset -500
        yoffset -20
    show abel at truecenter: 
        xoffset -300
        yoffset -20
    show chase at truecenter:
        xoffset -150
        yoffset -20
    show dean withers at truecenter:
        xoffset 230
        yoffset -70
    t "Okay."





return
