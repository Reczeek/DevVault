import sys

projects = []

def show_menu():
    print(f'=== DevVault ===')
    print(f'1. Dodaj projekt')
    print(f'2. Zobacz projekty')
    print(f'3. Usuń projekt')
    print(f'4. Wyjdź')

def get_choice(ile):
    while True: 
        try:
            choice = int(input())
            if 0 < choice <= ile:
                return choice
            else:
                raise ValueError
        except ValueError:
            print(f'Podaj poprawne dane!')

def validate_project_name(projects, name):
    name = name.strip()
    if len(name) == 0 or len(name) > 50:
        raise ValueError
    if name not in projects:
        return name 
    raise TypeError

def add_project(projects):
    while True:
        try:
            name = input()
            name = validate_project_name(projects, name)
            projects.append(name)
            print(f'Dodano projekt!')
            break
        except ValueError:
            print('Niepoprawne dane!')
        except TypeError:
            print(f'Nazwa zajęta!')

def show_projects(projects):
    if len(projects) == 0:
        print(f'Brak projektów')
        return 0
    else:
        for i, p in enumerate(projects, start=1):
            print(f'{i}. {p}')

def delete_project(projects):
    wynik = show_projects(projects)
    if wynik == 0:
        return 0
    choice = get_choice(len(projects))
    projects.pop(choice - 1)
    print(f'Usunięto projekt!')


def menu_choice(choice, projects):
    if choice == 1:
        add_project(projects)
    elif choice == 2:
        show_projects(projects)
    elif choice == 3:
        delete_project(projects)
    else:
        sys.exit()

def main():
    while True:
        show_menu()
        choice = get_choice(4)
        menu_choice(choice, projects)