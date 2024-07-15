
def menu():
  print("Welcome to Joe's To Do List App!")
  print("1. Add a task")
  print("2. Remove a task")
  print("3. View all tasks")
  print("4. Quit")
  option = int(input("What would you like to do? "))
  return option

def add_task(tasks):
  task = str(input("What task would you like to add? "))
  tasks.append(task)
  print(task + " has been added to the list.")

def del_task(tasks):
  task = str(input("What task would you like to remove? "))
  for i in tasks:
    if task in tasks:
      tasks.remove(task)
      print(task + " has been removed.\n")
    else:
      print(task + " is not in the list.\n")


def main():
  running = True
  tasks =[]
  while running:
    option = menu()
    if option == 4:
     print("Goodbye. ")
     running = False 
    elif option == 1:
      add_task(tasks)
      print("These are your tasks: \n")
      for i in tasks:
        print(i)
    elif option == 2:
      del_task(tasks)
      print("These are your tasks: \n")
      for i in tasks:
        print(i)
    elif option == 3:
      print("These are your tasks: \n")
      for i in tasks:
        print(i)
      
    

if __name__ == "__main__":
  main()