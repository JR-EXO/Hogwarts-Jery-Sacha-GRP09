def init_character(last_name, first_name, attributes):
    """
    Initialize a character with the given parameters.

    Args:
        last_name (str): The character's last name
        first_name (str): The character's first name
        attributes (dict): Dictionary containing character attributes

    Returns:
        dict: The initialized character dictionary
    """
    return {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "Money": 100,  # Starting money is 100 galleons
        "Inventory": [],  # Empty inventory
        "Spells": [],  # No spells initially
        "Attributes": dict(attributes)  # Make a copy of the attributes
    }


def display_character(character):
    """
    Display the character's information in a formatted way.

    Args:
        character (dict): The character to display
    """
    print("Character profile:")
    print(f"Last name: {character['Last Name']}")
    print(f"First name: {character['First Name']}")
    print(f"Money: {character['Money']} galleons")

    # Display inventory
    print("Inventory:", ", ".join(character['Inventory']) if character['Inventory'] else "Empty")

    # Display spells
    print("Spells:", ", ".join(character['Spells']) if character['Spells'] else "No spells learned")

    # Display attributes
    print("Attributes:")
    for attr, value in character['Attributes'].items():
        print(f"- {attr}: {value}")


def modify_money(character, amount):
    """
    Modify the character's money by the specified amount.

    Args:
        character (dict): The character to modify
        amount (int): The amount to add (positive or negative)
    """
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")
    character['Money'] += amount


def add_item(character, key, item):
    """
    Add an item or spell to the character's inventory or spells list.

    Args:
        character (dict): The character to modify
        key (str): Either 'Inventory' or 'Spells'
        item (str): The item or spell to add
    """
    if key not in ['Inventory', 'Spells']:
        raise ValueError("Key must be either 'Inventory' or 'Spells'")
    character[key].append(str(item))