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
        elif event.value == 0:
            print("Suelto")
#Gatillo izquierdo
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
            if absevent.event.value != 0:
                print("Gatillo izquierdo activo oscilante")
            if absevent.event.value == 255:
                print("Gatillo izquierdo maximo")
            elif absevent.event.value == 0:
                print("Gatillo izquierdo apagado")
#Gatillo derecho
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
            if absevent.event.value != 0:
                print("Gatillo derecho activo oscilante")
            if absevent.event.value == 255:
                print("Gatillo derecho maximo")
            elif absevent.event.value == 0:
                print("Gatillo derecho apagado")
# Joystick izquierdo
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                if absevent.event.value <= 127:
                    print("Joystick Iz - Izquierda oscilante")
                if absevent.event.value == -32768:
                    print("Joystick Iz - Izquierda maximo")
                elif absevent.event.value >= 129:
                    print("Joystick Iz - Derecha oscilante")
                if absevent.event.value == 32767:
                    print("Joystick Iz - Derecha maximo")
                elif absevent.event.value == 128:
                    print("Joystick Iz - Centrado")
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                if absevent.event.value <= -130:
                    print("Joystick Iz - Arriba oscilante")
                if absevent.event.value == -32768:
                    print("Joystick Iz - Arriba maximo")
                elif absevent.event.value >= -128:
                    print("Joystick Iz - Abajo oscilante")
                if absevent.event.value == 32767:
                    print("Joystick Iz - Abajo maximo")
                elif absevent.event.value == -129:
                    print("Joystick Iz - Centrado")     
# Joystick derecho
            elif event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
                    if absevent.event.value <= 127:
                        print("Joystick Der - Izquierda oscilante")
                    if absevent.event.value == -32768:
                        print("Joystick Der - Izquierda maxima")
                    elif absevent.event.value >= 129:
                        print("Joystick Der - Derecha oscilante")
                        if absevent.event.value == 32767:
                            print("Joystick Der - Derecha maxima")
                    elif absevent.event.value == 128:
                        print("Joystick Der - Centrado")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
                    if absevent.event.value <= -130:
                        print("Joystick Der - Arriba oscilante")
                    if absevent.event.value == -32768:
                        print("Joystick Der - Arriba maximo")
                    elif absevent.event.value >= -128:
                        print("Joystick Der - Abajo oscilante")
                    if absevent.event.value == 32767:
                        print("Joystick Der - Abajo maximo")
                    elif absevent.event.value == -129:
                        print("Joystick Der - Centrado")

                elif event.type == ecodes.EV_ABS:
                    if event.code == ecodes.ABS_HAT0X:
                        # Procesa el evento de ABS_HAT0X (eje X)
                        if absevent.event.value == -1:
                            print("Flecha izquierda activa")
                        if absevent.event.value == 1:
                            print("Flecha derecha activa")
                        if absevent.event.value == 0:
                            print("Flecha suelta")
                    elif event.code == ecodes.ABS_HAT0Y:
                        # Procesa el evento de ABS_HAT0Y (eje Y)
                        if absevent.event.value == -1:
                            print("Flecha arriba activa")
                        if absevent.event.value == 1:
                            print("Flecha abajo activa")
                        if absevent.event.value == 0:
                            print("Flecha suelta")
