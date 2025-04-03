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
# Some colouring of widgets does not work on MacOs as the OS overrides the tkinter properties.
# Work around can be to use labels rather than buttons, this adds complexity due to having to bind commands
btn_choice = tk.Button(
    text="Create Character",
    fg="yellow",
    highlightbackground="blue"
)
btn_choice.config(width=20, height=2)
banner.pack()
btn_choice.pack()
# Keep window open
window.mainloop()