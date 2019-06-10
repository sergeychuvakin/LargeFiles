class LargeFiles:
    '''
    Special class for changing big files. Note that, while make you make a changes,
    you should insert string in bytes. Par example, using changeThisLine, you should add b sign, near new string.
    like this: changeThisLine(b'my_new_line').
     
    Don't forget to close files with saveChanges()
 
    Now You do need initialize makeMM() - it will automatically 
    '''
    def __init__(self, filepath):
        self.mmap = __import__('mmap')
        self.file = filepath
        self.C = ()
        self.mm = None
        self.s = None
        self.stroka = None
        self.makeMM()
         
    def makeMM(self):
        with open(self.file, 'r+') as f:
            self.mm = self.mmap.mmap(f.fileno(), 0)
        return self.mm
     
    def nextLine(self):
        self.s = self.mm.readline()
        return self.s
     
    def lineCoor(self):
        self.C = [self.mm.tell() - len(self.s), self.mm.tell()]
        return self.C
     
    def lenthLine(self):
        return len(self.s)
     
    def changeThisLine(self, disString):
        '''
        Note that disString (from Disired String) should the same lenth as line you want to change.
        You can check the lenth by executing lenthLine().
        Besides, disString should be in bytes 
        '''
        self.C = self.lineCoor()
        self.mm[self.C[0]:self.C[1]] = disString
         
    def whereIam(self):
        return self.mm.tell()
     
    def writeHere(self, disS):
        '''
        disS should be in bytes
        '''
        self.mm.write(disS)
         
    def changeMyLocation(self, chislo):
        self.mm.seek(chislo)
     
    def showLine(self, start, end):
        print('This line has lenth:', len(self.mm[start: end+1]))
        return self.mm[start: end+1]
     
    def saveChanges(self):
        self.mm.close()
     
    def findFirst(self, stroka):
        '''
        stroka should be in bytes
        '''
        return self.mm.find(stroka)
     
    def findLast(self, stroka):
        '''
        stroka should be in bytes
        '''
        return self.mm.rfind(stroka)
     
    def findNext(self, stroka):
        '''
        Remember: while you, finding smth by findNext, you permanently changing your location.
        '''
        self.stroka = stroka
        print(self.findFirst(self.stroka))
        self.changeMyLocation(self.findFirst(self.stroka)+1)
     
    def changeLine(self, start, end, stroka):
        '''
        stroka should be in bytes
        '''
        self.mm[start: end+1] = stroka
