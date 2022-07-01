import json
from readline import set_pre_input_hook


content = {
    "Farm": "-1/-1/-1/-1/-1/-1/-1/-1/382 .05 770 .1 390 .25 330 1",
    "UndergroundMine": "-1/-1/-1/-1/153 -1 156 -1 157 -1/153 -1 156 -1 157 -1/153 -1 156 -1 157 -1/153 -1 156 -1 157 -1/107 .01",
    "Desert": "88 .5 90 .5/88 .5 90 .5/88 .5 90 .5/88 .5 90 .5/153 -1 164 -1 165 -1/153 -1 164 -1 165 -1/153 -1 164 -1 165 -1/153 -1 164 -1 165 -1/390 .25 330 1",
    "BusStop": "18 .9 20 .4 22 .7/396 .4 398 .4 402 .7/406 .6 408 .4/414 .33 418 .6 283 .5/-1/-1/-1/-1/584 .08 378 .15 102 .15 390 .25 330 1",
    "Forest": "16 .9 22 .9/396 .6 402 .9/404 .9 410 .9/418 .9 414 .9 283 .5/153 -1 145 0 143 0 137 1 132 0 706 0 702 0/153 -1 145 0 144 -1 138 0 132 0 706 0 704 0 702 0/143 0 153 -1 140 -1 139 0 137 1 132 0 706 0 702 0 699 0 269 1/699 0 143 0 153 -1 144 -1 141 -1 140 -1 132 0 707 0 702 0 269 1/378 .08 579 .1 588 .1 102 .15 390 .25 330 1",
    "Town": "18 .9/402 .9/410 .6/418 .7 414 .1 283 .5/137 -1 132 -1 143 -1 145 -1 153 -1 706 -1/138 -1 132 -1 144 -1 145 -1 153 -1 706 -1/139 -1 137 -1 132 -1 140 -1 143 -1 153 -1 706 -1 699 -1/132 -1 140 -1 141 -1 143 -1 144 -1 153 -1 707 -1 699 -1/378 .2 110 .2 583 .1 102 .2 390 .25 330 1",
    "Mountain": "20 .7 16 .5/396 .5 398 .8/404 .4 406 .4 408 .9/414 .85 418 .9 283 .5/136 -1 142 -1 153 -1 702 -1 700 -1/136 -1 142 -1 153 -1 138 -1 702 -1 700 -1 698 -1/136 -1 140 -1 142 -1 153 -1 702 -1 700 -1 269 -1/136 -1 140 -1 141 -1 153 -1 707 -1 702 -1 700 -1 698 -1 269 -1/382 .06 581 .1 378 .1 102 .15 390 .25 330 1",
    "Backwoods": "20 .7 16 .5/396 .5 398 .8/404 .4 406 .4 408 .9/414 .25 418 .4 283 .5/136 -1 142 -1 153 -1 702 -1 700 -1 163 -1/136 -1 142 -1 153 -1 138 -1 702 -1 700 -1 698 -1/136 -1 140 -1 142 -1 153 -1 702 -1 700 -1/136 -1 140 -1 141 -1 153 -1 707 -1 702 -1 700 -1 698 -1/382 .06 582 .1 378 .1 102 .15 390 .25 330 1",
    "Railroad": "18 .9 20 .4 22 .7/396 .4 398 .4 402 .7/406 .6 408 .4 410 .6/414 .8 418 .8/-1/-1/-1/-1/580 .1 378 .15 102 .19 390 .25 330 1",
    "Beach": "372 .9 718 .1 719 .3 723 .3/372 .9 394 .5 718 .1 719 .3 723 .3/372 .9 718 .1 719 .3 723 .3/372 .4 392 .8 718 .05 719 .2 723 .2/129 -1 131 -1 147 -1 148 -1 152 -1 708 -1 267 -1/128 -1 130 -1 146 -1 149 -1 150 -1 152 -1 155 -1 708 -1 701 -1 267 -1/129 -1 131 -1 148 -1 150 -1 152 -1 154 -1 155 -1 705 -1 701 -1/708 -1 130 -1 131 -1 146 -1 147 -1 150 -1 151 -1 152 -1 154 -1 705 -1/384 .08 589 .09 102 .15 390 .25 330 1",
    "Woods": "257 .5 404 .25 16 .8/259 .9 420 .25/281 .5 404 .6 420 .2/283 .9/734 -1 142 -1 143 -1/734 -1 142 -1 143 -1/734 -1 142 -1 143 -1/734 -1 142 -1 143 -1/390 .25 330 1",
    "Sewer": "-1/-1/-1/-1/142 -1 153 -1 157 -1/142 -1 153 -1 157 -1/142 -1 153 -1 157 -1/142 -1 153 -1 157 -1/-1",
    "BugLand": "-1/-1/-1/-1/796 -1 142 -1 153 -1 157 -1/796 -1 142 -1 153 -1 157 -1/796 -1 142 -1 153 -1 157 -1/796 -1 142 -1 153 -1 157 -1/-1",
    "WitchSwamp": "-1/-1/-1/-1/795 -1 153 -1 143 -1 157 -1/795 -1 153 -1 143 -1 157 -1/795 -1 153 -1 143 -1 157 -1/795 -1 153 -1 143 -1 157 -1/-1",
    "fishingGame": "-1/-1/-1/-1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/378 .08 390 .25 330 1",
    "Temp": "16 .9 22 .9/396 .6/404 .9 410 .9/418 .5 414 .2/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/153 -1 145 -1 143 -1 137 -1 132 -1 706 -1 702 -1/378 .08 390 .25 330 1",
    "IslandNorth": "-1/-1/-1/-1/701 -1 838 -1 269 -1/701 -1 838 -1 269 -1/701 -1 838 -1 269 -1/701 -1 838 -1 269 -1/791 .05 292 .05 774 .1 749 1",
    "IslandSouth": "-1/-1/-1/-1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/791 .05 292 .05 774 .1 749 1",
    "IslandWest": "-1/-1/-1/-1/149 1 155 1 130 1 128 1 267 1 837 1 701 2 838 2 269 2/149 1 155 1 130 1 128 1 267 1 837 1 701 2 838 2 269 2/149 1 155 1 130 1 128 1 267 1 837 1 701 2 838 2 269 2/149 1 155 1 130 1 128 1 267 1 837 1 701 2 838 2 269 2/791 .05 292 .05 774 .1 749 1",
    "IslandSouthEast": "-1/-1/-1/-1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/155 -1 130 -1 128 -1 267 -1 837 -1/791 .05 292 .05 774 .1 749 1",
    "IslandSouthEastCave": "-1/-1/-1/-1/155 -1 130 -1 128 -1 267 -1 836 -1/155 -1 130 -1 128 -1 267 -1 836 -1/155 -1 130 -1 128 -1 267 -1 836 -1/155 -1 130 -1 128 -1 267 -1 836 -1/791 .05 292 .05 774 .1 749 1",
    "IslandSecret": "372 .6 397 .5 394 .5 393 .3 718 .2 719 .3 723 .3/372 .6 397 .5 394 .5 393 .3 718 .2 719 .3 723 .3/372 .6 397 .5 394 .5 393 .3 718 .2 719 .3 723 .3/372 .6 397 .5 394 .5 393 .3 718 .2 719 .3 723 .3/836 -1 267 -1 151 -1 708 -1 146 -1 155 -1 130 -1/836 -1 267 -1 151 -1 708 -1 146 -1 155 -1 130 -1/836 -1 267 -1 151 -1 708 -1 146 -1 155 -1 130 -1/836 -1 267 -1 151 -1 708 -1 146 -1 155 -1 130 -1/791 .05 292 .05 774 .1 749 1",
    "IslandNorthCave1": "281 .9 404 .9 420 .5 422 .5/281 .9 404 .9 420 .9 422 .9/281 .9 404 .9 420 .9 422 .9/281 .9 404 .9 420 .9 422 .9/-1/-1/-1/-1/107 .01"
}

