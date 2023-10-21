#break statement

for i in range(10):
    print("13 X", i+1, "=", 13*(i+1) )
    if(i >= 5):
        break
print("Loop Breaked")

#continue statement


# for i in range(12):
#     if(i == 10):
#         print("Loop continue")
#         continue
# print("13 X", i+1, "=", 13*(i+1) )

for i in range(1, 11):
    if i % 2 != 0:
        print("iteration continue")
        continue 
    print(i)