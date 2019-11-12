#!/usr/bin/env python3
from tkinter import Tk
from screen import Screen
from state import CraneState

def main():
    
    root = Tk()
    state = CraneState()
    app = Screen(state)
    root.mainloop()


if __name__ == '__main__':
    main()
