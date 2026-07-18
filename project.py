import tkinter as tk
import pygame
import sys

tk_window = None
PresetName = ''
pygame.init()
pygame.font.init()  # required for pygame-ce

screen = pygame.display.set_mode((1200, 600))  # MUST come before SysFont
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 20)  # now safe
MENU_HEIGHT = 30
menu_items = [
    {"name": "File", "submenu": ["Close", "Load Preset...", "Create Simulation"]},
    {"name": "Options", "submenu": ["Toggle Trails"]},
]

active_menu = None
show_trails = False


# Colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
LIME    = (50, 205, 50)
ORANGE  = (255, 165, 0)
PURPLE  = (128, 0, 128)
NAVY    = (0, 0, 128)
MAROON  = (128, 0, 0)
TEAL    = (0, 128, 128)
GOLD    = (255, 215, 0)
PINK    = (255, 192, 203)
SKY_BLUE = (135, 206, 235)
VIOLET  = (238, 130, 238)

dbg = "[DEBUG / INFO] ->   "


# SETTINGS

# Add this near your other color definitions
SILVER = (192, 192, 192)

PRESETS = {
    "Preset A": {
        "Game_slowdown_percent": 0,
        "Obj_1_col": PINK,        # Changed from "PINK"
        "Obj_1_radius": 10,
        "Obj_1_weight": .00000000008,
        "Obj_1_coords": [-150.0, 100.0],
        "Velocity1": [.5, .9],

        "Obj_2_col": TEAL,        # Changed from "TEAL"
        "Obj_2_radius": 30,
        "Obj_2_weight": 1000000,
        "Obj_2_coords": [150.0, -50.0],
        "Velocity2": [0.0, 0.0]
    },

    "Preset B": {
        "Game_slowdown_percent": 20,
        "Obj_1_col": BLUE,        # Changed from "BLUE"
        "Obj_1_radius": 10,
        "Obj_1_weight": 50000,
        "Obj_1_coords": [-150.0, 0.0],
        "Velocity1": [0, .5],

        "Obj_2_col": RED,         # Changed from "RED"
        "Obj_2_radius": 30,
        "Obj_2_weight": 200000,
        "Obj_2_coords": [150.0, 0.0],
        "Velocity2": [0.0, -.125]
    },

    "Preset C": {
        "Game_slowdown_percent": 40,
        "Obj_1_col": LIME,        # Changed from "LIME"
        "Obj_1_radius": 3,
        "Obj_1_weight": .0000008,
        "Obj_1_coords": [150.0, -200.0],
        "Velocity1": [-1.3, 0],

        "Obj_2_col": GOLD,        # Changed from "GOLD"
        "Obj_2_radius": 70,
        "Obj_2_weight": 1000000,
        "Obj_2_coords": [0.0, 100.0],
        "Velocity2": [0.0, 0.0]
    },

    "Preset D": {
        "Game_slowdown_percent": 0,
        "Obj_1_col": SILVER,      # Changed from "SILVER"
        "Obj_1_radius": 10,
        "Obj_1_weight": 10000,
        "Obj_1_coords": [-270.0, 0.0],
        "Velocity1": [0, 0],

        "Obj_2_col": CYAN,        # Changed from "CYAN"
        "Obj_2_radius": 10,
        "Obj_2_weight": 10000,
        "Obj_2_coords": [270.0, 0.0],
        "Velocity2": [0.0, 0.0]
    },

    "Preset E": {
        "Game_slowdown_percent": 0,
        "Obj_1_col": SILVER,      # Changed from "SILVER"
        "Obj_1_radius": 3,
        "Obj_1_weight": 20000,
        "Obj_1_coords": [-270.0, 50.0],
        "Velocity1": [.1, .02],

        "Obj_2_col": CYAN,        # Changed from "CYAN"
        "Obj_2_radius": 3,
        "Obj_2_weight": 20000,
        "Obj_2_coords": [270.0, -50.0],
        "Velocity2": [-.1, -.02]
    },

    "Preset F": {
        "Game_slowdown_percent": 0,
        "Obj_1_col": LIME,        # Changed from "LIME"
        "Obj_1_radius": 5,
        "Obj_1_weight": .00000000001,
        "Obj_1_coords": [-180, 0],
        "Velocity1": [0, 1.05],

        "Obj_2_col": GOLD,        # Changed from "GOLD"
        "Obj_2_radius": 35,
        "Obj_2_weight": 200000,
        "Obj_2_coords": [0.0, 0.0],
        "Velocity2": [0.0, 0.0]
    }
}

