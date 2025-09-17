# Character definitions
define H = Character("Hitoro", color = '#003cff')  # main char
define H2 = Character("Hanabi", color = '#ff6bf9')  # main fem 
define N = Character("Nobi", color = '#bbff00')  # friend of male
define F = Character("Flix", color = '#720000')  # bully
define B = Character("Blake", color = '#720000')  # bully
define K = Character("Kagura", color = '#dcff2a')  # teacher
define M = Character("May", color = '#d07506')  # librarian
define A = Character("Ariane", color = '#fc8cfe')  # mother of H 
define JUNOS = Character("THE MIKU!!!!", color = '#fdfd96')
define Extra = Character("Student", color = '#8e979d')

# The story
label start:

    play music "audio/02 三葉の通学.mp3" fadein 2.0
    pause
    ". . . . . "

    H ". . . . . . *sleeping*"
    pause  

    # Downstairs
    A "HITO! Wake up... you’re late for school!"

    H "What? *gets up and bumps his head on the ceiling*"
    play audio "audio/bump-7-92964.mp3" volume 1.0

    H "Owww... *gets out of bed and starts to get ready*"
    H "Okay okay... *gets dressed and heads downstairs*"

    "Well... this is not a great start but... let me introduce myself. I’m Hitoro Shiranui, or better call me Hito."

    H "*goes downstairs* Mom! I’m going... *heading to the front door*"

    A "Wait! *gives him his lunch* Here... and where’s my hug and kiss?"

    H "Huh? *looks at his mom* Oh... *gives her a big hug and kiss on the cheek* Okay Mom..."
    H "See you later. *heads out the door*"

    A "Remember! Study before women, okay!?"

    H "Huh? *looks back at his mom* What? *laughs* Mom, you always say that."

    "Oh, and if you don’t know... I’m an animator. Sometimes I’m a tech nerd myself."
    "But... I’m cool with it."
    "Animator by day..."
    "Hacker by night..."
    "And... student by force."
    pause  

    # Kōyō Metropolitan High School
    stop music fadeout 2.0
    pause
    queue music "audio/03 糸守高校.mp3" fadein 1.5 volume 1.0

    "Ahhhh... Kōyō Metropolitan High School. Where smart kids live and suffer from bullies."
    "Like if you’re here..."
    "Get ready, ‘cause wedgies are common."

    "But me?"
    "I just animate..."
    "Mostly, I just hide like a bunny in a burrow."

    # The park
    pause
    # queue music "audio/park_calming_music.mp3" fadein 1.5 volume 1.0

    "So I wait there..."
    "Just, you know..."
    "Chilling..."
    "Until a student comes up to me and says..."

    Extra "Are you Hitoro by any chance?"

    H "Ummm... yes?"
    "Why are you here?"

    Extra "I would like to give you this."

    H "A letter?"
    "By who?"
    "Who gave this?"

    Extra "I don’t know..."
    "They said to just give it to you."
    "She never said her name."
    "She just gave it to me and left."

    H "Ohhh..."
    "I guess thanks?"
    "But I don’t know anybody yet."
    "So..."
    "I’ll just read it in my dorm."

    H "Thanks..."

    # Chapter One (ver_01: finding_the_color_pallet)
    return