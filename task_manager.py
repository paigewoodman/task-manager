#=====importing libraries===========
import datetime
from datetime import date
import os

#====Reusable Functions====

#Returns a dictionary where key = user and associated value = password
def getUsers():
    userf = open("user.txt", "r+")
    userList = userf.read()
    userf.close()
    userPasswords= {}
    pairs = userList.split("/")
    #iterating through the list "pairs" and putting into new lists - "users" and "passes"
    for x in range(0,len(pairs)):
        string = pairs[x]
        list = string.split(", ")
        #usernames and passwords will have the same index number on both the lists - eg users[0] = admin and passes[0] = adminpassword
        userPasswords.update({list[0] : list[1]})

    return userPasswords

#Returns a list of all task names
def getTaskNames():
    taskNames = []
    f = open("tasks.txt", "r")
    task = f.readline()      
    #ensuring the line is not empty
    while  task!= "":
        #splitting the list by comma space
        tasklist = task.split(", ")
        #adding task names to a list
        if len(tasklist) > 1:
            taskNames.append(tasklist[1])    
        #reading next line   
        task = f.readline()
    
    f.close()
    return taskNames

#Returns a list of keys from a dictionary
def getKeys(dict):
    list = []
    for k in dict.keys():
        list.append(k)

    return list

#allows the user to register a new account
def reg_user():
                
    print("You chose r - register a new user.")
    new_user = input("Please enter a username: ".lower())

    #Ensuring that the username entered does not already exist
    while new_user in users:
        new_user = input("This user already exists, please enter a unique username: ".lower())
        
    new_pass = input("Please enter your password: ")
    confirmed_pass = input("Please confirm your password: ")

    #Ensuring new pass == confirmed pass
    while new_pass != confirmed_pass:
        confirmed_pass = input("Your passwords do not match, please confirm your password: ")

    #writing the user details in user.txt using / as my seperator
    f = open("user.txt", "a")
    f.write(f"/{new_user}, {confirmed_pass}")
    f.close()
    print(f"Thank you, new user {new_user} has been registered.")    
    return

#Allows user to add a new task
def add_task():
    users = getUsers()
    print("You chose a - adding a new task.")
    asignee = input("Who is this task assigned to? ")
    #Assuring task is being assigned to a user that exists.
    while asignee not in users:
        asignee = input("That user doesn't exist, who is this task assigned to? ")

    #Taking details of the new task   
    title = input("Please enter a title of the task: ")
    #Ensuring the task name doesnt already exist to avoid errors later
    taskNames = getTaskNames()
    while title in taskNames:
        title = input("That task already exists, please enter a unique task name:")    
    
    desc = input("Please enter a description for the task: ")
    due = input("Please enter the due date of the task (YYYY-MM-DD): ")
    today = date.today()

    #adding all task info to tasks.txt folder
    f = open("tasks.txt", "a")
    f.write(f"{asignee}, {title}, {desc}, {due}, {today}, No")
    f.close
    print(f"Task {title} assigned to {asignee}, Thank you")

#Allows user to view all existing tasks
def view_all():
    f = open("tasks.txt", "r")
    #reading line by line
    task = f.readline()      
    #ensuring the line is not empty
    while  task!= "":
        #splitting the list by comma space
        tasklist = task.split(", ")
        asignee = tasklist[0]
        title = tasklist[1]
        desc = tasklist[2]
        due = tasklist[3]
        date_assigned = tasklist[4]
        completed = tasklist[5]

        #Printing the task 
        print(f"""
            Assigned To :         {asignee}
              Task Title:         {title}
             Description:         {desc}
                     Due:         {due}
                Assigned:         {date_assigned}
               Completed:         {completed}
               
               """)
            
        task = f.readline()

    f.close()

