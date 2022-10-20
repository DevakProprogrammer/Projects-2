#Write your code below this line 👇

def paint_calc(height, width, cover):
    r = (round((height*width) / cover))
    print(f"You'll need {r} cans of paint.")
    mul = r * 35
    print(f"It will cost you ${mul}")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

