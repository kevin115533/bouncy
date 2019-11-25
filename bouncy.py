from tkinter import *

class Bouncy(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bouncy")
        self.grid()
        # initial height
        self._initialHeightLabel = Label(self, text = "Initial Height")
        self._initialHeightLabel.grid(row = 0, column = 0)
        self._initialHeightVar = DoubleVar()
        self._initialHeightEntry = Entry(self, textvariable = self._initialHeightVar)
        self._initialHeightEntry.grid(row = 0, column = 1)
        # bounciness index
        self._bouncinessIndexLabel = Label(self, text = "Bounciness Index")
        self._bouncinessIndexLabel.grid(row = 1, column = 0)
        self._bouncinessIndexVar = DoubleVar()
        self._bouncinessIndexEntry = Entry(self, textvariable = self._bouncinessIndexVar)
        self._bouncinessIndexEntry.grid(row = 1, column = 1)
        # number of bounce
        self._numberOfBounceLabel = Label(self, text = "Number of bounces")
        self._numberOfBounceLabel.grid(row = 2, column = 0)
        self._numberOfBounceVar = DoubleVar()
        self._numberOfBounceEntry = Entry(self, textvariable = self._numberOfBounceVar)
        self._numberOfBounceEntry.grid(row = 2, column = 1)
        #button
        self._button = Button(self, text = "Compute", command = self._distance)
        self._button.grid(row = 3, column = 0, columnspan = 2)
        # total distance
        self._totalDistanceLabel = Label(self, text = "Total distance")
        self._totalDistanceLabel.grid(row = 4, column = 0)
        self._totalDistanceVar = DoubleVar()
        self._totalDistanceEntry = Entry(self, textvariable = self._totalDistanceVar)
        self._totalDistanceEntry.grid(row = 4, column = 1)

    def _distance(self):
        initialHeight = self._initialHeightVar.get()
        bounciness = self._bouncinessIndexVar.get()
        bounces = self._numberOfBounceVar.get()
        totalDistance = (initialHeight ** bounciness) * bounces
        self._totalDistanceVar.set(totalDistance)

def main():
    Bouncy().mainloop()

main()