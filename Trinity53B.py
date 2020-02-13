import turtle
import numpy as np

drawing = turtle.Turtle()
drawing.speed(10000)
pwr = 3

max_n = 200
converge_index = np.zeros(max_n) #like 153, 370, 371, 1
converge_steps = np.zeros(max_n) #the number of steps to come to the convergence point

def CubicAllDigits(n):
    r = 0
    for i in str(n):
        # print("i=", i, "^3=", Cubic(int(i)))
        r += int(i) ** pwr
    return (r)


def MultipleOf3P(n):
    if n % pwr == 0.0:
        return True
    return False


def drawingColor(n):
    if n == 7: return "LightGray"
    if n == 8: return "Gray"
    if (n == 9): return "LightYellow"
    if (n == 10): return "Yellow"
    if (n == 11): return "Green"
    if (n == 12): return "Blue"
    if (n == 13): return "Orange"
    if (n == 14): return "Red"
    if (n == 15): return "Purple"
    return False

def drawArrow(n):
    drawing.down()
    drawing.setposition(0, 0)
    drawing.forward(n * 30)
    if drawingColor(n):
        drawing.color(drawingColor(n))
        drawing.right(3)
        drawing.up()

def main(s1, s2, max_steps):
    global converge_index
    global converge_values
    # angle = 365.0/(s2-s1)
    angle = 3
    drawing.color('red', 'yellow')
    drawing.begin_fill()
    i1 = int(s1)
    i2 = int(s2)
    for i in range(i1, i2):
        steps = 1

        j = CubicAllDigits(i)
        prevj = j

        print()
        print(i)
        print("Steps 1 =>", j)

        while True:
            steps = steps + 1
            j = CubicAllDigits(j)
            #print("Steps", steps, "=>", j)
            if j == prevj:
                #print("steps:",steps)
                drawArrow(steps)
                print(i,"converge at",j,"after", steps,"steps")
                converge_index[i] = j
                converge_steps[i] = steps
                break

            if steps > max_steps: break
            prevj = j

main(str(1), str(max_n), 30)

print("index:", converge_index)
print("steps:", converge_steps)

'''Very large numbers
main(str(9999**1000),
     str(9999**1000)+"100",16)
'''

print("End")

'''The smallest number to reach 153 in 16 cycles will be more than 
1061042524005486968, so not advisable to try it. 
'''


