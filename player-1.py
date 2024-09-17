

# This is a class file for Muhammad Rizwan's Computing Lab 11 Assignment
# This will be a file with the 'player' class of the lab where the information for
a specific player will be provided.
class Player: # define Player class
def __init__(self, name, age, position): # define init method with self, name,
age, and position as parameters
self.set_name(name); # initialize player name using provided input
self.set_age(age); # initialize player age using the provided input
self.set_position(position); # initialize player position using the
provided input
def set_name(self, name): # define set_name method with self and name as
parameters
if not isinstance(name, str) or not name.strip(): # check if the input
'name' is not a string or if it is an empty string after stripping leading/trailing
spaces
raise ValueError("Invalid name. Name must be a non-empty string."); #
if the 'name' is an empty string, raise this error
self.name = name.strip(); # remove leading/trailing spaces and set the
player name
def set_age(self, age): # define set_age method with self and age as parameters
if not isinstance(age, int) or age <= 0: # check if the input 'age' is not
a positive integer
raise ValueError("Invalid age. Age must be a positive integer."); # if
the 'age' is not a positive integer, raise this error
self.age = age; # set the player age
def set_position(self, position): # define set_position method with self and
position as parameters
if not isinstance(position, str) or not position.strip(): # check if the
input 'position' is not a string or if it is an empty string after stripping
leading/trailing spaces
raise ValueError("Invalid position. Position must be a non-empty
string."); # if the 'position' is an empty string, raise this error
self.position = position.strip(); # remove leading/trailing spaces and set
the player position
def display_player_info(self): # define display_player_info method with self as
a parameter
print(f"Name: {self.name}"); # print player name
print(f"Age: {self.age}"); # print player age
print(f"Position: {self.position}"); # print player position
def __str__(self): # define str method with self as a parameter
return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"; #
provide a string representation of the player object
def change_position(self, new_position): # define change_position method with
self and new_position as parameters
# Action method to change player position
if not isinstance(new_position, str) or not new_position.strip(): # check
if the input 'new_position' is not a string or if it is an empty string after
stripping leading/trailing spaces
raise ValueError("Invalid new position. Position must be a non-empty
string."); # if the 'new_position' is an empty string, raise this error
self.position = new_position.strip(); # remove leading/trailing spaces and
set the new player position
