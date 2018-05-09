import flask
import random
import names

app = flask.Flask(__name__)

tropes = {"Batshit Crazy": 20,
    "Batteries Included": 20,
    "Blind Master": 21,
    "Born Wild": 21,
    "Bravehearted": 22,
    "Bumbling Sidekick": 22,
    "Chesty": 23,
    "Coward": 23,
    "Crime Robber": 23,
    "Cyborg": 24,
    "Die Hardly": 24,
    "Doctor": 25,
    "Dual Wielding": 25,
    "Gangster": 26,
    "Gumshoe": 26,
    "Hobo": 27,
    "Jack Burtonesque": 27,
    "Know-It-All": 27,
    "Mad Scientist": 28,
    "Man/Woman of Action": 28,
    "Man/Woman of the Cloth": 29,
    "Martial Artist": 29,
    "Net Hacker": 30,
    "Ninja": 30,
    "Nosy Reporter": 31,
    "Old Geezer": 31,
    "Otherworldly": 31,
    "Paid Sponsor": 32,
    "Police Cop": 32,
    "Protagonist": 33,
    "Psychic Mindfreaker": 33,
    "Road Rash": 34,
    "Rock and Roller": 34,
    "Sentimentalist": 35,
    "Shredmeister": 35,
    "Snot-Nosed Brat": 36,
    "Sophisticated": 36,
    "Stoner": 37,
    "Survivalist": 37,
    "Talking Animal": 38,
    "Troubled Athlete": 38,
    "Vampire": 38,
    "Voodoo Master": 39,
    "Werewolf": 39,
    "Wheelman": 40,
    "Wrestler": 40}

perks = {"Adrenaline Rush": 41,
    "Aspiring Script Writer": 41,
    "Calmly Walk Away": 41,
    "Crunch Time": 41,
    "Deceitful": 41,
    "Domino Strike": 41,
    "Dramatic Reval": 41,
    "Druid, or Possibly Farmer": 41,
    "Duct Tape and Solder": 42,
    "Eagle-Eyed": 42,
    "Elite Shooter": 42,
    "Evil Eye": 42,
    "Explosives Expert": 42,
    "Fight Me Like a Man": 42,
    "Float Like a Butterfly": 42,
    "Glancing Blows": 42,
    "Good Judge of Character": 42,
    "Hell of an Arm": 42,
    "High Five of Life": 42,
    "I'm Not Supposed to Die Like This": 43,
    "John Woo": 43,
    "Laser Focus": 43,
    "Leap of Faith": 43,
    "Masochistic": 43,
    "Mass Destruction": 43,
    "Master of Disguise": 43,
    "Mr. Roy Rodgers": 43,
    "My Body Is a Weapon": 43,
    "My Body Is Literally a Weapon": 43,
    "No Body, No Death": 44,
    "Noooo!": 44,
    "Payday": 44,
    "Photographic Memory": 44,
    "Point Blank": 44,
    "Push It Real Good": 44,
    "Ricochet": 44,
    "Sexual Tyrannosaurus": 44,
    "Sexy Nerd": 44,
    "Shock Absorber": 45,
    "Sleeper Hold": 45,
    "Smack-Talkin'": 45,
    "Small but Fierce": 45,
    "Speed of Plot": 45,
    "Spray and Pray": 45,
    "Still Breathing": 45,
    "The More The Merrier": 45,
    "Trenchcoat": 46,
    "Under the Radar": 45,
    "Warrior Training": 45,
    "Where's My Mark?": 45,
    "Why Didn't You Say So?": 45,
    "Wildcard": 45,
    "Winning Smile": 45,
    "Wire Work": 45,
    "Words of Wisdom": 45,
    "You Never Know": 45,
    "You Sick Sonavabitch": 46,
    "You Thought I Was Down": 46}

@app.route('/')
def homepage():
    """
    Create a character with a random name, two random tropes, and a random perk, with pagenumbers.
    """
    name = names.get_full_name()
    trope_1 = random.choice(list(tropes.keys()))
    trope_1_page = tropes[trope_1]
    trope_2 = None
    while trope_2 is None or trope_2 == trope_1:
        trope_2 = random.choice(list(tropes.keys()))
    trope_2_page = tropes[trope_2]
    perk = random.choice(list(perks.keys()))
    perk_page = perks[perk]
    return """
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        <title>Who the Fuck is my Straight to VHS Character?</title>
    </head>
    <body>
        <div class="container"> 
            <h1>Who the fuck is my Straight to VHS Character?</h1>
            <p>I am playing...</p>
            <h2>{name}</h2>
            <p>...whose two Tropes are...</p>
            <ol>
                <li><h2>{trope_1} <small>(page {trope_1_page})</small></h2></li>
                <li><h2>{trope_2} <small>(page {trope_2_page})</small></h2></li>
            </ol>
            <p>...and whose Perk is...</p>
            <ol>
                <li><h2>{perk} <small>(page {perk_page})</small></h2></li>
            </ol>
            <p class="small">This site uses Flask, Bootstrap, and Heroku. Its source code is available 
            <a href="https://github.com/BenQuigley/wtfvhs">here on Github</a>, where 
            you are welcome to contribute to it; pull requests and bug reports are welcome.</p>
            <p class="small">The minimal "who the fuck is my character" format was stolen from the 
            <a href="http://www.whothefuckismydndcharacter.com/">Who the fuck is my #DND character</a> generator by 
            <a href="https://twitter.com/ryanjgrant">Ryan Grant</a>.</p>
            <p class="small"><a href="http://lostcatgames.com/">Straight to VHS</a> is published by Lost Cat Games, and this site is 
            published with their permission. The game is currently in open beta and is available for free on their web 
            site.</p>
        </div>
    </body>
    </html>
    """.format(name=name, trope_1=trope_1, trope_1_page=trope_1_page, trope_2=trope_2, trope_2_page=trope_2_page,
               perk=perk, perk_page=perk_page)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

