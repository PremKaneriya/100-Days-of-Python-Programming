# a good morning excersice

time = int(input("Please Sir Enter Present Time: "))
print("Your Office time is", time, "Thank You Sir")

if(time > 8):
    print("Good Morning Sir")
elif(time > 12):
    print("Good Afternoon Sir")
elif(time < 6):
    print("Good Evening Sir")
else:
    print("Good Night Sir")

