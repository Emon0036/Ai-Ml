#We use this without using if-else (it's one kind of switch case)

color = input("enter the color:")

match color:
    case "Green":
        print("Go")
    case "Yello":
        print("Look")
    case "Red":
        print("Stop")
    case _: # it's define the default case
        print("Wrong color baby")    