from soldier_manager import add_solder, remove_soldier, view_all_soldiers
from duty_manager import add_duty, update_duty_status, get_soldier_duties
from data import data


def handle_add_soldier() -> None:
    """
    Handles the add soldier option

    input:
    None

    output:
    exception or success messages

    errors:
    catches ValueError, KeyError
    """
    try:
        soldier_id = int(input("Enter the soldiers ID: "))
        soldier_name = input("Enter the soldiers name: ")

        add_solder(soldier_id, soldier_name)
        print(f"Soldier {soldier_name}, ID: {soldier_id} added to system.")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_remove_soldier() -> None:
    """
    Handles the remove soldier option

    input:
    None

    output:
    exception or success messages

    errors:
    catches ValueError, KeyError
    """
    try:
        soldier_id = int(input("Enter the soldier ID you want to remove: "))

        remove_soldier(soldier_id)
        print(f"Soldier ID: {soldier_id} removed from system!")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def handle_view_soldiers() -> None:
    """
    Handles the view soldiers option

    input:
    None

    output:
    exception or success messages

    errors:
    None
    """
    view_all_soldiers()


def handle_add_duty() -> None:
    """
    Handles the add duty option

    input:
    None

    output:
    exception or success messages

    errors:
    catches ValueError, KeyError
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        duty_name = input("Enter the name of your duty: ")
        day = input("Enter the day of the duty (Sunday - thursday): ")
        status = "pending"

        add_duty(soldier_id, duty_name, day, status)
        print(f"Duty: {duty_name} added to soldier ID: {soldier_id} on day {day}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_update_status() -> None:
    """
    Handles the update duty status option

    input:
    None

    output:
    exception or success messages

    errors:
    catches ValueError, KeyError
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        duty_name = input("Enter the name of your duty: ")
        new_status = input("Enter your new status ('pending', 'completed', 'missed'): ")

        update_duty_status(soldier_id, duty_name, new_status)
        print(f"Duty {duty_name} status updated to {new_status}.")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


def handle_soldier_duty() -> None:
    """
    Handles the view soldier duty option

    input:
    None

    output:
    exception or success messages

    errors:
    None
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        print(get_soldier_duties(soldier_id))
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


def show_menu() -> None:
    """Shows the maim menu"""
    print("=========================")
    print("Soldier Management System")
    print("=========================")
    print("")
    print("=== Main Menu ===")
    print("")
    print("1. Add soldier")
    print("2. Remove soldier")
    print("3. View all soldiers")
    print("4. Add duty")
    print("5. Update duty status")
    print("6. View soldier duty")
    print("7. Exit")
    print()


def get_user_choice() -> str:
    try:
        choice = int(input("Enter your choice (number from 1 - 7): "))
        print(f"You choose {choice}")
        return choice
    except ValueError:
        return -1


def main():
    while True:
        show_menu()
        choice = get_user_choice()
        print(choice)

        if choice == 1:
            handle_add_soldier()
        elif choice == 2:
            handle_remove_soldier()
        elif choice == 3:
            handle_view_soldiers()
        elif choice == 4:
            handle_add_duty()
        elif choice == 5:
            handle_update_status()
        elif choice == 6:
            handle_soldier_duty()
        elif choice == 7:
            break
        else:
            print("Please enter a valid value")


if __name__ == "__main__":
    main()
