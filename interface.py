import os
import datetime
import PySimpleGUI as sg

diaryfile = "diary.txt"

def menu():
    print("\nDiary App!")
    print("1: Write a new entry.")
    print("2: View all entries.")
    print("3: Delete all entries.")
    print("4: Exit out of diary.")
    return input("Choose one of the options: ")

def write(entry_date, entry_text):
    with open(diaryfile, 'a') as file:
        file.write(f"\n{entry_date}\n{entry_text}\n{'-'*20}\n")

def view():
    if os.path.exists(diaryfile):
        with open(diaryfile, 'r') as file:
            text = file.read()
            if text:
                return text
            else:
                return "No entries found. Get to writing!"
    else:
        return "No content!"

def delete():
    if os.path.exists(diaryfile):
        os.remove(diaryfile)
        print("All entries deleted.")
    else:
        print("There are no entries to delete.")

# def main():
#     while True:
#         option = menu()
#         if option == "1":
#             write()
#         elif option == "2":
#             view()
#         elif option == "3":
#             delete()
#         elif option == "4":
#             print("Exiting diary. See you again!")
#             break
#         else:
#             print("Invalid option, try again.")

layout = [  [sg.Text('Welcome to diary!')],
            [sg.Text('What would you like to do today?')],
            [sg.Button('Write')],
            [sg.Button('View all entries')], 
            [sg.Button('Delete all entries')],
            [sg.Button('Exit')]]

window = sg.Window('Diary', layout)
entry_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

while True:
    event, values = window.read()
    if event == 'Write':
        write_layout = [[sg.Text('Time to write!'), sg.Input(key='entry_text')],
                        [sg.Text('Date and time: ' + entry_date)],
                        [sg.Button('Save')],
                        [sg.Button('Exit')]]
        write_window = sg.Window('Writing', write_layout)
        while True:
            write_event, write_values = write_window.read()
            if write_event == 'Save':
                write(entry_date, write_values['entry_text'])
                sg.popup('Your entry has been saved!', no_titlebar=True)
                break
            elif event == 'Exit':
                sg.popup('Exiting writing mode...', no_titlebar=True)
                break
    if event == 'View all entries':
        entries = view()
        view_layout = [[sg.Text('Your entries:')],
                       [sg.Multiline(entries, size=(50,10), disabled=True)],
                       [sg.Button('Exit')]]
        view_window = sg.Window('Viewing', view_layout)
        while True:
            view_event, view_values = view_window.read()
            if view_event == 'Exit' or view_event == sg.WIN_CLOSED:
                sg.popup('Exiting viewing mode...', no_titlebar=True)
                break
        view_window.close()
    if event == 'Delete all entries':
        delete_layout = [[sg.Text("Are you sure? This process cannot be undone")],
                         [sg.Button('Delete')],
                         [sg.Button('Exit')]]
        delete_window = sg.Window('Deleting', delete_layout)
        while True:
            delete_event, delete_values = delete_window.read()
            if delete_event == 'Exit' or delete_event == sg.WIN_CLOSED:
                sg.popup('Exiting delete mode...')
                break
            else:
                delete()
        delete_window.close()

    if event == sg.WIN_CLOSED or event == 'Exit': 
        sg.popup('Exiting diary. See you soon!.', no_titlebar=True)
        break

window.close()

if __name__ == "__main__":
    main()


            
