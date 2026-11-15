# Declare characters used by this game.
define h = Character(_("hermes"), color="#c87a4a")
define m = Character(_("Me"), color="#b46a72")
define e = Character(_("entity"), color="#4f3f3e")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "instt.wyl"

    scene bg_restaurant:
        xysize(1920,1080)
    with fade
    "It's my first day working at RiveraHerrans Greek Delicacies"

    "The owner, Jorge, seems quite acquainted with Greek culture despite being Puerto-Rican."

    "The taped off play-area seems akin to a siren's call, pulling me towards the dusty ball pit."
    
    show asset_ballpit

    "As I lower myself into the pit, my gut tells me when I resurface I might not appear in the play-area again."

    scene bg_basement:
        xysize(1920,1080)
    with fade
    
    show asset_crate

    "The balls don't feel like their expected smooth surface, instead I'm greeted by the feeling of...berries?"

    "I immediately try sittting up, but to no avail I just look like a fish out of water"

    "After about five embarassing minutes of trying to balance my self in the humongous crate I've found myself in, I feel a cool feeling on my collarbone."

    "I look down to find a chain pendant of two snakes wraped around a staff"

    show asset_pendant

    m "Well, that's new."

    "Suddenly, a dark fog enevelopes surrounds me and maniacal laughter rings in my ears."

    e "AHAAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHA"

    e "Well, well, well. What do we have here?"

    "The fog materializes into... a man?"

    show hermes_1

    "The man seems oddly familiar, yet I can't quite place my finger on it."

    e "You seem quite shocked to see me, Darling~ Why's that?"

    "The man pouts, as if I was supposed to recognize him already"

    "He was dressed in something I'd see in pictures that hanged off the walls of the restaurant."

    "The golden hair, the angel wings on the sides of his head and his sandals, the familiar staff he wielded with the two snakes,"

    "No way, could this man be..."

    m "Hermes?"

    show hermes_4

    "The man engulfs me in a bear hug in an instant"

    h "Took you quite a while to recognize me didn'tcha, my beloved?"

    "BELOVED??? Just who did this guy think he was? A massive pervert?"

    menu:

        "While engulfed in his arms, I decide to..."

        "Push him away with a look of shock and disgust.":

            jump disgust

        "Be confused and awkwardly reply back.":

            jump reply


label disgust:

    show hermes_2
    
    "Hermes levitates back in the air"

    h "What's wrong? You used to love my hugs whenever we reunited?"

    m "Just who do you think you are??"

    "He looks at me with a look of guilt, but it quickly morphed to to one of sarcasm"

    show hermes_3

    h "Oh please do you realllyyyy not remember me?"

    h "Your handsome, talented, immortal, the bestest and strongest god on Olympus and amazing lover, Hermes?"

    "I just stare at him"

    h "Huh, I guess I should've followed your advice when you were Circe's apprentice"

    "He pokes at the side of my skull"

    h "Mortals are truly not the srongest at memory, huh?"
    
    jump home

label home:

    scene black
    with dissolve

    "Hermes takes off the chain from my neck"

    scene bg_basement
    with dissolve

    h "Well, if you truly don't remember me, I guess I can't force you into this life."
    
    "He guides me towards the berry crate"

    h "Off you go then."

    m "Hermes,hold on what's going on-"

    "He pushes me into the crate with a dissapointed sigh"

    h "Maybe in the next life, my beloved"

    scene bg_restaurant
    with dissolve

    "I find myself back in the dusty ball pit."

    "Jorge's voice shouts my name and yet..."

    "I feel as thought I've made a mistake"

    "Frantically, I feel my collarbone for the necklace...It-It-s not there."

    "Tears stream down my eyes and I can't figure out why."

    "{b}Bad Ending{/b}."

    return

label reply:

    "I stare at him for a few moments before replying"

    m "Of course! I remember you... errh but care to refresh my memory?"

    "Hermes' face contorts into a wide grin and spins me around while I'm still in his arms"

    show hermes_4

    h "Oh this is such terrific news"

    "He looks ecstatic"

    h "I'll catch you up when we get to Olympus"

    h "Oh you won that bet by the way, Poseidon got back together with-"

    "Hermes shakes his head"

    h "Nah I'll just let you see for yourself."

    m "Wait wha-"

    "He taps his staff on the ground and a ray of light surrounds us."

    h "Let's go home, my love"

    "{b}Good Ending{/b}."
    
    return