def ApplyPreset(name):
    global Game_slowdown_percent
    global Obj_1_col, Obj_1_radius, Obj_1_weight, Obj_1_coords, Velocity1
    global Obj_2_col, Obj_2_radius, Obj_2_weight, Obj_2_coords, Velocity2

    preset = PRESETS[name]

    Game_slowdown_percent = preset["Game_slowdown_percent"]

    Obj_1_col = preset["Obj_1_col"]
    Obj_1_radius = preset["Obj_1_radius"]
    Obj_1_weight = preset["Obj_1_weight"]
    Obj_1_coords = preset["Obj_1_coords"].copy()
    Velocity1 = preset["Velocity1"].copy()

    Obj_2_col = preset["Obj_2_col"]
    Obj_2_radius = preset["Obj_2_radius"]
    Obj_2_weight = preset["Obj_2_weight"]
    Obj_2_coords = preset["Obj_2_coords"].copy()
    Velocity2 = preset["Velocity2"].copy()

    

Game_slowdown_percent = 0    # 0 to 100

# OBJECT 1 (Blue Planet)
Obj_1_col = PINK
Obj_1_radius = 10
Obj_1_weight = .00000000008           
Obj_1_coords = [-150.0, 100.0] # Use floats
Velocity1 = [.5, .9]    ## regs, op 

# OBJECT 2 (Red Star)
Obj_2_col = TEAL
Obj_2_radius = 30
Obj_2_weight = 1000000          
Obj_2_coords = [150.0, -50.0]     
Velocity2 = [0.0, 0.0]  

##### SETTINGS DONE 

Force_Scale = 0.0000001
FORCE_MODIFIER = 1000


def QuitGameCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
def set_tk_none():
    global tk_window;
    tk_window = None;
def NewPopupLoadPreset():
    global tk_window, PresetName

    # If window already open, don't open another
    if tk_window is not None:
        return

    tk_window = tk.Tk()
    tk_window.title("Preset Loader")
    tk_window.geometry("600x600")
    tk_window.configure(bg="#1e1e1e")  # dark background

    # Title
    title = tk.Label(
        tk_window,
        text="PRESET LOADER",
        font=("Consolas", 28, "bold"),
        fg="white",
        bg="#1e1e1e"
    )
    title.pack(pady=20)

    # Description
    desc_text = (
        "This menu allows you to choose from a predetermined list\n"
        "to change the look, behaviour and configuration of the\n"
        "two objects / planets in empty space."
    )

    desc = tk.Label(
        tk_window,
        text=desc_text,
        font=("Consolas", 12),
        fg="white",
        bg="#1e1e1e",
        justify="center"
    )
    desc.pack(pady=10)

    # Button frame
    frame = tk.Frame(tk_window, bg="#1e1e1e")
    frame.pack(pady=20)

    # Create 6 preset buttons
    presets = ["Preset A", "Preset B", "Preset C", "Preset D", "Preset E", "Preset F"]

    def preset_clicked(name):
        global PresetName
        
        PresetName = name
        ApplyPreset(name)

    for i, name in enumerate(presets):
        btn = tk.Button(
            frame,
            text=name,
            width=12,
            height=6,
            bg="#2d2d2d",
            fg="white",
            font=("Consolas", 12, "bold"),
            command=lambda n=name: preset_clicked(n)
        )
        btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    # Close button
    close_btn = tk.Button(
        tk_window,
        text="Close",
        width=20,
        bg="#444",
        fg="white",
        font=("Consolas", 12),
        command=lambda: (tk_window.destroy(), set_tk_none())
    )
    close_btn.pack(pady=0)
def get_color_name(color_tuple):
    # Dictionary mapping RGB tuples back to their string names
    COLOR_MAP = {
        WHITE: "WHITE", BLACK: "BLACK", RED: "RED", GREEN: "GREEN",
        BLUE: "BLUE", YELLOW: "YELLOW", CYAN: "CYAN", MAGENTA: "MAGENTA",
        LIME: "LIME", ORANGE: "ORANGE", PURPLE: "PURPLE", NAVY: "NAVY",
        MAROON: "MAROON", TEAL: "TEAL", GOLD: "GOLD", PINK: "PINK",
        SKY_BLUE: "SKY_BLUE", VIOLET: "VIOLET", SILVER: "SILVER"
    }
    
    # Return the color string if it matches, otherwise fallback to "WHITE"
    return COLOR_MAP.get(color_tuple, "WHITE")
