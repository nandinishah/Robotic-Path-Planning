__author__ = "Nandini Shah"
__email__ = "nss2158@columbia.edu"

import argparse
from collections import deque
import math


#location of start and goal
def get_location_s(arena,X,Y):
    for x in range(X):
        for y in range(Y):
            if arena[x][y]=='s':
                sx = x
                sy = y
                return(sx,sy) 
        y=0
    print "No start point found on arena. Please check input map." 
    exit()

def get_location_g(arena,X,Y):
    for x in range(X):
        for y in range(Y):
            if arena[x][y]=='g':
                gx = x
                gy = y
                return(gx,gy)
        y=0
    print "No goal found on arena. Please check input map."
    exit()


#BFS Algorithm
def BFS(arena):
    X = len(arena)                                                          #based on map: 7x8, 25x57, 35x96
    arena = [list(line) for line in arena]
    Y = len(arena[0])                                                       #2
    (sx, sy) = get_location_s(arena,X,Y)
    
    # strategy is to explore clockwise
    frontier = deque()
    parent = {}
    x,y = sx, sy                                                            #2                                                                  #1
    i=0                                                                     #1
    frontier.append([x,y])
    
    if arena[x][y]=='g':
        print "Already at goal!"
        return
    
    while (True):
        i=i+1
        if len(frontier)==0:
            print "Goal cannot be reached using BFS algorithm!"
            return 
        
        #marking as explored
        x,y=frontier.popleft()
        arena[x][y] = 'e'
        
        #checking nodes on generation to see if goal is reached
        if (x+1<X and arena[x+1][y]=='g') or (y+1<Y and arena[x][y+1]=='g') or (x-1>-1 and arena[x-1][y]=='g') or (y-1>-1 and arena[x][y-1]=='g'):
            print "Goal Reached"
            print "Number of iterations =",i
            arena[x][y]='*'
            i = 1
            while (not(sx==x and sy==y)):
                x,y=parent[(x,y)]
                arena[x][y]='*'
                i = i+1
            print "Number of steps =", i
            arena[sx][sy]='s'
            for k in range(X):                                                      #1
                for j in range(Y):                                                  #1
                    if arena[k][j]=='e':
                        arena[k][j]=' '
                    if arena[k][j]=='f':
                        arena[k][j]=' '
            for k in range(X):
                str1 = ''.join(str(j) for j in arena[k])
                print str1                                                        
            return
        
        #adding neighbors to frontier and tracking parent node
        if (x-1)>-1 and arena[x-1][y]==' ':
            frontier.append([x-1,y])
            arena[x-1][y]='f'
            parent[(x-1,y)]=(x,y)
        if (y+1)<Y and arena[x][y+1]==' ':
            frontier.append([x,y+1])
            arena[x][y+1]='f'
            parent[(x,y+1)]=(x,y)
        if (x+1)<X and arena[x+1][y]==' ':
            frontier.append([x+1,y])
            arena[x+1][y]='f'
            parent[(x+1,y)]=(x,y)
        if (y-1)>-1 and arena[x][y-1]==' ':
            frontier.append([x,y-1])
            arena[x][y-1]='f'
            parent[(x,y-1)]=(x,y)




#DFS Algorithm
def DFS(arena):
    X = len(arena)                                      # 1
    arena = [list(line) for line in arena]              #size of map
    Y = len(arena[0])                                   # 1
    (sx, sy) = get_location_s(arena,X,Y)                # 2
    
    frontier = deque()
    parent = {}
    frontier.append([sx,sy])
    (x,y)=(sx,sy)                                       
    
    if arena[x][y]=='g':
        print "Already at goal!"
        return
    
    i=0
    while (True):
        i = i+1                                         # 1
        if len(frontier)==0:
            print "Goal cannot be reached using DFS algorithm!"
            return 
        
        #marking as explored
        x,y = frontier.pop()
        arena[x][y]='e'        
        
        #checking nodes on generation to see if goal is reached
        if (x+1<X and arena[x+1][y]=="g") or (y+1<Y and arena[x][y+1]=="g") or (x-1>=0 and arena[x-1][y]=="g") or (y-1>=0 and arena[x][y-1]=="g"):
            print "Goal Reached"
            print "Number of iterations =",i
            arena[x][y]='*'
            i = 1
            while (not(sx==x and sy==y)):
                x,y=parent[(x,y)]
                arena[x][y]='*'
                i = i+1
            print "Number of steps =", i 
            arena[sx][sy]='s'
            for k in range(X):                                                      #1
                for j in range(Y):                                                  #1
                    if (arena[k][j]=='e' or arena[k][j]=='f'):
                        arena[k][j]=' '
                str1 = ''.join(str(j) for j in arena[k])    
                print str1                                                          # 56
            return
        
        #adding neighbor nodes to frontier and tracking parent node
        if y-1>=0 and arena[x][y-1]==' ':
            frontier.append([x,y-1])
            parent[(x,y-1)]=(x,y)
            arena[x][y-1]='f'   
        if x+1<X and arena[x+1][y]==' ':
            frontier.append([x+1,y])
            parent[(x+1,y)]=(x,y)
            arena[x+1][y]='f'
        if y+1<Y and arena[x][y+1]==' ':
            frontier.append([x,y+1])
            parent[(x,y+1)]=(x,y)
            arena[x][y+1]='f'
        if x-1>=0 and arena[x-1][y]==' ':
            frontier.append([x-1,y])
            parent[(x-1,y)]=(x,y)
            arena[x-1][y]='f'
    

    

