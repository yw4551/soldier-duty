def add_duty(id: int, duty_name: str, day: str, status: str) -> None:
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
    ValueError if solder booked already for a duty
    ValueError if status invalid
    """
    pass


def update_duty_status(id: int, duty_name: str, new_status: str) -> None:
    """
    Updates the status of a duty

    input:
    solder_id
    duty_name
    new_status

    output:
    None

    errors:
    ValueError if invalid status
    KeyError if duty not in system
    """
    pass


def get_soldier_duties(id: int) -> list:
    """
    Gets the soldiers duty list

    input:
    soldier_id

    output:
    Soldier duty list

    errors:
    KeyError if soldier not in system
    """
    pass
