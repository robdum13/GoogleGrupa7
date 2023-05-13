categorii_disponibile = set(["curs", "cumparaturi", "munca", "cadouri","mancare","animale"])

def read_tasks_from_file():
    tasks = []
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            task_data = line.strip().split(":")
            if len(task_data) >= 4:
                task = {
                    "task": task_data[0].strip(),
                    "data_limita": task_data[1].strip(),
                    "persoana_responsabila": task_data[2].strip(),
                    "categorie": task_data[3].strip()
                }
                tasks.append(task)
    return tasks

tasks = read_tasks_from_file()

def afisare_sortata(tasks):
    tasks_sortate = sorted(tasks, key=lambda t: t["categorie"])
    return tasks_sortate

tasks = read_tasks_from_file()

def print_tasks(tasks):
    for task in tasks:
        print("Task:", task)
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
            print(f"Categoria introdusă nu există. Vă rugăm să introduceți una din următoarele categorii:", categorii_disponibile)
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

    elif optiune == "2":
       listare=afisare_sortata(tasks)
       print(listare)

    elif optiune == "3":
        sorted_tasks = afisare_sortata(tasks)
        for task in sorted_tasks:
            print("Task:", task["task"])
            print("Data:", task["data_limita"])
            print("Persoana responsabilă:", task["persoana_responsabila"])
            print("Categorie:", task["categorie"])

    elif optiune == "4":

        field = input("Introduceți câmpul de filtrare (Task/data_limita/persoana_responsabila/categorie): ")
        value = input("Introduceți valoarea de filtrare: ")

        filtered_tasks = []

        with open("tasks.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                task = line.strip()
                task_data = task.split(": ")

                if len(task_data) < 2:
                    continue

                if field == "Task" and value in task_data[1]:
                    filtered_tasks.append(task)
                elif field == "data_limita" and value in task_data[1]:
                    filtered_tasks.append(task)
                elif field == "persoana_responsabila" and value in task_data[1]:
                    filtered_tasks.append(task)
                elif field == "categorie" and value in task_data[1]:
                    filtered_tasks.append(task)

        print(filtered_tasks)
    elif optiune == "5":
            task_nou = input("Introduceți un nou task: ")
            if task_nou in tasks:
                print("Task-ul deja adaugat")
            else:
                tasks.append({
                    "task": task_nou,
                    "data_limita": "",
                    "persoana_responsabila": "",
                    "categorie": "",
                })

    elif optiune == "6":
        task_name = input("Introduceți numele task-ului pe care doriți să-l editați: ")
        task_exists = False
        for task in tasks:
            if task["task"] == task_name:
                task_exists = True
                task["task"] = input("Introduceți noul nume pentru task: ")
                task["data_limita"] = input("Introduceți noua dată pentru task (format: dd.mm.yyyy hh:mm): ")
                task["persoana_responsabila"] = input("Introduceți noua persoană responsabilă pentru task: ")
                task["categorie"] = input("Introduceți noua categorie pentru task: ")
                print("Task-ul a fost editat cu succes!")
                break
        if not task_exists:
            print("Task-ul nu există!")

    elif optiune == "7":
        def delete_task(tasks):
            print_tasks(tasks)
            task_id = input("Introduceti identificatorul unic al task-ului pe care doriti sa-l stergeti: ")
            task_exists = False
            updated_tasks = []
            for task in tasks:
                if task["task"] == task_id:
                    task_exists = True
                    print("Task-ul a fost sters cu succes!")
                else:
                    updated_tasks.append(task)
            if not task_exists:
                print("Task-ul nu exista!")
            return updated_tasks


        tasks = delete_task(tasks)  # Update tasks with the updated_tasks list

    elif optiune == "8":
        with open("tasks.txt", "a") as f:
            for task in tasks:
                f.write(f"Task: {task['task']}\n")
                f.write(f"Date: {task['data_limita']}\n")
                f.write(f"Person: {task['persoana_responsabila']}\n")
                f.write(f"Category: {task['categorie']}\n")
                f.write("\n")

        break

    else:
        print("Please choose an available option!")