task_ex = {
    'task': 'description',
    'priority': 1
}

tasks = []


def priority_convert(task_priority):
    if task_priority == '1':
        return "low"
    if task_priority == '2':
        return "med"
    if task_priority == '3':
        return "high"
    else: 
        return "no priority given"

def all_tasks():
    if tasks:
            print('All tasks: ')
            for index, task_name in enumerate(tasks, start=1):
                print(f'{index}. {task_name["task"]} - {priority_convert(task_name["priority"])}')
    else: 
        print('You haven\'t made any tasks!')



print('Ricky\'s To-Do List')

app_Running = True

while app_Running:
    print('Press 1 to add task')
    print('Press 2 to delete task')
    print('Press 3 to view tasks')
    print('Press q to quit')
    user_choice = input('What do you want to do? ')

    if user_choice == '1':
        new_task = input('What task would you like to add? ')
        task_priority = input('How important is this task? \n 1 = low \n 2 = medium \n 3 = high ')
        tasks.append({
            'task': new_task,
            'priority': task_priority
        })
        print('Task added')

        with open('task.txt', 'a') as file:
            file.write(new_task + ' ' + task_priority)
            file.write('\n')
    
    elif user_choice == '2':
        all_tasks()
        print(int(input('Choose the task number to delete: ')))
        tasks.pop(int())

    elif user_choice == '3':
            all_tasks()
        
    elif user_choice == 'q':
        app_Running = False
        
        

