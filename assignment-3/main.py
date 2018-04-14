from c2_7.CP3 import output as task_0_output
from c2_7.CP5 import output as task_1_output
from c4_1.CP3 import output as task_2_output
from c4_2.CP3 import output as task_3_output
from c4_5.CP1a import output as task_4_output

tasks = ["2.7 - CP3", "2.7 - CP5", "4.1 - CP3", "4.2 - CP3", "4.5 - CP1a"]
current_task = -1

while True:
    current_task += 1
    if current_task >= len(tasks):
        current_task = 0

    next_task = tasks[current_task]
    text = input("Press enter to print output of " + next_task + ".\nEnter e to exit. ")
    if text == 'e':
        break

    if current_task == 0:
        print(task_0_output())
    elif current_task == 1:
        print(task_1_output())
    elif current_task == 2:
        print(task_2_output())
    elif current_task == 3:
        print(task_3_output())
    elif current_task == 4:
        print(task_4_output())

    print()
