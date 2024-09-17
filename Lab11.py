
# This program is for Muhammad Rizwan's Lab 11 Assignment for Computing I
# This program will involve the object-oriented representation of an NBA player
search, involving the player, the team they play for, and which conference the team
is in as well as information regarding the seed in the respective conference.
# Importing necessary classes from player, team, and conference modules
from player import Player; # Import the Player class
from team import Team; # Import the Team class
from conference import EasternConference, WesternConference; # Import
EasternConference and WesternConference classes
# Function to print a decorative line
def print_decorative_line():
print('.%@@-:@%. -****. .***+ *******+:. .*****='); # Print decorative line
print('=@@%.+@@= =@@@@- .@@@# @@@@@@@@@@- +@@@@@@.'); # Print decorative
line
print('=* .=@= =@@@@@..@@@# @@@@-..@@@@ .@@@#@@@:'); # Print decorative
line
print(': .#:@= =@@@@@-.@@@# @@@@- @@@% :@@@-@@@*'); # Print decorative
line
print('=: .%++= =@@@#@@.@@@# @@@@#*%@@@: +@@@:%@@@.'); # Print decorative
line
print('=: - =@@@.@@+@@@# @@@@@@@@@@. @@@@ +@@@:'); # Print decorative
line
print('=@+. :%#= =@@@.#@@@@@# @@@@- .@@@@.-@@@*:=@@@*'); # Print decorative
line
print('=@@%. +@= =@@@..@@@@@# @@@@- *@@@-+@@@@@@@@@@.'); # Print decorative
line
print('=@@@@%.@= =@@@. #@@@@# @@@@=..@@@@:@@@@...@@@@-'); # Print decorative
line
print('==:-=-*@= =@@@. .@@@@# @@@@@@@@@@=-@@@@. #@@@*'); # Print decorative
line
print('.%@@@@*=. -+++. -+++= +++++++=:. -+++= -++++'); # Print decorative
line
# Function to create a Player object with user input
def create_player():
name = input("Player Name: "); # Prompt user for player name
age = int(input("Player Age: ")); # Prompt user for player age and convert
input to integer
position = input("Player Position: "); # Prompt user for player position
return Player(name, age, position); # Return a new Player object with provided
input values
# Function to create a Team object with user input
def create_team():
team_name = input("Enter Team Name: "); # Prompt user for team name
city = input("Enter City: "); # Prompt user for city
return Team(team_name, city); # Return a new Team object with provided input
values
# Main function
def main():
print('NBA PLAYER INFORMATION SYSTEM'); # Print program header
print('This program implements an NBA player information system using object-
oriented programming.'); # Print program description
print('It includes classes for Player, Team, and Conference, allowing users to
input and display player, team, and conference information.'); # Print program
functionality description
print('\n'); # Print newline for spacing
print_decorative_line(); # Print a decorative line
print('\n'); # Print newline for spacing
try: # Try block to handle potential exceptions
# Creating a player object with user input values
player1 = create_player(); # Call the create_player function
# Creating a team object with user input values
team1 = create_team(); # Call the create_team function
# Creating a conference object based on user input for conference name
conference_name = input("Enter Conference Name (East or West): "); #
Prompt user for conference name
if conference_name == "East":
conference = EasternConference(conference_name); # Instantiate
EasternConference object
elif conference_name == "West":
conference = WesternConference(conference_name); # Instantiate
WesternConference object
else:
raise ValueError("Invalid conference name. Please enter 'East' or
'West'."); # Raise an error for invalid conference name
# Adding the player to the team
team1.add_player(player1); # Add the player to the team's player list
# Adding the team to the conference
conference.add_team(team1); # Add the team to the conference's list of
teams
# Displaying player, team, and conference information
print("\nPlayer Information:"); # Print section header for player
information
print(player1); # Print player information
print("\n\nTeam Information:"); # Print section header for team
information
print(team1); # Print team information
print("\n\nConference Information:"); # Print section header for
conference information
print(conference); # Print conference information
except ValueError as e: # Handle value error exceptions
print(f"Error: {e}"); # Print the error message
# Entry point of the program
if __name__ == "__main__":
main(); # Call the main function if the script is executed directly
