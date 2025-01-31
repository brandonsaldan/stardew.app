import json
import bs4
import requests

from datetime import datetime

content = {
    "128": "Pufferfish/80/floater/1/36/1200 1600/summer/sunny/690 .4 685 .1/4/.3/.5/0",
    "129": "Anchovy/30/dart/1/16/600 2600/spring fall/both/682 .2/1/.25/.3/0",
    "130": "Tuna/70/smooth/12/60/600 1900/summer winter/both/689 .35 681 .1/3/.15/.55/0",
    "131": "Sardine/30/dart/1/12/600 1900/spring summer fall winter/both/683 .3/1/.65/.1/0",
    "132": "Bream/35/smooth/12/30/1800 2600/spring summer fall winter/both/684 .35/1/.45/.1/0",
    "136": "Largemouth Bass/50/mixed/11/30/600 1900/spring summer fall winter/both/685 .35/3/.4/.2/0",
    "137": "Smallmouth Bass/28/mixed/12/24/600 2600/spring fall/both/682 .2/1/.45/.1/0",
    "138": "Rainbow Trout/45/mixed/10/25/600 1900/summer/sunny/684 .35/2/.35/.3/0",
    "139": "Salmon/50/mixed/24/65/600 1900/fall/both/684 .35/3/.4/.2/0",
    "140": "Walleye/45/smooth/10/40/1200 2600/fall winter/rainy/680 .35/2/.4/.15/0",
    "141": "Perch/35/dart/10/24/600 2600/winter/both/683 .2/1/.45/.1/0",
    "142": "Carp/15/mixed/15/50/600 2600/spring summer fall/both/682 .2/1/.45/.1/0",
    "143": "Catfish/75/mixed/12/72/600 2400/spring fall winter/rainy/689 .4 680 .1/4/.4/.1/0",
    "144": "Pike/60/dart/15/60/600 2600/summer winter/both/690 .3 681 .1/3/.4/.15/0",
    "145": "Sunfish/30/mixed/5/15/600 1900/spring summer/sunny/683 .2/1/.45/.1/0",
    "146": "Red Mullet/55/smooth/8/22/600 1900/summer winter/both/680 .25/2/.4/.15/0",
    "147": "Herring/25/dart/8/20/600 2600/spring winter/both/685 .2/1/.45/.1/0",
    "148": "Eel/70/smooth/12/80/1600 2600/spring fall/rainy/689 .35 680 .1/3/.55/.1/0",
    "149": "Octopus/95/sinker/12/48/600 1300/summer/both/688 .6 684 .1/5/.1/.08/0",
    "150": "Red Snapper/40/mixed/8/25/600 1900/summer fall winter/rainy/682 .25/2/.45/.1/0",
    "151": "Squid/75/sinker/12/48/1800 2600/winter/both/690 .35 680 .1/3/.35/.3/0",
    "152": "Seaweed/5/floater/5/30/600 2600/spring summer fall winter/both/-1/0/.3/0/0",
    "153": "Green Algae/5/floater/5/30/600 2600/spring summer fall winter/both/-1/0/.3/0/0",
    "154": "Sea Cucumber/40/sinker/3/20/600 1900/fall winter/both/683 .2 689 .4/3/.25/.25/0",
    "155": "Super Cucumber/80/sinker/12/36/1800 2600/summer winter/both/683 .2 689 .4/4/.1/.25/0",
    "156": "Ghostfish/50/mixed/10/35/600 2600/spring summer fall winter/both/684 .35/2/.3/.3/0",
    "157": "White Algae/5/floater/5/30/600 2600/spring summer fall winter/both/-1/0/.3/0/0",
    "158": "Stonefish/65/sinker/15/15/600 2600/spring summer fall winter/both/689 .2/2/.1/.1/3",
    "159": "Crimsonfish/95/mixed/20/20/600 2000/winter/both/690 .15/4/.1/.1/5",
    "160": "Angler/85/smooth/18/18/600 2600/spring summer fall winter/both/690 .1/4/.05/.1/3",
    "161": "Ice Pip/85/dart/8/8/600 2600/spring summer fall winter/both/682 .1/2/.05/.1/5",
    "162": "Lava Eel/90/mixed/32/32/600 2600/spring summer fall winter/both/684 .1/2/.05/.1/7",
    "163": "Legend/110/mixed/50/50/600 2000/spring summer fall winter/rainy/688 .05/5/0/.1/10",
    "164": "Sandfish/65/mixed/8/24/600 2000/spring summer fall winter/both/682 .2/1/.65/.1/0",
    "165": "Scorpion Carp/90/dart/12/32/600 2000/spring summer fall winter/both/683 .4/2/.15/.1/4",
    "267": "Flounder/50/sinker/4/16/600 2000/spring summer/both/680 .25/2/.15/.05/0",
    "269": "Midnight Carp/55/mixed/12/52/2200 2600/fall winter/both/682 .2/1/.33/.1/0",
    "372": "Clam/trap/.15/681 .35/ocean/1/5",
    "682": "Mutant Carp/80/dart/36/36/600 2600/spring summer fall winter/both/688 .1/5/0/.02/0",
    "698": "Sturgeon/78/mixed/12/60/600 1900/summer winter/both/689 .35 682 .1/3/.35/.2/0",
    "699": "Tiger Trout/60/dart/10/20/600 1900/spring summer fall winter/both/688 .45 685 .2/3/.2/.1/0",
    "700": "Bullhead/46/smooth/12/30/600 2600/spring summer fall winter/both/681 .25/2/.35/.2/0",
    "701": "Tilapia/50/mixed/11/30/600 1400/summer fall/both/683 .35/3/.4/.2/0",
    "702": "Chub/35/dart/12/24/600 2600/spring summer fall winter/both/684 .35/1/.45/.1/0",
    "704": "Dorado/78/mixed/24/32/600 1900/summer/both/689 .35 681 .1/3/.15/.1/0",
    "705": "Albacore/60/mixed/20/40/600 1100 1800 2600/fall winter/both/685 .35/3/.3/.15/0",
    "706": "Shad/45/smooth/20/48/900 2600/spring summer fall/rainy/684 .35/2/.35/.2/0",
    "707": "Lingcod/85/mixed/30/50/600 2600/winter/both/690 .4 685 .2/3/.3/.05/0",
    "708": "Halibut/50/sinker/10/33/600 1100 1900 2600/spring summer winter/both/681 .35/3/.4/.2/0",
    "715": "Lobster/trap/.05/688 .45 689 .35 690 .35/ocean/2/20",
    "716": "Crayfish/trap/.35/682 .4/freshwater/1/8",
    "717": "Crab/trap/.1/684 .45/ocean/1/20",
    "718": "Cockle/trap/.3/680 .2/ocean/1/5",
    "719": "Mussel/trap/.35/683 .15/ocean/1/5",
    "720": "Shrimp/trap/.2/681 .35/ocean/1/3",
    "721": "Snail/trap/.25/680 .35/freshwater/1/5",
    "722": "Periwinkle/trap/.55/681 .35/freshwater/1/3",
    "723": "Oyster/trap/.15/682 .35/ocean/1/5",
    "734": "Woodskip/50/mixed/11/30/600 2600/spring summer fall winter/both/685 .35/3/.2/.1/0",
    "775": "Glacierfish/100/mixed/27/27/600 2000/winter/sunny/688 .1/5/0/.02/7",
    "795": "Void Salmon/80/mixed/24/65/600 2600/spring summer fall winter/both/685 .35/2/.33/.1/0",
    "796": "Slimejack/55/dart/8/25/600 2600/spring summer fall winter/both/685 .35/3/.4/.1/0",
    "798": "Midnight Squid/55/sinker/8/25/600 2600/spring summer fall winter/both/685 .35/3/.4/.1/0",
    "799": "Spook Fish/60/dart/8/25/600 2600/spring summer fall winter/both/685 .35/3/.4/.1/0",
    "800": "Blobfish/75/floater/8/25/600 2600/spring summer fall winter/both/685 .35/3/.4/.1/0",
    "836": "Stingray/80/sinker/18/60/600 2600/spring summer fall winter/both/685 .35/4/.2/.1/0",
    "837": "Lionfish/50/smooth/3/12/600 2600/spring summer fall winter/both/685 .35/3/.4/.1/0",
    "838": "Blue Discus/60/dart/2/9/600 2600/spring summer fall winter/both/685 .35/1/.25/.1/0",
    "898": "Son of Crimsonfish/95/mixed/20/20/600 2000/winter/both/690 .15/4/.1/.1/5",
    "899": "Ms. Angler/85/smooth/18/18/600 2600/spring summer fall winter/both/690 .1/4/.05/.1/3",
    "900": "Legend II/110/mixed/50/50/600 2000/spring summer fall winter/rainy/688 .05/5/0/.1/10",
    "901": "Radioactive Carp/80/dart/36/36/600 2600/spring summer fall winter/both/688 .1/5/0/.02/0",
    "902": "Glacierfish Jr./100/mixed/27/27/600 2000/winter/sunny/688 .1/5/0/.02/7",
}

