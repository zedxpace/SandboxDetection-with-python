#code is explained in this page : https://www.codexpace.ml/2022/02/sandbox-detection.html
import ctypes
import random
import sys
import time

user32        = ctypes.windll.user32
kernel32      = ctypes.windll.kernel32

keystrokes    = 0
mouse_clicks  = 0
double_clicks = 0

class Last_Input_Info(ctypes.Structure):
    _fields_ = [("cbSize" ,ctypes.c_uint) ,("dwTime" ,ctypes.c_ulong)]
def get_last_input():
    struct_lastinputinfo        = Last_Input_Info()
    struct_lastinputinfo.cbSize = ctypes.sizeof(Last_Input_Info)

    user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))

    run_time = kernel32.GetTickCount()
    elasped  = run_time - struct_lastinputinfo.dwTime
    print("[*] It's been %d milliseconds since the last input event."%elasped)
    return elasped

def get_key_press():
    global mouse_clicks
    global keystrokes

    for i in range(0 ,0xff):

        if user32.GetAsyncKeyState(i) == -32767 :

            if 1 == 0x1 :

                mouse_clicks +=1
                return time.time()

            elif i>32 and i < 127:
                keystrokes += 1

    return None
def detect_Sandbox():
    global mouse_clicks
    global keystrokes

    max_keystrokes         = random.randint(10 ,25)
    max_mouse_clicks       = random.randint(5 ,25)
    double_clicks          = 0
    max_double_clicks      = 10
    double_click_threshold = 0.250 #in seconds
    first_double_click     = None
    average_mousetime      = 0
    detection_complete     = False
    previous_timestamp     = None

    last_input             = get_last_input()

    if last_input >= max_input_threshold :
        sys.exit(0)
        while not detection_complete :

            keypress_time  = get_key_press()
            if keypress_time is not None and previous_timestamp is not None :

                elapsed = keypress_time - previous_timestamp

                if elapsed <= double_click_threshold :
                    double_clicks += 1
                    if first_double_click is None :

                        first_double_click = time.time()
                    else :

                        if double_clicks == max_double_clicks :
                            if keypress_time -first_double_click <= (max_double_clicks * double_click_threshold):
                                sys.exit(0)

                if keystrokes >= max_keystrokes and double_clicks >= max_double_clicks and mouse_clicks >= max_mouse_clicks :
                    return
                previous_timestamp = keypress_time
            elif keypress_time is not None :
                previous_timestamp = keypress_time


detect_Sandbox()
print("We are Ok!")
while True :
    get_last_input()
    time.sleep(1)
  
