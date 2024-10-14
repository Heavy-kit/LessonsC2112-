# import datetime
#
# print(f"Добрий день, Троценкова Анастасія. Зараз: {datetime.datetime.now()}")

import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.stamina = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to hunt")
        self.progress += 0.12
        self.stamina -= 7

    def to_sleep(self):
        print("I will sleep")
        self.stamina += 5

    def to_chill(self):
        print("Rest time")
        self.stamina += 3
        self.progress = 0.1

    def is_alive(self):
        if self.progress < 0:
            print("Hunger...")
            self.alive = False
        elif self.stamina <= 0:
            print("Too tired...")
            self.alive = False
        elif self.progress > 5:
            print("Succeed")
            self.alive = False
        elif self.progress > 5:
            print("Very successful")
            self.alive = False


    def end_of_day(self):
        print(f"Stamina = {self.stamina}")
        print(f"Progress ={round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


Dog = Dog(name=" Homeless Dog ")
for day in range(365):
    if Dog.alive == False:
        break
    Dog.live(day)