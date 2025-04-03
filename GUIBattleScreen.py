# New window created 4/4/25.
# Creating a battle layout. Frames to hold widgets to enable attack and heal plus simple hit animations.
# Show health and stats for the Player

import tkinter as tk

# Set initial positions of x and y coordinates + the spacing between instances of stickmen.
initial_x = 100
initial_y = 50
spacing = 100

def draw_stickman(canvas, x1, y1):
    # Constants for sizes of elements.
    HEAD_SIZE = 40
    BODY_LTH = 40
    ARM_SPAN = 60
    LEG_LTH = 50

    # Head
    head_tl = (x1, y1) # Start top left corner
    head_br = (x1 + HEAD_SIZE, y1 + HEAD_SIZE) # bottom right relative to top left.

    # Body
    body_start = x1 + HEAD_SIZE/2, y1 + HEAD_SIZE
    body_end = (x1 + HEAD_SIZE/2, y1 + HEAD_SIZE + BODY_LTH)



    # Arms
    # canvas.create_line(80, 120, 140, 120, fill="black", width=2)

    # Legs
    # canvas.create_line(110, 170, 80, 220, fill="black", width=2)
    # canvas.create_line(110, 170, 140, 220, fill="black", width=2)

    # Draw Head
    # Takes arguments from coordinates (stored and referenced as a list
    canvas.create_oval(head_tl[0], head_tl[1], head_br[0], head_br[1], outline="black", width=2)

    # Draw body
    canvas.create_line(body_start[0], body_start[1], body_end[0], body_end[1], fill="black", width=2)


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

# Frame Geometry
frm_left_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3, width=350, height=250)
frm_left_frame.grid(row=1, column=1, pady=10, padx=10)
frm_left_frame.grid_propagate(False)

frm_right_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3, width=350, height=250)
frm_right_frame.grid(row=1, column=2, padx=10, pady=10)
frm_right_frame.grid_propagate(False)

frm_bottom_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=3,width=720, height=50)
frm_bottom_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
frm_bottom_frame.grid_propagate(False)

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

draw_stickman(cv, initial_x, initial_y)
draw_stickman(cv, initial_x + spacing, initial_y)

# Bottom Frame widgets
lbl_health = tk.Label(master=frm_bottom_frame, bg="green", text="health")
lbl_health.grid(row=1, column=3, padx=10, pady=10)
window.mainloop()