#Astar algorithm
def Astar(arena):
    X = len(arena)                                                          #1
    arena = [list(line) for line in arena]
    Y = len(arena[0])                                                       #1
    (sx, sy) = get_location_s(arena,X,Y)                                    #2
    (gx,gy) = get_location_g(arena,X,Y)                                     #2
    
    frontier = list()
    parent = dict()
    
    (x,y)=(sx,sy)
    arena[gx][gy]=' '

    #calculating heuristic function as manhattan distance
    h = math.fabs(x-gx)+math.fabs(y-gy)                                         #1 
    g = 0                                                                       #1
    f=g+h
    frontier.append([x,y,g,f])
    parent[(x,y)] = (-1,-1,g,f)

    i=0                                                                         #1
    while(True):
        if len(frontier)==0:
            print "Number of iterations:",i
            arena[sx][sy]='s'
            arena[gx][gy]='g'
            print "Goal cannot be reached using Astar algorithm!"
            for k in range(X):                                                  #1
                for j in range(Y):                                              #1
                    if arena[k][j]=='e':
                        arena[k][j]=' '
                    if arena[k][j]=='f':
                        arena[k][j]=' '
                str1 = ''.join(str(j) for j in arena[k])
                print str1
            return 
        
        #marking nodes as explored
        (x,y,g,f)=frontier.pop()
        arena[x][y] = 'e'

        #goal is reached when heuristic h = 0
        if (int(f-g)==0):
            print "Goal Reached"
            print "Number of iterations =",i
            print "h(n) and g(n)/number of steps =",f-g," ",g            
            arena[x][y]='*'
            while (not(sx==x and sy==y)):
                (x,y,g,f) = parent[(x,y)]
                arena[x][y]='*'
            arena[sx][sy]='s'
            arena[gx][gy]='g'
            for k in range(X):
                for j in range(Y):
                    if arena[k][j]=='e':
                        arena[k][j]=' '
                    if arena[k][j]=='f':
                        arena[k][j]=' '
                    str1 = ''.join(str(j) for j in arena[k])
                print str1
            return
        
        i = i+1
        g = g+1     #every step is cost = 1
        
        #adding neighbor nodes to frontier and tracking parents
        #if node already present in frontier and switching parent if current cost < prior cost
        if x-1>=0 and (arena[x-1][y]=='f' or arena[x-1][y]=='e'):
            h = math.fabs(x-1-gx)+math.fabs(y-gy)
            if parent[(x-1,y)][2]>g:
                parent[(x-1),y] = (x,y,g,h+g)
        if x-1>=0 and arena[x-1][y]==' ':
            h = math.fabs(x-1-gx)+math.fabs(y-gy)
            frontier.append([x-1,y,g,h+g])
            parent[(x-1,y)]=(x,y,g,h+g)
            arena[x-1][y]='f'
                
        if x+1<X and (arena[x+1][y]=='f' or arena[x+1][y]=='e'):
            h = math.fabs(x+1-gx)+math.fabs(y-gy)
            if parent[(x+1,y)][2]>g:
                parent[(x+1),y] = (x,y,g,h+g)
        if x+1<X and arena[x+1][y]==' ':
            h = math.fabs(x+1-gx)+math.fabs(y-gy)
            frontier.append([x+1,y,g,h+g])
            parent[(x+1),y] = (x,y,g,h+g)
            arena[x+1][y]='f'
            
        if y-1>=0 and (arena[x][y-1]=='f' or arena[x][y-1]=='e'):
            h = math.fabs(x-gx)+math.fabs(y-1-gy)
            if parent[(x,y-1)][2]>g:
                parent[x,(y-1)] = (x,y,g,h+g)
        if y-1>=0 and arena[x][y-1]==' ':
            h = math.fabs(x-gx)+math.fabs(y-1-gy)
            frontier.append([x,y-1,g,h+g])
            parent[x,(y-1)] = (x,y,g,h+g)
            arena[x][y-1]='f'
            
        if y+1<Y and (arena[x][y+1]=='f' or arena[x][y+1]=='e'):
            h = math.fabs(x-gx)+math.fabs(y-1-gy)
            if parent[(x,y+1)][2]>g:
                parent[x,(y+1)] = (x,y,g,h+g)
        if y+1<Y and arena[x][y+1]==' ':
            h = math.fabs(x-gx)+math.fabs(y+1-gy)
            frontier.append([x,y+1,g,h+g])
            parent[x,(y+1)] = (x,y,g,h+g)
            arena[x][y+1]='f'
        #sorting the frontier based on h+g to get next node based on minimum cost/path length
        frontier.sort(key = lambda x:x[3], reverse = True)


