import matplotlib.pyplot as plt
#phase 1 
import random
def particle_movement():
    zero = 0 
    right = zero + 1
    left = zero - 1
    #possible moves: left, right, or stay at current position.
    moves = [zero, left, right]
    #simply to moves = [-1,0,1] in phases 2-4 indicate this by *
    #randomly choose a move from the given moves.
    random_move = random.choice(moves)
    return(random_move)

print(particle_movement())

#phase 2
def repeat_movement():
    for step in range(5):
       #possible moves: left, right, or stay at current position.
       #*
       moves = [-1,0,1]
       #randomly choose a move from the given moves.
       random_move = random.choice(moves)
       print(random_move,step)

repeat_movement()

#phase 3 
def store_moves():
    store =[]
    for step in range (5):
        #possible moves: left, right, or stay at current position. 
        #*
        moves = [-1,0,1]
        #randomly choose a move from the given moves.
        random_move = random.choice(moves)
        store.append (random_move)
        print(store,step)  

store_moves()

#phase 4
def walk():
         #starts the particle trajectory at the orgin.
         walk_store =[0]
         current_position = 0
         for step in range(100):
            #possible moves: left, right, or stay at current position.
            #* 
            moves = [-1,0,1]
            #randomly choose a move from the given moves.
            random_move = random.choice(moves)
            #calculate particle's next position.
            new_position = current_position + random_move
            #record particle's new position in particle's path.
            walk_store.append(new_position)
            #print("step =",step,"length =",len(walk_store))
            #update current position for the next step
            current_position = walk_store[-1]
            print(walk_store)


walk()


 
#phase 5

#plt.plot(path)
#plt.title("random walk")
#plt.xlabel("step number")
#plt.ylabel("position")
#plt.grid(True)
#plt.show()