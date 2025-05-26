#!/usr/bin/env python3

import json
import sys
import uuid

# from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple


class ArmyForce:
    """Represents a force in the NR army JSON"""

    def __init__(self, file_path: str):
        self.nr_json_file_path: str = file_path
        # This will throw an exception if it fails
        # Now we need to parse the data from the New Recruit JSON file
        self.nr_json_data: Dict[str, Any] = read_json_file(self.nr_json_file_path)

        self.detachment: str = "Fake Detachment Force"
        self.units = list()  # List of Units
        self.points: int = 0  # Total points of the force
        self.side: str = "Imperium?"  # Flavor name of side
        self.faction: str = "Adeptus Astartes?"  # Flavor name of faction
        self.subfaction: str = "Megamarines"  # Flavor name of subfaction

        self.parse_nr_data()

    def parse_nr_data(self):
        """
        Get the detachment name from the index data.
        """
        # The path to the detachment is:
        # "roster" -> "forces" -> "selections" -> "selections" -> "group" = "Detachment"
        # In Test List.json, the Detachment is forces[0]["selections"][1]["selections"][0]["group"] = "Detachment"
        for force in self.nr_json_data["roster"]["forces"]:
            catalogue_name_raw: str = force.get("catalogueName", "")
            catalogue_parts = catalogue_name_raw.split(" - ")
            self.side = catalogue_parts[0]
            self.faction = catalogue_parts[1]
            self.subfaction = catalogue_parts[2]
            print(f"Side: {self.side}")
            print(f"Faction: {self.faction}")
            print(f"Subfaction: {self.subfaction}")

            for selection in force["selections"]:
                item_name = selection.get("name", "")
                if item_name.lower() == "show/hide options":
                    continue
                for new_selection in selection["selections"]:
                    if new_selection.get("group", "").lower() == "detachment":
                        self.detachment = new_selection["name"]
                        print(f"Detachment name: {self.detachment}")
                    elif new_selection.get("group", "").lower() == "battle size":
                        self.battle_size = new_selection["name"]
                        print(f"Battle Size: {self.battle_size}")
                if (
                    item_name.lower() == "battle size"
                    or item_name.lower() == "detachment"
                ):
                    # We already got these earlier
                    continue

                print(f"* {item_name}")
                # Now we are actually looking through the army
                # TODO: Things we need to actually inspect:
                # - Wargear Selections
                # - Unit Size
                # - Leading/Attachment
                for selection in selection["selections"]:
                    print(f"** {selection['name']}: {selection['number']}")

    def print_nr_army(self):
        """
        Print the army list from the New Recruit data.
        """
        force = self.nr_json_data["roster"]["forces"][0]
        # Iterate through forces to find 'army roster'
        if force.get("name", "").lower() != "army roster":
            print("Couldn't find army roster!")
            sys.exit(1)

        # Iterate through selections, skipping specific items
        # if "selections" in force:
        # The first one is typically "Battle Size"
        # for selection in force["selections"]:
        # item_name = selection.get("name", "")
        # if item_name == "Battle Size":
        #     print(f"Battle Size: {selection['selections'][0]['name']}")
        #     continue
        # if item_name == "Detachment":
        #     print(f"Detachment: {selection['selections'][0]['name']}")
        #     continue
        # if item_name == "Show/Hide Options":
        #     continue

        # print(f"* {item_name}")
        # # Now we are actually looking through the army
        # # Things we need to actually inspect:
        # # - Wargear Selections
        # # - Unit Size
        # # - Leading/Attachment
        # for selection in selection["selections"]:
        #     print(f"** {selection['name']}: {selection['number']}")


class Unit:
    def __init__(self, name: str):
        self.abilities: List[Any] = (
            list(),
        )  # TODO: figure out the data structure for this
        self.composition: List[str] = (
            list(),
        )  # TODO: text description of unit makeup; each index is a line
        self.factions: List[str] = (
            list(),
        )  # TODO: list of factions this belongs to; each index is a line
        self.faction_id: str = (
            "faction_id",
        )  # TODO: hardcoded list of possible faction ids
        self.fluff: str = "fluff"  # flavor text
        self.keywords: List[str] = (
            list(),
        )  # TODO: list of unit keywords; each index is a keyword
        self.leader: str = ""  # leader assigned? Not sure what this refers to
        self.loadout: str = "loadout fluff"  # flavor text explaining default loadouts
        self.meleeWeapons: List[Any] = (list(),)  # TODO: figure out data structure
        self.name: str = name  # Actual name of unit
        self.points: List[Points] = ([],)  # TODO: this needs a CARD data type


class DataCardShell:
    def __init__(self, name: Optional[str]):
        self.category: Dict[str, Any] = (
            {
                "uuid": uuid.uuid4(),
                "name": name,
                "type": "list",
                "closed": False,
                "cards": list(),  # TODO: fill out cards
            },
        )
        self.created_at: str = ("some_date",)  # generate a timestamp
        self.version: str = ("2.9.3",)
        self.website: str = "https://game-datacards.eu"


class Points:
    """Arbitrary structure used to represent the point costs of a unit"""

    def __init__(self, cost_grouping: Optional[Tuple[str, str]]):
        # These are fake values that should never be used, which means it's missing data
        self.cost = ("10000",)
        self.models: "500"
        if cost_grouping:
            self.cost = (cost_grouping[0],)
            self.model_count = cost_grouping[1]
        # The following seem to be fixed values and shouldn't be changed
        self.keyword = (None,)
        self.active: bool = (True,)


