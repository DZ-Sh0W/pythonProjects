print("Hello in 'The Quiz' !")
print("Answer with 'Yes' or 'No'.")
print()

y = "Yes"
n = "No"

# Question 1
q1 = print("Apple is a US company ?")
a1 = str(input("Answer 1 : "))
if a1 == y:
 p1 = 5
elif a1 == n:
 p1 = -1
else:
 print("Repeat !")
print()

# Question 2
q2 = print("There is 5 countries ?")
a2 = str(input("Answer 2 : "))
if a2 == y:
 p2 = 5
elif a2 == n:
 p2 = -1
else:
 print("Repeat !")
print()

# Question 3
q3 = print("Africa is the big country ?")
a3 = str(input("Answer 3 : "))
if a3 == y:
 p3 = 5
elif a3 == n:
 p3 = -1
else:
 print("Repeat !")
print()

# Question 4
q4 = print("The earth is round ?")
a4 = str(input("Answer 4 : "))
if a4 == y:
 p4 = 5
elif a4 == n:
 p4 = -1
else:
 print("Repeat !")
print()

points = p1+p2+p3+p4
print("Tu as obtenu {}/20 points.".format(points))

