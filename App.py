from fastapi import FastAPI, HTTPException
class Task:
  def __init__(self,sno,name,status):
    self.sno=sno
    self.name=name
    self.status=status

alltasks=[]

def createtask(sno,name,status):
  sno=len(alltasks)+1
  name=str(input("Enter the task: "))
  status="pending"
  task=Task(sno,name,status)
  alltasks.append(task)
  print("Task added successfully \n")

def display():
  if len(alltasks)==0:
    print("No tasks found \n")
    return
  for task in alltasks:
    print(f"S.No: {task.sno} Task: {task.name} Status: {task.status}\n")

def mark_as_completed(sno):
  for task in alltasks:
    if task.sno==sno:
      task.status="completed"
      print("Task marked as completed \n")
      return


def deletetask(sno):
  for task in alltasks:
    if task.sno==sno:
      alltasks.remove(task)
      print("Task deleted successfully \n")
      return

print("Welcome to TODO app")
print("Your menu here...")
while True:
  print("************************************************************************")
  print("Press 1 to add a task")
  print("Press 2 to display all tasks")
  print("Press 3 to mark a task as completed")
  print("Press 4 to delete a task")
  print("Press 5 to exit")
  print("************************************************************************ \n")
  choice = input("Enter your choice: \n")
  if choice == "1":
    createtask(0, "", "")
  elif choice == "2":
    display()
  elif choice == "3":
    sno=int(input("Enter the S.No of the task to be marked as completed: "))
    mark_as_completed(sno)
  elif choice == "4":
    sno=int(input("Enter the S.No of the task to be deleted: "))
    deletetask(sno)
  elif choice == "5":
    print("Thank you for using TODO app")
    break
  else:
    print("Invalid choice")