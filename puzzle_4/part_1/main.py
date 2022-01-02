import os
import numpy as np

class Puzzle:
    """ """
    def __init__(self, filepath):
        self.filepath = filepath
        self.filecontent = None
        self.calls = []
        self.boards = None

        # set all the inputs
        self.__openFile()
        self.__setCalls()
        self.__setBoards()

    def __openFile(self):
        """ """
        with open(self.filepath, "r") as f:
            self.filecontent = f.read()
    
    def __setCalls(self):
        """ get first line from file content and set as the calls """
        callsAsStr = self.getFileContent().split("\n")[0]
        self.calls = [int(i) for i in callsAsStr.split(",")]
    
    def __setBoards(self):
        """ set all the boards from filecontent """
        allRawBoards = np.fromstring(" ".join(self.getFileContent().split("\n")[1:]), int, sep=" ")
        self.boards = allRawBoards.reshape(25, len(allRawBoards)//25)

    def getCalls(self):
        """ return the list of calls """
        return self.calls

    def getBoards(self):
        """ """
        return self.boards

    def getFileContent(self):
        """ """
        return self.filecontent

def main():
    p = Puzzle(
        filepath=os.path.join(".", "input.txt")
    )
    print(p.getBoards())

if __name__ == "__main__":
    main()