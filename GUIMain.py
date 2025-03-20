# GUIMain - a GUI window to start the RPG
import tkinter as tk

# Create window
window = tk.Tk()

window.geometry("600x400")
window.title("ModRPG")

banner = tk.Label(
    text="MODRPG",
    foreground="blue",
    background="yellow",
    width= 600,
    height=2
)

btn_choice = tk.Button(
    text="Create Character",
    width=300,
    height=10,
    fg="yellow",
    bg="blue"
)
banner.pack()
btn_choice.pack()
# Keep window open (Pycharm)
window.mainloop()