import console
import time

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


class Cell:

    CHA_DED = "▫️"
    CHA_ALI = "◾️"

    def __init__(self, is_alive : bool) -> bool:
        self.is_alive = is_alive
        self.symbol = self.set_symbol()
    
    def set_symbol(self) {
        return CHA_ALI if self.is_alive else CHA_DED 
    }


def main():
    console.clear()
    a = InfiniteUniverse(20,20)

    while True:
        print(a)
        a.step()
        time.sleep(0.5)
        console.clear()

if __name__ == "__main__":
    main()