#Attempt to code the IDAstar algorithm

def manhattanDistanceToGoal(x1,y1):
    return math.fabs(x1-goalx)+math.fabs(y1-goaly)

def IDAstar(arena):
    X = len(arena)
    arena = [list(line) for line in arena]
    Y = len(arena[0])
    (sx, sy) = get_location_s(arena,X,Y)
    global goalx, goaly
    (goalx,goaly) = get_location_g(arena,X,Y)
    h = manhattanDistanceToGoal(sx,sy)
    print "initial bound", h
    bound = h
    print "X,Y,sx,sy,gx,gy,h,bound"
    print X, Y, sx, sy, goalx, goaly, h, bound
    count = 0
    while (count<8):
        print "Count ", count, "Bound ", bound
        frontier = list()
        frontier.append([sx,sy,0,h])
        print frontier
        l = search(frontier, bound, X, Y)
        bound = l
        print l
        if l==-1:
            return
        count = count +1
        print count
    return

def search(frontier, bound, sizeX, sizeY):
    #print frontier, bound, sizeX, sizeY
    x,y,g,f = frontier.pop()
    if f>bound:
        print f
        return f
    if int(f-g)==0:
        print "Goal Reached!"
        print "Number of steps =",g
        return -1
    if f<=bound:
        if x-1>=0 and arena[x-1][y]==' ':
            #left
            h = manhattanDistanceToGoal(x-1, y)
            frontier.append([x-1,y,g+1,g+1+h])
        #parent[(x-1,y)]=(x,y,h,g)
        if x+1<sizeX and arena[x+1][y]==' ':
            h = manhattanDistanceToGoal(x+1, y)
            frontier.append([x+1,y,g+1,g+1+h])
        if y-1>=0 and arena[x][y-1]==' ':
            h = manhattanDistanceToGoal(x, y-1)
            frontier.append([x,y-1,g+1,g+1+h])
        if y+1<sizeY and arena[x][y+1]==' ':
            h = manhattanDistanceToGoal(x, y+1)
            frontier.append([x,y+1,g+1,g+1+h])
        frontier.sort(key = lambda x:x[3], reverse = True)
        #h = math.fabs(x-goalx)+math.fabs(y-goaly)
        return search(frontier, bound, sizeX, sizeY)




parser = argparse.ArgumentParser(description='Robot Path Planning | HW 1 | COMS 4701')
parser.add_argument('-bfs', action="store_true", default=False , help="Run BFS on the map")
parser.add_argument('-dfs', action="store_true", default=False, help= "Run DFS on the map")
parser.add_argument('-astar', action="store_true", default=False, help="Run A* on the map")
parser.add_argument('-all', action="store_true", default=False, help="Run all the 3 algorithms")
parser.add_argument('-m', action="store", help="Map filename")

results = parser.parse_args()

if results.m=="" or not(results.all or results.astar or results.bfs or results.dfs):
    print "Check the parameters : >> python hw1_UNI.py -h"
    exit()

if results.all:
    results.bfs = results.dfs = results.astar = True

# Reading of map given and all other initializations
try:
    with open(results.m) as f:
        arena = f.read()
        arena = arena.split("\n")[:-1]
except:
    print "Error in reading the arena file."
    exit()
  
# Internal representation  
print arena

print "The arena of size "+ str(len(arena)) + "x" + str(len(arena[0]))
print "\n".join(arena)

if results.bfs:
    # Call / write your BFS algorithm
    print "BFS algorithm called"  # comment out later
    BFS(arena)
    
if results.dfs:
    # Call / write your DFS algorithm
    print "DFS algorithm called"  # comment out later
    DFS(arena)
    
if results.astar:
    # Call / write your A* algorithm
    print "A* algorithm called"  # comment out later
    Astar(arena)









