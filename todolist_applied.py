from todolist import  TodoList
instruction = 'Yay you can start adding your tasks '
your_todolist = TodoList(instruction)

#Show the instruction and add tasks to store the tasks to the list:#
your_todolist.show_instruction()
print('Enter "Q" anytime to quit.\n')
while True:
    tasks = input('task: ')
    if tasks.lower() == 'q':
        break
    your_todolist.store_tasks(tasks)
print('Your TodoList for today is: ')
your_todolist.show_task()



