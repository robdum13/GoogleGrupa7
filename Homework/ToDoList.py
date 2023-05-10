import json

categorii_disponibile = set(["curs", "cumparaturi", "munca", "cadouri","mancare","animale"])
tasks = []

def afisare_sortata():

    tasks_sortate = sorted(tasks, key=lambda t: t["categorie"])
    print("tasks sortate după categorie:")
    for t in tasks_sortate:
        print(t)
def sortare_ascendenta_task():
    tasks_sortate = sorted(tasks, key=lambda t: t["task"])
    print("tasks sortate ascendent după task:")
    for t in tasks_sortate:
        print(t)

def print_tasks(tasks):
    for task in tasks:
        print("Task:", task["task"])
        print("Date:", task["data_limita"])
        print("Person:", task["persoana_responsabila"])
        print("Category:", task["categorie"])
        print("")

# meniu
while True:
    print("\nMeniu:")
    print("1. Adăugare in Lista")
    print("2. Listare date")
    print("3. Sortare")
    print("4. Filtrare")
    print("5. Adaugare Task ")
    print("6. Editare Task ")
    print("7. Stergere Task")
    print("8. Ieșire")

    optiune = input("Introduceți o opțiune: ")

    if optiune == "1":
        task = input("Introduceți un task: ")
        data_limita = input("Introduceți data limită (format: dd.mm.yyyy hh:mm): ")
        persoana_responsabila = input("Introduceți persoana responsabilă: ")
        categorie = input("Introduceți categoria: ")

        if categorie not in categorii_disponibile:
            print(f"Categoria introdusă nu există. Vă rugăm să introduceți una din urmatoarele categorii:", categorii_disponibile)
            continue

        for t in tasks:
            if t["task"] == task:
                print("Taskul introdus deja există. Vă rugăm să introduceți un task nou.")
                continue

        tasks.append({
            "task": task,
            "data_limita": data_limita,
            "persoana_responsabila": persoana_responsabila,
            "categorie": categorie
        })

        adauga_alte_tasks = input("Doriți să adăugați alte tasks? (Da/Nu): ")
        if adauga_alte_tasks.lower() != "da":
            break

        with open("categorii.json", "w") as f:
            json.dump(list(categorii_disponibile), f)

        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    elif optiune=="2":
        afisare_sortata()
    elif optiune=="3":
        sortare_ascendenta_task()

    elif optiune=="4":
        def filter_tasks(tasks):
            field = input("Introduceti campul de filtrare (Task/data_limita/persoana_responsabila/categorie): ")
            value = input("Introduceti valoarea de filtrare: ")

            filtered_tasks = []
            for task in tasks:
                if field == "Task" and value in task['task']:
                    filtered_tasks.append(task)
                elif field == "data_limita" and value in task['data_limita']:
                    filtered_tasks.append(task)
                elif field == "persoana_responsabila" and value in task['persoana_responsabila']:
                    filtered_tasks.append(task)
                elif field == "categorie" and value in task['categorie']:
                    filtered_tasks.append(task)

            return filtered_tasks


        filtered_tasks = filter_tasks(tasks)
        print_tasks(filtered_tasks)

    elif optiune=="5":
        task_nou = input("Introduceți un nou task: ")
        if task_nou in tasks:
            print("Task-ul deja adaugat")
        else:
            tasks.append(task_nou)

    elif optiune=="6":
        def edit_task(tasks):
            print_tasks(tasks)
            task_id = input("Introduceti identificatorul unic al task-ului pe care doriti sa-l editati: ")
            task_exists = False
            for task in tasks:
                if task["id"] == task_id:
                    task_exists = True
                    task_name = input("Introduceti noul nume pentru task: ")
                    task_date = input("Introduceti noua data pentru task (format: DD.MM.YYYY HH:MM): ")
                    task_person = input("Introduceti noua persoana responsabila pentru task: ")
                    task_category = input("Introduceti noua categorie pentru task: ")
                    task["task"] = task_name
                    task["date"] = task_date
                    task["person"] = task_person
                    task["category"] = task_category
                    print("Task-ul a fost editat cu succes!")
            if not task_exists:
                print("Task-ul nu exista!")

    elif optiune == "7":
        def delete_task(tasks):
             print_tasks(tasks)
             task_id = input("Introduceti identificatorul unic al task-ului pe care doriti sa-l stergeti: ")
             task_exists = False
             for task in tasks:
                 if task["id"] == task_id:
                     task_exists = True
                     tasks.remove(task)
                     print("Task-ul a fost sters cu succes!")
             if not task_exists:
                 print("Task-ul nu exista!")
    elif optiune == 8:
        quit()

    else:
        print("Please choose an avaliable option!")