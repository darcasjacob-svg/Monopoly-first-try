import random


def roll_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


board = [
    {'name': 'Go', 'type': 'go'},
    {'name': 'Mediterranean Avenue', 'type': 'property', 'price': 60, 'rent': 2, 'color_group': 'brown'},
    {'name': 'Community Chest', 'type': 'community chest'},
    {'name': 'Baltic Avenue', 'type': 'property', 'price': 60, 'rent': 4, 'color_group': 'brown'},
    {'name': 'Income Tax', 'type': 'tax', 'amount': 200},
    {'name': 'Reading Railroad', 'type': 'railroad', 'price': 200, 'rent': 25},
    {'name': 'Oriental Avenue', 'type': 'property', 'price': 100, 'rent': 6, 'color_group': 'light blue'},
    {'name': 'Chance', 'type': 'chance'},
    {'name': 'Vermont Avenue', 'type': 'property', 'price': 100, 'rent': 6, 'color_group': 'light blue'},
    {'name': 'Connecticut Avenue', 'type': 'property', 'price': 120, 'rent': 8, 'color_group': 'light blue'},
    {'name': 'Jail', 'type': 'jail'},
    {'name': 'St. Charles Place', 'type': 'property', 'price': 140, 'rent': 10, 'color_group': 'pink'},
    {'name': 'Electric Company', 'type': 'utility', 'price': 150, 'rent': None},
    {'name': 'States Avenue', 'type': 'property', 'price': 140, 'rent': 10, 'color_group': 'pink'},
    {'name': 'Virginia Avenue', 'type': 'property', 'price': 160, 'rent': 12, 'color_group': 'pink'},
    {'name': 'Pennsylvania Railroad', 'type': 'railroad', 'price': 200, 'rent': 25},
    {'name': 'St. James Place', 'type': 'property', 'price': 180, 'rent': 14, 'color_group': 'orange'},
    {'name': 'Community Chest', 'type': 'community chest'},
    {'name': 'Tennessee Avenue', 'type': 'property', 'price': 180, 'rent': 14, 'color_group': 'orange'},
    {'name': 'New York Avenue', 'type': 'property', 'price': 200, 'rent': 16, 'color_group': 'orange'},
    {'name': 'Free Parking', 'type': 'free parking'},
    {'name': 'Kentucky Avenue', 'type': 'property', 'price': 220, 'rent': 18, 'color_group': 'red'},
    {'name': 'Chance', 'type': 'chance'},
    {'name': 'Indiana Avenue', 'type': 'property', 'price': 220, 'rent': 18, 'color_group': 'red'},
    {'name': 'Illinois Avenue', 'type': 'property', 'price': 240, 'rent': 20, 'color_group': 'red'},
    {'name': 'B. & O. Railroad', 'type': 'railroad', 'price': 200, 'rent': 25},
    {'name': 'Atlantic Avenue', 'type': 'property', 'price': 260, 'rent': 22, 'color_group': 'yellow'},
    {'name': 'Ventnor Avenue', 'type': 'property', 'price': 260, 'rent': 22, 'color_group': 'yellow'},
    {'name': 'Water Works', 'type': 'utility', 'price': 150, 'rent': None},
    {'name': 'Marvin Gardens', 'type': 'property', 'price': 280, 'rent': 24, 'color_group': 'yellow'},
    {'name': 'Go To Jail', 'type': 'go to jail'},
    {'name': 'Pacific Avenue', 'type': 'property', 'price': 300, 'rent': 26, 'color_group': 'green'},
    {'name': 'North Carolina Avenue', 'type': 'property', 'price': 300, 'rent': 26, 'color_group': 'green'},
    {'name': 'Community Chest', 'type': 'community chest'},
    {'name': 'Pennsylvania Avenue', 'type': 'property', 'price': 320, 'rent': 28, 'color_group': 'green'},
    {'name': 'Short Line', 'type': 'railroad', 'price': 200, 'rent': 25},
    {'name': 'Chance', 'type': 'chance'},
    {'name': 'Park Place', 'type': 'property', 'price': 350, 'rent': 35, 'color_group': 'dark blue'},
    {'name': 'Luxury Tax', 'type': 'tax', 'amount': 75},
    {'name': 'Boardwalk', 'type': 'property', 'price': 400, 'rent': 50, 'color_group': 'dark blue'}
]


