# Die folgende Übersicht der Aktionen wird lediglich beim Start des Programms angezeigt 
# und danach nicht mehr.
actions="""
TODO-Liste
==========
Verfügbare Aktionen:
- h: Hinzufügen einer neuen Aufgabe
- a: Anzeigen aller Aufgaben
- m: Markieren einer Aufgabe als erledigt
- l: Löschen einer Aufgabe
- b: Programm beenden
"""

# Die Liste descriptions speichert die Beschreibungen der Aufgaben. 
# Jeder Eintrag in dieser Liste ist ein String, der angibt, was zu tun ist.
descriptions = []

# Die Liste status speichert den Status jeder Aufgabe, wobei jeder Eintrag 
# ein Boolean-Wert ist. Ein False bedeutet, dass die Aufgabe an dieser Position in 
# der Liste descriptions noch nicht erledigt ist, und ein True zeigt an, dass die Aufgabe
# abgeschlossen wurde.
#
# Nehmen wir an, beide Listen sehen wie folgt aus:
#       descriptions = ["Aufgabe ABC", "Aufgabe DEF", "Aufgabe GHI"]
#       status = [True, False, True]
#
# Aus dieser Konstellation können wir entnehmen, dass die Aufgaben ABC und GHI erledigt wurden; 
# Aufgabe DEF ist noch offen.
status = []

# Schreib Dein Code unterhalb dieses Kommentars; der Code oberhalb dieses Kommentars darf nicht angepasst werden
def define_action(action:str):
    print(actions)
    user_input = input("bitte wähle einer der oben genannten aktionen: ")
    
    return user_input

def validate_input_and_choose_action(action:str):
    match action:
        case "h":
            add_task(input("welche Task möchtest du hinzufügen: "))
        case "a":
            get_all_tasks()
        case "m":
            get_all_tasks()
            mark_as_done(input("Welche nummer willst du als erledigt markieren: "))
        case "l":
            get_all_tasks
            delete_task(input("welche Nummer willst du löschen: "))
        case "b":
            set_run_todo_app_false()
        case _:
            print("please enter a valid input: ")

def get_all_tasks():
    counter = 0
    if len(descriptions) and len(status):
        for i in descriptions:
            counter+=1
            print(f"Aufgabe {counter}: {descriptions[counter -1]} erledigt: {status[counter-1]} ")
        sleep_and_space(200000000)


def get_specific_task(specific_task:int):
                print(f"Aufgabe {specific_task + 1}: {descriptions[specific_task]} erledigt: {status[specific_task-1]} ")
                sleep_and_space(200000000)


            
def add_task(task_to_add:str):
    descriptions.append(task_to_add)
    status.append(False)

def mark_as_done(task_done:str):
    task_array = get_task_array_and_convert_to_int(task_done)
    
    try:
        status[task_array] = True
        get_specific_task(task_array)
        sleep_and_space(200000000)
    except:
        print("deine nummer konnte nicht gefunden werden bitte gib eine gültige nummer ein")

def delete_task(task_delete:str):
    get_all_tasks()
    task_array = get_task_array_and_convert_to_int(task_delete)
    del status[task_array]
    del descriptions[task_array]
    print("succesfully deleted")
    sleep_and_space(200000000)


def set_run_todo_app_false():
    global run_todo_app
    run_todo_app = False
    return run_todo_app

def get_task_array_and_convert_to_int(task_done:str):
    try:
        task_id = int(task_done)
        task_array = task_id - 1
        return task_array
    except:
        print("please enter a valud number")

def sleep_and_space(time:int):
    print('\n')
    for i in range(time):
        time = 0   
if __name__ == "__main__":
    run_todo_app = True
    while run_todo_app:
        user_action = define_action(actions)
        validate_input_and_choose_action(user_action)