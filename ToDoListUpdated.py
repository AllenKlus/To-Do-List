#To Do list
#Developed by Allen Klus
#4/6/18

num_tasks = 1

tasks = []

def time():
    import datetime

    global today

    today = datetime.date.today()

    
def name():
    import time
    
    global name
    
    name = input("Hello, What is your name?").capitalize()

    print("Hello", name + ", I will create a simple to do list for you.")

    print("----------------------------------------")
    time.sleep(2)

def thing():

    global tasks

    for i in range(0, 1):
        tasks.append(input("What is an item on your to do list?"))

def main():

    
    answer = input("Would you like to add another task?(y/n)")

    
    if answer == "y":
        global num_tasks
        num_tasks = num_tasks + 1
        thing()
        main()
    else:
        finished_list()


def finished_list():
    import time

    global tasks

    print("----------------------------------------")    
    print("You have", str(num_tasks), "items on your list")
    time.sleep(2)
    print("Here is your list for", today, name)
    print("----------------------------------------")
    time.sleep(2)

    
    print(tasks, end = " ")

time()
name()
thing()
main()
