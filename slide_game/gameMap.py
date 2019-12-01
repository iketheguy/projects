class gameMap:

    
    def __init__(self, myfile):
        self.mymap = []
        self.pos = [0,0]
        with open(myfile,'r') as infile:
            for i,line in enumerate(infile.readlines()):
                mapline = []
                for j,char in enumerate(line.strip()):
                    if char == "P":
                        self.pos = [i,j]
                    mapline.append(char)
                self.mymap.append(mapline)

    def __str__(self):
        mystr = ""
        for line in self.mymap:
            mystr += ''.join(line) + '\n'
        return mystr

    def move(self, direc):  #can be U, D, L, R
        if direc == 'U':  # moving in -i dir
            nextspace = self.mymap[self.pos[0] - 1][self.pos[1]] 
            while nextspace != "X":
                self.mymap[self.pos[0]][self.pos[1]] = "V"
                self.pos[0] -= 1
                self.mymap[self.pos[0]][self.pos[1]] = "P"
                nextspace = self.mymap[self.pos[0] - 1][self.pos[1]]
        elif direc == 'D':  # moving in +i dir
            nextspace = self.mymap[self.pos[0] + 1][self.pos[1]]
            while nextspace != "X":
                self.mymap[self.pos[0]][self.pos[1]] = "V"
                self.pos[0] += 1
                self.mymap[self.pos[0]][self.pos[1]] = "P"
                nextspace = self.mymap[self.pos[0] + 1][self.pos[1]]
        elif direc == 'L':  # moving in -j dir
            nextspace = self.mymap[self.pos[0]][self.pos[1] - 1]
            while nextspace != "X":
                self.mymap[self.pos[0]][self.pos[1]] = "V"
                self.pos[1] -= 1
                self.mymap[self.pos[0]][self.pos[1]] = "P"
                nextspace = self.mymap[self.pos[0]][self.pos[1] - 1]
        elif direc == 'R':  # moving in +j dir
            nextspace = self.mymap[self.pos[0]][self.pos[1] + 1] 
            while nextspace != "X":
                self.mymap[self.pos[0]][self.pos[1]] = "V"
                self.pos[1] += 1
                self.mymap[self.pos[0]][self.pos[1]] = "P"
                nextspace = self.mymap[self.pos[0]][self.pos[1] + 1]
        else:
            print("Enter a valid key. (U,D,L,R)")
    
    def victory(self):
        vic = True
        for line in self.mymap:
            for char in line:
                if char == "O":
                    vic = False
        return vic
