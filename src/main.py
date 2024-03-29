from pydoc import cli
import threading as td
import server as sv
import audio as ad
from gui import Gui
import mouse as ms
import myConfig as mc

if __name__ == "__main__":

# comento por comodidad al probar
    td_bienvenida = td.Thread(target=ad.tss, args=['Hola! bienvenido al mouse controlado'])
    td_bienvenida.daemon = True
    td_bienvenida.start()

    root = Gui()
    # las imagenes son lo que mas tardan en cargar. Las cargo antes de arrancar los threads, asi lo hace mucho mas rapido,
    # y aparte ya quedan cargadas hasta que se finalice el programa
    print(f'{__name__}: cargando fotos')
    mc.cargar_fotos()
    print(f'{__name__}: fin carga fotos')

    print(f'{__name__}: iniciando thread socket')
    serverObject = sv.Server()
    td_socket = td.Thread(target=serverObject.create_server, args=[root])
    td_socket.daemon = True
    td_socket.start()
    print(f'{__name__}: thread socket iniciado')

    print(f'{__name__}: iniciando thread mouse')
    mouseObject = ms.Mouse()
    td_mouse = td.Thread(target=mouseObject.mouse, args=[root])
    td_mouse.daemon = True
    td_mouse.start()
    print(f'{__name__}: thread mouse iniciado')

    print(f'{__name__}: THREADS:\nsocket: {td_socket}\nmouse: {td_mouse}\n')
    print(f'{__name__}: abriendo interfaz')
    root.start_gui()
    print(f'{__name__}: interfaz cerrada')

    # comento por comodidad al probar
    ad.tss('Hasta luego!')

    mc.main_alive = False
    # margen de tiempo para que mueran threads
    print(f'{__name__}: esperando muerte de threads')
    if mc.socket_alive:
        serverObject.close_server()
        td_socket.join()
    print(f'{__name__}: murio el socket')
    if mc.mouse_alive:
        td_mouse.join()
    print(f'{__name__}: murio el mouse')

    print(f'{__name__}: THREADS:\nsocket: {td_socket}\nmouse: {td_mouse}')
