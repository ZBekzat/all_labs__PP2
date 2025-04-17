import csv
from lab10.db.PhoneBook import PhoneBook
from lab10.db.dbConnector import DBConnector

db = DBConnector()
db.createTable()

with open("users.csv", "r") as file:
    allUsers = csv.reader(file)
    for user in allUsers:
        name = user[0]
        surname = user[1]
        phone = user[2]

        u1 = PhoneBook(name, surname, phone)
        db.add_phone(u1)