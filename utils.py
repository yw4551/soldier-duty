from data import data, duty_types


def find_soldier_by_id(id: int) -> dict | None:
    """
    Gets the soldiers dict from the data

    input:
    soldier_id

    output:
    A dict with all the soldiers data or None if not found

    errors:
    None
    """
    for solder in data:
        if solder["id"] == id:
            return solder
    raise KeyError("The soldier is not in the system")


def is_valid_day(day: str) -> bool:
    """
    Validates the day is between sunday and Thursday

    input:
    day

    output:
    True if valid else False

    errors:
    None
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

    return day.title() in days


def is_status_valid(status: str) -> bool:
    """
    Validates the status

    input:
    status

    output:
    True is valid else False

    errors:
    None
    """
    statuses = ["pending", "completed", "missed"]

    return status in statuses


def is_valid_duty_name(name: str) -> bool:
    """
    Validates the duty name

    input:
    duty_name

    output:
    True is valid else False

    errors:
    None
    """
    return name in duty_types


print(is_valid_duty_name("Gate guard"))
