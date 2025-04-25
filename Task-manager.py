class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def edit(self, new_description, new_priority):
        self.description = new_description
        self.priority = new_priority

    def __str__(self):
        status = "Выполнена" if self.is_completed else "Не выполнена"
        return f"[{self.priority}] {self.description} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def edit_task(self, task_index, new_description, new_priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].edit(new_description, new_priority)
        else:
            print("Задача с таким индексом не найдена.")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


def main():
    task_manager = TaskManager()
    print("Программа менеджер задач")

    while True:
        print("\nДоступные команды:")
        print("1. Создать задачу")
        print("2. Отметить задачу выполненной")
        print("3. Редактировать задачу")
        print("4. Просмотреть список задач")
        print("5. Выход")

        command = input("Введите номер команды: ")

        if command == "1":
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет (высокий, средний, низкий): ")
            task_manager.add_task(description, priority)
            print("Задача добавлена.")

        elif command == "2":
            task_index = int(input("Введите индекс задачи для отметки как выполненной: "))
            task_manager.mark_task_completed(task_index)

        elif command == "3":
            task_index = int(input("Введите индекс задачи для редактирования: "))
            new_description = input("Введите новое описание задачи: ")
            new_priority = input("Введите новый приоритет (высокий, средний, низкий): ")
            task_manager.edit_task(task_index, new_description, new_priority)

        elif command == "4":
            task_manager.view_tasks()

        elif command == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")


main()