from Tkinter import Tk, Frame, Canvas, ALL, NW

WIDTH = 300
HEIGHT = 300

class Board(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, width = WIDTH, height = HEIGHT, background = "black", highlightthickness = 0)
        self.parent = parent
        self.pack()

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Nibbles")
        self.board = Board(parent)
        self.pack()

def main():
    root= Tk()
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()
