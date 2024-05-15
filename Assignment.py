# Lee Lerk Ann (TP063089)
# Lee Chui Teng (TP064407)

def Home_Page():
    db = open("Events.txt", "r")
    print("Available Events: ")
    for i in db:
        a, b, c, d, e, f, g = i.split(", ")
        g = g.strip()
        print("Event Categories: " + a + ", Event Name: " + b + ", Event Time: " + c + ", Event Date: " + d)
        print("Event Destination: " + e + ", Event Price: " + f + ", Event Organizer: " + g)
    db.close()
    while True:
        selection = input("Register/Login/Exit: ")
        if selection.capitalize() == "Register":
            Registration_Page()
        elif selection.capitalize() == "Login":
            Login_Page()
        elif selection.capitalize() == "Exit":
            print("Please come visit again! ")
            break
        else:
            print("Error, please reselect from the available options.")

def Registration_Page():
    db = open("Account(Customer).txt", "r")
    Username_list = []
    Password_list = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        Username_list.append(a)
        Password_list.append(b)
    db.close()
    while True:
        Username = input("Create username(Exit) to exit: ")
        if Username == "Exit" :
            break
        elif Username in Username_list:
            print("Username exists,please create a new one")
        else:
            while True:
                Password = input("Create password: ")
                if Password.capitalize() == "Exit":
                    break
                else:
                    Password1 = input("Confirm password: ")
                    if Password != Password1:
                        print("Password doesn't match")
                    elif len(Password) < 8:
                        print("Password too short")
                    elif sum(x.isupper() for x in Password) < 1:
                        print("Password did not consist of any uppercase letter, restart ")
                    elif sum(x.isnumeric() for x in Password) < 1:
                        print("Password did not consist of any number, restart ")
                    else:
                        db = open("Account(Customer).txt", "a")
                        db.write(Username + ", " + Password + "\n")
                        print("You have completed your registration!")
                        db.close()
                        break
            break

def Login_Page():
    while True:
        Role = input("Login in as \"Admin\"/\"Customer\" or \"Exit\" to the homepage: ")
        if Role.capitalize() == "Admin":
            db = open("Account(Admin).txt", "r")
            Username = login_system(db)
            if Username.capitalize() == "Exit":
                break
            else:
                Login_Admin(Username)
        elif Role.capitalize() == "Customer":
            db = open("Account(Customer).txt", "r")
            Username = login_system(db)
            if Username.capitalize() == "Exit":
                break
            else:
                Login_Customer(Username)
        elif Role.capitalize() == "Exit":
            break
        else:
            print("Error, please reselect the available options")

def login_system(db):
    Username_list = []
    Password_list = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        Username_list.append(a)
        Password_list.append(b)
    while True:
        Username = input("Enter your username <Exit> to exit: ")
        if Username.capitalize() == "Exit":
            return Username
        Password = input("Enter your password: ")
        if Username in Username_list:
            temp_score = Username_list.index(Username)
            if Password_list[temp_score] == Password:
                print("login Success")
                print("Welcome back,", Username)
                db.close()
                return Username
            else:
                print("Incorrect Username or Password \nPress <Exit> to quit")
        else:
            print("Incorrect Username or Password \nPress <Exit> to quit")