def NewPopupCreateSimulation():
    global tk_window

    if tk_window is not None:
        return

    tk_window = tk.Tk()
    tk_window.title("Create Simulation")
    tk_window.geometry("600x650")
    tk_window.configure(bg="#1e1e1e")

    # --- SCROLLABLE CANVAS SETUP ---
    canvas = tk.Canvas(tk_window, bg="#1e1e1e", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(tk_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame INSIDE canvas
    inner_frame = tk.Frame(canvas, bg="#1e1e1e")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Update scroll region when widgets change size
    def update_scroll_region(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scroll_region)

    # Mouse wheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # --- CONTENT STARTS HERE ---

    title = tk.Label(
        inner_frame,
        text="CREATE SIMULATION",
        font=("Consolas", 28, "bold"),
        fg="white",
        bg="#1e1e1e"
    )
    title.pack(pady=20)

    desc = tk.Label(
        inner_frame,
        text="Enter custom parameters for both objects.\nValues will be applied instantly.",
        font=("Consolas", 12),
        fg="white",
        bg="#1e1e1e"
    )
    desc.pack(pady=10)

    # Helper to create labeled entry fields
    def make_field(label_text, default):
        lbl = tk.Label(inner_frame, text=label_text, fg="white", bg="#1e1e1e", font=("Consolas", 12))
        lbl.pack()
        entry = tk.Entry(inner_frame, width=30, font=("Consolas", 12))
        entry.insert(0, str(default))
        entry.pack(pady=5)
        return entry

    # Object 1 fields
    e1_color   = make_field("Object 1 Color:", get_color_name(Obj_1_col))
    e1_radius  = make_field("Object 1 Radius:", Obj_1_radius)
    e1_weight  = make_field("Object 1 Weight:", Obj_1_weight)
    e1_x       = make_field("Object 1 X Coord:", Obj_1_coords[0])
    e1_y       = make_field("Object 1 Y Coord:", Obj_1_coords[1])
    e1_vx      = make_field("Object 1 Velocity X:", Velocity1[0])
    e1_vy      = make_field("Object 1 Velocity Y:", Velocity1[1])

    # Object 2 fields
    e2_color   = make_field("Object 2 Color:", get_color_name(Obj_2_col))
    e2_radius  = make_field("Object 2 Radius:", Obj_2_radius)
    e2_weight  = make_field("Object 2 Weight:", Obj_2_weight)
    e2_x       = make_field("Object 2 X Coord:", Obj_2_coords[0])
    e2_y       = make_field("Object 2 Y Coord:", Obj_2_coords[1])
    e2_vx      = make_field("Object 2 Velocity X:", Velocity2[0])
    e2_vy      = make_field("Object 2 Velocity Y:", Velocity2[1])

    # Apply button
    # Inside NewPopupCreateSimulation -> apply_sim()
    def apply_sim():
        global Obj_1_col, Obj_1_radius, Obj_1_weight, Obj_1_coords, Velocity1
        global Obj_2_col, Obj_2_radius, Obj_2_weight, Obj_2_coords, Velocity2

        # Use eval to convert user text input (like "PINK") into the variable PINK
        try:
            Obj_1_col = eval(e1_color.get().upper())
            Obj_2_col = eval(e2_color.get().upper())
        except:
            # Fallback default colors if user types something invalid
            Obj_1_col = PINK
            Obj_2_col = TEAL

        Obj_1_radius = int(e1_radius.get())
        Obj_1_weight = float(e1_weight.get())
        Obj_1_coords = [float(e1_x.get()), float(e1_y.get())]
        Velocity1 = [float(e1_vx.get()), float(e1_vy.get())]

        Obj_2_radius = int(e2_radius.get())
        Obj_2_weight = float(e2_weight.get())
        Obj_2_coords = [float(e2_x.get()), float(e2_y.get())]
        Velocity2 = [float(e2_vx.get()), float(e2_vy.get())]

    apply_btn = tk.Button(
        inner_frame,
        text="Apply Simulation",
        width=20,
        bg="#444",
        fg="white",
        font=("Consolas", 12),
        command=apply_sim
    )
    apply_btn.pack(pady=20)

    close_btn = tk.Button(
        inner_frame,
        text="Close",
        width=20,
        bg="#444",
        fg="white",
        font=("Consolas", 12),
        command=lambda: (tk_window.destroy(), set_tk_none())
    )
    close_btn.pack(pady=10)

def draw_menu():
    pygame.draw.rect(screen, (40, 40, 40), (0, 0, 1200, MENU_HEIGHT))

    x = 10
    for item in menu_items:
        text = FONT.render(item["name"], True, WHITE)
        screen.blit(text, (x, 5))
        item["rect"] = pygame.Rect(x, 0, text.get_width()+20, MENU_HEIGHT)
        x += text.get_width() + 40

    # Draw dropdown
    if active_menu is not None:
        submenu = active_menu["submenu"]
        active_menu["submenu_rects"] = []

        for i, name in enumerate(submenu):
            rect = pygame.Rect(active_menu["rect"].x, MENU_HEIGHT + i*30, 200, 30)
            active_menu["submenu_rects"].append(rect)

            pygame.draw.rect(screen, (60, 60, 60), rect)
            t = FONT.render(name, True, WHITE)
            screen.blit(t, (rect.x + 10, rect.y + 5))
def handle_menu_click(pos):
    global active_menu, show_trails

    # Click on top menu
    for item in menu_items:
        if item["rect"].collidepoint(pos):
            active_menu = item
            return

    # Click on submenu
    if active_menu and "submenu_rects" in active_menu:
        for i, rect in enumerate(active_menu["submenu_rects"]):
            if rect.collidepoint(pos):
                choice = active_menu["submenu"][i]

                if choice == "Close":
                    pygame.quit()
                    sys.exit()

                elif choice == "Load Preset...":
                    print("Load preset clicked")
                    NewPopupLoadPreset();

                elif choice == "Create Simulation":
                    print("Create simulation clicked")
                    NewPopupCreateSimulation() 
                    

                elif choice == "Toggle Trails":
                    show_trails = not show_trails
                    print("Trails:", show_trails)

                    

                active_menu = None
                return

    # Click outside closes dropdown
    active_menu = None

def Update_coords_and_vel():
    global Obj_1_coords, Velocity1, Obj_2_coords, Velocity2, FORCE_MODIFIER

    dx = Obj_2_coords[0] - Obj_1_coords[0]
    dy = Obj_2_coords[1] - Obj_1_coords[1]
    dist = (dx**2 + dy**2)**0.5
    if dist < 1: dist = 1

    force_mag = FORCE_MODIFIER * (Obj_1_weight * Obj_2_weight / dist**2)
    velocity_pull = (Velocity1[0]**2 + Velocity1[1]**2)**0.5 * (Obj_1_weight * Obj_2_weight / dist**3)

    total_force = (force_mag + velocity_pull) * Force_Scale

    force_x = total_force * (dx / dist)
    force_y = total_force * (dy / dist)

    Velocity1[0] += force_x / (Obj_1_weight * 0.1)
    Velocity1[1] += force_y / (Obj_1_weight * 0.1)

    Velocity2[0] -= force_x / (Obj_2_weight * 0.1)
    Velocity2[1] -= force_y / (Obj_2_weight * 0.1)

    Obj_1_coords[0] += Velocity1[0]
    Obj_1_coords[1] += Velocity1[1]

    Obj_2_coords[0] += Velocity2[0]
    Obj_2_coords[1] += Velocity2[1]


def main():
    global tk_window
    # MAIN LOOP
    trail_points = []
    while True:
        if tk_window is not None:
            try:
                tk_window.update()
            except:
                tk_window = None
        screen.fill(BLACK)
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(event.pos)

        
        

        Update_coords_and_vel()

        # Convert simulation coords to screen coords
        pos1 = (int(Obj_1_coords[0] + 600), int(300 - Obj_1_coords[1]))
        pos2 = (int(Obj_2_coords[0] + 600), int(300 - Obj_2_coords[1]))

        # Draw objects normally
        pygame.draw.circle(screen, Obj_1_col, pos1, Obj_1_radius)
        pygame.draw.circle(screen, Obj_2_col, pos2, Obj_2_radius)

        if show_trails:
            # Add current position to trail
            trail_points.append(pos1)

            # Limit trail length
            if len(trail_points) > 200:
                trail_points.pop(0)

            # Draw flame trail
            for i, p in enumerate(trail_points):
                # Fade effect: older points get smaller + darker
                age = i / len(trail_points)

                # Flame color gradient (yellow -> orange -> red)
                r = int(255 * age)
                g = int(150 * (1 - age))
                b = 0
                flame_color = (r, g, b)

                # Flame size (bigger near the object)
                size = int(6 * (1 - age)) + 1

                pygame.draw.circle(screen, flame_color, p, size)


        # FPS display
        fps = int(clock.get_fps())
        pygame.display.set_caption(f"2D Orbital Gravity Simulation | FPS: {fps}")
        
        pygame.display.flip()
        QuitGameCheck()
        clock.tick(120 - Game_slowdown_percent)

if __name__ == "__main__":
    main();
