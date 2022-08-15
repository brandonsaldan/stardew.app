import type { NextPage } from "next";
import type { Fish } from "../types";

import objects from "../research/processors/data/objects.json";
import shipping from "../research/processors/data/shipment.json";
import sprites from "../research/processors/data/sprites.json";
import achievements from "../research/processors/data/achievements.json";

import FishCard from "../components/fishing/fishcard";
import AchievementCard from "../components/achievementcard";
import InfoCard from "../components/infocard";
import SidebarLayout from "../components/sidebarlayout";

import { useState } from "react";
import Head from "next/head";

import { FilterIcon } from "@heroicons/react/outline";
import FishSlideOver from "../components/fishing/fishslideover";
import { useKV } from "../hooks/useKV";
import { InformationCircleIcon } from "@heroicons/react/solid";

// a mapping of achievements and their requirements
const requirements: Record<string, number> = {
  Fisherman: 10,
  "Ol' Mariner": 24,
  "Master Angler": 67,
};

const Shipping: NextPage = () => {
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(false);
  //   const [showFish, setShowFish] = useState<boolean>(false);
  const [name] = useKV("general", "name", "Farmer");
  //   const [totalFishCaught] = useKV("fish", "totalFishCaught", 0);
  //   const [uniqueCaught] = useKV("fish", "uniqueCaught", 0);
  //   const [selectedFish, setSelectedFish] = useState<Fish>(
  //     Object.values(fishes)[0]
  //   );

  return (
    <>
      <Head>
        <title>stardew.app | Shipping</title>
      </Head>
      <SidebarLayout
        activeTab="Shipping"
        sidebarOpen={sidebarOpen}
        setSidebarOpen={setSidebarOpen}
      >
        <div className="mx-auto flex max-w-screen-2xl flex-shrink-0 items-center justify-between px-4 sm:px-6 md:px-8">
          <h1 className="text-2xl font-semibold text-gray-900 dark:text-white">
            Shipping
          </h1>
        </div>
        <div className="mx-auto max-w-screen-2xl px-4 sm:px-6 md:px-8">
          <div>
            <h2 className="my-2 text-lg font-semibold text-gray-900 dark:text-white">
              Achievements
            </h2>
            <InfoCard
              title={`${name} has shipped \${put the items number here} items.`}
              Icon={InformationCircleIcon}
            />
            <div className="mt-4 grid grid-cols-2 gap-4 xl:grid-cols-3">
              {Object.values(achievements)
                .filter((achievement) => achievement.category === "shipping")
                .map((achievement) => (
                  <AchievementCard
                    id={achievement.id}
                    tag={"achievements"}
                    key={achievement.id}
                    title={achievement.name}
                    description={achievement.description}
                    sourceURL={achievement.iconURL}
                    // initialChecked={
                    //   achievement.name === "Mother Catch"
                    //     ? totalFishCaught >= 100
                    //     : uniqueCaught >= requirements[achievement.name]
                    // }
                  />
                ))}
            </div>
          </div>
          <h2 className="mt-4 text-lg font-semibold text-gray-900 dark:text-white">
            All Items to Ship
          </h2>
          <div className="grid grid-cols-1 gap-4 py-4 sm:grid-cols-2 xl:grid-cols-4">
            {Object.entries(shipping).map(([id, name]) => (
              <AchievementCard
                key={id}
                title={name}
                description={
                  Object.entries(objects).find(([oId, obj]) => oId === id)?.[1]
                    .description!
                }
                sourceURL={sprites[id as keyof typeof sprites]!}
                tag={"shipping"}
                id={id}
              />
            ))}
          </div>
        </div>
      </SidebarLayout>
    </>
  );
};

export default Shipping;