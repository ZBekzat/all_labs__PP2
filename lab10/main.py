from lab10.db.dbConnector import DBConnector
from lab10.db.PhoneBook import PhoneBook


def menu():
    db = DBConnector()
    db.createTable()

    while True:
        print("[1] ADD USER")
        print("[2] ALL USERS")
        print("[3] UPDATE USER")
        print("[4] DELETE USER")
        print("[0] EXIT")
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            print("ENTER NAME")
            name = input()
            print("ENTER SURNAME")
            surname = input()
            print("ENTER PHONE NUMBER")
            phone = input()
            user = PhoneBook(name, surname, phone)
            db.add_phone(user)
        elif choice == 2:
            allUsers = db.get_all_users()
            for user in allUsers:
                print(user)
        elif choice == 3:
            allUsers = db.get_all_users()
            for user in allUsers:
                print(user)
            print("ENTER ID")
            id = int(input())
            print("UPDATE BY name/phone?")
            upd = input()
            if upd == "name":
                print("ENTER NEW NAME")
                name = input()
                db.update_phone_by_name(id, name)
            elif upd == "phone":
                print("ENTER NEW PHONE")
                phone = input()
                db.update_phone_by_phone(id, phone)
        elif choice == 4:
            allUsers = db.get_all_users()
            for user in allUsers:
                print(user)
            print("ENTER ID FOR DELETE")
            id = input()
            db.delete_phone_by_id(id)


if __name__ == '__main__':
    menu()