import threading
import time
from threading import Thread

import pyautogui
from pynput import keyboard, mouse

# Biến cờ để theo dõi trạng thái của chương trình
is_holding = False
stop_flag = threading.Event()

def on_press(key):
    global is_holding
    # Bắt đầu giữ chuột trái khi nhấn phím F10
    if key == keyboard.Key.f10 and not is_holding:
        print("The F10 key has been pressed. Start holding the left mouse button.")
        pyautogui.mouseDown(button='left')
        is_holding = True
    elif key == keyboard.Key.esc:
        # Tùy chọn: dừng chương trình bằng phím ESC
        print("The ESC key has been pressed. Exit the program.")
        if is_holding:
            pyautogui.mouseUp(button='left')
        stop_flag.set() # Bật cờ dừng
        return False # Dừng listener

def on_click(x, y, button, pressed):
    global is_holding
    # Dừng giữ chuột trái khi click chuột phải
    if button == mouse.Button.right and pressed and is_holding:
        print("Right click detected. Release left mouse button.")
        pyautogui.mouseUp(button='left')
        is_holding = False
    
# Thiết lập và chạy trình lắng nghe phím
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Thiết lập và chạy trình lắng nghe chuột
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

print("The program is waiting for the F10 shortcut key to start. Right click to stop or ESC to exit.")

# Chờ cho đến khi cờ dừng được bật
stop_flag.wait()

# Dừng cả hai listener
keyboard_listener.stop()
mouse_listener.stop()

# Đợi cho đến khi các listener dừng
keyboard_listener.join()
mouse_listener.join()

print("The program has stopped completely.")