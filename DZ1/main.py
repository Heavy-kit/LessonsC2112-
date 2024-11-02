# import datetime
#
# print(f"Добрий день, Троценкова Анастасія. Зараз: {datetime.datetime.now()}")



# ░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗        ████████╗██╗░░██╗███████╗        ██████╗░░█████╗░░██████╗░
# ██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝        ╚══██╔══╝██║░░██║██╔════╝        ██╔══██╗██╔══██╗██╔════╝░
# ███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░        ░░░██║░░░███████║█████╗░░        ██║░░██║██║░░██║██║░░██╗░
# ██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░        ░░░██║░░░██╔══██║██╔══╝░░        ██║░░██║██║░░██║██║░░╚██╗
# ██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░        ░░░██║░░░██║░░██║███████╗        ██████╔╝╚█████╔╝╚██████╔╝
# ╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝        ╚═════╝░░╚════╝░░╚═════╝░
#
# ██╗░░██╗███████╗██████╗░███████╗
# ██║░░██║██╔════╝██╔══██╗██╔════╝
# ███████║█████╗░░██████╔╝█████╗░░
# ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
# ██║░░██║███████╗██║░░██║███████╗
# ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝


# import random
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.stamina = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print("Time to hunt")
#         self.progress += 0.12
#         self.stamina -= 7
#
#     def to_sleep(self):
#         print("I will sleep")
#         self.stamina += 5
#
#     def to_chill(self):
#         print("Rest time")
#         self.stamina += 3
#         self.progress = 0.1
#
#     def is_alive(self):
#         if self.progress < 0:
#             print("Hunger...")
#             self.alive = False
#         elif self.stamina <= 0:
#             print("Too tired...")
#             self.alive = False
#         elif self.progress > 5:
#             print("Succeed")
#             self.alive = False
#         elif self.progress > 5:
#             print("Very successful")
#             self.alive = False
#
#
#     def end_of_day(self):
#         print(f"Stamina = {self.stamina}")
#         print(f"Progress ={round(self.progress, 2)}")
#
#     def live(self, day):
#         day = "Day" + str(day) + "of" + self.name + "life"
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
#
# Dog = Dog(name=" Homeless Dog ")
# for day in range(365):
#     if Dog.alive == False:
#         break
#     Dog.live(day)




# ░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗        ███╗░░██╗██╗░█████╗░██╗░░██╗        ██╗░░██╗███████╗██████╗░███████╗
# ██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝        ████╗░██║██║██╔══██╗██║░██╔╝        ██║░░██║██╔════╝██╔══██╗██╔════╝
# ███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░        ██╔██╗██║██║██║░░╚═╝█████═╝░        ███████║█████╗░░██████╔╝█████╗░░
# ██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░        ██║╚████║██║██║░░██╗██╔═██╗░        ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
# ██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░        ██║░╚███║██║╚█████╔╝██║░╚██╗        ██║░░██║███████╗██║░░██║███████╗
# ╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░        ╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚═╝        ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝



import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def to_work(self):
        print("I will work")
        self.money += 10
        self.progress += 0.001
        self.gladness -= 3

    def pay_bills(self):
        bill_amount = 100
        print("Time to pay the bills!")
        if self.money >= bill_amount:
            self.money -= bill_amount
            print(f"Bills paid. Money left: {self.money}")
        else:
            print("Not enough money to pay the bills!")
            self.gladness == -100  # Если не может заплатить, теряет счастье
            if self.gladness <= 0:
                self.alive = False
                print("Lost my home...")

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("Broke...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day_str = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day_str:=^50}")

        # Каждые 30 дней Ник платит коммуналку
        if day % 30 == 0:
            self.pay_bills()

        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(366):
    if not nick.alive:
        break
    nick.live(day)
