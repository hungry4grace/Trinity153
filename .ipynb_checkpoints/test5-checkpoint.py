import turtle

drawing = turtle.Turtle()
drawing.speed(10000)
pwr = 4

def PwrAllDigits(n):
    r = 0
    for i in str(n):
        # print("i=", i, "^3=", Cubic(int(i)))
        r += int(i)**pwr
    return (r)

def MultipleOfPwr(n):
    if n % pwr == 0.0:
        return True
    return False

def drawingColor(n):
    if n==7:return "LightGray"
    if n==8: return "Gray"
    if (n==9): return "LightYellow"
    if (n==10): return "Yellow"
    if (n == 11): return "Green"
    if (n == 12): return "Blue"
    if (n == 13): return "Orange"
    if (n == 14): return "Red"
    if (n == 15): return "Purple"
    return "LightBlue"

def drawArrow(n):
    drawing.down()
    drawing.setposition(0, 0)
    drawing.forward(n * 30)
    drawing.color(drawingColor(n))
    drawing.right(3)
    drawing.up()

def main(s1, s2, max_steps):
    maxSteps = 0

    drawing.color('red', 'yellow')
    drawing.begin_fill()
    i1 = int(s1)
    i2 = int(s2)
    for i in range(i1, i2 + 1):
        steps = 1
        if (MultipleOfPwr(i)):
            j = PwrAllDigits(i)

            print()
            print(i)
            print("Steps 1 =>", j)

            while j != 4150 :
                if not(MultipleOfPwr(j)):break
                steps = steps + 1
                j = PwrAllDigits(j)
                print("Steps", steps, "=>", j)
                drawArrow(steps)

            if steps > maxSteps:
                maxSteps = steps
                maxStepsNum = i
            if (maxSteps >= max_steps):
                return print("maxStepsNum", maxStepsNum, "maxSteps", maxSteps)
    print("maxStepsNum", maxStepsNum, "maxSteps", maxSteps)

# todo visualize the array up to 100 million, to see if any steps are over 15
# already tested to 10M and not found. Question: can this be proved mathematically?

main(str(4155),
     str(10000),16)

'''Very large numbers
main(str(9999**1000),
     str(9999**1000)+"100",16)
'''

print("End")

'''The smallest number to reach 153 in 16 cycles will be more than 
1061042524005486968, so not advisable to try it. 
'''
