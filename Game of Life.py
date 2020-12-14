import console
import time

CHA_DED = "▫️"
CHA_ALI = "◾️"
class InfiniteUniverse:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        print((self.height,self.width))
        self.state = []
        for y in range(self.height):
            self.state.append(list(self.width*CHA_ALI))
        
    def __str__(self):
        output = ""
        for y in self.state:
            output += "".join(y) + "\n"
        return output
    
    def make_alive(self, position):
        self.state[position[1]][position[0]] = CHA_ALI
    
    def create_empty_board(self):
        new_board = []
        for y in range(self.height):
            new_board.append(list(self.width*CHA_DED))
        return new_board
            
    def check_neighbours(self,position):
        characters = []
        for y in range(position[1]-1,position[1]+2):
            for x in range(position[0]-1,position[0]+2):
                if y in range(self.height) and x in range(self.width):
                    characters.append(self.state[y][x])
                
        cha_at_pos = self.state[position[1]][position[0]]
        for i in range(len(characters)):
            if characters[i] == cha_at_pos:
                characters.pop(i)
                break
        dead = 0
        alive = 0
        for cell in characters:
            if cell == CHA_DED:
                dead += 1
            if cell == CHA_ALI:
                alive += 1 
        return (alive,dead)
        
    def is_alive(self,position):
        out = self.state[position[1]][position[0]]== CHA_ALI
        return out
        
    
    def step(self):
        next_frame = self.create_empty_board()
        for y in range(self.height):
            for x in range(self.width):
                alive = self.is_alive((x,y))
                neighbours = self.check_neighbours((x,y))
                
                if alive and neighbours[0] in {3,2}:
                    next_frame[y][x] = CHA_ALI
                elif not alive and neighbours[0] == 3:
                    next_frame[y][x] = CHA_ALI
                else:
                    next_frame[y][x] = CHA_DED
        self.state = next_frame
        
                    
                
                
        
    
        
        
         



a = InfiniteUniverse(20,20)
#a.make_alive((0+5,0+5))
#a.make_alive((2+5,0+5))
#a.make_alive((1+5,1+5))
#a.make_alive((2+5,1+5))
#a.make_alive((1+5,2+5))

#a.make_alive((1,1))
#a.make_alive((2,2))
#a.make_alive((1,2))
#a.make_alive((2,1))
'''
a.make_alive((6,5))
a.make_alive((6,6))
a.make_alive((6,8))
a.make_alive((6,9))
a.make_alive((6,10))
a.make_alive((6,11))
a.make_alive((6,13))
a.make_alive((6,14))
a.make_alive((5,12))
a.make_alive((7,12))
a.make_alive((5,7))
a.make_alive((7,7))

'''
console.clear()
while 1==1:

    
    print(a)
    a.step()
    time.sleep(0.5)
    console.clear()
    
 


