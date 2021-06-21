print("Greetings brave Hero! You received 30 points - use them wise.")

class Hero:
    base_points = 30
    spent_points = 0
    def __init__(self, strength, magic, health, swiftness):
        self.__strength = strength
        self.__magic = magic
        self.__health = health
        self.__swiftness = swiftness

    def alter(self, number):
        if number == 1:
            self.__strength = int(input("Add strength points: ", ))
            self.base_points -= self.__strength
            self.spent_points += self.__strength
            if self.spent_points < 30:
                print("Good choice !")
        if number == 3:
            self.__health = int(input("Add health points: ", ))
            self.base_points -= self.__health
            self.spent_points += self.__health
            if self.spent_points < 30:
                print("Good choice !")
        if number == 2:
            self.__magic = int(input("Add health points: ", ))
            self.base_points -= self.__magic
            self.spent_points += self.__magic
            if self.spent_points < 30:
                print("Good choice !")
        if number == 4:
            self.__swiftness = int(input("Add health points: ", ))
            self.base_points -= self.__swiftness
            self.spent_points += self.__swiftness
            if self.spent_points < 30:
                print("Good choice !")
        if number == 5:
            number = int(input("Substract __strength points: ", ))
            self.__strength -= number
            self.base_points += number
            self.spent_points -= number
            if self.spent_points < 30:
                print("Good choice !")
        if number == 6:
            self.__magic = int(input("Substract __magic points: ", ))
            self.base_points += self.__magic
            self.spent_points -= self.__magic
            if self.spent_points < 30:
                print("Good choice !")
        if number == 7:
            self.__health = int(input("Substract health points: ", ))
            self.base_points += self.__health
            self.spent_points -= self.__health
            if self.spent_points < 30:
                print("Good choice !")
        if number == 8:
            self.__swiftness = int(input("Substract __swiftness points: ", ))
            self.base_points += self.__swiftness
            self.spent_points -= self.__swiftness
            if self.spent_points < 30:
                print("Good choice !")

    def get_values(self):
        print(self.__strength)
        print(self.__health)
        print(self.__magic)
        print(self.__swiftness)

    def __init__(self,value):
        self.__strength = value
        self.__magic = value
        self.__health = value
        self.__swiftness = value

newhero = Hero(0)

choice = None
while choice != 0:
    print(
        """
        \tUpgrade Your attributes.

        0 - exit Hero's editing
        1 - add Strength 
        2 - add Health
        3 - add Magic
        4 - add Swiftness
        5 - decrease Strength 
        6 - decrease Health
        7 - decrease Magic
        8 - decrease Swiftness
        """
    )
    choice = int(input("Choose Your destiny: "))
    newhero.alter(choice)

print(newhero.base_points)
print(newhero.spent_points)

newhero.get_values()
