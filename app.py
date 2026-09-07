import matplotlib.pyplot as plt
#phase 1 
import random
def particle_movement():
    zero = 0 
    right = zero + 1
    left = zero - 1
    moves = [zero, left, right]
    random_move = random.choice(moves)
    return(random_move)

print(particle_movement())

#phase 2
def repeat_movement():
    for step in range(5):
       position = 0 
       right = position + 1
       left = position - 1
       moves = [position, left, right]
       random_move = random.choice(moves)
       print(random_move,step)

repeat_movement()

#phase 3 
def store_moves():
    store =[]
    for step in range (5):
        position = 0 
        right = position + 1
        left = position - 1
        moves = [position, left, right]
        random_move = random.choice(moves)
        store.append (random_move)
        print(store,step)  

store_moves()

#phase 4
def walk():
         walk_store =[0]
         current_new = 0
         for step in range(100):
            position = 0 
            right = position + 1
            left = position - 1
            moves = [position, left, right]
            random_move = random.choice(moves)
            new_position = current_new + random_move
            walk_store.append(new_position)
            #print("step =",step,"length =",len(walk_store))
            current_new = walk_store[-1]
            print(walk_store)


walk()


 
#phase 5

#plt.plot(path)
#plt.title("random walk")
#plt.xlabel("step number")
#plt.ylabel("position")
#plt.grid(True)
#plt.show()