class UnitStats:
    """The basic stat line of a data sheet"""

    def __init__(
        self,
        move: str,
        toughness: str,
        save: str,
        weapon: str,
        leadership: str,
        objctrl: str,
        name: str,
    ):
        self.name = (name,)
        self.m = (move,)
        self.t = (toughness,)
        self.sv = (save,)
        self.w = (weapon,)
        self.ld = (leadership,)
        self.oc = objctrl


class Card:
    def __init__(self, name: Optional[str]):
        self.abilities: List[Any] = (
            list(),
        )  # TODO: figure out the data structure for this
        self.cardType: str = ("DataCard",)
        self.composition: List[str] = (
            list(),
        )  # TODO: description of unit makeup; each index is a line
        self.factions: List[str] = (
            list(),
        )  # TODO: list of factions this belongs to; each index is a line
        self.faction_id: str = (
            "faction_id",
        )  # TODO: hardcoded list of possible faction ids
        self.fluff: str = "fluff"  # flavor text
        self.id: str = (uuid.uuid4(),)
        self.keywords: List[str] = (
            list(),
        )  # TODO: list of unit keywords; each index is a keyword
        self.leader: str = ""  # leader assigned? Not sure what this refers to
        self.loadout: str = "loadout fluff"  # flavor text explaining default loadouts
        self.meleeWeapons: List[Any] = (list(),)  # TODO: figure out data structure
        self.name: str = name  # Actual name of unit
        self.points: List[Points] = ([],)  # TODO: this needs a CARD data type
        self.rangedWeapons: List[Any] = list()  # TODO: figure out this data structure
        self.source = ("40k-10e",)
        self.stats: List[UnitStats] = (
            list()
        )  # TODO: this is essentially the data sheet stats
        self.transport: str = (
            ""  # If this is a transport, there will be transport text here
        )
        self.wargear: List[str] = (
            list()
        )  # Each index is a line of text about its wargear
        self.variant: Optional[str] = (
            None  # no idea what this actually means, it's either "double" or empty
        )
        self.leadBy: List[str] = list()  # List of unit names this can be led by

    # @classmethod
    # def from_dict(cls, data: Dict[str, Any]) -> "DataCardShell":
    #     """Create a DataCard instance from a dictionary."""
    #     return cls(
    #         id=data["id"],
    #         name=data["name"],
    #         description=data["description"],
    #         type=data["type"],
    #         status=data["status"],
    #         created_at=datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00")),
    #         updated_at=datetime.fromisoformat(data["updatedAt"].replace("Z", "+00:00")),
    #         created_by=data["createdBy"],
    #         updated_by=data["updatedBy"],
    #         tags=data.get("tags", []),
    #         metadata=data.get("metadata", {}),
    #     )

    # def to_dict(self) -> Dict[str, Any]:
    #     """Convert the DataCard instance to a dictionary."""
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #         "type": self.type,
    #         "status": self.status,
    #         "createdAt": self.created_at.isoformat() + "Z",
    #         "updatedAt": self.updated_at.isoformat() + "Z",
    #         "createdBy": self.created_by,
    #         "updatedBy": self.updated_by,
    #         "tags": self.tags,
    #         "metadata": self.metadata,
    #     }


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read and parse a JSON file.

    Args:
        file_path (str): Path to the JSON file

    Returns:
        Dict[str, Any]: Parsed JSON data

    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}': {str(e)}")
        raise


def find_gd_detachment_index(
    index_db: Dict[str, Any], detachment_name: str
) -> Optional[int]:
    """
    Perform a deep search through the index_db for a matching detachment, then return the index of it.

    Args:
        index_db (Dict[str, Any]): The index_db from the GD export keyvaluepairs key
        detachment_name (str): The name of the detachment to search for

    Returns:
        Optional[int]: The matching index of the indexdb data if found, None otherwise
    """
    # Convert target to lowercase for case-insensitive comparison
    target = detachment_name.lower()

    if "data" not in index_db:
        print("This is not a valid index_db keyvaluepair; it must contain a 'data' key")
        return None

    # First check if this dict has a detachments key
    index = 0
    for army in index_db["data"]:
        # Search through the detachments list
        for detachment in army["detachments"]:
            if detachment.lower() == target:
                print(f"Found detachment: {detachment} at index {index}")
                return index
        index += 1
    return None


def read_index_json(file_path: str) -> Dict[str, Any]:
    """
    Read and parse the IndexDB JSON file.
    """
    gd_json_data: Dict[str, Any] = read_json_file("GD-Exported-Data.json")
    print("Successfully read IndexDB file")
    # As of 5/24/25, this contains two keyvaluepairs - two separate versions.
    # The second index has the later version, so we'll just hardcode it for now.
    return gd_json_data["keyvaluepairs"][1]


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <New Recruit json_file_path>")
        sys.exit(1)

    # First, read in the IndexDB Exported Data from GD
    try:
        index_db = read_index_json("GD-Exported-Data.json")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldn't read the IndexDB file exported from Game-Datacards")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        army_force = ArmyForce(file_path)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldn't read the New Recruit file")
        sys.exit(1)

    print("**********")
    print("Now comparing Detachment to Game-Datacards Export Data")
    # The best way to figure out which faction we have in
    # common between NR and GD is the Detachment
    if army_force.detachment:
        detachment_index = find_gd_detachment_index(index_db, army_force.detachment)
        if detachment_index:
            print(f"Found matching detachment data: {detachment_index}")
        else:
            print(f"No matching detachment data found for {detachment_index}")
    else:
        print("No detachment name provided")

    # print("Printing New Recruit army:")
    # print_nr_army(nr_json_data)


if __name__ == "__main__":
    main()
