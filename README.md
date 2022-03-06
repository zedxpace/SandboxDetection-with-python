# Blackhat-SandboxDetection 
<div>
<a href="https://www.codexpace.ml/2022/02/sandbox-detection.html" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a>
</div>

Sandboxing :
- It is a computer security term reffering to when a program in set aside from other progams in a seprate environment so that if errors or security issues occur ,those issues will not spread to other areas on the computer .
- Programs are enabled in their own sequestered area ,where they can be worked on without posing any threat to other programs.
- Sandboxes can look like a regular operating environment ,or they cna be much more bare bones .V M are often used for what are reffered to as runtime sandboxes.

: SandBox Detection :
For defense against Sandbox or to detect wheather our trojan is running in sandbox or actual operating system.

We can use a few indicators to try to determine whether our trojan is executing within a sandbox. we'll monitor our target machine for recent user input ,including key-strokes and mouse-clicks.
                                                                          -ZED
