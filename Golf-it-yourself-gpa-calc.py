print("Welcome to the Overly Verbose GPA Calculator!")
while 1:
    num=input("How many classes are you in? (at least 5): ")
    if num.isdigit():
        c=int(num)
        if c>=5:break
        print("Please enter a number that is 5 or more.")
    else:print("Unfortunately, that is not a valid number. Please try again.")
g=[]
for i in range(c):
    while 1:
        try:
            x=float(input(f"Enter grade {i+1} (0.0 - 4.0): "))
            if 0<=x<=4:g.append(x);break
            print("Grade must be between 0.0 and 4.0.")
        except:print("Please enter a valid number like 3.5 or 4.0.")
t=sum(g);G=round(t/c,2)
print(f"\n Your current GPA is: {G} (from {c} classes)")
print("\nLet's look at your semesters!")
while 1:
    s=input("Check which semester?\n1. First half\n2. Second half\nEnter 1 or 2: ")
    if s in("1","2"):break
    print("Please enter either 1 or 2.")
h=c//2
if s=="1":sg=g[:h];l="First"
else:sg=g[h:];l="Second"
S=round(sum(sg)/len(sg),2)
print(f"\n{l} semester GPA: {S}")
print(f"Overall GPA: {G}")
if S>G:print("Nice job! You are improving! Keep up the good work!")
elif S<G:print("It looks like you are slipping a little. Time to start focusing a bit more!")
else:print("Your GPA is very steady.")
while 1:
    try:
        goal=float(input("\nWhat is your goal GPA? (0.0 - 4.0): "))
        if 0<=goal<=4:break
        print("Please enter a goal GPA between 0.0 and 4.0.")
    except:print("That’s not a valid number. Try again.")
if G>=goal:print(f"\nCongrats! Your current GPA of {G} already meets or exceeds your goal of {goal}!")
else:
    print(f"\nLet's see if you can reach your goal GPA of {goal} by changing just one grade to 4.0...")
    f=0
    for i,x in enumerate(g):
        if x<4:
            h=g.copy();h[i]=4
            ng=round(sum(h)/c,2)
            if ng>=goal:
                if not f:print("\nThere is good news! You can reach your goal GPA by improving just ONE grade:");f=1
                print(f"- If you raise your grade in class {i+1} from {x} to 4.0, your GPA would be {ng}")
    if not f:
        print("\nYou will need to improve more than one grade to hit your goal GPA.")
        print("It is time for you to lock in and start studying more!")
print("\nThank you for using the Overly Verbose GPA Calculator! Goodbye!")