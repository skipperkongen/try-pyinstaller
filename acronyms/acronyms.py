import random
from tkinter import *

import requests


def main():

    root = Tk()
    resp = requests.get('http://textfiles.com/humor/acronym.txt')
    acronyms = resp.text.splitlines()[5:]
    label_text = random.choice(resp.text.splitlines()[5:])
    a = Label(root, text = label_text)
    a.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
