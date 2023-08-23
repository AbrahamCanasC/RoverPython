# Control de Gamepad con Python

#import evdev
from evdev import InputDevice, categorize, ecodes

#Creamos el objecto gamepad
gamepad = InputDevice('/dev/input/event8')

#Muestra la info del gamepad
print(gamepad)

#Como las variables de python no admiten numeros usamos letras
Y = 308
A = 304
B = 305
X = 307
START = 315
BACK = 314
LOGO = 316
LB = 310
RB = 311


#Muestra los codigos
for event in gamepad.read_loop():
    #Botones
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == X:
                print("X")
            elif event.code == B:
                print("B")
            elif event.code == A:
                print("A")
            elif event.code == Y:
                print("Y")
            elif event.code == START:
                print("Start")
            elif event.code == BACK:
                print("BACK")
            elif event.code == LOGO:
                print("LOGO")
            elif event.code == LB:
                print("LB")
            elif event.code == RB:
                print("RB")
            elif event.value == 0:
                print("Suelto")

    #Joystick izquierdo
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print (ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value) #"Hace lo mismo que el archivo de botones"
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             if absevent.event.value == -32768:
                print("Izquierda")
             elif absevent.event.value == 32767:
                print("Derecha")
             elif absevent.event.value == 128:
                print("Centrado")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == -32768:
                print("Arriba")
             elif absevent.event.value == 32767:
                print("Abajo")
             elif absevent.event.value == -129:
                print("Centrado")
                
    #Joystick derecho
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print (ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value) #"Hace lo mismo que el archivo de botones"
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_XR":
             if absevent.event.value == -32768:
                print("Izquierda")
             elif absevent.event.value == 32767:
                print("Derecha")
             elif absevent.event.value == 128:
                print("Centrado")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_YR":
             if absevent.event.value == -32768:
                print("Arriba")
             elif absevent.event.value == 32767:
                print("Abajo")
             elif absevent.event.value == -129:
                print("Centrado")