def Login_Admin(Username):
    while True:
        Option = input("Do you wish to <Add> , <Modify> , <Display> , <Search> events or <Exit>: ")
        if Option.capitalize() == "Add":
            db = open("Events.txt", "a")
            while True:
                Event_Categories = input("Type of event Categories <Exit> to exit: ")
                Event_Categories = Event_Categories.capitalize()
                if Event_Categories == "Exit":
                    print("Successfully Exit!")
                    break
                else:
                    Event_Name = input("Name of the event: ")
                    Event_Name = Event_Name.title()
                    Event_Time = input("Time of the event <in 24h system>: ")
                    Event_Date = input("Date of event Categories: ")
                    Event_Date = Event_Date.title()
                    Event_Destination = input("Destination of event Categories: ")
                    Event_Destination = Event_Destination.title()
                    Event_Price = input("Price of event Categories<RM>: ")
                    Conformation = input("Do you wish to insert this?: " +
                    Event_Categories + ", " + Event_Name + ", " + Event_Time + ", " + Event_Date + ", " +
                             Event_Destination + ", " + Event_Price + ", " + Username + "\n" + "Y/N: ")
                    if Conformation.capitalize() == "Y":
                        db.write(Event_Categories + ", " + Event_Name + ", " + Event_Time + ", " + Event_Date + ", " +
                                 Event_Destination + ", " + Event_Price + ", " + Username + "\n")
                        print("Complete adding it.")
                        db.close()
                        break
                    elif Conformation.capitalize() == "N":
                        print("Please reenter the event or <Exit>")
        elif Option.capitalize() == "Modify":
            db = open("Events.txt", "r")
            filelist = db.readlines()
            New_list = filelist
            db.close()
            Event_Name_Edit = input("Which of the events u wish to edit (Enter the name of the event): ")
            Event_Name_Edit = Event_Name_Edit.title()
            for i in filelist:
                if Event_Name_Edit in i:
                    print(i)
                    while True:
                        Conformation = input("Is this event you wish to edit? <Y/N> :")
                        Conformation = Conformation.capitalize().strip()
                        if Conformation == "Y":
                            temp = filelist.index(i)
                            db = open("Events.txt", "w")
                            Event_Categories = input("Type of the event: ")
                            Event_Categories = Event_Categories.title().strip()
                            Event_Name = input("Name of the event: ")
                            Event_Name = Event_Name.title().strip()
                            Event_Time = input("Time of the event <in 24h system>: ")
                            Event_Date = input("Date of event Categories: ")
                            Event_Date = Event_Date.title().strip()
                            Event_Destination = input("Destination of event Categories: ")
                            Event_Destination = Event_Destination.title().strip()
                            Event_Price = input("Price of event Categories<RM>: ")
                            Event_Price = Event_Price.strip()
                            New_list[temp] = (
                                        Event_Categories + ", " + Event_Name + ", " + Event_Time + ", " + Event_Date
                                        + ", " + Event_Destination + ", " + Event_Price + ", " + Username + "\n")
                            for line in New_list:
                                db.write(line)
                            print("The event have successfully been modify!")
                            db.close()
                            break
                        elif Conformation == "N":
                            break
                        else:
                            print("There is only 2 option \"Y\" as Yes and \"N\" as No")
            print("End of the search and modify!")
        elif Option.capitalize() == "Display":
            print("Displaying The Events: ")
            db = open("Events.txt", "r")
            for i in db:
                a, b, c, d, e, f, g= i.split(", ")
                g = g.strip()
                print("Event Categories: " + a + ", Event Name: " + b + ", Event Time: " + c + ", Event Date: " + d)
                print("Event Destination: " + e + ", Event Price: " + f + ", Event Organizer: " + g)
            db.close()
            print("Displaying The Payment: ")
            db = open("Payment.txt", "r")
            for i in db:
                a, b, c = i.split(", ")
                c = c.strip()
                print("Register name: " + a + ", Events Name: " + b + "Payment Made: " + c)
            db.close()
        elif Option.capitalize() == "Search":
            record = input("Insert the keyword to search: ")
            record = record.title()
            while True:
                Selection = input("Do you wish to search regarding <Events> or <Payment>: ")
                Selection = Selection.capitalize()
                if Selection == "Events":
                    db = open("Events.txt", "r")
                    print("The following are the events base on the keywords given")
                    for line in db:
                        if record in line:
                            print(line)
                    db.close()
                    break
                elif Selection == "Payment":
                    db = open("Payment.txt", "r")
                    print("The following are the payment base on the keywords given")
                    for line in db:
                        if record in line:
                            print(line)
                    db.close()
                    break
                else:
                    print("There is only 2 option. Please reselect!")
        elif Option.capitalize() == "Exit":
            break
        else:
            print("Error, please reselect the available options")

