#working
import RPi.GPIO as IO  #calling for header file which helps in using GPIO’s of PI
import time            #calling for time to provide delays in program
IO.setwarnings(False)  #do not show any warnings
x=1
y=1
z=0

IO.setmode (IO.BCM)
IO.setup(4,IO.OUT)   #initialize GPIO4 as an output
IO.setup(17,IO.OUT)  #initialize GPIO17 as an output
IO.setup(27,IO.OUT)  #initialize GPIO27 as an output
IO.setup(24,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(5,IO.OUT)
IO.setup(6,IO.OUT)
IO.setup(13,IO.OUT)

columns = [4,17,27,24,23,18,25,12,16]  #GPIO pins of columns in order
rows =[5,6,13]  #GPIO pins of rows in order
random = [4,24,25,17,23,12,27,18,16]   #GPIO pins of columns in random

for z in range (3):
    IO.output(rows[z],1)      #pulling up the rows
for z in range (9):
    IO.output(columns[z],0)   #pulling down the columns

while 1:
    for y in range (3):       #execute the loop 3 times incrementing y value from zero to three
        IO.output(rows[y],0)  #pull down the rows pointed by 'y'
        for x in range (9):   #execute the loop 9 times incrementing x value from zero to eight
            IO.output(columns[x],1) #pull up the columns pointed by 'x'
            time.sleep(0.1)         #sleep for 100ms
            IO.output(columns[x],0) #pull down the columns after 100ms
        IO.output(rows[y],1)        #pull up the row after 100ms

    for y in range (3):
        IO.output(rows[2-y],0)
        for x in range (9):
            IO.output(columns[8-x],1)
            time.sleep(0.1)
            IO.output(columns[8-x],0)
        IO.output(rows[2-y],1)

    for y in range (3):
        IO.output(rows[y],0)
        
    for x in range (9):
        IO.output(columns[x],1)
        time.sleep(0.1)
        IO.output(columns[x],0)

    for y in range (3):
        IO.output(rows[y],1)

    for y in range (3):
        IO.output(rows[2-y],0)

    for x in range (9):
        IO.output(columns[8-x],1)
        time.sleep(0.1)
        IO.output(columns[8-x],0)
    for y in range (3):
        IO.output(rows[2-y],1)

    for y in range (3):
        IO.output(rows[y],0)
        for x in range (9):
            IO.output(random[x],1)
            time.sleep(0.1)
            IO.output(random[x],0)
        IO.output(rows[y],1)

    for y in range (3):
        IO.output(rows[2-y],0)
        for x in range (9):
            IO.output(random[8-x],1)
            time.sleep(0.1)
            IO.output(random[8-x],0)
        IO.output(rows[2-y],1)
