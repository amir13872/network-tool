import tkinter as tk
from gui.interface import NetworkToolGUI

def main():
    root = tk.Tk()
    root.title("Network Tool")
    app = NetworkToolGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()