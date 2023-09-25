import random


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
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider"]}
    ],
    "Turn and Float": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider"]}
    ],
    "Off the Glass": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider"]}
    ],
    "Turn and Float": [
        {"level": 1, "can_start": True, "can_follow": True},
        {"level": 2, "can_start": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "can_follow": True, "variations": ["Single Rider"]},
        {"level": 3, "can_start": True, "variations": ["Single Rider", "Double Rider"]},
        {"level": 4, "can_start": True, "can_follow": True, "variations": ["Single Rider", "Double Rider"]}
    ],
    "Leap Frog": [
        {"level": 2, "can_start": True, "can_follow": True},
    ],
    "Behind the Back Glass": [
        {"level": 2, "can_start": True, "can_follow": True},
    ],
    "Behind the Back Float": [
        {"level": 3, "can_start": True, "can_follow": True},
    ],
    "Front off the Glass": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
        {"level": 3, "can_start": True, "variations": ["Single Rider"]},
    ],
    "Front Float": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
    ],
    "Barani Bounce": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
    ],
    "Barani Float": [
        {"level": 1, "can_start": True},
        {"level": 2, "can_start": True, "can_follow": True},
    ],
    "Giddy Up": [
        {"level": 2, "can_start": True},
        {"level": 3, "can_start": True, "can_follow": True},
    ],
    "Rudy Bounce": [
        {"level": 2, "can_start": True},
        {"level": 4, "can_start": True, "can_follow": True},
    ],
    "1 and 3 Bounce": [
        {"level": 4, "can_start": True},
        {"level": 5, "can_start": True, "can_follow": True},
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

forbidden_pass_pairs = [
    (("Barani Bounce", "Behind the Back Glass"), 5),
    (("Barani Float", "Behind the Back Glass"), 5),
    (("Giddy Up", "Behind the Back Glass"), 5),
    (("Front off the Glass", "Behind the Back Glass"), 5),
    (("Front Float", "Behind the Back Glass"), 5),
    (("Rudy Bounce", "Behind the Back Glass"), 5),
    (("Barani Bounce", "Behind the Back Glass"), 5),
    # this cannot follow that
]



def make_a_train(num_people, level, forbidden_pass_pairs):
    valid_passes = []
    valid_dunks = []
    train = []

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
            variation_probability = min(1.0, 0.5 + (level - start_pass.level) * 0.15)
            if random.random() < variation_probability:
                variation = random.choice(start_pass.variations)
                train.append(f"Person 1: {variation} - {start_pass.name}")
            else:
                train.append(f"Person 1: {start_pass.name}")
    else:
        train.append(f"Person 1: {start_pass.name}")

    
    # Assign follow passes to the rest of the people
    follow_passes = [
        pass_ for pass_ in valid_passes if pass_.can_follow and pass_.level <= level
    ]
    if len(follow_passes) == 0:
        print("No valid follow passes for the specified level.")
        return

    for i in range(2, num_people):
         while True:  # Keep trying until a valid pass is chosen
            pass_ = random.choice(follow_passes)
            current_pass = f"Person {i}: {pass_.name}"

            # Check for forbidden pass pairs with level constraints
            for forbidden_pair, min_level in forbidden_pass_pairs:
                pass_name, cannot_follow_name = forbidden_pair
                if (current_pass, train[-1].split(" - ")[-1]) == (pass_name, cannot_follow_name) and level < min_level:
                    # The selected pass is part of a forbidden pair with a level constraint, choose another pass
                    break
            else:
                # No constraint violation, add the pass to the sequence and break the loop
                break

            # Check if there are variations available for the pass
            if pass_.variations:
                variation_probability = min(1.0, 0.5 + (level - pass_.level) * 0.15)  # Adjust scaling factor as needed
                if random.random() < variation_probability:
                    variation = pass_.get_random_variation()
                    current_pass = f"Person {i}: {variation} - {pass_.name}"

            train.append(f"Person {i}: current_pass")
            

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
            variation_probability = min(1.0, 0.65 + (level - dunk.level) * 0.15)
            if random.random() < variation_probability:
                variation = dunk.get_random_variation()
                train.append(f"Dunker: {variation} - {dunk.name}")
            else:
                train.append(f"Dunker: {dunk.name}")
    else:
        train.append(f"Dunker: {dunk.name}")
    


    return train



# How to read what trick was before and make sure you can't always follow, ex. barani bounce after BTB
# add 2 vs 1 trampoline functions, cross off the glass, cross baranis
# Add lay down float, OTB float, ball holds etc