class Player:
    def __init__(self, name, money=1500, position=0):
        self.name = name
        self.money = money
        self.position = position
        self.properties = []


def move_player(player, steps):
    """Moves the player on the board based on the number of steps."""
    old_position = player.position
    new_position = (player.position + steps) % len(board)
    player.position = new_position


    # Check if the player passed or landed on Go
    if new_position < old_position:
        print(f"{player.name} passed Go! Collect $200.")
        player.money += 200
    elif new_position == 0 and old_position != 0:
         print(f"{player.name} landed on Go! Collect $200.")
         player.money += 200


    print(f"{player.name} moved {steps} steps to {board[player.position]['name']}.")


def handle_square(player, board):
    """Handles the action when a player lands on a square."""
    current_square = board[player.position]
    print(f"{player.name} landed on {current_square['name']}.")


    if current_square['type'] == 'property' or current_square['type'] == 'railroad' or current_square['type'] == 'utility':
        if 'owner' not in current_square:
            # Property is unowned
            if player.money >= current_square['price']:
                buy_choice = input(f"Do you want to buy {current_square['name']} for ${current_square['price']}? (yes/no): ")
                if buy_choice.lower() == 'yes':
                    player.money -= current_square['price']
                    current_square['owner'] = player
                    player.properties.append(current_square)
                    print(f"{player.name} bought {current_square['name']}.")
                else:
                    print(f"{player.name} decided not to buy {current_square['name']}.")
            else:
                print(f"{player.name} cannot afford {current_square['name']}.")
        else:
            # Property is owned
            owner = current_square['owner']
            if owner != player:
                rent = current_square['rent'] # Basic rent for now
                if current_square['type'] == 'utility':
                     # Basic utility rent (e.g., 4 times dice roll for one utility, 10 times for two)
                     # For simplicity in this basic version, we'll just use a placeholder or base rent if available.
                     # A more complex version would need access to the last dice roll and the owner's other utilities.
                     print("Utility rent calculation is more complex and not fully implemented in this basic version.")
                     if rent is None: # Use a placeholder rent if rent is not defined for utility
                         rent = 50 # Example placeholder rent
                         print(f"Using a placeholder rent of ${rent}.")
                elif current_square['type'] == 'railroad':
                     # Basic railroad rent increases with the number of railroads owned.
                     # For simplicity, using base rent here. A more complex version would count owned railroads.
                     print("Railroad rent calculation depends on the number of railroads owned and is not fully implemented in this basic version.")
                     pass # Will use the base rent already assigned to 'rent'


                print(f"{player.name} pays ${rent} rent to {owner.name}.")
                player.money -= rent
                owner.money += rent
            else:
                print(f"{player.name} owns {current_square['name']}.")


    elif current_square['type'] == 'tax':
        print(f"{player.name} pays ${current_square['amount']} in tax.")
        player.money -= current_square['amount']


    elif current_square['type'] == 'chance' or current_square['type'] == 'community chest':
        print(f"{player.name} draws a {current_square['type']} card (card logic not implemented yet).")
        # Card drawing logic will be implemented later


    elif current_square['type'] == 'go to jail':
        print(f"{player.name} goes to Jail.")
        player.position = 10 # Assuming Jail is at index 10
        # Additional logic for being in jail would be needed here (e.g., turns in jail)


    elif current_square['type'] == 'jail':
        print(f"{player.name} is just visiting Jail.")


    elif current_square['type'] == 'free parking':
        print(f"{player.name} is on Free Parking.")


    elif current_square['type'] == 'go':
        # Handled by move_player function
        pass


    else:
        print(f"Unknown square type: {current_square['type']}")
import time


# Initialize players
players = [Player('Player 1'), Player('Player 2')]


def can_mortgage(property):
    """Checks if a property can be mortgaged."""
    return property['type'] in ['property', 'railroad', 'utility'] and property.get('mortgaged') is not True


