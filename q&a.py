x = 0
score = x

# Question One 
print("what are the plants and trees release into the air?")
answer_1 = input("a)air\nb)oxygen\nc)music\nd)zak's fart \n:")
if answer_1.lower() == "b" or answer_1.lower() == "oxygen":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, it's oxygen")

# Question Two
print("what color is the trash can you put the boxes in")
answer_2 = input("a) orange\nb)blue\nc)green\nd)black\n:")
if answer_2.lower() == "a" or answer_2.lower() == "orange":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, it's orange")

# Question Three
print("True or False... scientists say that till 2050 there will be more plastic than fish in the ocean?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

# Question Four
print("in the worldwide, how many single-use plastic bags are used per year?")
answer_4 = input("a)300,000\nb)6 billions\nc)500 billions\nd)2 trillions\n:")
if answer_4.lower() == "c" or answer_4 == "500 billions":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The last time the Toronto Maple Leafs won the Stanley Cup was 1967")

# Question Five 
print("True or False... 60,000 marine creaturs are dying from plactic entanglement every year")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct,100,000 marine creaturs are dying from plactic entanglement every year")
    x = x + 1
else:
    print("Incorrect, 100,000 marine creaturs are dying from plactic entanglement every year")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
