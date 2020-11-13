import time
import os

def main_menu():
    print("\n1.Add a contact\n2.Search Contact\n3.Delete Contact\n4.Disclaimer\n5.Credit\n6.Exit")
    main=input("\nEnter your choice:")
    if main == "1":
        add_contact()
    elif main == "2":
        search_contact()
    elif main == "3":
        delete_contact()
    elif main == "4":
        disclaimer()
    elif main == "5":
        credit()
    elif main == "6":
        exit()
    else:
        print("Invalid Input\n\n")
        main_menu()

def add_contact():
    print("\n1.Add a new contact\n2.Edit a contact\n3.Return to Main Menu\n")
    add1=input("\nEnter your choice:")
    if add1 == "1":
        add_new()
    elif add1 == "2":
        edit_contact()
    elif add1 == "3":
        main_menu()
    else:
        print("\nInvalid Input\n\n")
        add_contact()

def delete_contact():
    name=input("Enter Contact Name to Delete:")
    search=name.lower()+".txt"
    try:
        file=open(search,"r")
        file.close()
        os.remove(search)
        print("Contact Deleted!!")
        time.sleep(1.0)
        input("Press Enter to Main Menu:")
        main_menu()
    except FileNotFoundError:
        print("\nNo contact list found with that name.\n")
        time.sleep(1.0)
        input("Press Enter for Main Menu")
        main_menu()

def add_new():
    name=input("\nEnter Name:")
    search=name.lower()+".txt"
    try:
        file=open(search,"r")
        print("File Found!!\n\nDo you want to edit it?")
        choice=input()
        if choice == "Yes" or choice == "yes":
            edit_contact()
        elif choice == "No" or choice == "no":
            main_menu()
        else:
            print("\nInvalid Input!!")
            time.sleep(2.0)
            main_menu()
    except FileNotFoundError:
        add=name.lower()+".txt"
        name=name+"\n"
        nickname=input("Enter Nickname:")+"\n"
        phone=input("Enter Phone:")+"\n"
        email=input("Enter Email:")+"\n"
        dob=input("Enter DOB:")+"\n"
        file=open(add,"w")
        file.write(name)
        file.write(nickname)
        file.write(phone)
        file.write(email)
        file.write(dob)
        file.close()
        print("Contact Added!!")
        time.sleep(2.0)
        input("\nPress Enter for Main Menu:")
        main_menu()

def search_contact():
    sample=input("\nEnter Name to search:")
    search=sample.lower()+".txt"
    try:
        file=open(search,"r")
        print("\nName:",file.readline())
        print("Nickname:",file.readline())
        print("Phone:",file.readline())
        print("Email:",file.readline())
        print("DOB:",file.readline())
        file.close()
        time.sleep(1.0)
        input("Press Enter to Main Menu:")
        main_menu()
    except FileNotFoundError:
        print("\nNo contact list found with that name.\n")
        time.sleep(2.0)
        input("Press Enter for Main Menu")
        main_menu()

def edit_contact():
    sample=input("\nEnter Name to Edit:")
    search=sample.lower()+".txt"
    try:
        file=open(search,"r")
        name=file.readline()
        print("\nName:",name)
        nickname=file.readline()
        print("Nickname:",nickname)
        phone=file.readline()
        print("Phone:",phone)
        email=file.readline()
        print("Email:",email)
        dob=file.readline()
        print("DOB:",dob)
        file.close()
        print("\nWhat you want to edit?\n1.Name\n2.Nick Name\n3.Phone\n4.E-Mail\n5.DOB\n6.Exit")
        main=input("\nEnter your choice:")
        if main == "1":
            name=input()+"\n"
        elif main == "2":
            nickname=input()+"\n"
        elif main == "3":
            phone=input()+"\n"
        elif main == "4":
            email=input()+"\n"
        elif main == "5":
            dob=input()+"\n"
        elif main == "6":
            main_menu()
        else:
            print("Invalid Input\n\n")
            main_menu()
        file=open(search,"w")
        file.write(name)
        file.write(nickname)
        file.write(phone)
        file.write(email)
        file.write(dob)
        file.close()
        print("Contact Updated!!!")
        time.sleep(1.0)
        input("Press Enter to Main Menu:")
        main_menu()
    except FileNotFoundError:
        print("\nNo contact list found with that name.\n")
        time.sleep(2.0)

def developer_contact():
    print("\nDeveloper Name: Kumar Aditya\nE-mail: aditya.g.2005001@gmail.com\n")
    time.sleep(1.0)
    input("Press any key for Main Menu:")
    main_menu()

def disclaimer():
    print("This program is purely made for entertainment purpose! So kindly\ndon't take it on your heart, mind, leg etc")
    time.sleep(1.0)
    input("Press any key for main menu:")
    main_menu()

def credit():
    print("This program is made from the help of the greatest god of all time.\nShre Shree GOOGLE Baba")
    time.sleep(1.0)
    input("Press any key for main menu:")
    main_menu()

print("Welcome to Contact Book")
time.sleep(2.2)
main_menu()
