#TASK 1
"""A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a command-line or GUI-based
 application using Python, allowing users to create, update, and track their to-do lists """
#syed muhammad zain bin faisal
#first we will create an empty list for task to add in
z_to_do_list = []
# we need to create,update and track task
# 1st create task aka (task addition)
def Task_adding():
    z_to_do_list.append({"task": input("Enter TASK:"),"completed": False})
    print("TASK ADDED SUCCESSFULLY!!")

# 2ND UPDATE (IF WE WANT TO UPDATE N EXISTING TASK)
def updating_task():
    task_index = int(input("Enter the task index to update: "))
    if task_index<0 or task_index>=len(z_to_do_list):
        print("Invalid task index!")
        return
    n_task=input("Enter to update: ")
    z_to_do_list[task_index]["task"]=n_task
    print("Task updated successfully!")

def mark_as_complete():
    task_index=int(input("Enter the task index to mark as complete: "))
    if task_index<0 or task_index>=len(z_to_do_list):
        print("Invalid!")
        return
    z_to_do_list[task_index]["completed"]=True
    print("marked as complete!!!")

def view_all_tasks():
    if len(z_to_do_list)==0:
        print("No tasks found!")
        return
    print("To_DO list :")
    for in_, t in enumerate(z_to_do_list):
        s="Completed" if t["completed"] else "Not Completed"
        print(f"{in_}. {t['task']} - {s}")

# now we will create a menu
def menu():
    print("Zain's CodSoft TO_DO List: ")
    print("1.Add Task ")
    print("2.Update Task")
    print("3.Mark Task as Complete")
    print("4.View List")
    print("5.Exit")


def main():
    while True:
        menu()
        val=input("Enter your choice: ")
        if val=="1":
            Task_adding()
        elif val=="2":
            updating_task()
        elif val=="3":
            mark_as_complete()
        elif val=="4":
            view_all_tasks()
        elif val=="5":
            print("bye......")
            break
        else:
            print("Invalid!")


if __name__ == "__main__":
    main()
    print(z_to_do_list)