def mortgage_property(player, property):
    """Mortgages a property for the player."""
    if can_mortgage(property):
        mortgage_value = property['price'] // 2
        player.money += mortgage_value
        property['mortgaged'] = True
        print(f"{player.name} mortgaged {property['name']} for ${mortgage_value}.")
    else:
        print(f"{property['name']} cannot be mortgaged.")


def unmortgage_property(player, property):
    """Unmortgages a property for the player."""
    if property.get('mortgaged') is True:
        unmortgage_cost = int(property['price'] // 2 * 1.1) # Mortgage value + 10% interest
        if player.money >= unmortgage_cost:
            player.money -= unmortgage_cost
            property['mortgaged'] = False
            print(f"{player.name} unmortgaged {property['name']} for ${unmortgage_cost}.")
        else:
            print(f"{player.name} does not have enough money to unmortgage {property['name']}. Cost: ${unmortgage_cost}.")
    else:
        print(f"{property['name']} is not mortgaged.")


# Start the game loop
turn_limit = 2000 # Simple placeholder to end the game
turn_count = 0


def handle_square(player, board):
    """Handles the action when a player lands on a square."""
    current_square = board[player.position]
    print(f"{player.name} landed on {current_square['name']}.")


    if current_square['type'] in ['property', 'railroad', 'utility']:
        if 'owner' not in current_square:
            # Property is unowned
            if player.money >= current_square['price']:
                buy_choice = input(f"Do you want to buy {current_square['name']} for ${current_square['price']}? (yes/no): ")
                if buy_choice.lower() == 'yes':
                    player.money -= current_square['price']
                    current_square['owner'] = player
                    player.properties.append(current_square)
                    print(f"{player.name} bought {current_square['name']}.")
                else:
                    print(f"{player.name} decided not to buy {current_square['name']}.")
            else:
                print(f"{player.name} cannot afford {current_square['name']}.")
        else:
            # Property is owned
            owner = current_square['owner']
            if owner != player:
                if current_square.get('mortgaged') is True:
                    print(f"{current_square['name']} is mortgaged. No rent is due.")
                else:
                    rent = current_square.get('rent') # Use .get for potentially missing rent on utilities


                    if current_square['type'] == 'utility':
                         # Basic utility rent (e.g., 4 times dice roll for one utility, 10 times for two)
                         # This would require passing the dice roll to handle_square
                         # For now, use a placeholder or base rent if available.
                         print("Utility rent calculation is more complex and not fully implemented in this basic version.")
                         if rent is None:
                             rent = 50 # Example placeholder rent
                             print(f"Using a placeholder rent of ${rent}.")
                         else:
                              print(f"Using base rent of ${rent}.")


                    elif current_square['type'] == 'railroad':
                         # Basic railroad rent increases with the number of railroads owned.
                         # A more complex version would count owned railroads.
                         print("Railroad rent calculation depends on the number of railroads owned and is not fully implemented in this basic version.")
                         pass # Will use the base rent already assigned to 'rent'




                    if rent is not None: # Only attempt to pay rent if rent is defined or placeholder used
                        print(f"{player.name} pays ${rent} rent to {owner.name}.")
                        player.money -= rent
                        owner.money += rent
                    else:
                        print("Could not determine rent amount.")


            else:
                print(f"{player.name} owns {current_square['name']}.")
                # Option to mortgage if the player lands on their own property
                if can_mortgage(current_square):
                    mortgage_choice = input(f"Do you want to mortgage {current_square['name']} for ${current_square['price'] // 2}? (yes/no): ")
                    if mortgage_choice.lower() == 'yes':
                        mortgage_property(player, current_square)




    elif current_square['type'] == 'tax':
        print(f"{player.name} pays ${current_square['amount']} in tax.")
        player.money -= current_square['amount']


    elif current_square['type'] == 'chance' or current_square['type'] == 'community chest':
        print(f"{player.name} draws a {current_square['type']} card (card logic not implemented yet).")
        # Card drawing logic will be implemented later


    elif current_square['type'] == 'go to jail':
        print(f"{player.name} goes to Jail.")
        player.position = 10 # Assuming Jail is at index 10
        # Additional logic for being in jail would be needed here (e.g., turns in jail)


    elif current_square['type'] == 'jail':
        print(f"{player.name} is just visiting Jail.")


    elif current_square['type'] == 'free parking':
        print(f"{player.name} is on Free Parking.")


    elif current_square['type'] == 'go':
        # Handled by move_player function
        pass


    else:
        print(f"Unknown square type: {current_square['type']}")




# Start the game loop
turn_limit = 20 # Simple placeholder to end the game
turn_count = 0


while turn_count < turn_limit:
    turn_count += 1
    print(f"\n--- Turn {turn_count} ---")


    for player in players:
        print(f"\n{player.name}'s turn. Money: ${player.money}")


        # Option to mortgage/unmortgage at the start of the turn
        action_choice = input("Do you want to (r)oll dice, (m)ortgage, or (u)nmortgage? (r/m/u): ")


        if action_choice.lower() == 'm':
            if player.properties:
                print("Your properties:")
                for i, prop in enumerate(player.properties):
                    mortgaged_status = " (Mortgaged)" if prop.get('mortgaged') else ""
                    print(f"{i + 1}. {prop['name']} (Price: ${prop['price']}){mortgaged_status}")
                try:
                    prop_index = int(input("Enter the number of the property to mortgage: ")) - 1
                    if 0 <= prop_index < len(player.properties):
                        mortgage_property(player, player.properties[prop_index])
                    else:
                        print("Invalid property number.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("You have no properties to mortgage.")
            # After mortgaging, the player's turn continues with rolling the dice
            input("Press Enter to roll the dice...")




        elif action_choice.lower() == 'u':
             mortgaged_properties = [prop for prop in player.properties if prop.get('mortgaged')]
             if mortgaged_properties:
                 print("Your mortgaged properties:")
                 for i, prop in enumerate(mortgaged_properties):
                     unmortgage_cost = int(prop['price'] // 2 * 1.1)
                     print(f"{i + 1}. {prop['name']} (Unmortgage Cost: ${unmortgage_cost})")
                 try:
                     prop_index = int(input("Enter the number of the property to unmortgage: ")) - 1
                     if 0 <= prop_index < len(mortgaged_properties):
                         unmortgage_property(player, mortgaged_properties[prop_index])
                     else:
                         print("Invalid property number.")
                 except ValueError:
                     print("Invalid input.")
             else:
                 print("You have no mortgaged properties to unmortgage.")
             # After unmortgaging, the player's turn continues with rolling the dice
             input("Press Enter to roll the dice...")




        elif action_choice.lower() == 'r':
            input("Press Enter to roll the dice...") # Prompt for next turn


        else:
             print("Invalid action. Defaulting to rolling dice.")
             input("Press Enter to roll the dice...") # Prompt for next turn




        dice_roll = roll_dice()
        print(f"{player.name} rolled a {dice_roll}.")


        move_player(player, dice_roll)
        handle_square(player, board)


        # Simple condition to potentially end the game based on money
        if player.money <= 0:
            print(f"{player.name} has run out of money and is out of the game!")
            players.remove(player)
            if len(players) <= 1:
                print("Less than two players remaining. Ending game.")
                break # Break from the inner player loop


    if len(players) <= 1:
        break # Break from the outer turn loop





print("\n--- Game Over ---")
if len(players) == 1:
    print(f"{players[0].name} wins!")
elif len(players) == 0:
    print("No players remaining.")
   
while turn_count < turn_limit:
    turn_count += 1
    print(f"\n--- Turn {turn_count} ---")


    for player in players:
        print(f"\n{player.name}'s turn. Money: ${player.money}")
        input("Press Enter to roll the dice...") # Prompt for next turn


        dice_roll = roll_dice()
        print(f"{player.name} rolled a {dice_roll}.")


        move_player(player, dice_roll)
        handle_square(player, board)


        # Simple condition to potentially end the game based on money
        if player.money <= 0:
            print(f"{player.name} has run out of money and is out of the game!")
            players.remove(player)
            if len(players) <= 1:
                print("Less than two players remaining. Ending game.")
                break # Break from the inner player loop


    if len(players) <= 1:
        break # Break from the outer turn loop








print("\n--- Game Over ---")
if len(players) == 1:
    print(f"{players[0].name} wins!")
elif len(players) == 0:
    print("No players remaining.")



