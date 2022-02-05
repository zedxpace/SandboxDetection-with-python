# Blackhat-SandboxDetection

## code is explained in the below link 
## https://www.codexpace.ml/2022/02/sandbox-detection.html
Sandboxing :
- It is a computer security term reffering to when a program in set aside from other progams in a seprate environment so that if errors or security issues occur ,those issues will not spread to other areas on the computer .
- Programs are enabled in their own sequestered area ,where they can be worked on without posing any threat to other programs.
- Sandboxes can look like a regular operating environment ,or they cna be much more bare bones .V M are often used for what are reffered to as runtime sandboxes.

: SandBox Detection :
For defense against Sandbox or to detect wheather our trojan is running in sandbox or actual operating system.

We can use a few indicators to try to determine whether our trojan is executing within a sandbox. we'll monitor our target machine for recent user input ,including key-strokes and mouse-clicks.

[ Whole concept ]
The script will try to determine if the sandbox operator is sending input repeatedly (i.e. suspicious rapid succession of continous mouse clicks ) in order to try to respond to rudimentary sandbox detection methods. 
We'll compare the last time user intracted with the machine versus how long the machine has been running ,which should gives us the good idea wheather the we are inside a sandbox or not .
A typicall system has many interactions at some point during the day since it has been booted , whereas a sandbox environment usually has no user interface because sanboxes are typically used as an automated malware analysis techniques.
                                                                          -ZED
