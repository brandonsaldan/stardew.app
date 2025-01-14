import fish from "../../research/processors/data/fish.json";

type fishID = string;

interface ReturnType {
  totalCaught: number;
  uniqueCaught: number;
  allFish: Record<fishID, boolean>;
}

export function parseFishing(json: any): ReturnType {
  /* 
    Achievements Relevant:
      - Mother Catch (catch 100 total fish).
      - Fisherman (catch 10 different fish).
      - Ol' Mariner (catch 24 different fish).
      - Master Angler (catch every type of fish).
  */
  const totalCaught = json.SaveGame.player.stats.fishCaught;
  let uniqueCaught = 0;

  // get a list of all the fish possible and initialize it to all false for caught
  const allFish: Record<fishID, boolean> = {};
  for (const key in fish) {
    let itemID = fish[key as keyof typeof fish]["itemID"].toString() as fishID;
    allFish[itemID] = false;
  }

  if (totalCaught === 0) {
    return {
      totalCaught,
      uniqueCaught,
      allFish,
    };
  }

  // check to see if there are multiple types of fish caught
  if (typeof json.SaveGame.player.fishCaught.item.key === "undefined") {
    // multiple types of fish caught
    for (const idx in json.SaveGame.player.fishCaught.item) {
      let fish = json.SaveGame.player.fishCaught.item[idx];
      let itemID = fish.key.int.toString() as fishID;

      // some things you can catch but aren't fish or don't count towards the achievement
      // like the fish you catch on Mr. Qi's quest or trash
      if (!allFish.hasOwnProperty(itemID)) continue;
      allFish[itemID] = true;
      uniqueCaught++;
    }
  } else {
    // only one type caught
    let fish = json.SaveGame.player.fishCaught.item;
    let itemID = fish.key.int.toString() as fishID;

    if (!allFish.hasOwnProperty(itemID))
      return { totalCaught, uniqueCaught, allFish };

    allFish[itemID] = true;
    uniqueCaught++;
  }

  return {
    totalCaught,
    uniqueCaught,
    allFish,
  };
}
