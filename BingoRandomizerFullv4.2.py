#Fall Guys Bingo Randomizer
#Programmed with Python

#Instructions:
#1. Run program with IDLE or any other program or website that runs Python code
#Note: https://pynative.com/online-python-code-editor-to-execute-python-code/ is a website that runs python code online
#2. Copy the printed text from the output
#3. On [bingosync.com], begin to make a room and for [Game] select: Custom (Advanced) and for [Variant] select: Randomized
#4. Paste copied text for [Board]
#5. Select any other options as needed and finish creating the room

#Additional Notes:
#Although minigame categories of "Hunt" and "Logic" exist, each round may fall under the race, elimination, team, or finals category based on the method of qualification and as defined by the Stats Tracker created by DevilSquirrel
#"Pants": Grabbing a player in such a way that pulls them down during a jump; therefore, causing them to respawn or be eliminated

import random

choices = {
    14: "{\"name\": \"Win a finals without jumping\"}",
    15: "{\"name\": \"Win a finals without diving\"}",
    16: "{\"name\": \"Win a finals without grabbing\"}",
    19: "{\"name\": \"Qualify 2 rounds in a row without jumping\"}",
    20: "{\"name\": \"Qualify 2 rounds in a row without diving\"}",
    21: "{\"name\": \"Qualify 2 rounds in a row without grabbing\"}",
    22: "{\"name\": \"Earn a gold medal from a race round without jumping\"}",
    23: "{\"name\": \"Earn a gold medal from a race round without diving\"}",
    29: "{\"name\": \"Earn a gold medal on any Tail round\"}",
    30: "{\"name\": \"Land and progress from 2 Big Yeetuses (Limit 1 per Yeetus)\"}",
    31: "{\"name\": \"Land and progress from 4 Big Yeetuses (Limit 1 per Yeetus)\"}",
    32: "{\"name\": \"Land and progress from 6 Big Yeetuses (Limit 1 per Yeetus)\"}",
    59: "{\"name\": \"Earn a gold medal from a team round\"}",
    60: "{\"name\": \"Earn a silver medal from a team round\"}",
    61: "{\"name\": \"Qualify last on any race round\"}",
    62: "{\"name\": \"Qualify last on race rounds twice in a row\"}",
    63: "{\"name\": \"Qualify any round holding a pegwin\"}",
    64: "{\"name\": \"Find a Lil' Yeety\"}",
    65: "{\"name\": \"Win back-to-back episodes\"}",
    66: "{\"name\": \"Take the out of bounds shortcut on Whirlygig\"}",
    67: "{\"name\": \"Have any race or final round end by timing out\"}",
    68: "{\"name\": \"Qualify from Lily Leapers without retouching the ground\"}",
    69: "{\"name\": \"Jump up on the moving blocks on Block Party\"}",
    70: "{\"name\": \"Take the ramp of shame on Skyline Stumble (Side-path ending)\"}",
    71: "{\"name\": \"Pop 1 golden bubble\"}",
    72: "{\"name\": \"Pop 3 golden bubbles\"}",
    74: "{\"name\": \"Win an episode without ever respawning\"}",
    75: "{\"name\": \"Be first to die in a final\"}",
    76: "{\"name\": \"Get second place in any final\"}",
    77: "{\"name\": \"Eliminate yourself on any elimination round\"}",
    78: "{\"name\": \"Eliminate yourself on any elimination round 2 times\"}",
    79: "{\"name\": \"Eliminate yourself on any elimination round 3 times\"}",
    80: "{\"name\": \"Qualify from any round without jumping, diving or grabbing\"}",
    82: "{\"name\": \"Qualify from any round without touching the analog stick\"}",
    83: "{\"name\": \"Get top 3 in any final without touching the analog stick\"}",
    86: "{\"name\": \"Be first to die in 2 UNIQUE finals\"}",
    87: "{\"name\": \"Qualify from Big Fans without jumping, grabbing, or respawning\"}",
    88: "{\"name\": \"Qualify from Slime Climb or Slimescraper without jumping\"}",
    93: "{\"name\": \"Get at least 1 of every type of medal in a single episode\"}",
    100: "{\"name\": \"Earn a gold medal from a race round with the camera actively faced backwards\"}",
    108: "{\"name\": \"Qualify from Airtime while making a full outer-revolution\"}",
    109: "{\"name\": \"Qualify from Airtime while only using the middle obstacles\"}"
}

