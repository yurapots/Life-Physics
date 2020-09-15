import random

#randomwalk() computes the distance from the origin after a random walk with nsteps
#     each step has length of 1 unit
#requires: nsteps>0
def randomwalk(nsteps):
    position=0
    for i in range (nsteps):
        step=random.choice([-1, 1])
        position+=step
    return abs(position)

#averagerandomwalk() computes the average distance from the origin of (number) random walks
#   each with nsteps, each step has length of 1 unit
#requires: number, nsteps > 0
def averagerandomwalk(number, nsteps):
    sum_distance=0
    for i in range (number):
        sum_distance+=randomwalk(nsteps)
    average_distance = sum_distance/number
    print (average_distance)