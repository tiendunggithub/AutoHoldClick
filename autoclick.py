import threading
import time
from threading import Thread

import pyautogui
from pynput import keyboard, mouse

is_click = False
stop_flag = threading.Event()

# Tốc độ click (số lần click mỗi giây)
# Bạn có thể thay đổi giá trị này
CLICK_SPEED = 90 
CLICK_INTERVAL = 1 / CLICK_SPEED

def onClick(key): 
    global is_click

    if key == keyboard.Key.f8 and not is_click:
        print("The F8 key has been pressed. Start auto click.")
        click_thread = threading.Thread(target=autoClick)
        click_thread.start()
    elif key == keyboard.Key.f9:
        print("The F9 key has been pressed. stop the program.")
        is_click = False
    elif key == keyboard.Key.esc:
        print("The ESC key has been pressed. Exit the program.")
        is_click = False
        stop_flag.set() # Bật cờ dừng
        return False # Dừng listener

def autoClick():
    global is_click
    is_click = True
    print("is clicking...")
    while True:
        if is_click == False:
            break
        print("is clicking...")

        # pyautogui.click()
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')
        time.sleep(CLICK_INTERVAL)

# Thiết lập và chạy trình lắng nghe phím
keyboard_listener = keyboard.Listener(on_press=onClick)
keyboard_listener.start()


print("====The program is running===")
print("- F8 to start")
print("- F9 to pause")
print("- ESC to exit.")

# Chờ cho đến khi cờ dừng được bật
stop_flag.wait()

# Dừng cả hai listener
keyboard_listener.stop()

# Đợi cho đến khi các listener dừng
keyboard_listener.join()

print("====The program has stopped completely.====")
