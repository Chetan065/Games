print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
a= name1.lower()
b= name2.lower()
e= a+b
c= e.count("t")
d= e.count("r")
f= e.count("u")
g= e.count("e")
h= c+d+f+g
aa= e.count("l")
bb= e.count("o")
cc= e.count("v")
dd= e.count("e")
i= aa+bb+cc+dd
j= str(h) + str(i)
k=int(j)
if k<10 or k>90:
    print(f"Your score is {k}, you go together like coke and mentos.")
elif k>40 and k<50:
    print(f"Your score is {k}, you are alright together.")
else:
    print(f"Your score is {k}")
