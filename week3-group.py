from random import randrange

user_pets = []


class Pet:
    hunger_threshold = 3
    hunger_decrement = 1
    boredom_threshold = 3
    boredom_decrement = 2
    sounds = ["Hi", "Hello"]

    # INITIALIZE ATTRIBUTES
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    # INCREMENTS HUNGER AND BOREDOM
    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    # CURRENT MOOD OF PET
    def current_mood(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return "happy"
        elif self.boredom >= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry & bored"
        elif self.boredom <= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    # STR TO DISPLAY CURRENT MOOD OF PET
    def __str__(self) -> str:
        mood = self.current_mood()
        return " I'm " + self.name + " current mood is " + mood + " Type is " + self.type + "."

    # REDUCE BOREDOM
    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    # REDUCE HUNGER
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    # TEACH WORD METHOD TO REDUCE BOREDOM
    def teach(self, word):
        print(f"\n I learned the new word '{word}'")
        self.sounds.append(word)
        self.reduce_boredom()

    # SAY HI TO REDUCE BOREDOM
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    # FEED THE PET
    def feed(self):
        print("\nThank you for feeding me!")
        self.hunger -= self.hunger_decrement
        self.reduce_hunger()


class Dog1(Pet):
    def __init__(self):
        print("Dog 1 created")


class Dog2(Pet):
    sounds = ["Woof", "ruff ruff"]

    def __init__(self):
        print("Dog 2 created")


class Dog3(Dog1, Dog2):
    def __init__(self):
        Dog1.__init__(self)
        Dog2.__init__(self)
        print("Dog 3 created")


class Cat(Pet):
    def __init__(self):
        print("Cat created")


def display_user_pets():
    print("Your Pets")
    for pet in user_pets:
        print(f"\n{pet}")


# MAIN GAME
p1 = Dog1()
p2 = Dog2()
p3 = Dog3()
c1 = Cat()
print("Welcome")
game_on = True
while game_on:
    if len(user_pets) == 0:
        print("\nNo Pets!")
        name = input("Enter the name of your pet: ")
        type = input("Enter the type of the pet: ")
        user_pets.append(Pet(name, type))
    print("1.Display pets\n2.Adopt a Pet\n3.Greet\n4.Teach\n5.Feed\n6.Exit")
    user_choice = int(input("Enter your choice(1-6):"))
    print(user_choice)
    if user_choice == 1:
        display_user_pets()
    elif user_choice == 2:
        print("\nAdopting a new pet!")
        name = input("Enter the name of your pet: ")
        type = input("Enter the type of the pet: ")
        user_pets.append(Pet(name, type))
    elif user_choice in range(2, 6):
        name = input("Enter the name of pet you want to interact with: ")
        pet_exists = False
        for pet in user_pets:
            if pet.name == name:
                if user_choice == 3:
                    pet.hi()
                elif user_choice == 4:
                    word = input("Enter the word you want to teach: ")
                    pet.teach(word)
                elif user_choice == 5:
                    pet.feed()
                pet_exists = True
                pet.clock_tick()
        if pet_exists == False:
            print(f"You don't have a pet with the name {name}")
    else:
        game_on = False
