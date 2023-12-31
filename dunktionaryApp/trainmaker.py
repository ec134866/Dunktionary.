import random
from django.shortcuts import render
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing


class Pass:
    def __init__(self, name, level, can_start=False, can_follow=False, variations=None):
        self.name = name
        self.level = level
        self.can_start = can_start
        self.can_follow = can_follow
        self.variations = variations if variations is not None else []

    def get_random_variation(self):
        if self.variations:
            return random.choice(self.variations)
        else:
            return self.name
        
class Dunk:
    def __init__(self, name, level, variations=None):
        self.name = name
        self.level = level
        self.variations = variations if variations is not None else []

    def get_random_variation(self):
        if self.variations:
            return random.choice(self.variations)
        else:
            return self.name


passes = {
    "Turn and Bounce": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World", "Double Around the World", "Double Cradle"]},
    ],
    "Turn and Float": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World", "Double Around the World", "Double Cradle"]},
    ],
    "Off the Glass": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World", "Double Around the World", "Double Cradle"]},
    ],
    "Front off the Glass": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Front Float": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Barani Bounce": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Barani Float": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Giddy Up": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "can_follow": True},
        {"level": 5, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 6, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 7, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider"]},
        {"level": 8, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Rudi Bounce": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True},
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True, "can_follow": True},
    ],
    "Rudi Up (glass)": [
        {"level": 3, "can_start": True},
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True, "can_follow": True},
    ],
    "Front Full off the Glass": [
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True, "can_follow": True},
    ],
    "Gainer Float": [
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True},
        {"level": 7, "can_start": True, "can_follow": True},
    ],
    "Gainer off the Glass": [
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True},
        {"level": 7, "can_start": True, "can_follow": True},
    ],
    "Randi Bounce": [
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True},
        {"level": 7, "can_start": True, "can_follow": True},
    ],
    "Randi Up (glass)": [
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True},
        {"level": 7, "can_start": True},
        {"level": 8, "can_start": True, "can_follow": True},
    ],
    "Leap Frog": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "variations": ["Single Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Behind the Back Glass": [
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "variations": ["Single Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "Behind the Back Float": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "variations": ["Single Rider"]},
        {"level": 5, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
        {"level": 7, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World", "Double Rider", "Cradle"]},
    ],
    "1 and 3 Bounce": [
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True},
        {"level": 6, "can_start": True, "can_follow": True},
    ],
    "540 Turn and Bounce": [
        {"level": 3, "can_start": True},
        {"level": 4, "can_start": True, "can_follow": True},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 8, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 9, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
    ],
    "540 Turn and Float": [
        {"level": 3, "can_start": True},
        {"level": 4, "can_start": True, "can_follow": True},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 8, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 9, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
    ],
    "360 Off the Glass": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 5, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 7, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 8, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
    ],
    "360 Leap Frog": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True, "can_follow": True},
        {"level": 4, "can_start": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 5, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 7, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 8, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
    ],
    "540 Leap Frog": [
        {"level": 3, "can_start": True},
        {"level": 4, "can_start": True, "can_follow": True},
        {"level": 5, "can_start": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 6, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Around the World"]},
        {"level": 7, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 8, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Around the World"]},
        {"level": 9, "can_start": True, "variations": ["Single Rider", "Double Rider", "Cradle", "Triple Rider", "Around the World"]},
    ],
}

dunks = {
    "Dunk": [
        {"level": 1},
        {"level": 2, "variations": ["Back Scratcher", "Single Rider", "Look Back"]},
        {"level": 3, "variations": ["Back Scratcher", "Single Rider", "360", "Look Back", "Double Rider"]},
        {"level": 4, "variations": ["Back Scratcher", "Single Rider", "360", "Look Back", "Double Rider", "Cradle", "YoYo", "Cradle Pop"]},
    ],
}

scoring_table = {
    "Turn and Bounce": 0.1,
    "Single Rider Turn and Bounce": 0.2,
    "Double Rider Turn and Bounce": 0.4,
    "Triple Rider Turn and Bounce": 0.7,
    "Cradle Turn and Bounce": 0.3,
    "Double Cradle Turn and Bounce": 0.7,
    "Around the World Turn and Bounce": 0.3,
    "Double Around the World Turn and Bounce": 0.7,
    "YoYo Turn and Bounce": 0.4,
    "Cradle Pop Turn and Bounce": 0.5,
    # 
    "Turn and Float": 0.1,
    "Single Rider Turn and Float": 0.2,
    "Double Rider Turn and Float": 0.4,
    "Triple Rider Turn and Float": 0.7,
    "Cradle Turn and Float": 0.3,
    "Double Cradle Turn and Float": 0.7,
    "Around the World Turn and Float": 0.3,
    "Double Around the World Turn and Float": 0.7,
    "YoYo Turn and Float": 0.4,
    "Cradle Pop Turn and Float": 0.5,
    #   
    "Off the Glass": 0.0,
    "Single Rider Off the Glass": 0.1,
    "Double Rider Off the Glass": 0.3,
    "Triple Rider Off the Glass": 0.6,
    "Cradle Off the Glass": 0.2,
    "Double Cradle Off the Glass": 0.6,
    "Around the World Off the Glass": 0.2,
    "Double Around the World Off the Glass": 0.6,
    "YoYo Off the Glass": 0.4,
    "Cradle Pop Off the Glass": 0.5,
    # 
    "Front off the Glass": 0.4,
    "Single Rider Front off the Glass": 0.5,
    "Double Rider Front off the Glass": 0.7,
    "Triple Rider Front off the Glass": 1.0,
    "Cradle Front off the Glass": 0.6,
    "Double Cradle Front off the Glass": 1.0,
    "Around the World Front off the Glass": 0.7,
    "Double Around the World Front off the Glass": 1.1,
    "YoYo Front off the Glass": 0.7,
    "Cradle Pop Front off the Glass": 0.8,
    # 
    "Front Float": 0.4,
    "Single Rider Front Float": 0.5,
    "Double Rider Front Float": 0.7,
    "Triple Rider Front Float": 1.0,
    "Cradle Front Float": 0.6,
    "Double Cradle Front Float": 1.0,
    "Around the World Front Float": 0.7,
    "Double Around the World Front Float": 1.1,
    "YoYo Front Float": 0.7,
    "Cradle Pop Front Float": 0.8,
    # 
    "Barani Bounce": 0.4,
    "Single Rider Barani Bounce": 0.6,
    "Double Rider Barani Bounce": 0.8,
    "Triple Rider Barani Bounce": 1.1,
    "Cradle Barani Bounce": 0.7,
    "Double Cradle Barani Bounce": 1.2,
    "Around the World Barani Bounce": 0.5,
    "Double Around the World Barani Bounce": 0.8,
    "YoYo Barani Bounce": 0.8,
    "Cradle Pop Barani Bounce": 0.9,
    # 
    "Barani Float": 0.4,
    "Single Rider Barani Float": 0.6,
    "Double Rider Barani Float": 0.8,
    "Triple Rider Barani Float": 1.1,
    "Cradle Barani Float": 0.7,
    "Double Cradle Barani Float": 1.2,
    "Around the World Barani Float": 0.5,
    "Double Around the World Barani Float": 0.8,
    "YoYo Barani Float": 0.8,
    "Cradle Pop Barani Float": 0.9,
    # 
    "Giddy Up": 0.4,
    "Single Rider Giddy Up": 0.6,
    "Double Rider Giddy Up": 0.8,
    "Triple Rider Giddy Up": 1.1,
    "Cradle Giddy Up": 0.7,
    "Double Cradle Giddy Up": 1.2,
    "Around the World Giddy Up": 0.5,
    "Double Around the World Giddy Up": 0.8,
    "YoYo Giddy Up": 0.8,
    "Cradle Pop Giddy Up": 0.9,
    # 
    "Rudi Bounce": 0.7,
    "Single Rider Rudi Bounce": 0.9,
    "Double Rider Rudi Bounce": 1.0,
    "Triple Rider Rudi Bounce": 1.3,
    "Cradle Rudi Bounce": 0.9,
    "Double Cradle Rudi Bounce": 1.3,
    "Around the World Rudi Bounce": 0.9,
    "Double Around the World Rudi Bounce": 1.3,
    "YoYo Rudi Bounce": 1.0,
    "Cradle Pop Rudi Bounce": 1.1,
    # 
    "Front Full off the Glass": 0.7,
    "Single Rider Front Full off the Glass": 0.8,
    "Double Rider Front Full off the Glass": 1.0,
    "Triple Rider Front Full off the Glass": 1.3,
    "Cradle Front Full off the Glass": 0.8,
    "Double Cradle Front Full off the Glass": 1.3,
    "Around the World Front Full off the Glass": 0.8,
    "Double Around the World Front Full off the Glass": 1.2,
    "YoYo Front Full off the Glass": 0.9,
    "Cradle Pop Front Full off the Glass": 1.0,
    # 
    "Gainer Float": 0.6,
    "Single Rider Gainer Float": 0.7,
    "Double Rider Gainer Float": 0.9,
    "Triple Rider Gainer Float": 1.2,
    "Cradle Gainer Float": 0.8,
    "Double Cradle Gainer Float": 1.2,
    "Around the World Gainer Float": 0.8,
    "Double Around the World Gainer Float": 1.2,
    "YoYo Gainer Float": 0.9,
    "Cradle Pop Gainer Float": 1.0,
    # 
    "Gainer off the Glass": 0.6,
    "Single Rider Gainer off the Glass": 0.7,
    "Double Rider Gainer off the Glass": 0.9,
    "Triple Rider Gainer off the Glass": 1.2,
    "Cradle Gainer off the Glass": 0.8,
    "Double Cradle Gainer off the Glass": 1.2,
    "Around the World Gainer off the Glass": 0.8,
    "Double Around the World Gainer off the Glass": 1.2,
    "YoYo Gainer off the Glass": 0.9,
    "Cradle Pop Gainer off the Glass": 1.0,
    # 
    "Rudi Up (glass)": 0.7,
    "Single Rider Rudi Up (glass)": 0.9,
    "Double Rider Rudi Up (glass)": 1.0,
    "Triple Rider Rudi Up (glass)": 1.3,
    "Cradle Rudi Up (glass)": 0.9,
    "Double Cradle Rudi Up (glass)": 1.3,
    "Around the World Rudi Up (glass)": 0.9,
    "Double Around the World Rudi Up (glass)": 1.3,
    "YoYo Rudi Up (glass)": 1.0,
    "Cradle Pop Rudi Up (glass)": 1.1,
    # 
    "Randi Bounce": 0.9,
    "Single Rider Rudi Bounce": 1.0,
    "Double Rider Rudi Bounce": 1.2,
    "Triple Rider Rudi Bounce": 1.5,
    "Cradle Rudi Bounce": 1.1,
    "Double Cradle Rudi Bounce": 1.5,
    "Around the World Rudi Bounce": 1.1,
    "Double Around the World Rudi Bounce": 1.5,
    "YoYo Rudi Bounce": 1.2,
    "Cradle Pop Rudi Bounce": 1.3,
    # 
    "Randi Up (glass)": 0.9,
    "Single Rider Rudi Up (glass)": 1.0,
    "Double Rider Rudi Up (glass)": 1.2,
    "Triple Rider Rudi Up (glass)": 1.5,
    "Cradle Rudi Up (glass)": 1.1,
    "Double Cradle Rudi Up (glass)": 1.5,
    "Around the World Rudi Up (glass)": 1.1,
    "Double Around the World Rudi Up (glass)": 1.5,
    "YoYo Rudi Up (glass)": 1.2,
    "Cradle Pop Rudi Up (glass)": 1.3,
    # 
    "Leap Frog": 0.0,
    "Single Rider Leap Frog": 0.1,
    "Double Rider Leap Frog": 0.3,
    "Triple Rider Leap Frog": 0.6,
    "Cradle Leap Frog": 0.2,
    "Double Cradle Leap Frog": 0.6,
    "Around the World Leap Frog": 0.2,
    "Double Around the World Leap Frog": 0.6,
    "YoYo Leap Frog": 0.4,
    "Cradle Pop Leap Frog": 0.5,
    # 
    "Behind the Back Glass": 0.0,
    "Single Rider Behind the Back Glass": 0.1,
    "Double Rider Behind the Back Glass": 0.3,
    "Triple Rider Behind the Back Glass": 0.6,
    "Cradle Behind the Back Glass": 0.2,
    "Double Cradle Behind the Back Glass": 0.6,
    "Around the World Behind the Back Glass": 0.2,
    "Double Around the World Behind the Back Glass": 0.6,
    "YoYo Behind the Back Glass": 0.4,
    "Cradle Pop Behind the Back Glass": 0.5,
    # 
    "Behind the Back Float": 0.0,
    "Single Rider Behind the Back Float": 0.1,
    "Double Rider Behind the Back Float": 0.3,
    "Triple Rider Behind the Back Float": 0.6,
    "Cradle Behind the Back Float": 0.2,
    "Double Cradle Behind the Back Float": 0.6,
    "Around the World Behind the Back Float": 0.2,
    "Double Around the World Behind the Back Float": 0.6,
    "YoYo Behind the Back Float": 0.4,
    "Cradle Pop Behind the Back Float": 0.5,
    # 
    "1 and 3 Bounce": 0.8,
    "Single Rider 1 and 3 Bounce": 0.8,
    "Double Rider 1 and 3 Bounce": 1.0,
    "Triple Rider 1 and 3 Bounce": 1.3,
    "Cradle 1 and 3 Bounce": 0.9,
    "Double Cradle 1 and 3 Bounce": 1.3,
    "Around the World 1 and 3 Bounce": 0.9,
    "Double Around the World 1 and 3 Bounce": 1.3,
    "YoYo 1 and 3 Bounce": 1.0,
    "Cradle Pop 1 and 3 Bounce": 1.1,
    # 
    "540 Turn and Bounce": 0.5,
    "Single Rider 540 Turn and Bounce": 0.5,
    "Double Rider 540 Turn and Bounce": 0.7,
    "Triple Rider 540 Turn and Bounce": 1.0,
    "Cradle 540 Turn and Bounce": 0.6,
    "Double Cradle 540 Turn and Bounce": 1.0,
    "Around the World 540 Turn and Bounce": 0.6,
    "Double Around the World 540 Turn and Bounce": 1.0,
    "YoYo 540 Turn and Bounce": 0.7,
    "Cradle Pop 540 Turn and Bounce": 0.8,
    # 
    "540 Turn and Float": 0.5,
    "Single Rider 540 Turn and Float": 0.5,
    "Double Rider 540 Turn and Float": 0.7,
    "Triple Rider 540 Turn and Float": 1.0,
    "Cradle 540 Turn and Float": 0.6,
    "Double Cradle 540 Turn and Float": 1.0,
    "Around the World 540 Turn and Float": 0.6,
    "Double Around the World 540 Turn and Float": 1.0,
    "YoYo 540 Turn and Float": 0.7,
    "Cradle Pop 540 Turn and Float": 0.8,
    # 
    "540 Leap Frog": 0.5,
    "Single Rider 540 Leap Frog": 0.5,
    "Double Rider 540 Leap Frog": 0.7,
    "Triple Rider 540 Leap Frog": 1.0,
    "Cradle 540 Leap Frog": 0.6,
    "Double Cradle 540 Leap Frog": 1.0,
    "Around the World 540 Leap Frog": 0.6,
    "Double Around the World 540 Leap Frog": 1.0,
    "YoYo 540 Leap Frog": 0.7,
    "Cradle Pop 540 Leap Frog": 0.8,
    #   
    "360 Off the Glass": 0.3,
    "Single Rider 360 Off the Glass": 0.4,
    "Double Rider 360 Off the Glass": 0.6,
    "Triple Rider 360 Off the Glass": 0.9,
    "Cradle 360 Off the Glass": 0.5,
    "Double Cradle 360 Off the Glass": 0.9,
    "Around the World 360 Off the Glass": 0.7,
    "Double Around the World 360 Off the Glass": 1.1,
    "YoYo 360 Off the Glass": 0.6,
    "Cradle Pop 360 Off the Glass": 0.7,
    # 
    "360 Leap Frog": 0.3,
    "Single Rider 360 Leap Frog": 0.4,
    "Double Rider 360 Leap Frog": 0.6,
    "Triple Rider 360 Leap Frog": 0.9,
    "Cradle 360 Leap Frog": 0.5,
    "Double Cradle 360 Leap Frog": 0.9,
    "Around the World 360 Leap Frog": 0.7,
    "Double Around the World 360 Leap Frog": 1.1,
    "YoYo 360 Leap Frog": 0.6,
    "Cradle Pop 360 Leap Frog": 0.7,
    # 
    "Dunk": 0.2,
    "Single Rider Dunk": 0.3,
    "Look Back Dunk": 0.4,
    "Double Rider Dunk": 0.5,
    "Triple Rider Dunk": 0.8,
    "Cradle Dunk": 0.4,
    "Double Cradle Dunk": 0.8,
    "Around the World Dunk": 0.4,
    "Double Around the World Dunk": 0.9,
    "YoYo Dunk": 0.5,
    "Cradle Pop Dunk": 0.6,
    # 
    "360 Dunk": 0.6,
    "360 Single Rider Dunk": 0.7,
    "360 Look Back Dunk": 0.7,
    "360 Double Rider Dunk": 0.9,
    "360 Triple Rider Dunk": 1.2,
    "360 Cradle Dunk": 0.8,
    "360 Double Cradle Dunk": 1.3,
    "360 Around the World Dunk": 0.8,
    "360 Double Around the World Dunk": 1.3,
    "360 YoYo Dunk": 1.0,
    "360 Cradle Pop Dunk": 1.1,
    # 
    "720 Dunk": 1.0,
    "720 Single Rider Dunk": 1.2,
    "720 Look Back Dunk": 1.3,
    "720 Double Rider Dunk": 1.4,
    "720 Triple Rider Dunk": 1.7,
    "720 Cradle Dunk": 1.3,
    "720 Double Cradle Dunk": 1.8,
    "720 Around the World Dunk": 1.3,
    "720 Double Around the World Dunk": 1.8,
    "720 YoYo Dunk": 1.9,
    "720 Cradle Pop Dunk": 2.0,
    # 
    "Front Dunk": 0.6,
    "Front Single Rider Dunk": 0.7,
    "Front Double Rider Dunk": 1.0,
    "Front Triple Rider Dunk": 1.2,
    "Front Cradle Dunk": 0.8,
    "Front Double Cradle Dunk": 1.2,
    "Front Around the World Dunk": 0.8,
    "Front Double Around the World Dunk": 1.1,
    "Front YoYo Dunk": 0.9,
    "Front Cradle Pop Dunk": 1.1,
    # 
    "Front Full Dunk": 1.0,
    "Front Full Single Rider Dunk": 1.2,
    "Front Full Double Rider Dunk": 1.4,
    "Front Full Triple Rider Dunk": 1.7,
    "Front Full Cradle Dunk": 1.3,
    "Front Full Double Cradle Dunk": 1.8,
    "Front Full Around the World Dunk": 1.3,
    "Front Full Double Around the World Dunk": 1.8,
    "Front Full YoYo Dunk": 1.4,
    "Front Full Cradle Pop Dunk": 1.5,
    # 
    "Double Front Dunk": 1.5,
    "Double Front Single Rider Dunk": 1.7,
    "Double Front Double Rider Dunk": 1.9,
    "Double Front Triple Rider Dunk": 2.2,
    "Double Front Cradle Dunk": 1.8,
    "Double Front Double Cradle Dunk": 2.3,
    "Double Front Around the World Dunk": 1.8,
    "Double Front Double Around the World Dunk": 2.3,
    "Double Front YoYo Dunk": 1.9,
    "Double Front Cradle Pop Dunk": 2.0,
}




def make_a_train(num_people, level):
    valid_passes = []
    valid_dunks = []
    train = []

    total_score = 0

    for pass_name, pass_variations in passes.items():
        for pass_details in pass_variations:
            if pass_details["level"] <= level:
                valid_passes.append(Pass(pass_name, **pass_details))
    
    for dunk_name, dunk_variations in dunks.items():
        for dunk_details in dunk_variations:
            if dunk_details["level"] <= level:
                valid_dunks.append(Dunk(dunk_name, **dunk_details))

    if len(valid_passes) == 0:
        print("No valid passes for the specified level.")
        return

    random.shuffle(valid_passes)
    random.shuffle(valid_dunks)


    # Assign start pass to the first person
    start_passes = [
        pass_ for pass_ in valid_passes if pass_.can_start and pass_.level <= level
    ]
    if len(start_passes) == 0:
        print("No valid start passes for the specified level.")
        return

    start_pass = random.choice(start_passes)

        # Check if there are variations available for the start
    if start_pass.variations:
            variation_probability = min(1.0, 0.5 + (level - start_pass.level) * 0.25)
            if random.random() < variation_probability:
                variation = random.choice(start_pass.variations)
                train.append(f"Person 1: {variation} - {start_pass.name}")
                total_score += scoring_table.get(f"{variation} {start_pass.name}", 0)
            else:
                train.append(f"Person 1: {start_pass.name}")
                total_score += scoring_table.get(start_pass.name, 0)
    else:
        train.append(f"Person 1: {start_pass.name}")
        total_score += scoring_table.get(start_pass.name, 0)

    
    # Assign follow passes to the rest of the people
    follow_passes = [
    pass_ for pass_ in valid_passes if pass_.level <= level
    ]
    

    if len(follow_passes) == 0:
        print("No valid follow passes for the specified level.")
        return

    for i in range(2, num_people):
        pass_ = random.choice(follow_passes)

        # Check if there are variations available for the pass
        if pass_.variations:
            variation_probability = min(1.0, 0.5 + (level - pass_.level) * 0.20)  # Adjust scaling factor as needed
            if random.random() < variation_probability:
                variation = pass_.get_random_variation()
                train.append(f"Person {i}: {variation} - {pass_.name}")
                total_score += scoring_table.get(f"{variation} {pass_.name}", 0)
                total_score += .1
            else:
                train.append(f"Person {i}: {pass_.name}")
                total_score += scoring_table.get(pass_.name, 0)
                total_score += .1
        
        else:
            train.append(f"Person {i}: {pass_.name}")
            total_score += scoring_table.get(pass_.name, 0)
            total_score += .1

    # Assign dunk to the dunker
    dunker = [
        dunk for dunk in valid_dunks if dunk.level <= level
    ]
    if len(dunker) == 0:
        print("No valid dunks for the specified level.")
        return

    dunk = random.choice(dunker)

     # Check if there are variations available for the dunk
    if dunk.variations:
            variation_probability = min(1.0, 0.65 + (level - dunk.level) * 0.3)
            if random.random() < variation_probability:
                variation = dunk.get_random_variation()
                train.append(f"Dunker: {variation} - {dunk.name}")
                total_score += scoring_table.get(f"{variation} {dunk.name}", 0)
                total_score += .1
            else:
                train.append(f"Dunker: {dunk.name}")
                total_score += scoring_table.get(dunk.name, 0)
                total_score += .1
    else:
        train.append(f"Dunker: {dunk.name}")
        total_score += scoring_table.get(dunk.name, 0)
        total_score += .1
    


    return train, total_score

def custom_train(custom_train_names):
    total_score = 0
    not_found_passes = []

    for pass_name in custom_train_names:
        score = scoring_table.get(pass_name)
        if score is not None:
            total_score += score
        else:
            not_found_passes.append(pass_name)

    return total_score, not_found_passes

# def get_pass_wheel(level):
#     valid_passes = []

#     for pass_name, pass_variations in passes.items():
#         for pass_details in pass_variations:
#             if pass_details["level"] <= level:
#                 valid_passes.append(pass_name)

#     return valid_passes

# How to read what trick was before and make sure you can't always follow, ex. barani bounce after BTB
# add 2 vs 1 trampoline functions, cross off the glass, cross baranis
# Add lay down float, OTB float, ball holds etc
