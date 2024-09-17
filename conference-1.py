# This is a class file for Muhammad Rizwan's Computing Lab 11 Assignment
# This will be a file with the 'Conference' class of the lab where the information
for a specific conference will be provided.
import random; # Importing the random module for generating random seeds
from team import Team; # Importing the Team class
class Conference: # Defining the class 'Conference'
def __init__(self, name): # Constructor method for initializing the object
self.set_name(name); # Setting the conference name using the provided
input
self.teams = []; # Initializing an empty list to store teams
def set_name(self, name): # Method to set the conference name
if not isinstance(name, str) or not name.strip(): # Checking if the input
'name' is not a string or if it is an empty string after stripping leading/trailing
spaces
raise ValueError("Invalid conference name. Conference name must be a
non-empty string."); # Raising an error if the 'name' is an empty string
self.name = name.strip(); # Removing leading/trailing spaces and setting
the conference name
def add_team(self, team): # Method to add a team to the conference
if not isinstance(team, Team): # Checking if the input 'team' is an
instance of the Team class
raise ValueError("Invalid team object. Team must be an instance of the
Team class."); # Raising an error if it's not
self.teams.append(team); # Adding the provided team object to the list of
teams
def set_teams(self, teams): # Setter method for teams
if not all(isinstance(team, Team) for team in teams): # Checking if all
elements in the input 'teams' list are instances of the Team class
raise ValueError("Invalid teams list. All elements must be instances of
the Team class."); # Raising an error if any element is not an instance of the
Team class
self.teams = teams; # Setting the teams list
def get_name(self): # Getter method for conference name
return self.name; # Returning self.name
def get_teams(self): # Getter method for teams
return self.teams; # Returning self.teams
def print_teams_info(self): # Action method for printing teams information
print(f"Conference Name: {self.get_name()}"); # Printing the conference
name using the getter method
print("Teams in the Conference:");
for team in self.get_teams(): # Iterating through teams using the getter
method
print(f"- {team.get_name()}"); # Printing each team's name using the
getter method
def __str__(self): # String method with self as a parameter
teams_info = "\n".join([f"- {team.get_name()}" for team in
self.get_teams()]); # Creating a formatted string with team names using the getter
method
return f"Conference Name: {self.get_name()}, Teams in the Conference:\
n{teams_info}, Seed Information: N/A"; # Providing a string representation of the
conference object using the getter method
def seed_method(self): # Method to retrieve the seed information
return "Seed Information: N/A"; # Placeholder information, as the base
Conference class does not have a seed
# Child class for Eastern Conference
class EasternConference(Conference): # Defining the child class
'EasternConference'
def __init__(self, name): # Constructor method for initializing the object
super().__init__(name); # Call the constructor of the parent class
(Conference)
self.seed = random.randint(1, 15); # Set a random seed between 1 and 15
for the Eastern Conference
def seed_method(self): # Define 'seed_method' as a method
# Provide meaningful information related to EasternConference
return f"The Eastern Conference seed for the team is {self.seed}"; #
Returning the seed information
def __str__(self):
# Override the string method to provide a custom string representation for
Eastern Conference
teams_info = "\n".join([f"- {team.get_name()}" for team in
self.get_teams()]);
# Returning the formatted string including conference name, teams, and seed
information for the Eastern Conference
return f"Eastern Conference: Conference Name: {super().get_name()}, Teams
in the Conference:{teams_info}, The Eastern Conference seed (standing) for the team
is number {self.seed}";
# Child class for Western Conference
class WesternConference(Conference): # Defining the child class
'WesternConference'
def __init__(self, name): # Constructor method for initializing the object
super().__init__(name); # Call the constructor of the parent class
(Conference)
self.seed = random.randint(1, 15); # Set a random seed between 1 and 15
for the Western Conference
def seed_method(self): # Define 'seed_method' as a method
# Provide meaningful information related to WesternConference
return f"The Western Conference seed for the team is {self.seed}"; #
Returning the seed information
def __str__(self):
# Override the string method to provide a custom string representation for
Western Conference
teams_info = "\n".join([f"- {team.get_name()}" for team in
self.get_teams()]);
# Returning the formatted string including conference name, teams, and seed
information for the Western Conference
return f"Western Conference: Conference Name: {super().get_name()}, Teams
in the Conference:{teams_info}, The Western Conference seed (standing) for the team
is number {self.seed}";
