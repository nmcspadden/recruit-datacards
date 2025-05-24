#!/usr/bin/env python3

import json
import sys
import uuid

# from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple


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
        self.faction_id: str = "faction_id",  # TODO: hardcoded list of possible faction ids
        self.fluff: str = "fluff"  # flavor text
        self.keywords: List[str] = (
            list(),
        )  # TODO: list of unit keywords; each index is a keyword
        self.leader: str = "" # leader assigned? Not sure what this refers to
        self.loadout: str = "loadout fluff"  # flavor text explaining default loadouts
        self.meleeWeapons: List[Any] = (list(),)  # TODO: figure out data structure
        self.name: str = name  # Actual name of unit
        self.points: List[Points] = [], #TODO: this needs a CARD data type


class DataCardShell:
    def __init__(self, name: Optional[str]):
        self.category: Dict[str, Any] = (
            {
                "uuid": uuid.uuid4(),
                "name": name,
                "type": "list",
                "closed": False,
                "cards": list(), #TODO: fill out cards
            },
        )
        self.created_at: str = ("some_date",)  # generate a timestamp
        self.version: str = ("2.9.3",)
        self.website: str = "https://game-datacards.eu"

class Points:
    """Arbitrary structure used to represent the point costs of a unit"""
    def __init__(self, cost_grouping: Optional[Tuple[str, str]]):
        # These are fake values that should never be used, which means it's missing data
        self.cost = "10000",
        self.models: "500"
        if cost_grouping:
            self.cost = cost_grouping[0],
            self.model_count = cost_grouping[1]
        # The following seem to be fixed values and shouldn't be changed
        self.keyword = None,
        self.active: bool = True,


class UnitStats:
    """The basic stat line of a data sheet"""
    def __init__(self, move: str, toughness: str, save: str, weapon: str, leadership: str, objctrl: str, name: str):
        self.name = name,
        self.m = move,
        self.t = toughness,
        self.sv = save,
        self.w = weapon,
        self.ld = leadership,
        self.oc = objctrl


class Card:
    def __init__(self, name: Optional[str]):
        self.abilities: List[Any] = (
            list(),
        )  # TODO: figure out the data structure for this
        self.cardType: str = "DataCard",
        self.composition: List[str] = (
            list(),
        )  # TODO: description of unit makeup; each index is a line
        self.factions: List[str] = (
            list(),
        )  # TODO: list of factions this belongs to; each index is a line
        self.faction_id: str = "faction_id",  # TODO: hardcoded list of possible faction ids
        self.fluff: str = "fluff"  # flavor text
        self.id: str = (uuid.uuid4(),)
        self.keywords: List[str] = (
            list(),
        )  # TODO: list of unit keywords; each index is a keyword
        self.leader: str = "" # leader assigned? Not sure what this refers to
        self.loadout: str = "loadout fluff"  # flavor text explaining default loadouts
        self.meleeWeapons: List[Any] = (list(),)  # TODO: figure out data structure
        self.name: str = name  # Actual name of unit
        self.points: List[Points] = [], #TODO: this needs a CARD data type
        self.rangedWeapons: List[Any] = list() # TODO: figure out this data structure
        self.source = "40k-10e",
        self.stats: List[UnitStats] = list() # TODO: this is essentially the data sheet stats
        self.transport: str = "" # If this is a transport, there will be transport text here
        self.wargear: List[str] = list() # Each index is a line of text about its wargear
        self.variant: Optional[str] = None # no idea what this actually means, it's either "double" or empty
        self.leadBy: List[str] = list() # List of unit names this can be led by



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


def main():
    """
    Main function to read and process a JSON file.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <json_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        # Store the JSON data in a dictionary
        json_data: Dict[str, Any] = read_json_file(file_path)
        print("Successfully read JSON file")
        # print(json.dumps(json_data, indent=2))

        # Now you can use json_data dictionary throughout your program
        # For example:
        # print(json_data.keys())  # Print all top-level keys
        # print(json_data['roster'])  # Access specific data
        # print(json.dumps(json_data['roster'], indent=2))

        # Looking for specific data in the JSON file
        force = json_data["roster"]["forces"][0]

        # Iterate through forces to find 'army roster'
        if force.get("name", "").lower() != "army roster":
            print("Couldn't find army roster!")
            sys.exit(1)

        # Iterate through selections, skipping specific items
        if "selections" in force:
            # The first one is typically "Battle Size"
            for selection in force["selections"]:
                item_name = selection.get("name", "")
                if item_name == "Battle Size":
                    print(f"Battle Size: {selection['selections'][0]['name']}")
                    continue
                if item_name == "Detachment":
                    print(f"Detachment: {selection['selections'][0]['name']}")
                    continue
                if item_name == "Show/Hide Options":
                    continue

                print(f"* {item_name}")
                # Now we are actually looking through the army
                # Things we need to actually inspect:
                # - Wargear Selections
                # - Unit Size
                # - Leading/Attachment
                for selection in selection["selections"]:
                    print(f"** {selection['name']}: {selection['number']}")



    except (FileNotFoundError, json.JSONDecodeError):
        sys.exit(1)


if __name__ == "__main__":
    main()