fish = {}

trap_fish = set(["Clam", "Lobster", "Crayfish", "Crab", "Cockle", "Mussel", "Shrimp", "Snail", "Periwinkle", "Oyster"])
ignore = set(["Clam", "Son of Crimsonfish", "Legend II", "Radioactive Carp", "Glacierfish Jr.", "Ms. Angler"])

def upper_first(s: str) -> str:
    return s[0].upper() + s[1:]

def convert_time(time: str) -> str:
    return datetime.strptime(time, "%H%M%S").strftime("%-I%p")

with open("../raw_data/ObjectInformation.json", "r") as f:
    ObjInfo = json.load(f)

for key, value in content.items():
    
    fields = value.split("/")
    name = fields[0]
    if name in ignore: continue
    
    # look up the fish description from ObjectInformation.json
    description = ObjInfo["content"][key].split("/")[5]
    
    # find the icon url using BS4
    wiki_url = f"https://stardewvalleywiki.com/File:{name}.png"
    r = requests.get(wiki_url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    iconURL = soup.find("div", {"class": "fullImageLink"}).find("img")["src"]
    
    # find the locations by scraping the wiki article
    wiki_url = f"https://stardewvalleywiki.com/{name}"
    r = requests.get(wiki_url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    if name in trap_fish:
        locations = soup.find_all("td", {"id": "infoboxdetail"})[1].text.strip().split("\n")
    else:
        locations = soup.find_all("td", {"id": "infoboxdetail"})[1].text.strip().split(" • ")
    
    if name in trap_fish:
        location, min_size, max_size = fields[4], fields[5], fields[6]
        fish[name] = {
            "itemID": int(key),
            "name": name,
            "iconURL": "https://stardewvalleywiki.com" + iconURL,
            "trapFish": True,
            "description": description,
            "locations": locations,
            "minInch": int(min_size),
            "maxInch": int(max_size)
        }
        continue

    start_time = convert_time(fields[5].split(" ")[0])
    end_time = convert_time(fields[5].split(" ")[1])
    
    difficulty = f"{fields[1]} {fields[2]}"
    min_inch, max_inch = fields[3], fields[4]
    time = f"{start_time} - {end_time}"
    seasons = fields[6].split(" ")
    weather = fields[7]
    min_level = fields[12]
    
    fish[name] = {
        "itemID": int(key),
        "name": name,
        "iconURL": "https://stardewvalleywiki.com" + iconURL,
        "trapFish": False,
        "description": description,
        "locations": locations,
        "minInch": int(min_inch),
        "maxInch": int(max_inch),
        "difficulty": difficulty,
        "time": time,
        "seasons": [upper_first(season) for season in seasons],
        "weather": upper_first(weather),
        "minLevel": min_level
    }

with open("./data/fish.json", "w") as f:
    json.dump(fish, f, indent=4)