# New window created 4/4/25.
# Creating a battle layout. Frames to hold widgets to enable attack and heal plus simple hit animations.
# Show health and stats for the Player

import tkinter as tk

# functions
def attack():
    return

def heal():
    return

# Create window
window = tk.Tk()

window.geometry("750x500")
window.title("Battle")
window.resizable(False, False)

frm_left_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3, width=350, height=250)
frm_left_frame.grid(row=1, column=1, pady=10, padx=10)
frm_left_frame.grid_propagate(False)

frm_right_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3, width=350, height=250)
frm_right_frame.grid(row=1, column=2, padx=10, pady=10)
frm_right_frame.grid_propagate(False)

frm_bottom_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_bottom_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Left Frame widgets
lbl_actions = tk.Label(
    master=frm_left_frame,
    text="Player Actions",
    borderwidth=2,
    bg="white"
)
btn_attack = tk.Button(frm_left_frame, text="Attack", command=attack)
btn_heal = tk.Button(frm_left_frame, text="Heal", command=heal)

lbl_actions.grid(row=1, column=1, padx=10,pady=10, sticky="nsew")
btn_attack.grid(row=3, column=1, sticky='w'+'e'+'n'+'s')
btn_heal.grid(row=4, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

# Right Frame widgets
cv = tk.Canvas(master=frm_right_frame, bg="lightblue", width=325, height=225)
cv.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)



window.mainloop()