def Login_Customer(Username):
    db = open("Events.txt", "r")
    Events_Categories = []
    Events_Name = []
    Events_Price = []
    Temp_Events_Name = []
    Temp_Events_Price = []
    Total_Price = 0
    for i in db:
        a, b, c, d, e, f, g = i.split(", ")
        Events_Categories.append(a)
        Events_Name.append(b)
        f = f.strip()
        if f == "Free":
            Events_Price.append(f)
        else:
            f = int(f)
            Events_Price.append(f)
    Events_Categories = set(Events_Categories)
    print(Events_Categories)
    db.close()
    print("Please select the type of event you wish to see base on the given categories: ")
    print("If you wish to exit, Please enter <Exit>")
    Categories_Selection = input("> ")
    db = open("Events.txt", "r")
    while True:
        while True:
            Categories_Selection = Categories_Selection.capitalize()
            if Categories_Selection in Events_Categories:
                print("This are the events base on the categories you have chosen!\n")
                for i in db:
                    if i.startswith(Categories_Selection):
                        a, b, c, d, e, f, g = i.split(", ")
                        f = f.strip()
                        print("Event Name: " + b + ", Event Time: " + c + ", Event Date: " + d)
                        print("Event Destination: " + e + ", Event Price: " + f + ", Event Organizer: " + g)
                break
            elif Categories_Selection == "Exit":
                break
            else:
                print("There is no such categories of events! Please reselect the categories base on the given option")
                print("If you wish to exit, Please enter <Exit>")
                print(Events_Categories)
                Categories_Selection = input("> ")
        db.close()
        break
    print("Which event are you interest in and wish to add to cart")
    print("If you wish to exit, Please enter <Exit>")
    Events_Selection = input("Enter the Events Name: ")
    Events_Selection = Events_Selection.title()
    while True:
        if Events_Selection == "Exit":
            break
        elif Events_Selection in Events_Name:
            temp = Events_Name.index(Events_Selection)
            Temp_Events_Name.append(Events_Selection)
            if Events_Price[temp] == "Free":
                Temp_Events_Price.append(0)
            else:
                Total_Price += Events_Price[temp]
                Temp_Events_Price.append(Events_Price[temp])
            while True:
                Add = input("Is there anymore event you wish to join from this categories? <Y/N> : ")
                if Add.capitalize() == "N":
                    Events_Selection = "Exit"
                    break
                elif Add.capitalize() == "Y":
                    Events_Selection = input("Enter the Events Name,<Exit> to return: ")
                    Events_Selection = Events_Selection.title()
                    break
                else:
                    print("There is only <Y> as Yes and <N> as No in the option")
        else:
            print("There is no such events")
            Events_Selection = input("Enter the Events Name: ")
            Events_Selection = Events_Selection.title()
    if len(Temp_Events_Name) > 0 :
        print("This is the price you need to pay for all of the events: RM" + str(Total_Price))
        Conformation = input("Do you wish to make the payment and register to the event? <Y/N>: ")
        while True:
            Conformation = Conformation.capitalize()
            if Conformation == "N":
                print ("Your registration have been cancel!")
            elif Conformation == "Y":
                Payment = int(input("Please insert the amount that need to pay: RM"))
                while True:
                    if Total_Price <= Payment:
                        print("U have complete the payment")
                        print("The remaining money have been return: RM" + str(Payment - Total_Price))
                        for i in range (len(Temp_Events_Name)):
                            db = open("Payment.txt", "a")
                            Temp_Name = Temp_Events_Name.pop(0)
                            Temp_Price = Temp_Events_Price.pop(0)
                            db.write(Username + ", " + str(Temp_Name) + ", RM" + str(Temp_Price) + "\n")
                        break
                    else:
                        print("The payment have not been complete. You have not fully pay the price yet. Remaining: RM"
                              + str(Total_Price - Payment))
                        temp_Payment = int(input("Please pay the remaining payment: "))
                        Payment += temp_Payment
                break
            else:
                print("There is only 2 option, <Y/N>")
                Conformation = input("Do you wish to make the payment and register to the event? <Y/N>: ")

Home_Page()
