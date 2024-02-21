class TodoList:
    '''Collect tasks for a todolist '''
    def __init__(self, instruction):
        self.instruction = instruction
        self.task = []

    def show_instruction(self):
        ''''Display the instruction'''
        print(self.instruction)

    def store_tasks(self, new_task):
        '''Store tasks'''
        self.task.append(new_task)

    def show_task(self):
        'display all tasks that have been added'
        print('Your todo list for today is: ')
        for task in self.task:
            print(f'- {task}')


