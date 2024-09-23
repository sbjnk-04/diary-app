import os
import datetime

diaryfile = "diary.txt"

def menu():
    print("\nDiary App!")
    print("1: Write a new entry.")
    print("2: View all entries.")
    print("3: Delete all entries.")
    print("4: Exit out of diary.")
    return input("Choose one of the options: ")

def write():
    with open(diaryfile, 'a') as file:
        entry_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        print(f"Date and time: {entry_date}")
        entry = input("Write your entry: ")
        file.write(f"\n{entry_date}\n{entry}\n{'-'*20}\n")
        print("Your entry has been added successfully.")

def view():
    if os.path.exists(diaryfile):
        with open(diaryfile, 'r') as file:
            content = file.read()
            if content:
                print("\nYour diary entries: ")
                print(content)
            else:
                print("\nNo entries found. Get to writing!")
    else:
        print("\nNo entries found.")

def delete():
    if os.path.exists(diaryfile):
        os.remove(diaryfile)
        print("All entries deleted.")
    else:
        print("There are no entries to delete.")

def main():
    while True:
        option = menu()
        if option == "1":
            write()
        elif option == "2":
            view()
        elif option == "3":
            delete()
        elif option == "4":
            print("Exiting diary. See you again!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()


            
