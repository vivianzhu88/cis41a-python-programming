#Vivian Zhu
#Exercise 4

class Person():
    def __init__(self, line):
        s = line.rstrip()
        ss = s.split(",")
        self.first = ss[0]
        self.last = ss[1]
        self.room = ss[2]
    def __str__(self):
        return self.last + ", " + self.first
    def __lt__(self, rhs):
        return self.last + self.first < rhs.last + rhs.first
    def __eq__(self, rhs):
        return self.last + self.first == rhs.last + rhs.first
    def getRoom(self):
        return self.room

class Hotel():
    def __init__(self, filename):
        self.filename = filename
        self.directory = []
 
    def read(self):
        handle = open(self.filename)

        '''
        for line in handle:
            person = Person(line)
            self.directory.append(person)
        '''
        self.directory = [Person(line) for line in handle]

    def printRoomOrder(self):
        print("HOTEL IN ROOM ORDER")
        print("___________________")
        
        '''
        for i in range (1, len(self.directory)+1):
            for j in self.directory:
                if j.getRoom() == i:
                    print(j,  ":", "Room", i)
        '''
        [[print(j,  ":", "Room", i) for j in self.directory if str(i) == j.getRoom()] for i in range (1, len(self.directory)+1)]

    def getRoomGivenName(self, name):
        n = name.split()
        newName = n[1] + ", " + n[0]

        '''
        for i in self.directory:
            if i.__str__() == newName:
                return i.getRoom()
        '''
        return [i.getRoom() for i in self.directory if i.__str__() == newName]
                
    def printNameOrder(self):
        self.directory.sort()
            
        print("HOTEL IN NAME ORDER")
        print("___________________")
        
        '''
        for i in self.directory:
            print(i,  ":", "Room", i.getRoom())
        '''
        [print(i,  ":", "Room", i.getRoom()) for i in self.directory]

    def search(self, name):
        room = self.getRoomGivenName(name)
        print(name, "is in Room", room[0])
        
h = Hotel("Hotel.csv")
h.read()
h.printRoomOrder()
print()
h.printNameOrder()
print()
h.search("Vivian Zhu")
    
