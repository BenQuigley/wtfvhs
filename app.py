import flask
import random
import names

app = flask.Flask(__name__)

tropes = ["Batshit Crazy",
    "Batteries Included",
    "Blind Master",
    "Born Wild",
    "Bravehearted",
    "Bumbling Sidekick",
    "Chesty",
    "Coward",
    "Crime Robber",
    "Cyborg",
    "Die Hardly",
    "Doctor",
    "Dual Wielding",
    "Gangster",
    "Gumshoe",
    "Hobo",
    "Jack Burtonesque",
    "Know-It-All",
    "Mad Scientist",
    "Man/Woman of Action",
    "Man/Woman of the Cloth",
    "Martial Artist",
    "Net Hacker",
    "Ninja",
    "Nosy Reporter",
    "Old Geezer",
    "Otherworldly",
    "Paid Sponsor",
    "Police Cop",
    "Protagonist",
    "Psychic Mindfreaker",
    "Road Rash",
    "Rock and Roller",
    "Sentimentalist",
    "Shredmeister",
    "Snot-Nosed Brat",
    "Sophisticated",
    "Stoner",
    "Survivalist",
    "Talking Animal",
    "Troubled Athlete",
    "Vampire",
    "Voodoo Master",
    "Werewolf",
    "Wheelman",
    "Wrestler",
]

perks = ["Adrenaline Rush",
    "Aspiring Script Writer",
    "Calmly Walk Away",
    "Crunch Time",
    "Deceitful",
    "Domino Strike",
    "Dramatic Reval",
    "Druid, or Possibly Farmer",
    "Duct Tape and Solder",
    "Eagle-Eyed",
    "Elite Shooter",
    "Evil Eye",
    "Explosives Expert",
    "Fight Me Like a Man",
    "Float Like a Butterfly",
    "Glancing Blows",
    "Good Judge of Character",
    "Hell of an Arm",
    "High Five of Life",
    "I'm Not Supposed to Die Like This",
    "John Woo",
    "Laser Focus",
    "Leap of Faith",
    "Masochistic",
    "Mass Destruction",
    "Master of Disguise",
    "Mr. Roy Rodgers",
    "My Body Is a Weapon",
    "My Body Is Literally a Weapon",
    "No Body, No Death",
    "Noooo!",
    "Payday",
    "Photographic Memory",
    "Point Blank",
    "Push It Real Good",
    "Ricochet",
    "Sexual Tyrannosaurus",
    "Sexy Nerd",
    "Shock Absorber",
    "Sleeper Hold",
    "Smack-Talkin'",
    "Small but Fierce",
    "Speed of Plot",
    "Spray and Pray",
    "Still Breathing",
    "The More The Merrier",
    "Trenchcoat",
    "Under the Radar",
    "Warrior Training",
    "Where's My Mark?",
    "Why Didn't You Say So?",
    "Wildcard",
    "Winning Smile",
    "Wire Work",
    "Words of Wisdom",
    "You Never Know",
    "You Sick Sonavabitch",
    "You Thought I Was Down",
]

@app.route('/')
def homepage():
    name = names.get_full_name()
    trope_1 = random.choice(tropes)
    trope_2 = None
    while trope_2 is None or trope_2 == trope_1:
        trope_2 = random.choice(tropes)
    perk = random.choice(perks)
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
                <li><h2>{trope_1}</h2></li>
                <li><h2>{trope_2}</h2></li>
            </ol>
            <p>...and whose Perk is...</p>
            <ol>
                <li><h2>{perk}</h2></li>
            </ol>
            <p class="small">This site uses Flask, Bootstrap, and Heroku. Its source code is available 
            <a href="https://github.com/BenQuigley/wtfvhs">here on Github</a>, where 
            you are welcome to contribute to it; pull requests and bug reports are welcome.</p>
            <p class="small">The minimal "who is my character" format was stolen from the 
            <a href="http://www.whothefuckismydndcharacter.com/">Who the fuck is my #DND character</a> generator by 
            <a href="https://twitter.com/ryanjgrant">Ryan Grant</a>.</p>
            <p class="small"><a href="http://lostcatgames.com/">Straight to VHS</a> is published by Lost Cat Games, and this site is 
            published with their permission. The game is currently in open beta and is available for free on their web 
            site.</p>
        </div>
    </body>
    </html>
    """.format(name=name, trope_1=trope_1, trope_2=trope_2, perk=perk)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)