#Allows user to view tasks assigned to them
def view_mine():
        #Similar to view_all
        f = open("tasks.txt", "r+")
        #reading line by line
        task = f.readline() 
        #Creating a dictionary with the tasks and the number they are assigned to so the user can reference them later.
        userTasks = {}     
        number = 1
        #ensuring the line is not empty
        while  task!= "":
            #splitting the list by comma space
            taskList = task.split(", ")
            asignee = taskList[0]
            #seeing is asignee is = to current user - if yes, print task
            if asignee == username:
                #Adding the task to the users task list along with the assigned task number
                userTasks.update({number:task})
                title = taskList[1]
                desc = taskList[2]
                due = taskList[3]
                date_assigned = taskList[4]
                completed = taskList[5]
                
                print(f"""  
            ============= Task {number} =============

            Task Title:         {title}
            Description:        {desc}
            Due:                {due}
            Assigned:           {date_assigned}
            Completed:          {completed}
            
            """)
                number+=1
            
            task = f.readline()
       
        f.close()
        #Allowing user to edit a task on their task list, or return to main menu
        specificTask = int(input("Please enter the task number you would like to view/edit, or enter -1 to return to the main menu: "))
        if specificTask != -1:
            if specificTask in userTasks:
                #getting the taskdetails from the dictionary
                selectedTask = userTasks.get(specificTask)
                #Splitting the details of the task by ", "
                taskDetails = selectedTask.split(", ")
                title = taskDetails[1]
                desc = taskDetails[2]
                due = taskDetails[3]
                date_assigned = taskDetails[4]
                completed = taskDetails[5]
                #Printing the task that the user has selected, then letting them chose how they would like to edit the task, or return to the menu   
                print(f"""  
            ============= Task {specificTask} =============

            Task Title:         {title}
            Description:        {desc}
            Due:                {due}
            Assigned:           {date_assigned}
            Completed:          {completed}""")
            
                editTask = input(f"""
            You have selected task {specificTask} would you like to:
            e - Edit task details
            c - Mark task as complete
            r - return to menu
            : """.lower())
            #If user enters a incorrect option
            while editTask != "e" and editTask != "c" and editTask != "r":
                editTask = input(f"""
            You have entered an incorrect option please enter:
            e - Edit task details
            c - Mark task as complete
            r - return to menu
            : """.lower())

            #If user decides to edit the task details
            if editTask == "e":
                toEdit = input("""

            You have selected edit task. What would you like to edit?
            a - Task asignee
            d - Task due date
            : """.lower())

            #If the user inputs an invalid answer
                while toEdit != "a" and toEdit !="d":
                    toEdit = input("""
            That is an invalid option. Please select what you would like to edit: 
            a - Task asignee
            d - Task due date
                    """.lower())

            #If the user would like to change the assignee
                if toEdit == "a":
                    f = open("tasks.txt", "r+")
                    lines = f.readlines()
                    #removing existing line for the task
                    f.seek(0)
                    for l in lines:
                        if title not in l:
                            f.write(f"{l}")
                    #Who would user like to assign task to?
                    users = getUsers()
                    new_assignee = input("Who would you like to assign the task to? ".lower())
                    #ensuring user enters a new asignee that exists
                    while new_assignee not in users:
                        new_assignee = input("This user doesn't exist, who would you like to assign the task to? ".lower())

                    #Adding task back to file, with new assignee
                    f.write(f"{new_assignee}, {title}, {desc}, {due}, {date_assigned}, {completed}")
                    f.close()
                    print(f"Task {title} assigned to {new_assignee}, returning to menu...")

                #If user would like to change the due date of the task                        
                if toEdit == "d":
                    f = open("tasks.txt", "r+")
                    lines = f.readlines()
                    #removing existing line for the task
                    f.seek(0)
                    for l in lines:
                        if title not in l:
                            f.write(f"{l}")
                    #When would they like to set the due date?
                    new_due = input("When is the task due (YYYY-MM-DD)? ".lower())
                    #Adding task back to file, with new assignee
                    f.write(f"{username}, {title}, {desc}, {new_due}, {date_assigned}, {completed}")
                    f.close()
                    print(f"Due date now set to {new_due}, returning to menu...")


            #If user wants to mark the task as complete
            if editTask == "c":
                f = open("tasks.txt", "r+")
                lines = f.readlines()
                #removing existing line for the task
                f.seek(0)
                for l in lines:
                    if title not in l:
                        f.write(f"{l}")

                #Adding task back to file, marked as complete
                f.write(f"{username}, {title}, {desc}, {due}, {date_assigned}, Yes")
                f.close()
                print(f"Task {specificTask}: {title} marked as complete, returning to main menu...")


            #If user enters r return them to main menu
            if editTask == "r":
                print("Returning to main menu...")
        
        #If user enters -1 return them to main menu
        else:
            print("Returning to main menu...")


