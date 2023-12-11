import pygetwindow as gw
import pyautogui
import keyboard

def on_hotkey():
    active_window = gw.getActiveWindow()
    if active_window:
        x, y = pyautogui.position()
        rel_x = x - active_window.left
        rel_y = y - active_window.top
        print(f"Mouse Position within '{active_window.title}': X: {rel_x}, Y: {rel_y}")
    else:
        print("No active window found.")

hotkey_combination = "alt+1" # Set your grab X and Y keybind here
keyboard.add_hotkey(hotkey_combination, on_hotkey)

print(f"Press {hotkey_combination} to grab mouse position within the active window.")

keyboard.wait("alt+2")  # Set your grab close application keybind here