with open("../data/ObjectInformation.json", "r") as f:
     ObjInfo = json.load(f)
    
locations = {}
for key, value in content.items():    
    if key == "Farm": continue
    
    # spring forage items
    locations[key] = {}
    
    locations[key]["spring"] = {}
    locations[key]["spring"]["fish"] = {}
    locations[key]["spring"]["foraging"] = {}
    locations[key]["summer"] = {}
    locations[key]["summer"]["fish"] = {}
    locations[key]["summer"]["foraging"] = {}
    locations[key]["fall"] = {}
    locations[key]["fall"]["fish"] = {}
    locations[key]["fall"]["foraging"] = {}
    locations[key]["winter"] = {}
    locations[key]["winter"]["fish"] = {}
    locations[key]["winter"]["foraging"] = {}
    
    entries = value.split("/")
    
    spring_forage = entries[0]
    if not spring_forage == "-1":
        i = iter(spring_forage.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            forage_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["spring"]["foraging"][forage_name] = {"chance": pair.split(" ")[1]}
            
    summer_forage = entries[1]
    if not summer_forage == "-1":
        i = iter(summer_forage.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            forage_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["summer"]["foraging"][forage_name] = {"chance": pair.split(" ")[1]}
            
    fall_forage = entries[2]
    if not fall_forage == "-1":
        i = iter(fall_forage.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            forage_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["fall"]["foraging"][forage_name] = {"chance": pair.split(" ")[1]}
            
    winter_forage = entries[3]
    if not winter_forage == "-1":
        i = iter(winter_forage.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            forage_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["winter"]["foraging"][forage_name] = {"chance": pair.split(" ")[1]}
            
    spring_fish = entries[4]
    if not spring_fish == "-1":
        i = iter(spring_fish.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            fish_id, fish_zone = pair.split(" ")[0], pair.split(" ")[1]
            fish_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["spring"]["fish"][fish_id] = {"fish_name": fish_name, "zoneNumber": fish_zone}

    summer_fish = entries[5]
    if not summer_fish == "-1":
        i = iter(summer_fish.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            fish_id, fish_zone = pair.split(" ")[0], pair.split(" ")[1]
            fish_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["summer"]["fish"][fish_id] = {"fish_name": fish_name, "zoneNumber": fish_zone}

    fall_fish = entries[6]
    if not fall_fish == "-1":
        i = iter(fall_fish.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            fish_id, fish_zone = pair.split(" ")[0], pair.split(" ")[1]
            fish_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["fall"]["fish"][fish_id] = {"fish_name": fish_name, "zoneNumber": fish_zone}

    winter_fish = entries[7]
    if not winter_fish == "-1":
        i = iter(winter_fish.split(" "))
        pairs = map(" ".join, zip(i, i))
        for pair in pairs:
            fish_id, fish_zone = pair.split(" ")[0], pair.split(" ")[1]
            fish_name = ObjInfo["content"][pair.split(" ")[0]].split("/")[0]
            
            locations[key]["winter"]["fish"][fish_id] = {"fish_name": fish_name, "zoneNumber": fish_zone}



with open("locations.json", "w") as f:
    json.dump(locations, f, indent=4)
    