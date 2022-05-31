from Functions import funcs
hello from kate p *********************
#Initialization of tasks list
list_of_tasks = {}

while True:
    # Main menu
    main_menu = funcs.func_list()
    # Finishing the program
    if main_menu == 0:
        funcs.finish_program()

    # Creating new task
    elif main_menu == 1:
        funcs.create_new_task(list_of_tasks)
        continue

    # Looking through all the tasks
    elif main_menu == 2:
        funcs.tasks_list(list_of_tasks)

    # Looking through the details of the tasks
    elif main_menu == 3:
        funcs.task_detail(list_of_tasks)

    # Correction the tasks
    elif main_menu == 4:
        funcs.task_correction(list_of_tasks)

    # Deleting the tasks
    elif main_menu == 5:
        funcs.task_del(list_of_tasks)

    # Searching by names of tasks
    elif main_menu == 6:
        funcs.search_by_title(list_of_tasks)

    # Sorting tasks by priority field
    elif main_menu == 7:
        funcs.priority_sorted(list_of_tasks)

    # Looking for expired tasks
    elif main_menu == 8:
        funcs.expired_date(list_of_tasks)