choicesTwo = {
    5: ["{\"name\": \"Eliminate a total of 2 beans on elimination rounds from Season 1 (& Slime Climb)\"}", "{\"name\": \"Eliminate a total of 4 beans on elimination rounds from Season 1 (& Slime Climb)\"}"],
    6: ["{\"name\": \"Eliminate a total of 1 bean on elimination rounds from Seasons 3 or 5\"}", "{\"name\": \"Eliminate a total of 2 beans on elimination rounds from Seasons 3 or 5\"}"],
    7: ["{\"name\": \"Eliminate a total of 2 beans on elimination rounds from Season 4 (& Slimescraper)\"}", "{\"name\": \"Eliminate a total of 4 beans on elimination rounds from Season 4 (& Slimescraper)\"}"],
    8: ["{\"name\": \"Eliminate a total of 2 beans on Roll Out / Roll Off\"}", "{\"name\": \"Eliminate a total of 4 beans on Roll Out / Roll Off\"}"],
    9: ["{\"name\": \"Pants a total of 4 people on Big Fans\"}", "{\"name\": \"Pants a total of 6 people on Big Fans\"}"],
    10: ["{\"name\": \"Win a crown on a final from Season 1\"}", "{\"name\": \"Win 2 crowns on finals from Season 1\"}"],
    24: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 1\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 1\"}"],
    25: ["{\"name\": \"Earn a gold medal on 2 race rounds from Seasons 2 or 3\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Seasons 2 or 3\"}"],
    26: ["{\"name\": \"Earn a gold medal on 2 race rounds from Seasons 4 or 5\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Seasons 4 or 5\"}"],
    37: ["{\"name\": \"Share a hug with 2 different beans\"}", "{\"name\": \"Share a hug with 4 different beans\"}"],
    38: ["{\"name\": \"Share a hug with 6 different beans\"}", "{\"name\": \"Share a hug with 8 different beans\"}"],
    39: ["{\"name\": \"Qualify from round 3 at least 3 times\"}", "{\"name\": \"Qualify from round 3 at least 4 times\"}"],
    40: ["{\"name\": \"Qualify from round 4 at least 2 times\"}", "{\"name\": \"Qualify from round 4 at least 3 times\"}"],
    41: ["{\"name\": \"Qualify from round 5 at least 1 time\"}", "{\"name\": \"Qualify from round 5 at least 2 times\"}"],
    43: ["{\"name\": \"Qualify from team rounds 1 time\"}", "{\"name\": \"Qualify from team rounds 2 times\"}"],
    44: ["{\"name\": \"Qualify from race rounds 6 times\"}", "{\"name\": \"Qualify from elimination rounds 5 times\"}"],
    45: ["{\"name\": \"Qualify from elimination rounds 3 times\"}", "{\"name\": \"Qualify from race rounds 9 times\"}"],
    46: ["{\"name\": \"Earn a total of 6 gold medals\"}", "{\"name\": \"Earn a total of 12 gold medals\"}"],
    47: ["{\"name\": \"Earn a total of 4 silver medals\"}", "{\"name\": \"Earn a total of 8 silver medals\"}"],
    48: ["{\"name\": \"Earn a total of 4 bronze medals\"}", "{\"name\": \"Earn a total of 8 bronze medals\"}"],
    49: ["{\"name\": \"Earn a total of 3 pink medals\"}", "{\"name\": \"Earn a total of 6 pink medals\"}"],
    51: ["{\"name\": \"Earn at least 4 gold medals in a single episode\"}", "{\"name\": \"Earn at least 3 silver medals in a single episode\"}"],
    52: ["{\"name\": \"Earn at least 3 bronze medals in a single episode\"}", "{\"name\": \"Earn at least 2 pink medals in a single episode\"}"],
    53: ["{\"name\": \"Earn a total of 1000+ kudos\"}", "{\"name\": \"Earn a total of 1500+ kudos\"}"],
    54: ["{\"name\": \"Earn a total of 2000+ kudos\"}", "{\"name\": \"Earn a total of 2500+ kudos\"}"],
    55: ["{\"name\": \"Earn a total of 3000+ kudos\"}", "{\"name\": \"Earn a total of 3500+ kudos\"}"],
    56: ["{\"name\": \"Jump through a total of 4 hoops\"}", "{\"name\": \"Jump through a total of 8 hoops\"}"],
    57: ["{\"name\": \"Jump through a total of 12 hoops\"}", "{\"name\": \"Jump through a total of 16 hoops\"}"],
    73: ["{\"name\": \"I Spy: A Magnet Obstacle \"}", "{\"name\": \"I Spy: A Banana Obstacle \"}"],
    81: ["{\"name\": \"Qualify 2 races without respawning\"}", "{\"name\": \"Qualify 4 races without respawning\"}"],
    84: ["{\"name\": \"I Spy: A Star Obstacle\"}", "{\"name\": \"I Spy: A Dragonfruit Obstacle\"}"],
    85: ["{\"name\": \"Get second place on hex-a-gone or thin ice\"}", "{\"name\": \"Get second place on jump showdown or roll off\"}"],
    94: ["{\"name\": \"Earn between 50 and 100 kudos in an episode\"}", "{\"name\": \"Earn between 100 and 150 kudos in an episode\"}"],
    95: ["{\"name\": \"Earn between 150 and 200 kudos in an episode\"}", "{\"name\": \"Earn between 200 and 250 kudos in an episode\"}"],
    96: ["{\"name\": \"Earn between 250 and 300 kudos in an episode\"}", "{\"name\": \"Earn between 300 and 350 kudos in an episode\"}"],
    97: ["{\"name\": \"Earn between 350 and 400 kudos in an episode\"}", "{\"name\": \"Earn between 400 and 450 kudos in an episode\"}"],
    98: ["{\"name\": \"Qualify 2 race rounds with the camera actively faced backwards\"}", "{\"name\": \"Qualify 4 race rounds with the camera actively faced backwards\"}"],
    99: ["{\"name\": \"Qualify 2 elimination rounds with the camera actively faced backwards\"}", "{\"name\": \"Qualify 3 elimination rounds with the camera actively faced backwards\"}"],
    103: ["{\"name\": \"Earn a gold medal on Tip Toe or Treetop Tumble\"}", "{\"name\": \"Earn a gold medal on Tundra Run, Whirlygig, or Wall Guys\"}"],
    104: ["{\"name\": \"Earn a gold medal on 2 race rounds from Season 6\"}", "{\"name\": \"Earn a gold medal on 3 race rounds from Season 6\"}"],
    105: ["{\"name\": \"I Spy: A Cheese Puff Obstacle\"}", "{\"name\": \"I Spy: A Snowball Obstacle\"}"],
    106: ["{\"name\": \"I Spy: A Purple Pegwin\"}", "{\"name\": \"I Spy: A Rhino Obstacle\"}"],
    107: ["{\"name\": \"I Spy: A Bonkus Obstacle\"}", "{\"name\": \"I Spy: A Coconut Obstacle\"}"],
    110: ["{\"name\": \"Jump 100 times in a single round\"}", "{\"name\": \"Dive 80 times in a single round\"}"]
}

