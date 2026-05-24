from data import data
from utils import is_valid_soldier_name, is_unique_id, find_soldier_by_id


def add_solder(solider_id: int, solider_name: str) -> None:
    """
    Adds a soldier to the system

    input:
    soldier_id
    name

    output:
    None

    errors:
    ValueError if ID used already in system or empty name
    """
    if not is_unique_id(solider_id):
        raise ValueError("You must have a unique ID!")
    elif is_valid_soldier_name(solider_name):
        raise ValueError("Soldier name can't be empty!")
    data.append({"id": solider_id, "name": solider_name, "duties": []})


def remove_soldier(solider_id) -> None:
    """
    Removes a soldier from the system

    input:
    soldier_id

    output:
    None

    errors:
    KeyError if ID not is system
    """
    if not find_soldier_by_id(solider_id):
        raise KeyError("Solider not find.")

    for index, soldier in enumerate(data):
        if soldier["id"] == solider_id:
            del data[index]
            return


def view_all_soldiers() -> None:
    """
    Returns a list with all solders in the system.

    input:
    None

    output:
    A list with all of the soldiers in the unit.

    errors:
    None
    """
    for soldier in data:
        print(soldier)
