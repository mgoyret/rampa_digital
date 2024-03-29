import tkinter as tk
import myConfig as mc
from PIL import ImageTk, Image
# se define la clase de la ventana principal, con un frame dentro
# con los labes deseados


class Window_use(tk.Frame):

    # idx = list()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background=mc.background)
        self.coords_clicks_Labels = tk.LabelFrame(self)
        self.coords_clicks_Labels.grid(row=0, column=0)
        # mod=avanzado --> mod=0
        if mc.use_advanced_mod:
            self.img_ul = mc.img_ul
            self.lbl_ul = tk.Label(self.coords_clicks_Labels,image=self.img_ul["black"])
            self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_u = mc.img_u
        self.lbl_u = tk.Label(self.coords_clicks_Labels,image=self.img_u["black"])
        self.lbl_u.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        if mc.use_advanced_mod:
            self.img_ur = mc.img_ur
            self.lbl_ur = tk.Label(self.coords_clicks_Labels,image=self.img_ur["black"])
            self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

        self.img_l = mc.img_l
        self.lbl_l = tk.Label(self.coords_clicks_Labels,image=self.img_l["black"])
        self.lbl_l.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.img_r = mc.img_r
        self.lbl_r = tk.Label(self.coords_clicks_Labels,image=self.img_r["black"])
        self.lbl_r.grid(row=1, column=2, padx=2, pady=2, sticky='nesw')

        if mc.use_advanced_mod:
            self.img_dl = mc.img_dl
            self.lbl_dl = tk.Label(self.coords_clicks_Labels,image=self.img_dl["black"])
            self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

        self.img_d = mc.img_d
        self.lbl_d = tk.Label(self.coords_clicks_Labels,image=self.img_d["black"])
        self.lbl_d.grid(row=2, column=1, padx=2, pady=2, sticky='nesw')

        if mc.use_advanced_mod:
            self.img_dr = mc.img_dr
            self.lbl_dr = tk.Label(self.coords_clicks_Labels,image=self.img_dr["black"])
            self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')

        self.clickLabels = tk.LabelFrame(self.coords_clicks_Labels, text='clicks')
        self.clickLabels.grid(row=1, column=1, padx=2, pady=2)

        self.img_ci = mc.img_ci
        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci['black'])
        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_cd = mc.img_cd
        self.lbl_cd = tk.Label(self.clickLabels, image=self.img_cd['black'])
        self.lbl_cd.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.extraLabels = tk.LabelFrame(self)
        self.extraLabels.grid(row=0, column=1)

        if mc.use_advanced_mod:
            self.ruedaLabels = tk.LabelFrame(self.extraLabels, text='Rueda')
            self.ruedaLabels.grid(row=0, column=0)

            self.img_wu = mc.img_wu
            self.lbl_wu = tk.Label(self.ruedaLabels, image=self.img_wu['black'])
            self.lbl_wu.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')

            self.img_wd = mc.img_wd
            self.lbl_wd = tk.Label(self.ruedaLabels, image=self.img_wd['black'])
            self.lbl_wd.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')

        self.accionesLabels = tk.LabelFrame(self.extraLabels, text='extras')
        self.accionesLabels.grid(row=1, column=0)

        self.img_pausa = mc.img_pausa
        self.lbl_pausa = tk.Label(self.accionesLabels, image=self.img_pausa['black'], borderwidth=0, highlightthickness=0)
        self.lbl_pausa.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_salir = mc.img_salir
        self.lbl_salir = tk.Label(self.accionesLabels, image=self.img_salir['black'], borderwidth=0, highlightthickness=0)
        self.lbl_salir.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.idx = {
            "ul":   "b",
            "u":    "b",
            "ur":   "b",
            "l":    "b",
            "r":    "b",
            "dl":   "b",
            "d":    "b",
            "dr":   "b",
            'ci':   'b',
            'cd':   'b',
            'wu':   'b',
            'wd':   'b',
            'pausa': 'b',
            'salir': 'r'
        }

        self.color_use()

    def color_use(self):
        if mc.color_flag and mc.gui_alive:
            for i in self.idx:
                if self.idx[i] == 'r':
                    if i == 'ul':
                        self.lbl_ul = tk.Label(self.coords_clicks_Labels, image=self.img_ul["black"])
                        self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_u = tk.Label(self.coords_clicks_Labels, image=self.img_u["red"])
                        self.lbl_u.grid(row=0, column=1, padx=2,pady=2, sticky='nesw')
                        self.idx['u'] = 'r'

                    elif i == 'u':
                        self.lbl_u = tk.Label(self.coords_clicks_Labels, image=self.img_u["black"])
                        self.lbl_u.grid(row=0, column=1, padx=2,pady=2, sticky='nesw')
                        if mc.use_advanced_mod:
                            self.lbl_ur = tk.Label(self.coords_clicks_Labels, image=self.img_ur["red"])
                            self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')
                            self.idx['ur'] = 'r'
                        else:
                            self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["red"])
                            self.lbl_l.grid(row=1, column=0,padx=2, pady=2, sticky='nesw')
                            self.idx['l'] = 'r'

                    elif i == 'ur':
                        self.lbl_ur = tk.Label(self.coords_clicks_Labels, image=self.img_ur["black"])
                        self.lbl_ur.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["red"])
                        self.lbl_l.grid(row=1, column=0, padx=2,pady=2, sticky='nesw')
                        self.idx['l'] = 'r'

                    elif i == 'l':
                        self.lbl_l = tk.Label(self.coords_clicks_Labels, image=self.img_l["black"])
                        self.lbl_l.grid(row=1, column=0, padx=2,pady=2, sticky='nesw')
                        self.lbl_r = tk.Label(self.coords_clicks_Labels, image=self.img_r["red"])
                        self.lbl_r.grid(row=1, column=2, padx=2,pady=2, sticky='nesw')
                        self.idx['r'] = 'r'

                    elif i == 'r':
                        self.lbl_r = tk.Label(self.coords_clicks_Labels, image=self.img_r["black"])
                        self.lbl_r.grid(row=1, column=2, padx=2,pady=2, sticky='nesw')
                        if mc.use_advanced_mod:
                            self.lbl_dl = tk.Label(self.coords_clicks_Labels, image=self.img_dl["red"])
                            self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['dl'] = 'r'
                        else:
                            self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["red"])
                            self.lbl_d.grid(row=2, column=1,padx=2, pady=2, sticky='nesw')
                            self.idx['d'] = 'r'

                    elif i == 'dl':
                        self.lbl_dl = tk.Label(self.coords_clicks_Labels, image=self.img_dl["black"])
                        self.lbl_dl.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["red"])
                        self.lbl_d.grid(row=2, column=1, padx=2,pady=2, sticky='nesw')
                        self.idx['d'] = 'r'

                    elif i == 'd':
                        self.lbl_d = tk.Label(self.coords_clicks_Labels, image=self.img_d["black"])
                        self.lbl_d.grid(row=2, column=1, padx=2,pady=2, sticky='nesw')
                        if mc.use_advanced_mod:
                            self.lbl_dr = tk.Label(self.coords_clicks_Labels, image=self.img_dr["red"])
                            self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')
                            self.idx['dr'] = 'r'
                        else:
                            self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci["red"])
                            self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['ci'] = 'r'

                    elif i == 'dr':
                        self.lbl_dr = tk.Label(self.coords_clicks_Labels, image=self.img_dr["black"])
                        self.lbl_dr.grid(row=2, column=2, padx=2, pady=2, sticky='nesw')
                        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci["red"])
                        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['ci'] = 'r'

                    elif i == 'ci':
                        self.lbl_ci = tk.Label(self.clickLabels, image=self.img_ci['black'])
                        self.lbl_ci.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_cd = tk.Label(self.clickLabels, image=self.img_cd['red'])
                        self.lbl_cd.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.idx['cd'] = 'r'

                    elif i == 'cd':
                        self.lbl_cd = tk.Label(self.clickLabels, image=self.img_cd['black'])
                        self.lbl_cd.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        if mc.use_advanced_mod:
                            self.lbl_wu = tk.Label(self.ruedaLabels, image=self.img_wu['red'])
                            self.lbl_wu.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')
                            self.idx['wu'] = 'r'
                        else:
                            self.lbl_pausa = tk.Label(self.accionesLabels, image=self.img_pausa['red'])
                            self.lbl_pausa.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['pausa'] = 'r'

                    elif i == 'wu':
                        self.lbl_wu = tk.Label(self.ruedaLabels, image=self.img_wu['black'])
                        self.lbl_wu.grid(row=0, column=3, padx=2, pady=2, sticky='nesw')
                        self.lbl_wd = tk.Label(self.ruedaLabels, image=self.img_wd['red'])
                        self.lbl_wd.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')
                        self.idx['wd'] = 'r'

                    elif i == 'wd':
                        self.lbl_wd = tk.Label(self.ruedaLabels, image=self.img_wd['black'])
                        self.lbl_wd.grid(row=2, column=3, padx=2, pady=2, sticky='nesw')
                        self.lbl_pausa = tk.Label(self.accionesLabels, image=self.img_pausa['red'])
                        self.lbl_pausa.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['pausa'] = 'r'

                    elif i == 'pausa':
                        self.lbl_pausa = tk.Label(self.accionesLabels, image=self.img_pausa['black'])
                        self.lbl_pausa.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_salir = tk.Label(self.accionesLabels, image=self.img_salir['red'])
                        self.lbl_salir.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['salir'] = 'r'

                    elif i == 'salir':
                        self.lbl_salir = tk.Label(self.accionesLabels, image=self.img_salir['black'])
                        self.lbl_salir.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')
                        if mc.use_advanced_mod:
                            self.lbl_ul = tk.Label(self.coords_clicks_Labels, image=self.img_ul['red'])
                            self.lbl_ul.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                            self.idx['ul'] = 'r'
                        else:
                            self.lbl_u = tk.Label(self.coords_clicks_Labels, image=self.img_u["red"])
                            self.lbl_u.grid(row=0, column=1,padx=2, pady=2, sticky='nesw')
                            self.idx['u'] = 'r'

                    self.idx[i] = 'b'
                    break
        self.after(mc.velocidad_barrido, self.color_use)

