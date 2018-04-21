#!/usr/bin/env python

# state_space.py
# This program simulates the state space of a point robot

import sys, random, math, pygame
from pygame.locals import *
from math import sqrt,cos,sin,atan2,pi
from time import sleep
from gen_beliefs import discretize_P

#constants
XDIM = 600
YDIM = 600
WINSIZE = [XDIM, YDIM]
EPSILON = 1.0
MAXDIST = 10000000.0
# This sets the boundary
boundary = [(550,550),(50,550),(50,50),(550,50)]
obstacle = [(200,400),(200,300),(300,300),(300,400)]
delta_t = 1
T = 100

# n is the inward edge normal (in degrees 0 to 2pi)
def PerformBounce(s,bp,n,strategy):
    # Random bounce
    if strategy == 0:
        dir = n + random.random()*pi - pi/2.0

    # Right angle bounce
    elif strategy == 1:
        dir = s[2] + pi/2.0
        if AngleDistance(dir,n) > pi/2.0:
            dir += pi

    # Billiard bounce
    elif strategy == 2:
        rebound = FixAngle(s[2] + pi)
#    print "ad:",AngleDifference(rebound,n),"rebound:",rebound,"n:",n
        dir = rebound + 2.0*AngleDifference(rebound,n)

    # Normal bounce
    elif strategy == 3:
        dir = n
    dir = FixAngle(dir)
    if AngleDistance(dir,n) > pi/2.0:
        print("Error: Illegal bounce.  n:",n,"dir:",dir)
#    print "n:",n,"dir:",dir,"angledist:",AngleDistance(dir,n)
    return (bp[0], bp[1], dir)

def take_step(state, dt, v, theta):
    (x,y) = state
    return (x + v*cos(theta)*dt, y + v*sin(theta)*dt)


def main():
    # Initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    white = 255, 240, 200
    black = 20, 20, 40    
    green = 50, 130, 50
    screen.fill(black)
    pint = (0.0,0.0)

    poly = boundary
    obs = obstacle
    # Set the initial robot state (x,y)
    state = (60.0, 60.0)
    v = 1.0
    theta = 0.0

    disc_s = discretize_P(poly, 10)

    for row in disc_s:
        for pt in row:
            (x,y) = pt
            int_pt = (int(x), int(y)) # pygame is stupid
            pygame.draw.circle(screen, white, int_pt, 1)


    for i in range(0, T, delta_t):

        new_state = take_step(state, delta_t, v, theta)


        pygame.draw.polygon(screen,white,poly,5)
        pygame.draw.polygon(screen,white,obstacle)
        pygame.draw.line(screen,green,new_state,state,3)
        pygame.display.update()
#        print "state:",state
        state = new_state
        sleep(0.1)

        for e in pygame.event.get():
	        if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
	            sys.exit("Leaving because you requested it.")
    while (1):
        1 == 1

# if python says run, then we should run
if __name__ == '__main__':
    main()


