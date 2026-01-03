import pyautogui
import keyboard
import time
import random

def run_reaction_bot():
    print("--- Reaction Speed Bot ---")
    print("1. Hover your mouse over the reaction area.")
    print("2. Press '\\' to arm the bot.")
    print("3. The bot will click automatically when the color changes.")
    print("4. Press 'Ctrl + C' in this terminal to quit completely.")
    print("--------------------------")

    while True:
        # Wait until the user presses '\' to start this round
        keyboard.wait('\\')
        
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Get the "starting" color (Red) to compare against
        # We assume the user presses '\' while the screen is currently Red (waiting)
        start_color = pyautogui.pixel(x, y)
        print(f"Bot armed! Watching pixel at {x}, {y} with color {start_color}...")

        # Loop to check for color change
        while True:
            # Check the current color at the mouse position
            current_color = pyautogui.pixel(x, y)

            # Detect if the color has changed significantly (Red -> Green)
            # We check if colors are different. PyAutoGUI colors are (R, G, B) tuples.
            if current_color != start_color:
                
                # --- The Delay Logic ---
                # To get a score of 130-150ms, we wait 0.13 to 0.15 seconds.
                # Note: Python execution takes a few ms, so this usually results in ~130-160ms total.
                delay = random.uniform(0.13, 0.15)
                time.sleep(delay)
                
                # Click immediately after delay
                pyautogui.click()
                
                print(f"Clicked! (Simulated reaction delay: {delay:.3f}s)")
                break  # Stop the clicking loop
            
        # Small pause to prevent restarting immediately if you hold the key
        time.sleep(0.5) 
        print("Ready for next round. Press '\\' again to restart.")

if __name__ == "__main__":
    run_reaction_bot()