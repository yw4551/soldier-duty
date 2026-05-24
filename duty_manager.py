from utils import find_soldier_by_id, is_valid_day, is_valid_status
from data import data


def add_duty(soldier_id: int, duty_name: str, day: str, status: str) -> None:
    """
    Adds a duty to the system

    input:
    soldier_id
    duty_name
    day
    status

    output:
    None

    errors:
    KeyError if no soldier ID matches
    ValueError if day is Friday or Saturday
    ValueError if soldier booked already for a duty
    ValueError if status invalid
    """
    soldier = find_soldier_by_id(soldier_id)

    if not soldier:
        raise KeyError("Soldier ID not found!")
    elif not is_valid_day(day):
        raise ValueError("You can't add a duty on Friday or Saturday!")
    elif any(duty["name"] == duty_name for duty in soldier["duties"]):
        raise ValueError("Soldier is booked for this duty already!")
    elif not is_valid_status(status):
        raise ValueError("Status is invalid!")

    soldier["duties"].append({"name": duty_name, "day": day, "status": status})


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    Updates the status of a duty

    input:
    soldier_id
    duty_name
    new_status

    output:
    None

    errors:
    ValueError if invalid status
    KeyError if soldier or duty not in system
    """
    soldier = find_soldier_by_id(soldier_id)

    if not soldier:
        raise KeyError("Soldier not found!")
    elif not is_valid_status(new_status):
        raise ValueError("Invalid status!")

    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            duty["status"] = new_status
            return

    raise KeyError("Duty not found for this soldier!")


def get_soldier_duties(solider_id: int) -> list:
    """
    Gets the soldiers duty list

    input:
    soldier_id

    output:
    Soldier duty list

    errors:
    KeyError if soldier not in system
    """
    solider = find_soldier_by_id(solider_id)

    if not solider:
        raise KeyError("Solider not found!")

    return solider["duties"]


print(get_soldier_duties(12345))
update_duty_status(12345, "Test", "completed")
print(get_soldier_duties(12345))