choicesThree = {
    1: ["{\"name\": \"Earn a gold medal on Airtime or Big Fans\"}", "{\"name\": \"Earn a gold medal on Bubble Trouble or Door Dash\"}", "{\"name\": \"Earn a gold medal on Dizzy Heights or Freezy Peak\"}"], 
    2: ["{\"name\": \"Earn a gold medal on Fruit Chute or Full Tilt\"}", "{\"name\": \"Earn a gold medal on Gate Crash or Hit Parade\"}", "{\"name\": \"Earn a gold medal on Hoopsie Heroes or Knight Fever\"}"], 
    3: ["{\"name\": \"Earn a gold medal on Leading Light or Lily Leapers\"}", "{\"name\": \"Earn a gold medal on Party Promenade or Pegwin Party\"}", "{\"name\": \"Earn a gold medal on Pipe Dream or Roll On\"}"], 
    4: ["{\"name\": \"Earn a gold medal on See Saw or Short Circuit\"}", "{\"name\": \"Earn a gold medal on Ski Fall or Skyline Stumble\"}", "{\"name\": \"Earn a gold medal on Slime Climb or Slimescraper\"}"], 
    11: ["{\"name\": \"Win a crown on a final from Season 3\"}", "{\"name\": \"Win a crown on a final from Season 5\"}", "{\"name\": \"Win a final that contains low gravity\"}"],
    12: ["{\"name\": \"Qualify 2 race rounds without jumping\"}", "{\"name\": \"Qualify 2 race rounds without diving\"}", "{\"name\": \"Qualify 2 race rounds without grabbing\"}"],
    13: ["{\"name\": \"Qualify 4 race rounds without jumping\"}", "{\"name\": \"Qualify 4 race rounds without diving\"}", "{\"name\": \"Qualify 4 race rounds without grabbing\"}"],
    17: ["{\"name\": \"Qualify 2 elimination rounds without jumping\"}", "{\"name\": \"Qualify 2 elimination rounds without diving\"}", "{\"name\": \"Qualify 2 elimination rounds without grabbing\"}"],
    18: ["{\"name\": \"Qualify 3 elimination rounds without jumping\"}", "{\"name\": \"Qualify 3 elimination rounds without diving\"}", "{\"name\": \"Qualify 3 elimination rounds without grabbing\"}"],
    27: ["{\"name\": \"Earn a gold medal on 3 race rounds\"}", "{\"name\": \"Earn a gold medal on 4 race rounds\"}", "{\"name\": \"Earn a gold medal on 5 race rounds\"}"],
    28: ["{\"name\": \"Earn a gold medal on 6 race rounds\"}", "{\"name\": \"Earn a gold medal on 7 race rounds\"}", "{\"name\": \"Earn a gold medal on 8 race rounds\"}"],
    33: ["{\"name\": \"Grab a plain (no-outfit) bean\"}", "{\"name\": \"Grab a medieval themed bean\"}", "{\"name\": \"Grab a water animal bean\"}"],
    34: ["{\"name\": \"Grab a golden outfit top bean\"}", "{\"name\": \"Grab a cat themed bean\"}", "{\"name\": \"Grab a jungle animal bean\"}"],
    35: ["{\"name\": \"Grab an egg bean\"}", "{\"name\": \"Grab a food-related bean\"}", "{\"name\": \"Grab a dinosaur themed bean\"}"],
    36: ["{\"name\": \"Grab an alien themed bean\"}", "{\"name\": \"Grab a christmas themed bean\"}", "{\"name\": \"Grab a ninja or samurai themed bean\"}"],
    42: ["{\"name\": \"Qualify from any round 10 times\"}", "{\"name\": \"Qualify from any round 15 times\"}", "{\"name\": \"Qualify from any round 20 times\"}"],
    58: ["{\"name\": \"Jump through a total of 2 gold hoops\"}", "{\"name\": \"Jump through a total of 3 gold hoops\"}", "{\"name\": \"Jump through a total of 4 gold hoops\"}"],
    89: ["{\"name\": \"Share a hug with a plain (no-outfit) bean\"}", "{\"name\": \"Pants a medieval themed bean\"}", "{\"name\": \"Share a hug with a water animal bean\"}"],
    90: ["{\"name\": \"Pants a golden outfit top bean\"}", "{\"name\": \"Share a hug with a cat themed bean\"}", "{\"name\": \"Pants a jungle animal bean\"}"],
    91: ["{\"name\": \"Share a hug with an egg bean\"}", "{\"name\": \"Pants a food-related bean\"}", "{\"name\": \"Share a hug with a dinosaur themed bean\"}"],
    92: ["{\"name\": \"Pants an alien themed bean\"}", "{\"name\": \"Share a hug with a christmas themed bean\"}", "{\"name\": \"Pants a ninja or samurai themed bean\"}"],
    101: ["{\"name\": \"Grab a birb bean\"}", "{\"name\": \"Grab a robotic bean\"}", "{\"name\": \"Grab a SEGA themed bean\"}"],
    102: ["{\"name\": \"Share a hug with a birb bean\"}", "{\"name\": \"Pants a robotic bean\"}", "{\"name\": \"Share a hug with a SEGA themed bean\"}"]
}

choicesFour = {
    50: ["{\"name\": \"Earn a total of 15 gold medals\"}", "{\"name\": \"Earn a total of 10 silver medals\"}", "{\"name\": \"Earn a total of 10 bronze medals\"}", "{\"name\": \"Earn a total of 8 pink medals\"}"] 
}



numbers = random.sample(range(1, 110), 25)
print("[", end='')

for x in range(25):
    numcheck = numbers[x]

    if numcheck in choices:
        print(choices[numcheck], end='')

    if numcheck in choicesTwo:
        print(choicesTwo[numcheck][random.randint(1, 2) - 1], end='')

    if numcheck in choicesThree:
        print(choicesThree[numcheck][random.randint(1, 3) - 1], end='')

    if numcheck in choicesFour:
        print(choicesFour[numcheck][random.randint(1, 4) - 1], end='')


    if x == 24:
        print("]")
    else:
        print(",")
