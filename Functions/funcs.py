import copy
import datetime

def func_list():
        """Повертає обрану функцію у вигляді числа
        """
        func_choice = input('Виберіть зі списку номер функції, яку треба виконати:\n'
                            '0 - Завершення роботи\n'
                            '1 - Створити нову задачу\n'
                            '2 - Переглянути список задач\n'
                            '3 - Переглянути деталі задачі\n'
                            '4 - Редагувати задачу\n'
                            '5 - Видалити задачу\n'
                            '6 - Знайти за назвою\n'
                            '7 - Сортувати за пріоритетом\n'
                            '8 - Знайти прострочені задачі\n\n'
                            'Ваш вибір: ')
        if func_choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print('Не правильно введене значення функції!\n'
                  'Може бути введене число від 0 до 8 відповідно до обираємої функції')
        else:
            return int(func_choice)

def finish_program():
        """ Виводить повідомлення про завершення програми
        """
        print('Програма завершує свою роботу')
        return quit()

def create_new_task(list_of_tasks) -> dict:
        """ Повертає нову задачу у вигляді словника
        """
        if len(list_of_tasks) == 0:
            value_id: int = 1
        else:
            value_id = max(list_of_tasks) + 1
        status = 'pending'
        title = input('Введіть стислий опис задачі:\n')
        while len(title) < 3:
            title = input("Введіть стислий опис задачі (не менше 3 знаків):\n")
        description = input('Детально опишіть задачу:\n')
        while len(description) < 5:
            description = input("Детально опишіть задачу (не менше 5 символів):\n")
        priority = input('Введіть пріорітет задачі (від 1 до 10):\n')
        while priority not in ['1','2','3','4','5','6','7','8','9','10']:
            priority = input('Введене некоректне значення.\n'
                  'Введіть пріорітет задачі (від 1 до 10):\n')
        while True:
            due_time = input('Введіть дедлайн виконання задачі у форматі DD.MM.YYYY: ')
            due_time_parsed = due_time.split('.')
            if len(due_time_parsed) == 3 \
                and len(due_time_parsed[0]) == 2 \
                and len(due_time_parsed[1]) == 2 \
                and due_time_parsed[0].isnumeric() \
                and due_time_parsed[1].isnumeric() \
                and due_time_parsed[2].isnumeric() \
                and 0 < int(due_time_parsed[0]) <= 31 \
                and 0 < int(due_time_parsed[1]) <= 12 \
                and 2022 <= int(due_time_parsed[2]) < 2100:
                break
            print('Дата дедлайну введена некоректно.')
        list_of_tasks[value_id] = [title, description, priority, status, due_time]
        print(f'Створена нова задача:\n'
              f' id: {value_id}\n',
              f'title: {list_of_tasks[value_id][0]}\n',
              f'description: {list_of_tasks[value_id][1]}\n',
              f'priority: {list_of_tasks[value_id][2]}\n',
              f'status: {list_of_tasks[value_id][3]}\n',
              f'due_time: {list_of_tasks[value_id][4]}\n')
        return list_of_tasks

def tasks_list(list_of_tasks):
        """Вивести всі задачі, що існують, відсортовані за значенням поля id. Вивод у форматі “{id} {title} {status}”.
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            list_of_tasks_sorted = sorted(list_of_tasks)
            for item in list_of_tasks_sorted:
                print(f'id: {item}',
                      f'title: {list_of_tasks[item][0]}',
                      f'status: {list_of_tasks[item][3]}',
                      sep=' ' * 10)

def task_detail(list_of_tasks):
        """ Вивести всі поля обраної задачі.
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            input_id = input('Введіть значення id задачі, щоб переглянути деталі задачі:\n')
            while True:
                if input_id.isnumeric() and int(input_id) in list(list_of_tasks.keys()):
                    input_id = int(input_id)
                    break
                else:
                    input_id = input('Введене значення не відповідає існуючим id.\n'
                                     'Введіть значення id задачі, щоб переглянути деталі задачі\n')
            print(f' id: {input_id}\n',
                  f'title: {list_of_tasks[input_id][0]}\n',
                  f'description: {list_of_tasks[input_id][1]}\n',
                  f'priority: {list_of_tasks[input_id][2]}\n',
                  f'status: {list_of_tasks[input_id][3]}\n',
                  f'due_time: {list_of_tasks[input_id][4]}\n')

