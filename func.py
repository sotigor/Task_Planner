class Funcs:
    @staticmethod
    def func_list():
        """Повертає обрану функцію у вигляді числа
        """
        func_choice = input('Виберіть зі списку номер функції, яку треба виконати:\n'
                            '0 - Завершення роботи\n'
                            '1 - Створити нову задачу\n'
                            '2 - Переглянути список задач\n'
                            '3 - Переглянути деталі задачі\n'
                            '4 - Редагувати задачу'
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

    @staticmethod
    def finish_program():
        """ Виводить повідомлення про завершення програми
        """
        print('Програма завершує свою роботу')
        return quit()

    @staticmethod
    def create_new_task(value_id :int) -> dict:
        """ Повертає нову задачу у вигляді словника
        """
        status = 'pending'
        value_id: int = value_id + 1
        title = input('Введіть стислий опис задачі:\n')
        while len(title) < 3:
            title = input("Введіть стислий опис задачі (не менше 3 знаків):\n")
        description = input('Детально опишіть задачу:\n')
        while len(description) < 5:
            description = input("Детально опишіть задачу (не менше 5 символів):\n")
        priority = input('Введіть пріорітет задачі (від 1 до 10):')
        while priority not in ['1','2','3','4','5','6','7','8','9','10']:
            priority = input('Введене некоректне значення.\n'
                  'Введіть пріорітет задачі (від 1 до 10):')
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
        new_task = {value_id: [title, description, priority, status, due_time]}
        return new_task



