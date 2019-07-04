'''ctypes is a foreign function library for Python.
It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
It can be used to wrap these libraries in pure Python.'''
import ctypes
import random
import sys
import time

user32        = ctypes.windll.user32
kernel32      = ctypes.windll.kernel32
'''The main variables we are going to track total number of mouse clicks ,double clicks and keystrokes.
we'll also track the timing of the events '''
keystrokes    = 0
mouse_clicks  = 0
double_clicks = 0
'''code for detecting how long the system has been running and how long since the last user input '''
'''It will hold the time-stamp of when the last input event was detected on the system'''
class Last_Input_Info(ctypes.Structure):
    _fields_ = [("cbSize" ,ctypes.c_uint) ,("dwTime" ,ctypes.c_ulong)]
def get_last_input():
    struct_lastinputinfo        = Last_Input_Info()
    struct_lastinputinfo.cbSize = ctypes.sizeof(Last_Input_Info)
    '''Get last input registered'''
    user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))
    '''Now determine how long the machine has been running'''
    '''It is helping to determine that how long the system has been running  by using the GetTickCount functino'''
    run_time = kernel32.GetTickCount()
    elasped  = run_time - struct_lastinputinfo.dwTime
    print("[*] It's been %d milliseconds since the last input event."%elasped)
    return elasped
'''This function tells the number of mouse clicks ,the time of the mouse-clicks ,as well as how many keystrokes
the target has issued .'''
def get_key_press():
    global mouse_clicks
    global keystrokes
    '''Iterating over the range of valid input keys'''
    for i in range(0 ,0xff):
        '''For each key pressed , we check wheather the key has been pressed using GetAsyncKeyState() call'''
        if user32.GetAsyncKeyState(i) == -32767 :
            '''If the key is detected as being pressed we check  if it is 0x1'''
            '''0x1 is the code for a left mouse-click'''
            if 1 == 0x1 :
                '''Incrementing the total number of mouse-clicks and return the current time stamp 
                so that we can perform timing calculations '''
                mouse_clicks +=1
                return time.time()
                '''we will also check if there are ASCII  keypresses on the keyboard '''
            elif i>32 and i < 127:
                keystrokes += 1

    return None
def detect_Sandbox():
    global mouse_clicks
    global keystrokes
    '''Track the timing of mouse clicks ,and some thresholds with regard to how many keystrokes or mouse clicks'''
    max_keystrokes         = random.randint(10 ,25)
    max_mouse_clicks       = random.randint(5 ,25)
    double_clicks          = 0
    max_double_clicks      = 10
    double_click_threshold = 0.250 #in seconds
    first_double_click     = None
    average_mousetime      = 0
    detection_complete     = False
    previous_timestamp     = None
    max_input_threshold    = 30000 #in milliseconds
    '''now we will retrieve the elpsed time ,if time for which user interction becomes long the trojan will die '''
    last_input             = get_last_input()
    '''If we hit our threshold let's bail out '''
    if last_input >= max_input_threshold :
        sys.exit(0)
        while not detection_complete :
            '''check mouse clicks or keystrokes'''
            keypress_time  = get_key_press()
            if keypress_time is not None and previous_timestamp is not None :
                '''Calculate the time between double clicks'''
                '''we are calculating the time between the mouse-clicksand then compare with threshold'''
                elapsed = keypress_time - previous_timestamp
                '''The user double clicked'''
                if elapsed <= double_click_threshold :
                    double_clicks += 1
                    if first_double_click is None :
                        '''Grab the timestamp of the first double click'''
                        first_double_click = time.time()
                    else :
                        '''we ware checking wheather the sandbox is inputting to to fake our sandbox detection '''
                        if double_clicks == max_double_clicks :
                            if keypress_time -first_double_click <= (max_double_clicks * double_click_threshold):
                                sys.exit(0)
                '''The final step is to see if we have made it through all of the checks and reached our maximum number of clicks 
                ,keystrokes , and double clicks'''
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
  
