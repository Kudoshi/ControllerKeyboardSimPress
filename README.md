# ControllerKeyboardSimPress
A simple program to use controller to simulate keyboard key press. Can bypass some games' anti-simulate key press.

Uses pycharm to get controller input

Replace the '0x44' with the appropriate hexadecimal

Format: '0x<keycode>'
Look below for the keycode
https://www.csee.umbc.edu/portal/help/theory/ascii.txt
  

  
---------------------------------------
Pygame controller button (https://www.pygame.org/docs/ref/joystick.html):
  
Left Stick:
Left -> Right   - Axis 0
Up   -> Down    - Axis 1
  
Right Stick:
Left -> Right   - Axis 2
Up   -> Down    - Axis 3
  
Left Trigger:
Out -> In       - Axis 4
  
Right Trigger:
Out -> In       - Axis 5
  
Buttons:
Cross Button    - Button 0
Circle Button   - Button 1
Square Button   - Button 2
Triangle Button - Button 3
Share Button    - Button 4
PS Button       - Button 5
Options Button  - Button 6
L. Stick In     - Button 7
R. Stick In     - Button 8
Left Bumper     - Button 9
Right Bumper    - Button 10
D-pad Up        - Button 11
D-pad Down      - Button 12
D-pad Left      - Button 13
D-pad Right     - Button 14
Touch Pad Click - Button 15
 -------------------------------------------
Pygame event (https://www.pygame.org/docs/ref/event.html):
 
QUIT              none
ACTIVEEVENT       gain, state
KEYDOWN           key, mod, unicode, scancode
KEYUP             key, mod
MOUSEMOTION       pos, rel, buttons
MOUSEBUTTONUP     pos, button
MOUSEBUTTONDOWN   pos, button
JOYAXISMOTION     joy (deprecated), instance_id, axis, value
JOYBALLMOTION     joy (deprecated), instance_id, ball, rel
JOYHATMOTION      joy (deprecated), instance_id, hat, value
JOYBUTTONUP       joy (deprecated), instance_id, button
JOYBUTTONDOWN     joy (deprecated), instance_id, button
VIDEORESIZE       size, w, h
VIDEOEXPOSE       none
USEREVENT         code