def task_correction(list_of_tasks: dict) -> dict:
        """ Повертає відредаговану задачу у вигляді словника
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            while True:
                input_id = input('Введіть значення id задачі, яку потрібно корегувати:\n')
                if input_id.isnumeric() and int(input_id) in list(list_of_tasks.keys()):
                    input_id = int(input_id)
                    break
                else:
                    print('Введене значення не відповідає існуючим id.')

            while True:
                title = input('Введіть стислий опис задачі:\n')
                if len(title) == 0:
                    break
                elif len(title) < 3:
                    print("Введено некоректне значення "
                          "(опис повинен містити не менше 3 символів).")

                else:
                    list_of_tasks[input_id][0] = title
                    break

            while True:
                description = input('Детально опишіть задачу:\n')
                if len(description) == 0:
                    break
                elif len(description) < 5:
                    print("Введено некоректне значення "
                          "(опис повинен містити не менше 5 символів).")
                else:
                    list_of_tasks[input_id][1] = description
                    break

            while True:
                priority = input('Введіть пріорітет задачі (від 1 до 10):\n')
                if len(priority) == 0:
                    break
                elif priority in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    list_of_tasks[input_id][2] = priority
                    break
                else:
                    print('Некоректно введене значення.')

            while True:
                status = input('Введіть число, що відповідає статусу задачі:\n'
                               '1 - pending\n'
                               '2 - in process\n'
                               '3 - done\n'
                               'Оберіть поточний статус задачі:\n')
                if len(status) == 0:
                    break
                elif status in ['1', '2', '3']:
                    status = int(status)
                    if status == 1:
                        status = 'pending'
                    elif status == 2:
                        status = 'in process'
                    elif status == 3:
                        status = 'done'
                    list_of_tasks[input_id][3] = status
                    break
                else:
                    print('Введено некоректне значення для статусу задачі.')

            while True:
                due_time = input('Введіть дедлайн виконання задачі у форматі DD.MM.YYYY: ')
                due_time_parsed = due_time.split('.')
                if len(due_time) == 0:
                    break
                elif len(due_time_parsed) == 3 \
                        and len(due_time_parsed[0]) == 2 \
                        and len(due_time_parsed[1]) == 2 \
                        and due_time_parsed[0].isnumeric() \
                        and due_time_parsed[1].isnumeric() \
                        and due_time_parsed[2].isnumeric() \
                        and 0 < int(due_time_parsed[0]) <= 31 \
                        and 0 < int(due_time_parsed[1]) <= 12 \
                        and 2022 <= int(due_time_parsed[2]) < 2100:
                    list_of_tasks[input_id][4] = due_time
                    break
                else:
                    print('Дата дедлайну введена некоректно.')
            changed_task = {input_id: [title, description, priority, status, due_time]}
            print(f'Скорегована задача:\n'
                  f' id: {input_id}\n',
                  f'title: {list_of_tasks[input_id][0]}\n',
                  f'description: {list_of_tasks[input_id][1]}\n',
                  f'priority: {list_of_tasks[input_id][2]}\n',
                  f'status: {list_of_tasks[input_id][3]}\n',
                  f'due_time: {list_of_tasks[input_id][4]}\n')
            return list_of_tasks

def task_del(list_of_tasks):
        """Видалення задачі за id"""
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            while True:
                input_id = input('Введіть значення id задачі, яку потрібно видалити:\n')
                if input_id.isnumeric() and int(input_id) in list(list_of_tasks.keys()):
                    input_id = int(input_id)
                    break
                else:
                    print('Введене значення не відповідає існуючим id.')
            del list_of_tasks[input_id]
            return list_of_tasks

def search_by_title(list_of_tasks):
        """Пошук задачі за ключовими словами
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            while True:
                search_words = input('Введіть слова за якими вести пошук у назвах задач:\n')
                if len(search_words) == 0:
                    print("Нічого не було введено.")
                else:
                    break
            search_words_parsed_1 = search_words.split(' ')
            search_words_parsed_2 = search_words.split(',')
            search_words_parsed = search_words_parsed_1 + search_words_parsed_2
            searching_tasks = []
            for item in search_words_parsed:
                for key in list_of_tasks:
                    if item.lower() in list_of_tasks[key][0].lower():
                        searching_tasks.append(key)
            if len(searching_tasks) > 0:
                searching_tasks = set(searching_tasks)
                print(f'У назвах задач з наступними id виявлено співпадіння:\n {searching_tasks}')
            else:
                print(f'Співпадіння за введеними словами {search_words} не знайдено')

def priority_sorted(list_of_tasks):
        """Вивести задачі відсортовані за значенням поля priority. Вивод у форматі “{id} {title} {status} {priority}”.
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            list_of_tasks_sorted = sorted(list_of_tasks, key = lambda x: (list_of_tasks[x][2], -x), reverse = True)
            for item in list_of_tasks_sorted:
                print(f'id: {item}',
                      f'title: {list_of_tasks[item][0]}',
                      f'status: {list_of_tasks[item][3]}',
                      f'priority: {list_of_tasks[item][2]}',
                      sep=' ' * 10)

def expired_date(list_of_tasks):
        """Виводить прострочені задачі зі статусом відмінним від "Done". Вивод у форматі ““{id} {title} {status} {due_date}””.
        """
        if len(list_of_tasks) == 0:
            print('Поки що не створено ні однієї задачі.')
        else:
            # import copy
            # import datetime
            list_of_tasks_1 = copy.deepcopy(list_of_tasks)
            for key in list_of_tasks:
                due_date = list_of_tasks[key][4]
                due_date_parsed = due_date.split('.')
                due_date_converted = datetime.date(int(due_date_parsed[2]),
                                                   int(due_date_parsed[1]),
                                                   int(due_date_parsed[0]))

                list_of_tasks_1[key][4] = due_date_converted
            current_date = datetime.date.today()
            expired_tasks = [key_ for key_ in list_of_tasks_1 if
                             list_of_tasks_1[key_] != 'done' and current_date > list_of_tasks_1[key_][4]]
            if len(expired_tasks) > 0:
                print('Прострочені задачі:')
                for item in expired_tasks:
                    print(f'id: {item}',
                          f'title: {list_of_tasks[item][0]}',
                          f'status: {list_of_tasks[item][3]}',
                          f'due_date: {list_of_tasks[item][4]}',
                          sep=' ' * 10)
            else:
                print('Немає прострочених завдань!')















