# List Method

name = ["Neil","Nitin","Mukesh"]
print(name)

num = [5,2,6,8,1,3,9,4,7,10]
num.sort()
print(num)

num = [5,2,6,8,1,3,9,4,7,10]
num.sort(reverse=True)
print(num)

num = [5,2,6,8,1,3,9,4,7,10]
print(num.index(4))

name = ["Neil","Nitin","Mukesh"]
newName = name.copy()
print(newName)

# append
name = ["Neil","Nitin","Mukesh"]
name.append("Patel")
print(name)

name1 = ["chacha", "chachi","Mirchi", "chataie"]
name2 = ["chachi", "chacha", "kutai", "huie"]
name1.extend(name2)
print(name1)

bookcatogery = ["fiction", "non-fiction"]
bookname = ["Time Machine", "Power of Your subconsiours mind"]
print(bookcatogery + bookname)
