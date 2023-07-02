import json

def load_language():
    try:
        with open('lg.json', 'r') as file:
            language_data = json.load(file)
            return language_data['language']
    except FileNotFoundError:
        return None

def save_language(language):
    with open('lg.json', 'w') as file:
        language_data = {'language': language}
        json.dump(language_data, file)

def choose_language():
    while True:
        language = input("Choose the script language (fr/en): ")
        if language == "fr" or language == "en":
            save_language(language)
            break
        else:
            print("Invalid language. Please choose a valid language.")

language = load_language()

if language is None:
    choose_language()

def load_translations():
    try:
        with open(f'{language}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

translations = load_translations()

if translations is None:
    print(f"To apply the language, you need to rerun the script.")
    exit()

def translate(key):
    if key in translations:
        return translations[key]
    else:
        return key

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

task_list = []

def add_task():
    description = input(f"{translate('enter_description')} ({language}): ")
    task = Task(description)
    task_list.append(task)
    save_tasks()
    print(translate('task_added'))

def complete_task():
    index = int(input(f"{translate('enter_index_to_complete')} ({language}): "))
    if index >= 0 and index < len(task_list):
        task = task_list[index]
        task.completed = True
        save_tasks()
        print(translate('task_marked_completed'))
    else:
        print(translate('invalid_index'))

def delete_task():
    index = int(input(f"{translate('enter_index_to_delete')} ({language}): "))
    if index >= 0 and index < len(task_list):
        del task_list[index]
        save_tasks()
        print(translate('task_deleted'))
    else:
        print(translate('invalid_index'))

def display_tasks():
    load_tasks()
    if len(task_list) == 0:
        print(translate('no_tasks'))
    else:
        for i, task in enumerate(task_list):
            status = translate('completed') if task.completed else translate('in_progress')
            print(f"{i}. {task.description} ({status})")

def save_tasks():
    with open('tasks.json', 'w') as file:
        task_data = []
        for task in task_list:
            task_data.append({
                'description': task.description,
                'completed': task.completed
            })
        json.dump(task_data, file)
        print(translate('tasks_saved'))

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            task_data = json.load(file)
            task_list.clear()
            for data in task_data:
                task = Task(data['description'])
                task.completed = data['completed']
                task_list.append(task)
        print(translate('tasks_loaded'))
    except FileNotFoundError:
        print(translate('no_tasks_file'))

def change_language():
    while True:
        new_language = input(translate('change_languageO'))
        if new_language == "fr" or new_language == "en":
            save_language(new_language)
            print(translate('language_changed'))
            print(translate('valid_lg'))
            break
        else:
            print(translate('invalid_language'))

while True:
    print("\n" + translate('menu'))
    print('1. ' + (translate('add_task')))
    print('2. ' + (translate('complete_task')))
    print('3. ' + (translate('delete_task')))
    print('4. ' + (translate('display_tasks')))
    print('5. ' + (translate('change_language')))
    print('6. ' + (translate('quit')))

    choice = input(f"{translate('enter_choice')} ({language}): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        change_language()
        break
    elif choice == "6":
        print(translate('goodbye'))
        break
    else:
        print(translate('invalid_choice'))
