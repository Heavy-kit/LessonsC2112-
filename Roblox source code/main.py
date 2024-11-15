# class Player:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# class Team:
#     def __init__(self, team_name):
#         self.team_name = team_name
#         self.players = []
#
#     def add_player(self, player):
#         self.players.append(player)
#         print(f"{player} доданий до команди {self.team_name}.")
#
#     def remove_player(self, player):
#         if player in self.players:
#             self.players.remove(player)
#             print(f"{player} видалений з команди {self.team_name}.")
#         else:
#             print(f"{player} не знайдений у команді {self.team_name}.")
#
#     def show_players(self):
#         print(f"Гравці команди {self.team_name}:")
#         for player in self.players:
#             print(f"- {player}")
#
#
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def __str__(self):
#         return f"{self.name}, {self.position}"
#
#
# class Company:
#     def __init__(self, company_name):
#         self.company_name = company_name
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#         print(f"{employee} доданий до компанії {self.company_name}.")
#
#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             print(f"{employee} видалений з компанії {self.company_name}.")
#         else:
#             print(f"{employee} не знайдений у компанії {self.company_name}.")
#
#     def show_employees(self):
#         print(f"Працівники компанії {self.company_name}:")
#         for employee in self.employees:
#             print(f"- {employee}")
#
#
# class Department:
#     def __init__(self, department_name):
#         self.department_name = department_name
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#         print(f"{employee} доданий до відділу {self.department_name}.")
#
#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             print(f"{employee} видалений з відділу {self.department_name}.")
#         else:
#             print(f"{employee} не знайдений у відділі {self.department_name}.")
#
#     def show_employees(self):
#         print(f"Працівники у відділі {self.department_name}:")
#         for employee in self.employees:
#             print(f"- {employee}")
#
# player1 = Player("Андрій")
# player2 = Player("Марія")
# team = Team("Команда Мрія")
# team.add_player(player1)
# team.add_player(player2)
# team.show_players()
# team.remove_player(player1)
#
# employee1 = Employee("Іван", "Менеджер")
# employee2 = Employee("Олена", "Інженер")
# company = Company("TechCorp")
# company.add_employee(employee1)
# company.add_employee(employee2)
# company.show_employees()
# company.remove_employee(employee1)
#
# department = Department("IT")
# department.add_employee(employee2)
# department.show_employees()
#
# print("Hello world")

# import urllib.request
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())
#
# import requests
# response = requests.get("https://httpbin.org/get")
# print(response.content())
#
# import requests
# response = requests.get("https://httpbin.org/get")
# print(response.content())
# print(f"Datatype - {type(response.content)}")
# print(response.text)
# print(f"Datatype - {type(response.content)}")
#
# import requests
# response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
# print(response.text())
#
# import requests
# response = requests.get("https://coinmarketcap.com/aet")


# from bs4 import BeautifulSoup
# import requests
# response = requests.get("http:quotes.com")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, features="html.parser")
#     soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
#     for elem in soup_list:
#         print(elem)
#     res = soup_list[0].find("p")
#     print(res.text)


# Домашнє завдання eIxhh9h6jQp8zMySKzV_q2D8gq_dCaEJ (назва PDF-Файлу)
# ЗАВДАННЯ 1

print("{TASK 1}")
import random

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type  # ексклюзивний атрибут
        print(f"Engine: {self.engine_type} initialized.")

    def start_engine(self):
        print(f"{self.engine_type} engine started.")  # ексклюзивний метод


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count  # ексклюзивний атрибут
        print(f"Wheels: {self.wheel_count} wheels initialized.")

    def rotate_wheels(self):
        print(f"All {self.wheel_count} wheels are rotating.")  # ексклюзивний метод


class Body:
    def __init__(self, body_type):
        self.body_type = body_type  # ексклюзивний атрибут
        print(f"Body: {self.body_type} body initialized.")

    def open_doors(self):
        print(f"The {self.body_type} body doors are open.")  # ексклюзивний метод


class Car(Engine, Wheels, Body):
    def __init__(self, engine_type, wheel_count, body_type):
        Engine.__init__(self, engine_type)
        Wheels.__init__(self, wheel_count)
        Body.__init__(self, body_type)

    def drive(self):
        self.start_engine()
        self.rotate_wheels()
        print(f"The car with {self.body_type} body is now driving.")


my_car = Car(engine_type="V8", wheel_count=4, body_type="sedan")
my_car.drive()
my_car.open_doors()




# ЗАВДАННЯ 2

print(
    "{"
    ""
    "TASK 2"
    "}"
    )
class Encryptor:
    def __init__(self, number):
        self.__number = number
        self.__result = self.__process_number()

    def __process_number(self):
        operation = random.choice(["add", "multiply", "subtract", "divide"])
        modifier = random.randint(1, 10)
        if operation == "add":
            return self.__number + modifier
        elif operation == "multiply":
            return self.__number * modifier
        elif operation == "subtract":
            return self.__number - modifier
        elif operation == "divide":
            return self.__number / modifier if modifier != 0 else self.__number

    def __str__(self):
        return f"Task 2 encrypted result: {self.__result}"

encrypted_object = Encryptor(42)
print(encrypted_object)