def gen_reports():

    #collecting Task Report data 
    taskCount = len(getTaskNames())
    completedTasks = 0
    unfinishedTasks = 0
    overdueTasks = 0

    f = open("tasks.txt", "r")
    lines = f.readlines()
    f.close()

    today = datetime.datetime.now()
    for l in lines:
        list = l.split(", ")
        #Checking if line has a task
        if(len(list)) > 1 :
            #checks if task is complete 
            complete = list[5].strip("\n")
            if complete.lower() == "yes":
                completedTasks+=1
            else:
                #if task is incomplete, check if overdue
                unfinishedTasks+=1

                date = list[3].split("-")
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])
                due_date = datetime.datetime(year,month,day)
                if due_date < today:
                    overdueTasks += 1
    
    #rounding percentages to 2 dp
    incompletePercent = round((unfinishedTasks/taskCount)*100,2)
    overduePercent = round((overdueTasks/unfinishedTasks)*100,2)

    #Writing gathered data in file
    taskRep = open("task_overview.txt", "w")
    taskRep.write(f"""
    ================ Tasks Overview ================
    Total number of tasks: {taskCount}
    Completed tasks:       {completedTasks}
    Incompleted Tasks:     {unfinishedTasks}
    Overdue Tasks:         {overdueTasks}
    _______________________________________________

    Incomplete:            {incompletePercent}%
    Overdue:               {overduePercent}%
    """)            
    taskRep.close()


    #Collecting User report data
    userList = getKeys(getUsers())
    userCount = len(userList)
    userTaskData = {}
    
    #iterating through all existing users
    for u in userList:
        userIncompleteTasks = 0
        userCompleteTasks = 0
        userOverdueTasks = 0
        #iterating through lines (gathered line 287)
        for l in lines:
            list = l.split(", ")
            #Checking if line has full task details
            if(len(list)) > 1 :        
                assignee = list[0]    
                #If the task is assigned to the current user
                if assignee == u:
                    complete = list[5].strip("\n")
                    #Counting how many completed tasks user has
                    if complete.lower() == "yes":
                        userCompleteTasks+=1
                    else:
                        #counting how many incomplete tasks user has
                        userIncompleteTasks+=1
                        #checking how many incomplete tasks are overdue
                        date = list[3].split("-")
                        year = int(date[0])
                        month = int(date[1])
                        day = int(date[2])
                        due_date = datetime.datetime(year,month,day)

                        if due_date < today:
                            userOverdueTasks += 1

                    #Assigning variables to gathered data    
                    totalUserTasks = userIncompleteTasks+userCompleteTasks
                    userPercentage = ((totalUserTasks/taskCount)*100)
                    userCompleted = ((userCompleteTasks/taskCount)*100)
                    toComplete = ((userIncompleteTasks/taskCount)*100)
                    userOverdue = ((userOverdueTasks/taskCount)*100)
                    #Adding data to dictionary
                    userTaskData.update({u:[totalUserTasks, round(userPercentage,2), round(userCompleted),
                     round(toComplete,2), round(userOverdue,2)]})
    
    #Writing data into file
    userRep = open("user_overview.txt", "w")
    userRep.write(f"""
    ================ Users Overview ================
    Total number of users: {userCount}
    Total number of tasks: {taskCount}
    _______________________________________________""") 
    #Adding individual user data
    for u in userList:
        if u in userTaskData:
            #getting list of data from user key in dictionary
            userDataList = userTaskData.get(u)
            userRep.write(f""" 
                    {u}
    Total tasks assigned:        {userDataList[0]}
    Percentage of total tasks:   {userDataList[1]}%
    Completed:                   {userDataList[2]}%
    Incomplete:                  {userDataList[3]}%
    Overdue:                     {userDataList[4]}%
    _______________________________________________    
    """)
    userRep.close()

    print("Reports generated")
    

def print_stats():
    #Checking if file already exists
    try:
        userRep = open("user_overview.txt", "r")
        taskRep = open("task_overview.txt", "r")
    except IOError:
        gen_reports()
        userRep = open("user_overview.txt", "r")
        taskRep = open("task_overview.txt", "r")

    #Printing lines from file 
    for line in userRep.readlines():
        line.strip("\n")
        print(line)

    userRep.close()

    #Printing lines from file 
    for line in taskRep.readlines():
        line.strip("\n")
        print(line)

    userRep.close()



#====Login Section====
users = getUsers()
username = input("Username: ".lower())
while username not in users:
    username = input("That user doesnt exist, please enter your user:")
#if the username entered exists in the dict. of usernames
password = input("Password: ")
#correct password is the value to the username key in users
correctPass = users.get(username)
while password != correctPass:
    password = input("incorrect password. Please enter your password: ")


while True:
    #presenting the menu to the user and  making sure that the user input is coneverted to lower case.
    print("Select one of the following Options below:")
    if username == "admin":
        print('''
====== Admin Options ======
r - Registering a user
gr - generate reports
ds - display statistics
''')

    menu = input('''a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    #Registering a new user
    if menu == 'r':
        if username == "admin":
            reg_user()
        else:
            print("You need admin access to register a new user")        
        

    #Adding a new task
    elif menu == 'a':
        add_task()

    #Viewing all tasks
    elif menu == 'va':
        view_all()

    #Viewing users own tasks
    elif menu == 'vm':
        view_mine()
    
    #Generating Tasks and Users reports
    elif menu == 'gr':
        if username == "admin":
            gen_reports()
        else:
            print("You need admin access to generate reports")
    
    #Displaying Task and user Reports in console
    elif menu == "ds":
        if username == "admin":
            print_stats()
        else:
            print("You need admin access to view statistics")


    #User decides to exit menu
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #User enters an invalid value
    else:
        print("You have made a wrong choice, Please Try again")
