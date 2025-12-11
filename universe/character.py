def init_character(last_name, first_name, attributes):
    """
    Initialize a character with the given parameters
    Arg:
        last_name (str): The character's last name
        first_name (str): The character's first name
        attributes (dict): Dictionary containing character attribute
    Return:
        dict: The initialized character dictionary
    """
    return {
        "Last Name": str(last_name),
        "First Name": str(first_name),
        "Inventory": [],  # blanck inventory
        "Spells": [],  #no spells
        "Attributes": dict(attributes)  # Make a copy of the attributes
        "Money": 100,  #starting money
    }


def display_character(character):
    """
    Display the character's information in a formatted way.
    Arg:
        character (dict): The character to display
    """
    print("Character profile:")
    print(f"Last name: {character['Last Name']}")
    print(f"First name: {character['First Name']}")
    print(f"Money: {character['Money']} galleons")

    # show inventory
    print("Inventory:", ", ".join(character['Inventory']) if character['Inventory'] else "Empty")

    # spells
    print("Spells:", ", ".join(character['Spells']) if character['Spells'] else "No spells learned")

    # attributes
    print("Attributes:")
    for attr, value in character['Attributes'].items():

        print(f"- {attr}: {value}")


def modify_money(character, amount):
    """
    Modify the character's money
    Arg:
        character (dict): The character to modify
        amount (int): The amount to add or substract
    """
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")
    character['Money'] += amount


def add_item(character, key, item):
    """
    Add an item or spell to the character's inventory or spells list.
    Args:
        character (dict):the character to modify
        key (str): Either'inventory' or 'spells'
        item (str): The item or spell to add
    """
    if key not in ['Inventory', 'Spells']:
        raise ValueError("Key must be either 'Inventory' or 'Spells'")
    character[key].append(str(item))