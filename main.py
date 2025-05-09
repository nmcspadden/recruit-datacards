#!/usr/bin/env python3

import json
import sys
from typing import Any, Dict


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
        forces = json_data['roster']['forces']
        
        # Iterate through forces to find 'army roster'
        for force in forces:
            if force.get('name', '').lower() == 'army roster':
                print("Found army roster")
                
                # Iterate through selections, skipping specific items
                if 'selections' in force:
                    for selection in force['selections']:
                        selection_name = selection.get('name', '')
                        if selection_name in ["Show/Hide Options", "Detachment", "Battle Size"]:
                            continue
                        print(f"Selection: {selection_name}")
                break
        else:
            print("Army roster not found in forces")

    except (FileNotFoundError, json.JSONDecodeError):
        sys.exit(1)


if __name__ == "__main__":
    main()
