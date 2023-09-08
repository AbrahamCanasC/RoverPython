from evdev import InputDevice, categorize, ecodes

# Creamos el objeto gamepad
gamepad = InputDevice('/dev/input/event8')

# Muestra la info del gamepad
print(gamepad)

# Como las variables de python no admiten numeros usamos letras
Y = 308
A = 304
B = 305
X = 307
START = 315
BACK = 314
LOGO = 316
LB = 310
RB = 311
ClicIz = 317
ClicDer = 318

# Muestra los codigos
for event in gamepad.read_loop():
    # Botones
    if event.type == ecodes.EV_KEY:
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
            elif event.code == ClicIz:
                print("Presion izquierda")
            elif event.code == ClicDer:
                print("Presion derecha")
            elif event.code == HATOY:
                print("Presion derecha")
        #elif event.value == 0:
            #print("Suelto")
#Gatillo izquierdo
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
            if absevent.event.value == 255:
                print("Gatillo izquierdo encendido")
            elif absevent.event.value == 0:
                print("Gatillo izquierdo apagado")
#Gatillo derecho
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
            if absevent.event.value == 255:
                print("Gatillo derecho encendido")
            elif absevent.event.value == 0:
                print("Gatillo derecho apagado")
# Joystick izquierdo
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                if absevent.event.value == -32768:
                    print("Joystick Iz - Izquierda")
                elif absevent.event.value == 32767:
                    print("Joystick Iz - Derecha")
                elif absevent.event.value == 128:
                    print("Joystick Iz - Centrado")
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                if absevent.event.value == -32768:
                    print("Joystick Iz - Arriba")
                elif absevent.event.value == 32767:
                    print("Joystick Iz - Abajo")
                elif absevent.event.value == -129:
                    print("Joystick Iz - Centrado")     
# Joystick izquierdo
            elif event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
                    if absevent.event.value == -32768:
                        print("Joystick Der - Izquierda")
                    elif absevent.event.value == 32767:
                        print("Joystick Der - Derecha")
                    elif absevent.event.value == 128:
                        print("Joystick Der - Centrado")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
                    if absevent.event.value == -32768:
                        print("Joystick Der - Arriba")
                    elif absevent.event.value == 32767:
                        print("Joystick Der - Abajo")
                    elif absevent.event.value == -129:
                        print("Joystick Der - Centrado")