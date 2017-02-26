import random
import math

print("This program calculates the value of Pi by simulating the throwing of darts onto a round target on a square background.")
n=eval(input("How many darts to throw? "))

hits=0

for i in range (1, n+1):
    randX=random.uniform(-1.0, 1.0)
    randY=random.uniform(-1.0, 1.0)
    if math.sqrt(randX**2 + randY**2) <=1 :
        hits=hits+1
   

piApprox = 4*hits/n

if n==1:
   print("The value of Pi after" , n, "iteration is", piApprox)
if n!=1:
    print("The value of Pi after" , n, "iterations is", piApprox)
