# This is a class file for Muhammad Rizwan's Computing Lab 11 Assignment
# This will be a file with the 'Team' class of the lab where the information for a
specific team is provided.
from player import Player; # Importing the Player class
class Team: # Definition of the Team class
def __init__(self, name, city): # Constructor method for initializing the
object
self.set_name(name); # Setting the team name using the provided input
self.set_city(city); # Setting the city using the provided input
self.players = []; # Initializing an empty list to store players
def set_name(self, name): # Method to set the team name
if not isinstance(name, str) or not name.strip(): # Checking if the input
'name' is not a string or if it is an empty string after stripping leading/trailing
spaces
raise ValueError("Invalid team name. Team name must be a non-empty
string."); # Raising an error if the 'name' is an empty string
self.name = name.strip(); # Removing leading/trailing spaces and setting
the team name
def set_city(self, city): # Method to set the city
if not isinstance(city, str) or not city.strip(): # Checking if the input
'city' is not a string or if it is an empty string after stripping leading/trailing
spaces
raise ValueError("Invalid city. City must be a non-empty string."); #
Raising an error if the 'city' is an empty string
self.city = city.strip(); # Removing leading/trailing spaces and setting
the city
def add_player(self, player): # Method to add a player to the team
if not isinstance(player, Player): # Checking if the input 'player' is not
an instance of the Player class
raise ValueError("Invalid player object. Player must be an instance of
the Player class."); # Raising an error if it's not
self.players.append(player); # Adding the provided player object to the
list of players
def remove_player(self, player_name): # Method to remove a player from the
team
player_to_remove = next((player for player in self.players if
player.get_name() == player_name), None); # 'next()' function returns the first
player with a matching name, or None if no such player is found
if player_to_remove: # If player is found
self.players.remove(player_to_remove); # Removing the player with the
specified name from the list
def display_team_info(self): # Method to display team information
print(f"Team Name: {self.get_name()}"); # Printing the team name using the
getter method
print(f"City: {self.get_city()}"); # Printing the city using the getter
method
print("Players:");
for player in self.get_players(): # Iterating through players using the
getter method
print(f"- {player.get_name()}"); # Printing each player's name using
the getter method
def __str__(self): # Providing a string representation of the team object
using the getter method
return f"Team Name: {self.get_name()}, City: {self.get_city()}";
def set_players(self, players): # Setter method for players
if not all(isinstance(player, Player) for player in players): # Checking
if all elements in the input 'players' list are instances of the Player class
raise ValueError("Invalid players list. All elements must be instances
of the Player class."); # Raising an error if any element is not an instance of
the Player class
self.players = players; # Setting the players list
def get_name(self): # Getter method for team name
return self.name; # Return self.name
def get_city(self): # Getter method for city
return self.city; # Return self.city
def get_players(self): # Getter method for players
return self.players; # Return self.players
