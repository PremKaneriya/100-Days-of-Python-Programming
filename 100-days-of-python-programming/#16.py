vote = int(input("Enter your age: "))

match vote:
    case _ if (vote >= 18):
        print("you are Eligible fo vote")
    case _ if (vote < 18):
        print("you are not Eligible fo vote")
    case _:
        print("Invalid input")