class Window_config(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background=mc.background)
        # velocidad puntero
        self.frame_velocidad_puntero = tk.LabelFrame(self, background=mc.background)
        self.frame_velocidad_puntero.pack(padx=10, pady=(20, 10), expand=True, fill='both')
        ## label
        # el  valor dividido por 5 es para que visualmente hayan 4 velocidades
        self.label_velocidad_puntero = tk.Label(self.frame_velocidad_puntero, text=f'Velocidad del puntero: {int(mc.velocidad_puntero/5)}', background=mc.background)
        self.label_velocidad_puntero.pack(side=tk.LEFT, padx=5, pady=5)

        ## valores
        self.frame_valores_puntero = tk.LabelFrame(self.frame_velocidad_puntero, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_valores_puntero.pack(side=tk.RIGHT, padx=10, pady=5)

        self.btn_5 = tk.Button(self.frame_valores_puntero, text='1', background='white')
        self.btn_5.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_10 = tk.Button(self.frame_valores_puntero, text='2', background='white')
        self.btn_10.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.btn_15 = tk.Button(self.frame_valores_puntero, text='3', background='white')
        self.btn_15.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_20 = tk.Button(self.frame_valores_puntero, text='4', background='white')
        self.btn_20.grid(row=1, column=1, padx=2, pady=2, sticky='nesw')

        # velocidad barrido
        self.frame_velocidad_barrido = tk.LabelFrame(self, background=mc.background)
        self.frame_velocidad_barrido.pack(padx=10, pady=(10, 5), expand=True, fill='both')
        ## label
        self.label_velocidad_barrido = tk.Label(self.frame_velocidad_barrido, text=f'Velocidad del barrido [ms]: {mc.velocidad_barrido}', background=mc.background)
        self.label_velocidad_barrido.pack(side=tk.LEFT, padx=5, pady=5)

        ## valores
        self.frame_valores_barrido = tk.LabelFrame(self.frame_velocidad_barrido, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_valores_barrido.pack(side=tk.RIGHT, padx=10, pady=5)

        self.btn_750 = tk.Button(self.frame_valores_barrido, text='750', background='white')
        self.btn_750.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_1000 = tk.Button(self.frame_valores_barrido, text='1000', background='white')
        self.btn_1000.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.btn_1500 = tk.Button(self.frame_valores_barrido, text='1500', background='white')
        self.btn_1500.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_2000 = tk.Button(self.frame_valores_barrido, text='2000', background='white')
        self.btn_2000.grid(row=1, column=1, padx=2, pady=2, sticky='nesw')


        # modo pausa
        self.frame_pausa = tk.LabelFrame(self, background=mc.background)
        self.frame_pausa.pack(padx=10, pady=(10, 5), expand=True, fill='both')
        ## label
        self.label_pausa = tk.Label(self.frame_pausa, text=f'Al pausar ejecución:', background=mc.background)
        self.label_pausa.pack(side=tk.LEFT, padx=5, pady=5)

        ## valores
        self.frame_opciones_pausa = tk.LabelFrame(self.frame_pausa, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_opciones_pausa.pack(side=tk.RIGHT, padx=10, pady=5)

        self.btn_mostrar = tk.Button(self.frame_opciones_pausa, text='mostrar', background='white')
        self.btn_mostrar.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_esconder = tk.Button(self.frame_opciones_pausa, text='esconder', background='white')
        self.btn_esconder.grid(row=0, column=2, padx=2, pady=2, sticky='nesw')

##########################################################################################
        # posicion ventana
        self.frame_posicion = tk.LabelFrame(self, background=mc.background)
        self.frame_posicion.pack(padx=10, pady=(10, 5), expand=True, fill='both')
        ## label
        self.label_posicion = tk.Label(self.frame_posicion, text=f'Posicion de la ventana:', background=mc.background)
        self.label_posicion.pack(side=tk.LEFT, padx=5, pady=5)

        ## valores
        self.frame_opciones_posicion = tk.LabelFrame(self.frame_posicion, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_opciones_posicion.pack(side=tk.RIGHT, padx=10, pady=5)

        self.btn_tr = tk.Button(self.frame_opciones_posicion, text='superior derecha', background='white')
        self.btn_tr.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_c = tk.Button(self.frame_opciones_posicion, text='central', background='white')
        self.btn_c.grid(row=1, column=0, padx=2, pady=2, sticky='nesw')

        self.btn_td = tk.Button(self.frame_opciones_posicion, text='inferior derecha', background='white')
        self.btn_td.grid(row=2, column=0, padx=2, pady=2, sticky='nesw')

##########################################################################################
        # aplicar
        self.frame_aplicar = tk.LabelFrame(self, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_aplicar.pack(padx=50, pady=(5, 10), expand=True, fill='y')
        ## ok button
        self.btn_aplicar = tk.Button(self.frame_aplicar, text='aplicar', width=10, height=2, background='red')
        self.btn_aplicar.pack(side=tk.RIGHT, padx=(10, 5), pady=10)
        
        self.idx = [self.btn_5, self.btn_10, self.btn_15, self.btn_20, self.btn_750, self.btn_1000, self.btn_1500, self.btn_2000, self.btn_mostrar, self.btn_esconder, self.btn_tr, self.btn_c, self.btn_td, self.btn_aplicar]
        self.config_color()

    def config_color(self):
        if mc.in_window == 'config' and mc.gui_alive:
            for i in range(len(self.idx)):
                if self.idx[i].cget('background') == 'red':
                    self.idx[i].configure(bg='white')
                    self.idx[(i+1) % len(self.idx)].configure(bg='red')
                    break
            self.after(mc.velocidad_barrido, self.config_color)

class Gui(tk.Tk):

    # defino esta variable para que sea miembro y luego
    # igualarla a la ventana principal de la gui
    wd_use = None
    wd_config = None

    def __init__(self):
        mc.gui_alive = True # guarda, antes estaba en start gui que es cuando abre la interfaz
        print(f'{__name__}: INICIO Gui()')
        tk.Tk.__init__(self)
        self.title("Mouse4All")
        self.geometry(f"{mc.wd_with_main}x{mc.wd_hight_main}")
        self.resizable(False, False)
#        self.configure(background='#F2B33D')
        self.configure(background=mc.background)
        self.overrideredirect(2) #sin botones minimizar, etc
        self.protocol("WM_DELETE_WINDOW", self.finish_gui)
        self.eval('tk::PlaceWindow . center')
        # ICONO
        # self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        # self.tk.call('wm', 'iconphoto', self._w, self.img_icon)

        self.attributes("-topmost", True) # ventana siempre al frente
        mc.in_window = 'main'

        self.frame_general = tk.LabelFrame(self, background=mc.background, borderwidth=0, highlightthickness=0)
        self.frame_general.pack(padx=10, pady=10)

        self.frame_settings = tk.LabelFrame(self.frame_general, background=mc.background, text='Opciones')
        self.frame_settings.grid(row=0, column=0)

        self.img_settings = {"black": ImageTk.PhotoImage(Image.open("../recursos/settings_b.png").resize(mc.size_settings)), "red": ImageTk.PhotoImage(Image.open("../recursos/settings_r.png").resize(mc.size_settings))}
        self.lbl_settings = tk.Label(self.frame_settings, image=self.img_settings['black'])
        self.lbl_settings.grid(row=0, column=0, padx=(18, 8), pady=5, sticky='nesw')

        self.img_salir = {"black": ImageTk.PhotoImage(Image.open("../recursos/salir_b.png").resize(mc.size_settings)), "red": ImageTk.PhotoImage(Image.open("../recursos/salir_r.png").resize(mc.size_settings))}#mc.img_salir
        self.lbl_salir = tk.Label(self.frame_settings, image=self.img_salir['black'], borderwidth=0, highlightthickness=0)
        self.lbl_salir.grid(row=0, column=1, padx=(8, 18), pady=5, sticky='nesw')

        self.frame_modos = tk.LabelFrame(self.frame_general, background=mc.background, text='Modos de uso')
        self.frame_modos.grid(row=1, column=0)

        self.img_simple = {"black": ImageTk.PhotoImage(Image.open("../recursos/simple_b.png").resize(mc.size_modo)), "red": ImageTk.PhotoImage(Image.open("../recursos/simple_r.png").resize(mc.size_modo))}
        self.lbl_simple = tk.Label(self.frame_modos, image=self.img_simple["black"])
        self.lbl_simple.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')

        self.img_avanzado = {"black": ImageTk.PhotoImage(Image.open("../recursos/avanzado_b.png").resize(mc.size_modo)), "red": ImageTk.PhotoImage(Image.open("../recursos/avanzado_r.png").resize(mc.size_modo))}
        self.lbl_avanzado = tk.Label(self.frame_modos, image=self.img_avanzado["red"])
        self.lbl_avanzado.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')

        self.idx = {
            "settings": "b",
            "salir":    "b",
            "simple":   "b",
            'avanzado': 'r'
        }

        self.color()

    # esta funcion miembro analiza cuando un label tiene color rosa
    # y lo pone el azul, para luego poner el siguiente en rosa
    def color(self):
        if mc.color_flag and mc.gui_alive:
            for i in self.idx:
                if self.idx[i] == 'r':
                    if i == 'settings':
                        self.lbl_settings = tk.Label(self.frame_settings, image=self.img_settings['black'])
                        self.lbl_settings.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_salir = tk.Label(self.frame_settings, image=self.img_salir['red'], borderwidth=0, highlightthickness=0)
                        self.lbl_salir.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.idx['salir'] = 'r'

                    if i == 'salir':
                        self.lbl_salir = tk.Label(self.frame_settings, image=self.img_salir['black'], borderwidth=0, highlightthickness=0)
                        self.lbl_salir.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.lbl_simple = tk.Label(self.frame_modos, image=self.img_simple["red"])
                        self.lbl_simple.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['simple'] = 'r'

                    elif i == 'simple':
                        self.lbl_simple = tk.Label(self.frame_modos, image=self.img_simple["black"])
                        self.lbl_simple.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.lbl_avanzado = tk.Label(self.frame_modos, image=self.img_avanzado["red"])
                        self.lbl_avanzado.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.idx['avanzado'] = 'r'

                    elif i == 'avanzado':
                        self.lbl_avanzado = tk.Label(self.frame_modos, image=self.img_avanzado["black"])
                        self.lbl_avanzado.grid(row=0, column=1, padx=2, pady=2, sticky='nesw')
                        self.lbl_settings = tk.Label(self.frame_settings, image=self.img_settings['red'])
                        self.lbl_settings.grid(row=0, column=0, padx=2, pady=2, sticky='nesw')
                        self.idx['settings'] = 'r'
                    self.idx[i] = 'b'
                    break

        self.after(mc.velocidad_barrido, self.color)

        # si destruyo la gui desde el server, nunca sale de la funcion destroy() por lo que
        # el thread server se queda tildado ahi. Desde el server apago el flag alive, y esta funcion
        # se encarga de destruir
        if not mc.gui_alive: self.destroy()

    def start_gui(self):
        mc.in_window = 'main'
        self.mainloop()

    def finish_gui(self):
        mc.gui_alive = False
        self.quit()

    def open_config(self):
        print(f'{__name__}: open_config()')
        self.wd_config = tk.Toplevel(self)
        self.wd_config.title("Configuración")
        self.wd_config.geometry("%dx%d+%d+%d" % (mc.wd_with_config, mc.wd_hight_config, self.winfo_x()-0, self.winfo_y()-50))
        self.wd_config.maxsize(mc.wd_with_config, mc.wd_hight_config)
        self.wd_config.minsize(mc.wd_with_config, mc.wd_hight_config)
        self.wd_config.resizable(False, False)
        self.wd_config.configure(background=mc.background)
        self.wd_config.overrideredirect(1) #sin botones minimizar, etc
        # ICONO
        # self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        # self.wd_config.tk.call('wm', 'iconphoto', self.wd_config._w, self.img_icon)

        mc.in_window = 'config' # antes de instanciar la ventana, para que el color_config() corra correctamente
        self.wd_config.wd = Window_config(self.wd_config)
        self.wd_config.wd.pack(padx=20, pady=20)

        self.wd_config.protocol('WM_DELETE_WINDOW', self.config_on_closing)
        self.withdraw()  # esconde mainwindow
        self.wd_config.attributes("-topmost", True)

    def config_on_closing(self):
        print(f'{__name__}: config_on_closing()')
        mc.in_window = 'main'
        self.wd_config.destroy()
        self.deiconify()  # muestra nuevamente mainwindow

    def open_use(self):
        print(f'{__name__}: open_use()')
        self.wd_use = tk.Toplevel(self)
        if mc.use_advanced_mod:
            self.wd_use.title("Modo avanzado")
        else:
            self.wd_use.title("Modo simple")
        self.wd_use.geometry("%dx%d+%d+%d" % (mc.wd_with_use, mc.wd_hight_use, self.winfo_x()-40, self.winfo_y()-40))
#        self.wd_use.geometry(f'{mc.wd_with_use}x{mc.wd_hight_use}')
        self.set_position_use()
        self.wd_use.maxsize(mc.wd_with_use, mc.wd_hight_use)
        self.wd_use.minsize(mc.wd_with_use, mc.wd_hight_use)
        self.wd_use.resizable(False, False)
        self.wd_use.configure(background=mc.background)
        self.wd_use.overrideredirect(1) #sin botones minimizar, etc
        # ICONO
        # self.img_icon = ImageTk.PhotoImage(Image.open("../recursos/logo.jpg"))
        # self.wd_use.tk.call('wm', 'iconphoto', self.wd_use._w, self.img_icon)

        mc.in_window = 'use' # antes de instanciar la ventana, para que el color_use() corra correctamente
        self.wd_use.wd = Window_use(self.wd_use)
        self.wd_use.wd.pack(padx=20, pady=20)

        self.wd_use.protocol('WM_DELETE_WINDOW', self.use_on_closing)
        self.withdraw()  # esconde mainwindow
        self.wd_use.attributes("-topmost", True)

    def set_position_use(self):
            if mc.wd_position == 0:
                # coloca ventana en esquina superior derecha
                self.wd_use.geometry("+{}+{}".format(int(self.winfo_screenwidth()-mc.wd_with_use), int(0)))
            elif mc.wd_position == 1:
                # coloca ventana en el centro
                self.wd_use.geometry("+{}+{}".format(int(self.winfo_screenwidth()/2-mc.wd_with_use/2), int(self.winfo_screenheight()/2-mc.wd_hight_use/2)))
            elif mc.wd_position == 2:
                # coloca ventana en esquina inferior derecha
                self.wd_use.geometry("+{}+{}".format(int(self.winfo_screenwidth()-mc.wd_with_use), int(self.winfo_screenheight()-mc.wd_hight_use)))


    def use_on_closing(self):
        print(f'{__name__}: use_on_closing()')
        mc.in_window = 'main'
        self.wd_use.destroy()
        self.deiconify()  # muestra nuevamente mainwindow
