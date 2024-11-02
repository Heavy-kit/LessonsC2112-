class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f"{player} доданий до команди {self.team_name}.")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"{player} видалений з команди {self.team_name}.")
        else:
            print(f"{player} не знайдений у команді {self.team_name}.")

    def show_players(self):
        print(f"Гравці команди {self.team_name}:")
        for player in self.players:
            print(f"- {player}")


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.position}"


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} доданий до компанії {self.company_name}.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee} видалений з компанії {self.company_name}.")
        else:
            print(f"{employee} не знайдений у компанії {self.company_name}.")

    def show_employees(self):
        print(f"Працівники компанії {self.company_name}:")
        for employee in self.employees:
            print(f"- {employee}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} доданий до відділу {self.department_name}.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee} видалений з відділу {self.department_name}.")
        else:
            print(f"{employee} не знайдений у відділі {self.department_name}.")

    def show_employees(self):
        print(f"Працівники у відділі {self.department_name}:")
        for employee in self.employees:
            print(f"- {employee}")

player1 = Player("Андрій")
player2 = Player("Марія")
team = Team("Команда Мрія")
team.add_player(player1)
team.add_player(player2)
team.show_players()
team.remove_player(player1)

employee1 = Employee("Іван", "Менеджер")
employee2 = Employee("Олена", "Інженер")
company = Company("TechCorp")
company.add_employee(employee1)
company.add_employee(employee2)
company.show_employees()
company.remove_employee(employee1)

department = Department("IT")
department.add_employee(employee2)
department.show_employees()

print("Hello world")

import random
from random import randint

number = random.randint(1,10)
print(number)