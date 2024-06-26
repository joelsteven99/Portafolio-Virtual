from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as tkagg, NavigationToolbar2Tk as toolbar
from matplotlib.animation import FuncAnimation as animation
from datetime import datetime
import customtkinter as ctk

#Funcion para crear entry's
def crear_entry(master, font, state = 'normal'):
    entry = ctk.CTkEntry(master, font = font, fg_color = '#D1BB9E', border_color = '#A79277', corner_radius = 15, text_color = '#76453B', state = state)
    return entry

#Funcion para crear botones
def crear_button(master, font, text, command):
    button = ctk.CTkButton(master, font = font, text = text, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', command = command)
    return button

#Funcion para crear label's
def crear_label(master, font, text):
    label = ctk.CTkLabel(master, font = font, fg_color = '#D1BB9E', corner_radius = 15, text_color = '#76453B', text = text, anchor='nw', justify='left')
    return label 

#Funcion para crear menus de opciones
def crear_option_menu(master, font, values):
    option_menu = ctk.CTkOptionMenu(master, font = font, button_color = '#EAD8C0', fg_color = '#EAD8C0', dropdown_font = font, dropdown_fg_color = '#EAD8C0', text_color = '#76453B', dropdown_text_color = '#76453B', corner_radius = 15, values = values, state = 'readonly')
    return option_menu

#Funcion para crear el menu superior
def crear_barra_menu(ventana):
    barra_menu = tk.Menu(ventana) #Crea el menu
    ventana.config(menu = barra_menu) #Agrega el menu a la ventana

    archivo = tk.Menu(barra_menu, tearoff = 0) #Crea la opcion de archivo
    barra_menu.add_cascade(label = "Archivo", menu = archivo) #Se le asigna un nombre y se agrega al menu
    archivo.add_command(label = "Salir", command = ventana.destroy) #Opcion Salir

    ajustes = tk.Menu(barra_menu, tearoff = 0) #Crea la opcion de ajustes
    barra_menu.add_cascade(label = "Ajustes", menu = ajustes) #Se le asigna un nombre y se agrega al menu
    ajustes.add_command(label = "Pantalla Completa",command = lambda:ventana.attributes('-fullscreen', True)) #Pone pantalla completa
    ajustes.add_command(label = "Pantalla normal",command = lambda:ventana.attributes('-fullscreen', False)) #Pone modo ventana

    matematicas_especiales = tk.Menu(barra_menu, tearoff = 0) #Crea la opcion de matematicas especiales
    barra_menu.add_cascade(label = "Matematicas Especiales", menu = matematicas_especiales) #Se le asigna un nombre y se agrega al menu
    matematicas_especiales.add_command(label = "Graficar", command = graficar) #Opcion de graficar
    matematicas_especiales.add_command(label = "Operaciones Basicas", command = operaciones_basicas) #Opcion de operaciones basicas
    matematicas_especiales.add_command(label = "Valor Absoluto", command = valor_absoluto) #Opcion de valor absoluto
    matematicas_especiales.add_command(label = "Conversión a Polar", command = polar) #Opcion de conversion a polar
    matematicas_especiales.add_command(label = "Operaciones Polares", command = operaciones_polares) #Opcion de operaciones polares
    matematicas_especiales.add_command(label = "Polinomio Complejo", command = polinomio_complejo) #Opcion polinomio complejo
    matematicas_especiales.add_command(label = "Funciones Complejas", command = funciones_complejas) #Opcion funciones complejas
    matematicas_especiales.add_command(label = "Limites de Funciones Complejas", command = limites) #Opcion de limites 
    matematicas_especiales.add_command(label = "Derivadas", command = derivadas) #Opcion de derivadas
    matematicas_especiales.add_command(label = "Numeros Complejos de Forma Exponencial", command = exponencial) #Opcion de exponencial
    matematicas_especiales.add_command(label = "Logaritmos", command = logaritmos) #Opcion de logaritmos
    matematicas_especiales.add_command(label = "Integración", command = integrales) #Opcion de integrales
    matematicas_especiales.add_command(label = "Trigonometricas Inversas", command = inversas) #Opcion de trigonometricas inversas
    matematicas_especiales.add_command(label = "Producto entre Funciones", command = producto) #Opcion de producto entre funciones
    matematicas_especiales.add_command(label = "Norma de Conjuntos Ortonormales", command = conjuntos) #Opcion de norma de conjuntos
    matematicas_especiales.add_command(label = "Series de Fourier", command = series) #Opcion de series de fourier
    matematicas_especiales.add_command(label = "Funciones Pares e Impares", command = par_impar) #Opcion de funciones pares e impares 

    ondas_senales = tk.Menu(barra_menu, tearoff = 0) #Crea la opcion de ondas y señales
    barra_menu.add_cascade(label = "Ondas y Señales", menu = ondas_senales) #Se le asigna un nombre y se agrega al menu
    ondas_senales.add_command(label = "Graficar Ondas", command = graficar_onda) #Opcion de graficar ondas
    ondas_senales.add_command(label = "Pendulo", command = pendulo) #Opcion de pendulo
    ondas_senales.add_command(label = "Resorte", command = resortes) #Opcion de resortes 
    ondas_senales.add_command(label = "Ecuaciones de Maxwell", command = maxwell) #Opcion de ecuaciones de maxwell

#Funcion para crear los botones, entrys, menus, etc
def crear_widgets(ventana):
    #Asignar de forma global los botnes, entrys, menus, etc. Para poder usarlo en otras partes del codigo
    global zona_entrada, boton_graficar, boton_calcular, zona_resultado, espacio_grafica, boton_borrar, opciones_polar, zona_historial, boton_decimal, opciones_exponencial, boton_pausa_reanudar
    
    fuente_letra = ctk.CTkFont(family = 'Consolas', size = 16) #Fuente de letra de los labels
    fuente_botones = ctk.CTkFont(family = 'Consolas', size = 14) #Fuente de letra de los botones

    boton_graficar = crear_button(ventana, fuente_botones, "Graficar", definir_grafico)
    boton_calcular = crear_button(ventana, fuente_botones, "Calcular", resolver)
    boton_decimal = crear_button(ventana, fuente_botones, "Decimal", decimal)
    zona_resultado = crear_entry(ventana, fuente_letra, state = 'readonly')
    zona_entrada = crear_entry(ventana, fuente_letra)
    espacio_grafica = crear_label(ventana, fuente_letra, "")
    boton_borrar = crear_button(ventana, fuente_botones, "Borrar", limpiar)
    opciones_polar = crear_option_menu(ventana, fuente_botones, ["Complejo/Polar", "Polar/Complejo"])
    opciones_exponencial = crear_option_menu(ventana, fuente_botones, ["Complejo/Exponencial", "Polar/Exponencial", "Exponencial/Complejo", "Exponencial/Polar"])
    zona_historial = crear_label(ventana, fuente_botones, "\n Creditos:\n Miguel Angel Ayala\n Jose Danilo Beltran\n Joel Steven Betancourt\n Juan Manuel Olave\n\n Leer la guia de usuario antes de usar la calculadora.\n\n Esta Calculadora esta bajo la proteccion de derechos intelectuales,\n cualquier copia de forma no autorizada esta prohibida.")
    boton_pausa_reanudar = crear_button(ventana, fuente_botones, "Pausa", pausar_reanudar)

#Funcion para mostrar y ubicar los entrys, botones, menus, etc. En la ventana
def mostrar_widgets():
    zona_entrada.place(relx = .02, rely = .02, relwidth = .4,relheight = .1)
    boton_graficar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)
    boton_calcular.place(relx = .03, rely = .15, relwidth = .05, relheight = .04)
    boton_decimal.place(relx = .09, rely = .15, relwidth = .05, relheight = .04)
    zona_resultado.place(relx = .02, rely = .22, relwidth = .4,relheight = .1)
    espacio_grafica.place(relx = .47, rely = .05, relwidth = .5, relheight = .85)
    boton_borrar.place(relx = .35, rely = .15, relwidth = .06, relheight = .04)
    opciones_polar.place(relx = .15, rely = .15, relwidth = .12, relheight = .04)
    opciones_exponencial.place(relx = .15, rely = .15, relwidth = .12, relheight = .04)
    zona_historial.place(relx = .02, rely = .4, relwidth = .4, relheight = .5)

#Funcion para ocultar los entrys, botones, menus, etc. En la ventana
def ocultar_widgets():  
    zona_entrada.place_forget()
    boton_graficar.place_forget()
    boton_calcular.place_forget()
    boton_decimal.place_forget()
    zona_resultado.place_forget()
    boton_borrar.place_forget()
    opciones_polar.place_forget()
    opciones_exponencial.place_forget()
    zona_historial.place_forget()
    boton_pausa_reanudar.place_forget()

#Funcion para la interfaz de calculo
def interfaz_defecto():
    ocultar_widgets()
    mostrar_widgets()
    limpiar()
    
    boton_graficar.place_forget()
    boton_decimal.place_forget()
    opciones_polar.place_forget()
    opciones_exponencial.place_forget()
    zona_resultado.configure(state = 'readonly')

#Funcion para la interfaz graficas 
def interfaz_graficas():
    ocultar_widgets()
    mostrar_widgets()
    limpiar()

    boton_decimal.place_forget()
    opciones_polar.place_forget()
    opciones_exponencial.place_forget()
    zona_entrada.place_forget()
    boton_calcular.place_forget()   
    boton_graficar.place(relx = .03, rely = .15, relwidth = .1, relheight = .04) #Mover el boton para graficar
    zona_resultado.place(relx = .02, rely = .02, relwidth = .4,relheight = .1) #Mover el entry donde se pone el resultado
    zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable

#Establecer la interfaz de graficas de funciones complejas
def graficar():
    ventana.title("Calculadora de Heinrich (Graficar)") #Cambiar el nombre de la ventana
    opcion.set("Graficar") #Define la opcion seleccionada del menu

    interfaz_graficas()

#Establecer la interfaz de operaciones basicas 
def operaciones_basicas():
    ventana.title("Calculadora de Heinrich (Operaciones Basicas)") #Cambiar el nombre de la ventana
    opcion.set("Operaciones Basicas")

    interfaz_defecto()

    boton_decimal.place(relx = .09, rely = .15, relwidth = .05, relheight = .04)
    boton_graficar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

#Establecer la interfaz de valor absoluto
def valor_absoluto():
    ventana.title("Calculadora de Heinrich (Valor Absoluto)") #Cambiar el nombre de la ventana
    opcion.set("Valor Absoluto") #Define la opcion seleccionada del menu

    interfaz_defecto()

    boton_decimal.place(relx = .09, rely = .15, relwidth = .05, relheight = .04)

#Establecer la interfaz de conversion a polar
def polar():
    ventana.title("Calculadora de Heinrich (Polar)") #Cambiar el nombre de la ventana
    opcion.set("Polar") #Define la opcion seleccionada del menu

    interfaz_defecto() 

    boton_graficar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)
    opciones_polar.place(relx = .15, rely = .15, relwidth = .12, relheight = .04)

#Establecer la interfaz de operaciones polares
def operaciones_polares():
    ventana.title("Calculadora de Heinrich (Operaciones Polares)") #Cambiar el nombre de la ventana
    opcion.set("Operaciones Polares") #Define la opcion seleccionada del menu

    interfaz_defecto()

    boton_graficar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

#Establecer la interfaz de polinomio complejo
def polinomio_complejo():
    ventana.title("Calculadora de Heinrich (Polinomio Complejo)") #Cambiar el nombre de la ventana
    opcion.set("Polinomio Complejo") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de funciones complejas
def funciones_complejas():
    ventana.title("Calculadora de Heinrich (Funciones Complejas)") #Cambiar el nombre de la ventana
    opcion.set("Funciones Complejas")

    interfaz_defecto()

#Establecer la interfaz de limites    
def limites():
    ventana.title("Calculadora de Heinrich (Limites de Funciones Complejas)")
    opcion.set("Limites")

    interfaz_defecto()

#Establecer la interfaz de derivadas
def derivadas():
    ventana.title("Calculadora de Heinrich (Derivadas)")
    opcion.set("Derivadas")

    interfaz_defecto()

#Establecer la interfaz de conversion a exponencial 
def exponencial():
    ventana.title("Calculadora de Heinrich (Exponencial)") #Cambiar el nombre de la ventana
    opcion.set("Exponencial") #Define la opcion seleccionada del menu

    interfaz_defecto() 

    opciones_exponencial.place(relx = .15, rely = .15, relwidth = .12, relheight = .04)

#Establecer la interfaz de logaritmos
def logaritmos():
    ventana.title("Calculadora de Heinrich (Logaritmos)") #Cambiar el nombre de la ventana
    opcion.set("Logaritmos") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de integrales
def integrales():
    ventana.title("Calculadora de Heinrich (Integrales)") #Cambiar el nombre de la ventana
    opcion.set("Integrales") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de trigonometricas inversas
def inversas():
    ventana.title("Calculadora de Heinrich (Trigonometricas Inversas)") #Cambiar el nombre de la ventana
    opcion.set("Inversas") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de producto entre funciones
def producto():
    ventana.title("Calculadora de Heinrich (Producto entre Funciones)") #Cambiar el nombre de la ventana
    opcion.set("Producto") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de normas de conjuntos
def conjuntos():
    ventana.title("Calculadora de Heinrich (Normas de Conjuntos Ortonormales)") #Cambiar el nombre de la ventana
    opcion.set("Conjuntos") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de series de fourier
def series():
    ventana.title("Calculadora de Heinrich (Series de Fourier)") #Cambiar el nombre de la ventana
    opcion.set("Series") #Define la opcion seleccionada del menu

    interfaz_defecto()

    boton_graficar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

#Establecer la interfaz de funciones pares e impares
def par_impar():
    ventana.title("Calculadora de Heinrich (Funciones Pares e Impares)") #Cambiar el nombre de la ventana
    opcion.set("Par_Impar") #Define la opcion seleccionada del menu

    interfaz_defecto()

#Establecer la interfaz de graficas de ondas
def graficar_onda():
    ventana.title("Calculadora de Heinrich (Graficar Ondas)") #Cambiar el nombre de la ventana
    opcion.set("Graficar Onda") #Define la opcion seleccionada del menu

    interfaz_graficas()

#Establecer la interfaz del pendulo
def pendulo():
    ventana.title("Calculadora de Heinrich (Pendulo)") #Cambiar el nombre de la ventana
    opcion.set("Pendulo") #Define la opcion seleccionada del menu

    interfaz_graficas()

    boton_pausa_reanudar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

def resortes():
    ventana.title("Calculadora de Heinrich (Resorte)") #Cambiar el nombre de la ventana
    opcion.set("Resorte") #Define la opcion seleccionada del menu

    interfaz_graficas()

    boton_pausa_reanudar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

def maxwell():
    ventana.title("Calculadora de Heinrich (Maxwell)") #Cambiar el nombre de la ventana
    opcion.set("Maxwell") #Define la opcion seleccionada del menu

    interfaz_graficas()

    boton_pausa_reanudar.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)


#Establecer la forma decimal en false
forma_decimal = False

#Funcion para pasar de forma simbolica a forma numerica
def decimal():
    global forma_decimal #Establecer de forma global el estadod e la forma decimal 
    entrada = zona_resultado.get() #Obtener el resultado
    entrada = str(entrada) #Convertirlo en un string
    verificar = verificar_simbolico(entrada) #Enviar el resultado para verificar si tiene opciones simbolicas

    if forma_decimal is False and verificar is True: #Si el resultado es simbolico y tiene funciones simbolicas
        forma_decimal = True #Establecer la forma decimal como verdadera

        entrada = sp.sympify(entrada) #Volver el resultado un funcion sympy
        entrada = entrada.evalf() #Evaluar el resultado para que sea numerico
        entrada = round(entrada, 4) #Redondear a 4 digitos el resultado
        entrada = str(entrada).replace(" ", "") #Convertir el resultado a un string y eliminar los espacios

        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, entrada) #Inserta el resultado
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
        boton_decimal.configure(text = "Simbolico") #Cambia el nombre del boton a simbolico
    elif forma_decimal is True: #Si esta en forma decimal 
        resolver() #Volver a resolver el ejercicio para que el resultado este en forma decimal

#Funcion para verificar si la entrada tiene funciones simbolicas copn el parametro: funcion
def verificar_simbolico(entrada):
    funciones_simbolicas = {"sin","cos","tan","log","ln","sqrt","/","e"} #Se crea un diccionario con funciones simbolicas

    for funcion in funciones_simbolicas: #Verificar en cada termino de la entrada si se encuentra una funcion del diccionario
        if funcion in entrada: #Si se encuentra una funcion
            return True #Regresar un verdadero 
    
    return False #En caso contrario regresar un falso

#Definir la funcion para ingresar el resultado con 4 parametros: funcion; theta; parte real; parte imaginaria
def ingresar_resultado(entrada, theta, entrada_real, entrada_imaginaria):
    #Si la opcion es polar y sea de la forma complejo/polar o si la opcion es de opciones polares o si la opcion es de exponencial y sea de la forma exponencial/polar
    if (opcion.get() == "Polar" and opciones_polar.get() == "Complejo/Polar") or opcion.get() == "Operaciones Polares" or (opcion.get() == "Exponencial" and opciones_exponencial.get() == "Exponencial/Polar"):
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, f'{entrada}*(cos({theta})+I*sin({theta}))') #Inserta el resultado de la forma r*(cos(theta)+i*sin(theta))
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable  
    #Si la opcion es exponencial y es de la forma exponencial/complejo
    elif opcion.get() == "Exponencial" and opciones_exponencial.get() != "Exponencial/Complejo":
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, f'{entrada}*e^(I*{theta})') #Inserta el resultado de la forma r*e^(i*theta)
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable  
    #Si la opcion es polinomio complejo o la opcion es funciones complejas
    elif opcion.get() == "Polinomio Complejo" or opcion.get() == "Funciones Complejas":
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, f'U = {entrada_real}  ;  V = {entrada_imaginaria}') #Inserta el resultado de la forma U = Parte real ; V = Parte compleja
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable 
    #Si la opcion es logaritmos
    elif opcion.get() == "Logaritmos":
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, f'ln({entrada})+I*({theta})') #Inserta el resultado de la forma ln(funcion)+i*theta
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable 
    #Si la opcion es producto entre funciones
    elif opcion.get() == "Producto":
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        if entrada == 0: #Si la integral es cero
            zona_resultado.insert(0, f'{entrada} ; Es ortogonal') #La funcion es ortogonal
        elif entrada != 0: #Si la integral no es cero
            zona_resultado.insert(0, f'{entrada} ; No es ortogonal') #La funcion no es ortogonal
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable  
    #Si no se cumplen ninguno de los anteriores
    else:
        zona_resultado.configure(state = 'normal') #Configura el entry del resultado para que sea editable
        zona_resultado.delete(0, 'end') #Elimina lo que haya en el entry
        zona_resultado.insert(0, entrada) #Inserta el resultado
        zona_resultado.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable

#Funcion de evaluar un complejo con un parametro: la funcion
def evaluar_complejo(entrada):
    entrada = sp.sympify(entrada) #Se convierte la entrada a una funcion de sympy
    parte_real = sp.re(entrada) #Se separa la parte real
    parte_imaginaria = sp.im(entrada) #Se separa la parte imaginaria

    return parte_real, parte_imaginaria #Se regresa una lista con los valores reales e imaginarios

#Funcion para evaluar theta con 2 parametros: theta; valor de pi
def evaluar_theta(theta, pi):
    theta = (theta + pi).evalf() #Evaluar el resultado para que sea numerico
    theta = round(theta, 4) #Redondear el resultado a 4 digitos
    return theta #Regresar el valor de theta de forma numerica

#Funcion para evaluar theta dependiendo del cuadrante con un parametro: funcion
def evaluar_cuadrantes(theta):
    if sp.im(theta) == 0: #Caso si la parte imaginaria vale cero
        theta = 0 #Theta vale cero
    elif sp.re(theta) == 0 and sp.im(theta) < 0: #Caso si la parte real es cero y la imaginaria es negativa
        theta = sp.atan(-sp.oo) #Calcular el arctan de menos infinito
        theta = evaluar_theta(theta, 2*sp.pi) #Sumar 2 pi a theta
    elif sp.re(theta) == 0 and sp.im(theta) > 0: #Caso si la parte real es cero y la imaginaria es positiva
        theta = sp.atan(sp.oo) #Calcular el arctan de infinito
        theta = evaluar_theta(theta, 0) #Sumar 0 a theta
    elif sp.re(theta) > 0 and sp.im(theta) > 0: #Caso si la parte real e imaginaria son positivas
        theta = sp.atan(sp.im(theta)/sp.re(theta)) #Calcular el arctan
        theta = evaluar_theta(theta, 0) #Sumar 0 a theta
    elif sp.re(theta) < 0 and sp.im(theta) < 0: #Caso si la parte real e imaginaria son negativas
        theta = sp.atan(sp.im(theta)/sp.re(theta)) #Calcular el arctan
        theta = evaluar_theta(theta, sp.pi) #Sumar pi a theta
    elif sp.re(theta) < 0 and sp.im(theta) > 0: #Caso si la parte real es negativa y la imaginaria positiva
        theta = sp.atan(sp.im(theta)/sp.re(theta)) #Calcular el arctan
        theta = evaluar_theta(theta, sp.pi) #Sumar pi a theta
    elif sp.re(theta) > 0 and sp.im(theta) < 0: #Caso si la parte real es positiva y la imaginaria negativa
        theta = sp.atan(sp.im(theta)/sp.re(theta)) #Calcular el arctan
        theta = evaluar_theta(theta, 2*sp.pi) #Sumar 2 pi a theta

    return theta #Regresar el valor de theta

#Funcion que hace los calculos
def resolver():
    global forma_decimal 
    seleccion_menu = opcion.get() #Obtener la opcion escogida en el menu
    forma_decimal = False #Establecer la forma decimal en false
    boton_decimal.configure(text = "Decimal") #Poner el texto del boton decimal
    entrada = zona_entrada.get() #Obtener la funcion de la zona de entrada
    
    if seleccion_menu == "Operaciones Basicas":
        #(4+8*I)+(3+8*I)
        try:   
            entrada = entrada.replace("^", "**") #Cambiar el signo de la potencia
            x = evaluar_complejo(entrada) #Evaluar los complejos y operarlos
            entrada = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
            entrada = str(entrada).replace(" ", "") #Convertir la funcion en un string y eliminar los espacios

            ingresar_resultado(entrada, None, None, None) #Ingresar el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Valor Absoluto":
        #(5+8*I)
        try:
            entrada = entrada.replace("^", "**") #Cambiar el signo de la potencia
            x = evaluar_complejo(entrada) #Evaluar el complejo y extraer la parte real y la imaginaria
            entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
            entrada = str(entrada).replace(" ", "") #Convertir la funcion en un string y eliminar los espacios
            
            ingresar_resultado(entrada, None, None, None) #Ingresar el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Polar":
        if opciones_polar.get() == "Complejo/Polar":
            try:
                #1+sqrt(3)*I
                entrada = entrada.replace("^", "**") #Cambiar el signo de la potencia
                x = evaluar_complejo(entrada) #Evaluar el complejo y extraer la parte real y la imaginaria
                entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
                funcion_reconstruida = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
                theta = evaluar_cuadrantes(funcion_reconstruida) #Evaluar theta
                entrada = str(entrada).replace(" ", "") #Convertir la funcion en un string y eliminar los espacios
                               
                ingresar_resultado(entrada, theta, None, None) #Ingresar el resultado
                
                return theta #Regresar el valor de theta
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
        elif opciones_polar.get() == "Polar/Complejo":
            #3*(cos(pi)+I*sin(pi))
            try:
                entrada = entrada.replace("^", "**") #Cambiar el signo de la potencia
                x = evaluar_complejo(entrada) #Evaluar el complejo y extraer la parte real y la imaginaria             
                entrada = round(x[0], 4) + round(x[1], 4) * sp.I #Juntar la parte real y la imaginaria redondeadas a 4 digitos
                entrada = str(entrada).replace(" ", "") #Convertir la funcion en un string y eliminar los espacios

                ingresar_resultado(entrada, None, None, None) #Ingresar el resultado
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Operaciones Polares":
        #2*(cos(pi/4)+I*sin(pi/4))+3*(cos(pi)+I*sin(pi))
        try:
            entrada = entrada.replace("^", "**") #Cambiar el signo de la potencia
            x = evaluar_complejo(entrada) #Evaluar el complejo y extraer la parte real y la imaginaria 
            entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
            entrada = round(entrada.evalf(), 4) #Evaluar r y redondearlo a 4 digitos
            funcion_reconstruida = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
            theta = evaluar_cuadrantes(funcion_reconstruida) #Evaluar theta
            entrada = str(entrada).replace(" ", "") #Convertir la funcion en un string y eliminar los espacios
                            
            ingresar_resultado(entrada, theta, None, None) #Ingresar el resultado

            return theta #Regresar el valor de theta
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Polinomio Complejo":
        #x+y*I ; z^2
        try:
            entrada = entrada.replace("^", "**").split(";") #Convertir el simbolo de la potencia y separar los terminos
            z = entrada[0] #Guardar el valor de la funcion de z
            polinomio = entrada[1] #Guardar el valor del polinomio
            polinomio = polinomio.replace("z", f'({z})') #Reemplazar el polinomio en cada z de la funcion 
            polinomio = sp.sympify(polinomio) #Convertir a sympy y resolver
            polinomio = sp.expand(polinomio) #Expandir la expresion
            polinomio = polinomio.as_ordered_terms() #Separar cada termino de la funcion (crea una lista)
            parte_real = 0 #Crear una variable donde se guardara los terminos reales
            parte_imaginaria = 0 #Crear una variable donde se guardara los terminos imaginarios

            for termino in polinomio: #Verificar los terminos de la lista
                if termino.has(sp.I): #Si el termino es imaginario
                    parte_imaginaria += termino #Lo guarda en la variable imaginaria
                else: #Si el termino no es imaginario
                    parte_real += termino #Lo guarda en la variable real

            parte_real = str(parte_real).replace("**", "^").replace(" ", "") #Vuelve la variable real un string, cambia el signo de la potencia y elimina los espacios
            parte_imaginaria = str(parte_imaginaria).replace("**", "^").replace(" ", "") #Vuelve la variable imaginaria un string, cambia el signo de la potencia y elimina los espacios

            ingresar_resultado(None, None, parte_real, parte_imaginaria) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Funciones Complejas":
        #z^2
        try:
            x, y = sp.symbols('x, y') #Crea los simbolos de x y y
            z = x + y * sp.I #Crea la funcion z
            entrada = entrada.replace("^", "**").replace("z", f'({z})') #Cambia el signo de la potencia y reemplaza z en la funcion
            entrada = sp.sympify(entrada) #Convertir a sympy y resolver
            entrada = sp.expand(entrada) #Expandir la expresion
            entrada = entrada.as_ordered_terms() #Separar cada termino de la funcion (crea una lista)
            parte_real = 0 #Crear una variable donde se guardara los terminos reales
            parte_imaginaria = 0 #Crear una variable donde se guardara los terminos imaginarios

            for termino in entrada: #Verificar los terminos de la lista
                if termino.has(sp.I): #Si el termino es imaginario
                    parte_imaginaria += termino #Lo guarda en la variable imaginaria
                else: #Si el termino no es imaginario
                    parte_real += termino #Lo guarda en la variable real

            parte_real = str(parte_real).replace("**", "^").replace(" ", "") #Vuelve la variable real un string, cambia el signo de la potencia y elimina los espacios
            parte_imaginaria = str(parte_imaginaria).replace("**", "^").replace(" ", "") #Vuelve la variable imaginaria un string, cambia el signo de la potencia y elimina los espacios

            ingresar_resultado(None, None, parte_real, parte_imaginaria) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Limites":
        #z^2+2*z ; 1
        try:
            x, y = sp.symbols('x, y') #Crea los simbolos de x y y
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            z = x + y * sp.I #Crea la funcion z
            funcion = entrada[0].replace("z", f'({z})') #Reemplaza z en la funcion
            lim = entrada[1] #Establece los limites
            limite_z = sp.limit(funcion, x, lim) #Realiza el limite respecto a la variable x
            limite_z = sp.limit(limite_z, y, lim) #Realiza el limite respecto a la variable y
            limite_z = sp.expand(limite_z) #Expande el resultado
            limite_z = str(limite_z).replace(" ", "") #Convertir el resultado en un string y eliminar los espacios

            ingresar_resultado(limite_z, None, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Derivadas":
        #8^4+sin(z)-8^3
        try:
            z = sp.symbols('z') #Crea el simbolo de z
            entrada = entrada.replace("^", "**") #Cambia el signo de la potencia
            entrada = sp.sympify(entrada) #Convertir a sympy y resolver
            entrada = sp.diff(entrada, z) #Realizar la derivada con respecto a z
            entrada = str(entrada).replace("**", "^").replace(" ", "") #Cambia el signo de la potencia del resultado y elimina los espacios

            ingresar_resultado(entrada, None, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Exponencial":
        if opciones_exponencial.get() == "Complejo/Exponencial":
            #-sqrt(2)+sqrt(2)*I
            try:
                x = evaluar_complejo(entrada) #Evaluar el complejo y extraer la parte real y la imaginaria 
                entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
                funcion_reconstruida = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
                theta = evaluar_cuadrantes(funcion_reconstruida) #Evaluar theta
                entrada = str(entrada).replace(" ", "") #Convertir el resultado en un string y eliminar los espacios

                ingresar_resultado(entrada, theta, None, None) #Ingresa el resultado
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
        elif opciones_exponencial.get() == "Polar/Exponencial":
            #2*(cos(pi/4)+I*sin(pi/4))
            try:
                x = evaluar_complejo(entrada) #Evaluar el polar y extraer la parte real y la imaginaria              
                entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
                funcion_reconstruida = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
                theta = evaluar_cuadrantes(funcion_reconstruida) #Evaluar theta
                entrada = str(entrada).replace(" ", "") #Convertir el resultado en un string y eliminar los espacios

                ingresar_resultado(entrada, theta, None, None) #Ingresa el resultado
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
        elif opciones_exponencial.get() == "Exponencial/Polar":
            #2*e^(I*0.7854)
            try:
                entrada = entrada.replace(")", "") #Elimina el parentesis queda asi r*e^(i*theta
                entrada = entrada.split("*e^(I*") #Separa la funcion quedando a parte r y theta
                theta = entrada[1] #Guarda theta
                entrada = entrada[0] #Guarda r

                ingresar_resultado(entrada, theta, None, None) #Ingresa el resultado
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
        elif opciones_exponencial.get() == "Exponencial/Complejo":
            #2*e^(I*0.7854)
            try:            
                entrada = entrada.replace(")", "") #Elimina el parentesis queda asi r*e^(i*theta
                entrada = entrada.split("*e^(I*") #Separa la funcion quedando a parte r y theta
                theta = entrada[1] #Guarda theta
                entrada = entrada[0] #Guarda r
                entrada = f"{entrada}*(cos({theta})+I*sin({theta}))" #Recrea la funcion polar con r y theta
                x = evaluar_complejo(entrada) #Resuelve la funcion polar para pasar a una funcion compleja
                funcion_reconstruida = round(x[0], 4) + round(x[1], 4) * sp.I #Juntar la parte real y la imaginaria redondeadas a 4 digitos
                entrada = str(funcion_reconstruida).replace(" ", "") #Convertir el resultado en un string y eliminar los espacios

                ingresar_resultado(entrada, None, None, None) #Ingresa el resultado
            except Exception as e:
                messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Logaritmos":
        #-1-1*I ; 0
        try:
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            x = evaluar_complejo(entrada[0]) #Evaluar la funcion y extraer la parte real y la imaginaria
            n = int(entrada[1]) #Guardar n
            entrada = sp.sqrt(x[0]**2 + x[1]**2) #Sacar la raiz de la parte real al cuadrado mas la parte imaginaria al cuadrado
            funcion_reconstruida = x[0] + x[1] * sp.I #Juntar la parte real y la imaginaria
            theta = evaluar_cuadrantes(funcion_reconstruida) #Evaluar theta
            entrada = str(entrada).replace(" ", "") #Convertir el resultado en un string y elimina los espacios
            parte_angular = round((theta + 2 * sp.pi * n).evalf(), 4) #Calcular la parte angular del logaritmo

            ingresar_resultado(entrada, parte_angular, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Integrales":
        #3*t+2*I ; 20, 2
        try:
            t = sp.symbols('t') #Crea el simbolo de t
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            funcion = entrada[0] #Guarda la funcion
            limites = entrada[1].split(",") #Guarda los limite y los separa
            limite_superior = limites[0] #Guarda el limite superior
            limite_inferior = limites[1] #Guarda el limite inferior

            integral = sp.integrate(funcion, (t, limite_inferior, limite_superior)) #Realiza la integral definida

            ingresar_resultado(integral, None, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Inversas":       
        #sin^-1(sqrt(5))
        #cos^-1(sqrt(5))
        #tan^-1(4^5) 
        try:      
            if "sin^-1" in entrada:
                z = entrada.replace("sin^-1", "").replace("^", "**") #Elimina la funcion trigonometrica para obtener z y cambia el signo de la potencia
                arcsin = "sqrt(1-z**2)+z*I" #Crea la funcion de la funcion trigonometrica inversa
                arcsin = arcsin.replace("z", f'({z})') #Reemplaza z en la funcion
                arcsin = sp.sympify(arcsin) #Convierte la entrada a sympy y la resuelve
                arcsin = str(arcsin).replace(" ", "") #Convertir el resultado en un string y elimina los espacios
                arcsin = f'-I*ln({arcsin})' #Crea el resultado final
                
                ingresar_resultado(arcsin, None, None, None) #Ingresa el resultado
            if "cos^-1" in entrada:
                z = entrada.replace("cos^-1", "").replace("^", "**") #Elimina la funcion trigonometrica para obtener z y cambia el signo de la potencia
                arccos = "z+sqrt(z**2-1)" #Crea la funcion de la funcion trigonometrica inversa
                arccos = arccos.replace("z", f'({z})') #Reemplaza z en la funcion
                arccos = sp.sympify(arccos) #Convierte la entrada a sympy y la resuelve
                arccos = str(arccos).replace(" ", "") #Convertir el resultado en un string y elimina los espacios
                arccos = f'-I*ln({arccos})' #Crea el resultado final
                
                ingresar_resultado(arccos, None, None, None) #Ingresa el resultado
            if "tan^-1" in entrada:
                z = entrada.replace("tan^-1", "").replace("^", "**") #Elimina la funcion trigonometrica para obtener z y cambia el signo de la potencia
                arctan = "(I+z)/(I-z)" #Crea la funcion de la funcion trigonometrica inversa
                arctan = arctan.replace("z", f'({z})') #Reemplaza z en la funcion
                arctan = sp.sympify(arctan) #Convierte la entrada a sympy y la resuelve
                arctan = str(arctan).replace(" ", "") #Convertir el resultado en un string y elimina los espacios
                arctan = f'I/2*ln({arctan})' #Crea el resultado final
                
                ingresar_resultado(arctan, None, None, None) #Ingresa el resultado   
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Producto":
        #x, x^2 ; -1, 1
        try:
            x = sp.symbols('x') #Crea el simbolo de x
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            funcion = entrada[0].split(",") #Guarda la funcion y separa las funciones
            primera_funcion = funcion[0] #Guarda la primera funcion
            segunda_funcion = funcion[1] #Guarda la segunda funcion
            funcion = f'{primera_funcion}*{segunda_funcion}' #Crea la multiplicacion de las dos funciones
            funcion = sp.sympify(funcion) #Pasa la funcion a sympy y la resuelve
            limites = entrada[1].split(",") #Guarda los limite y los separa
            limite_inferior = limites[0] #Guarda el limite inferior
            limite_superior = limites[1] #Guarda el limite superior

            integral = sp.integrate(funcion, (x, limite_inferior, limite_superior)) #Realiza la integral definida

            ingresar_resultado(integral, None, None, None) #Ingresa el resultado  
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Conjuntos":   
        #x ; -pi, pi
        try:
            x = sp.symbols('x') #Crea el simbolo de x     
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            funcion = entrada[0] #Guarda la funcion
            funcion = f'{funcion}**2' #Crea la potencia de la funcion
            funcion = sp.sympify(funcion) #Pasa la funcion a sympy y la resuelve
            limites = entrada[1].split(",") #Guarda los limites y los separa
            limite_inferior = limites[0] #Guarda el limite inferior
            limite_superior = limites[1] #Guarda el limite superior

            integral = sp.integrate(funcion, (x, limite_inferior, limite_superior)) #Realiza la integral definida
            integral = str(integral).replace("**", "^") #Convierte el resultado en un string y cambia el signo de la potencia
            integral = f'sqrt({integral})' #Crea la funcion final encerrando el resultado en una raiz

            ingresar_resultado(integral, None, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Series":
        #x ; -pi, pi ; 3
        try:
            x = sp.symbols('x') #Crea el simbolo de x        
            entrada = entrada.replace("^", "**").split(";") #Cambia el signo de la potencia y separa las variables
            funcion = sp.sympify(entrada[0]) #Guarda la funcion y la convierte en sympy
            limites = entrada[1].split(",") #Guarda los limites y los separa
            limite_inferior = limites[0] #Guarda el limite inferior
            limite_superior = limites[1] #Guarda el limite superior
            intervalos = int(entrada[2]) #Define el numero de intervalos

            serie = sp.fourier_series(funcion, (x, limite_inferior, limite_superior)) #Realiza la serie de fourier
            serie = serie.truncate(n = intervalos) #Evalua la serie hasta n intervalos
            series = str(serie).replace(" ", "").replace("**", "^") #Pasa la funcion a string y cambia el signo de la potencia y elimina los espacios

            ingresar_resultado(series, None, None, None) #Ingresa el resultado

            limite_inferior = sp.sympify(limite_inferior).evalf() #Pasa los limites a sympy y los convierte a forma numerica
            limite_superior = sp.sympify(limite_superior).evalf() #Pasa los limites a sympy y los convierte a forma numerica

            return serie, x, limite_inferior, limite_superior #Regresa los valores de la serie, x, el limite inferior, el limite superior
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
    elif seleccion_menu == "Par_Impar":
        #x^2
        try:
            #Se verifica a traves de la regla f(x) = f(-x)
            valor_1 = 2 #Se define un valor x
            valor_2 = -2 #Se define un valor -x
            primera_funcion = entrada.replace("^", "**").replace("x", f'({valor_1})') #Se reemplaza el valor en x de la funcion
            primera_funcion = sp.sympify(primera_funcion) #Convierte la funcion a sympy y la resuelve
            segunda_funcion = entrada.replace("^", "**").replace("x", f'({valor_2})') #Se reemplaza el valor en x de la funcion
            segunda_funcion = sp.sympify(segunda_funcion) #Convierte la funcion a sympy y la resuelve

            if primera_funcion == segunda_funcion: #Si ambos resultados son iguales 
                funcion = "Es par" #La funcion es par
            elif primera_funcion != segunda_funcion: #Si ambos resultado son diferentes
                funcion = "Es impar" #La funcion es impar

            ingresar_resultado(funcion, None, None, None) #Ingresa el resultado
        except Exception as e:
            messagebox.showerror('Error', f'{e}')
              
def limpiar():  
    try:
        boton_decimal.configure(text = 'Decimal') #Configuar el texto del boton de decimal
        zona_entrada.delete(0, 'end') #Borrar lo que haya en la zona de entrada
        zona_resultado.configure(state = 'normal') #Configuar la zona de resultado para que sea editable
        zona_resultado.delete(0, 'end') #Borrar lo que haya en la zona de resultado
        if opcion.get() != "Graficar" or opcion.get() != "Graficar Onda" or opcion.get() != "Pendulo": #Si la opcion del menu es diferente a alguna de unicamente grafico 
            zona_resultado.configure(state = 'readonly') #Configuar la zona de resultado para que no sea editable
        eliminar_canvas() #Llama la funcion para eliminar el grafico
    except Exception as e:
        messagebox.showerror('Error', f'{e}')

global pausado #Variable global para pausar
pausado = False #Establecer el pausado en false

#Funcion para pausar animaciones
def pausar_reanudar():
    global pausado

    if pausado == False: #Si no esta pausada la animacion
        ani.pause() #Pausa la animacion
        pausado = True #Establece que la animacion esta pausada
        boton_pausa_reanudar.configure(text = "Reanudar") #Cambia el texto del boton
    elif pausado == True: #Si esta pausada la animacion
        ani.resume() #Reanuda la animacion
        pausado = False #Establece que la animacion no esta pausada 
        boton_pausa_reanudar.configure(text = "Pausar") #Cambia el texto del boton


def borrar_historial():
    pass

#Definir la funcion para eliminar el grafico
def eliminar_canvas():
    #En caso de que no se haya creado, evitar que se crashee
    try:
        canvas.get_tk_widget().destroy() #Eliminar el grafico
        barra_herramientas.destroy() #Eliminar la barra de herramientas
        plt.clf()
    except Exception:
        pass #En caso de que no haya grafica que no haga nada

#Definir el grafico que se va a realizar
def definir_grafico():
    eliminar_canvas() #Eliminar cualquier grafico anterior
    
    entrada = zona_resultado.get() #Obtener el resultado
    entrada_polar = zona_entrada.get() #Obtener el resultado de funciones polares

    if opcion.get() == "Graficar" or opcion.get() == "Operaciones Basicas": #Si la opcion es graficar o operaciones basicas
        funcion = evaluar_complejo(entrada) #Evalua el resultado para obtener la parte real y la imaginaria
        realizar_grafico() #Crear el grafico
        grafico(funcion, entrada) #Crear la funcion en el grafico
    elif opcion.get() == "Polar":
        if opciones_polar.get() == "Complejo/Polar": #Si la opcion es complejo/polar
            funcion = evaluar_complejo(entrada_polar) #Evalua el resultado para obtener la parte real y la imaginaria
            theta = resolver() #Obtiene el valor de theta
            realizar_grafico() #Crear el grafico
            grafico_polar(funcion, entrada, theta) #Crear la funcion en el grafico
        elif opciones_polar.get() == "Polar/Complejo": #Si la opcion es polar/complejo
            funcion = evaluar_complejo(entrada) #Evalua el resultado para obtener la parte real y la imaginaria
            realizar_grafico() #Crear el grafico
            grafico_polar(funcion, entrada) #Crear la funcion en el grafico
    elif opcion.get() == "Operaciones Polares": #Si la opcion es operaciones polares
        funcion = evaluar_complejo(entrada) #Evalua el resultado para obtener la parte real y la imaginaria
        theta = resolver() #Obtiene el valor de theta
        realizar_grafico() #Crear el grafico
        grafico_polar(funcion, entrada, theta) #Crea la funcion en el grafico
    elif opcion.get() == "Series": #Si la opcion es series de fourier
        funcion = resolver() #Obtiene la serie de fourier
        realizar_grafico() #Crear el grafico
        grafico_fourier(funcion[0], funcion[1], funcion[2], funcion[3]) #Crea la funcion en el grafico
    elif opcion.get() == "Graficar Onda": #Si la opcion es graficar onda
        realizar_grafico() #Crear el grafico
        grafico_ondas() #Crea la funcion en el grafico
    elif opcion.get() == "Pendulo": #Si la opcion es pendulo
        grafico_pendulo() #Crea la funcion del pendulo
    elif opcion.get() == "Resorte":
        grafico_resorte()
    elif opcion.get() == "Maxwell":
        grafico_maxwell()
        
def realizar_grafico():  
    global canvas, barra_herramientas #Variable global para controlar el grafico y la barra de herramientas desde cualquier parte del codigo

    plt.rc('font', family = 'sans-serif', size = 5.5) #Cambiar la fuente de todo el grafico y el tamanio
    plt.subplot().spines['left'].set_position('zero') #Poner la margen izquierda en el centro y hacer que no se mueva
    plt.subplot().spines['bottom'].set_position('zero') #Poner la margen inferior en el centro y hacer que no se mueva
    plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
    plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
    plt.xlim(-15.5, 15.5) #Limitar el eje x entre -15.5 y 15.5
    plt.ylim(-15.5, 15.5) # Limitar el eje y entre -15.5 y 15.5
    plt.subplot().set_aspect('equal', adjustable = 'box') #Hacer que el aspecto entre los puntos del eje x y y sean completamente simetricas
    plt.tight_layout() #Ajustar la grafica al tamanio del cuadro
    plt.grid(True, alpha = 0.4) #Crear la rejila
    plt.axvline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje x
    plt.axhline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje y
    canvas = tkagg(plt.gcf(), master = ventana) #Crear un canvas con el grafico del matplolib
    barra_herramientas = toolbar(canvas, ventana) #Crear una barra de herramientas
    barra_herramientas.update() #Llama a la barra de herramientas
    canvas.get_tk_widget().place(relx = .47, rely = .05, relwidth = .5, relheight = .85) #Ubica el canvas en la ventana   
    barra_herramientas.place(relx = .47, rely = .9, relwidth = .5, relheight = .05) #Ubica la barra de herramientas en la ventana
    canvas.draw() #Dibuja el canvas en la ventana

def grafico(funcion, entrada):
    parte_real = float(funcion[0]) #Guardar la parte real que es el valor x
    parte_imaginaria = float(funcion[1]) #Guardar la parte imaginaria que es el valor y
    plt.quiver(0, 0, parte_real, parte_imaginaria, color = "black", angles = 'xy', scale_units = 'xy', scale = 1, width = 0.002) #Ubicar la funcion en el plano
    plt.plot([0, -parte_real], [0, -parte_imaginaria], color = "white", alpha = 0) #Ubicar la funcion en el plano pero en el otro eje, de manera invisible para hacer visible los otros 3 ejes
    plt.plot([0, parte_real], [parte_imaginaria, parte_imaginaria], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje x hasta el punto 
    plt.plot([parte_real, parte_real], [0, parte_imaginaria], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje y hasta el punto

    #Ubica el texto en la funcion (la ubicacion del texto dependiendo del cuadrante)
    if parte_real > 0 and parte_imaginaria > 0:
        plt.text(parte_real, parte_imaginaria, f'  {entrada}', verticalalignment = 'bottom', horizontalalignment = 'left')

    if parte_real < 0 and parte_imaginaria > 0:
        plt.text(parte_real, parte_imaginaria, f'{entrada}  ', verticalalignment = 'bottom', horizontalalignment = 'right')

    if parte_real < 0 and parte_imaginaria < 0:
        plt.text(parte_real, parte_imaginaria, f'{entrada}  ', verticalalignment = 'top', horizontalalignment = 'right')

    if parte_real > 0 and parte_imaginaria < 0:
        plt.text(parte_real, parte_imaginaria, f'  {entrada}', verticalalignment = 'top', horizontalalignment = 'left')

def grafico_fourier(funcion, x, limite_inferior, limite_superior):
    valores_x = np.linspace(float(limite_inferior), float(limite_superior), 200) #Crear una lista de 200 valores entre el limite inferior y superior
    valores_y = [funcion.subs(x, val) for val in valores_x] #Evaluar la serie de fourier en cada uno de los 200 valores
    
    plt.plot(valores_x, valores_y, color = 'black') #Graficar
        
def grafico_polar(funcion, entrada, theta):   
    parte_real = float(funcion[0]) #Guardar la parte real que es el valor x
    parte_imaginaria = float(funcion[1]) #Guardar la parte imaginaria que es el valor y
    plt.quiver(0, 0, parte_real, parte_imaginaria, color = "black", angles = 'xy', scale_units = 'xy', scale = 1, width = 0.002) #Ubicar la funcion en el plano
    plt.plot([0, -parte_real], [0, -parte_imaginaria], color = "white", alpha = 0) #Ubicar la funcion en el plano pero en el otro eje, de manera invisible para hacer visible los otros 3 ejes
    plt.plot([0, parte_real], [parte_imaginaria, parte_imaginaria], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje x hasta el punto 
    plt.plot([parte_real,parte_real], [0, parte_imaginaria], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje y hasta el punto

     #Ubica el texto en la funcion (la ubicacion del texto dependiendo del cuadrante)
    if parte_real > 0 and parte_imaginaria > 0:
        plt.text(parte_real, parte_imaginaria, f'  {entrada}', verticalalignment = 'bottom', horizontalalignment = 'left')

    if parte_real < 0 and parte_imaginaria > 0:
        plt.text(parte_real, parte_imaginaria, f'{entrada}  ', verticalalignment = 'bottom', horizontalalignment = 'right')

    if parte_real < 0 and parte_imaginaria < 0:
        plt.text(parte_real, parte_imaginaria, f'{entrada}  ', verticalalignment = 'top', horizontalalignment = 'right')

    if parte_real > 0 and parte_imaginaria < 0:
        plt.text(parte_real, parte_imaginaria, f'  {entrada}', verticalalignment = 'top', horizontalalignment = 'left')

    if opciones_polar.get() == "Complejo/Polar": #Si la opcion es para graficar una funcion polar
        if parte_real < 3 or parte_imaginaria < 3: #Si es pequeño el vector osea menor que 3
            valor_menor = min(parte_real, parte_imaginaria) #Se elige el valor menor entre el real y el imaginario
            radio = valor_menor * 0.4 #Se obtiene el 40% de ese valor
        else: #Si el vector no es pequeño osea mayor que 3
            radio = 1.6 #El radio sera fijo
                                                
        punto_inicio = 0 #Establece el punto de inicio
        theta = float(theta.evalf()) #Se evalua el valor de theta de forma numerica
        theta = round(theta, 2) #Se redondea a 2 digitos
        angulo = np.linspace(0, theta , 50) #Se crean 50 puntos entre 0 y theta
        angulo_ejex = punto_inicio + radio * np.cos(angulo) #Se calculan 50 puntos creando los valores de x para el radio
        angulo_ejey = punto_inicio + radio * np.sin(angulo) #Se calculan 50 puntos creando los valores de y para el radio

        plt.plot(angulo_ejex, angulo_ejey, color = 'red', linewidth = 0.8) #Se grafica el angulo del vector

def grafico_ondas():
    x = sp.symbols('x') #Se define el simbolo x
    funcion = zona_resultado.get().replace("^", "**") #Se cambia el signo de potencia
    funcion = sp.sympify(funcion) #Se convierte en funcion sympy
    valoresx = np.linspace(-100, 100, 1000) #Se crean 1000 puntos entre -100 y 100
    valoresy = [funcion.subs(x, val) for val in valoresx] #Se evaluan los 1000 puntos en la funcion
    
    plt.plot(valoresx, valoresy, color = 'black') #Se grafica la funcion
    
def grafico_pendulo():
    #Parámetros del péndulo: longitud ; ángulo inicial
    #10; 90
    
    global ani #Se establece la animacion de forma global para poder manipularlo en otras partes del codigo

    entrada = zona_resultado.get().split(";") #Se separan los parametros
    longitud = float(entrada[0]) #Se guarda la longitud
    gravedad = 9.8 #Se establece el valor de la gravedad
    angulo_inicial = float(entrada[1]) / 100 #Se establece el angulo de incio (en grados)

    if angulo_inicial > 0.9: #Si el angulo es mayor a 90 grados
        messagebox.showerror('Error', "Angulos menores a 90 grados") #Lanzar un error y evitar graficar
    else: #Si es igual o menor a 90 grados
        realizar_grafico() #Crear el grafico

        amortiguamiento = 0.1 #Establece el amortiguamiento

        tiempo_de_simulacion = 3600 #Establecer la duracion de la simulacion (en segundos)
        paso_de_tiempo = 0.01  #Establecer el paso del tiempo (en segundos)
        t = np.arange(0, tiempo_de_simulacion, paso_de_tiempo) #Crear una lista desde 0 hasta el tiempo de simulacion, con valores de un intervalo del paso del tiempo

        theta = angulo_inicial * np.exp(-amortiguamiento * t) * np.cos(np.sqrt(gravedad / longitud - amortiguamiento**2) * t) #Calcular la ecuacion teniendo en cuenta el paso del tiempo y el amortiguamento

        x = longitud * np.sin(theta) #Calcula los puntos del eje x para la curva, teniendo en cuenta el resultado de la ecuacion
        y = -longitud * np.cos(theta) #Calcula los puntos del eje y para la curva, teniendo en cuenta el resultado de la ecuacion

        linea, = plt.plot([], [], 'o-', color = 'black', linewidth = 2) #Crear la linea o el pendulo, los [], [], son los valores de x y y que van variando
        plt.xlim(-15, 15) #Limitar el eje x desde -15.5 a 15.5
        plt.ylim(-27, 0.5) # Limitar el eje y dese -27.5 a 0.5

        #Definir la funcion de inicio
        def init():
            linea.set_data([], []) #Establecer los datos para la grafica
            return linea, #Regresar los datos para graficarlos

        #Definir la funcion para actualizar
        def update(frame):
            linea.set_data([0, x[frame]], [0, y[frame]]) #Establecer los datos para la grafica, que iran cambiando cada frame
            return linea, #Regresar los datos para graficarlos

        #Crear la animacion
        ani = animation(plt.gcf(), update, frames = 2000, init_func = init, blit = True, interval = paso_de_tiempo * 1000)
        #va asi animation(figura, funcion de actualizacion, cuantas veces se hace, funcion de inicio, blit hace que se dibujen solamente las partes que han cambiado, el intervalo entre cada frame (en segundos))
        canvas.draw() #Dibujar la grafica

def grafico_resorte():
    #3; 1; 5; 0; 20
    #Longitud; Masa; Posicion inicial; Velocidad inicial; Constante elastica
    
    global ani #Se establece la animacion de forma global para poder manipularlo en otras partes del codigo

    realizar_grafico() #Realizar la plantilla para el grafico

    entrada = zona_resultado.get().split(";") #Separar los parametros

    masa = float(entrada[1]) #Masa kg
    constante_elastica = float(entrada[4]) #Constante elastica
    posicion_inicial = float(entrada[2]) #Posicion inicial 
    velocidad_inicial = float(entrada[3]) #Velocidad inicial
    longitud = float(entrada[0]) #Longitud
    tiempo_inicial = 0 #Tiempo inicial

    amortiguamento = 0.1 #Amortiguamiento

    omega = np.sqrt(constante_elastica / masa) #Frecuencia angular
    phi = np.arctan((-velocidad_inicial) / ((posicion_inicial - longitud) * omega)) - omega * tiempo_inicial #Fase inicial
    amplitud_inicial = (posicion_inicial - longitud) / (np.cos(omega * tiempo_inicial + phi)) #Amplitud inicial

    p = 50 #Cantidad de períodos que deseo ver en la animación

    t = np.linspace(tiempo_inicial, tiempo_inicial + p * 2 * np.pi / omega, 1000) #Defino el inicio y el final del movimiento del resorte
    x = amplitud_inicial * np.exp(-amortiguamento * t / (2 * masa)) * np.cos(omega * t + phi) + longitud #Ecuacion de movimiento con amortiguamiento

    def actualizar(i):
        plt.clf() #Eliminar la figura actual para actualizarla
        plt.subplot().spines['left'].set_position('zero') #Poner la margen izquierda en el centro y hacer que no se mueva
        plt.subplot().spines['bottom'].set_position('zero') #Poner la margen inferior en el centro y hacer que no se mueva
        plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
        plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
        plt.xlim(-0.1, longitud * 3) #Limitar el eje x entre -15.5 y 15.5
        plt.ylim(-3, 3) # Limitar el eje y entre -15.5 y 15.5
        plt.subplot().set_aspect('equal', adjustable = 'box') #Hacer que el aspecto entre los puntos del eje x y y sean completamente simetricas
        plt.tight_layout() #Ajustar la grafica al tamanio del cuadro
        plt.grid(True, alpha = 0.4) #Crear la rejila
        plt.axvline(longitud, linestyle='--', label='l0', color='blue') #Longitud natural del resorte
        plt.axvline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje x
        plt.axhline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje y
        plt.scatter(x[i], 0, color='black')  # Masa
        valores_x = np.linspace(0, x[i], 1000)
        amplitud_x = 20 * np.pi / x[i]
        valores_y = np.sin(amplitud_x * valores_x)  # Resorte
        plt.plot(valores_x, valores_y, color='black')

    ani = animation(plt.gcf(), actualizar, frames=2000, interval=10)
    #Figura, Funcion que actualiza, Numero de frames que se ejecuta, Intervalo entre cada frame

    canvas.draw() #Dibujar la grafica en un canva

def grafico_maxwell():
    #2; 10
    #Amplitud; Frecuencia
    
    entrada = zona_resultado.get().split(";") #Separar los parametros 

    amplitud = float(entrada[0]) #Amplitud de la onda
    frecuencia = float(entrada[1]) #Frecuencia de la onda
    frecuencia_angular = 2 * np.pi * frecuencia #Frecuencia angular de la onda

    x = np.linspace(0, 2*np.pi, 1000) #Numero de datos para calcular

    campo_electrico = amplitud * np.cos(frecuencia_angular * x) #Ecuacion de la onda E
    campo_magnetico = amplitud * np.cos(frecuencia_angular * x) #Ecuacion de la onda B

    plt.subplot(111, projection='3d') #Crear el grafico en 3D

    plt.plot(x, np.zeros_like(x), campo_electrico, label='Campo Eléctrico') #Ubicar los puntos de la funcion y graficarlos
    plt.plot(x, campo_magnetico, np.zeros_like(x), label='Campo Magnético') #Ubicar los puntos de la funcion y graficarlos 

    canvas = tkagg(plt.gcf(), master = ventana) #Crear un canvas con el grafico del matplolib
    barra_herramientas = toolbar(canvas, ventana) #Crear una barra de herramientas
    barra_herramientas.update() #Llama a la barra de herramientas
    canvas.get_tk_widget().place(relx = .47, rely = .05, relwidth = .5, relheight = .85) #Ubica el canvas en la ventana   
    barra_herramientas.place(relx = .47, rely = .9, relwidth = .5, relheight = .05) #Ubica la barra de herramientas en la ventana
 
    canvas.draw() #Dibujar la grafica en un canva

ventana = tk.Tk() #Crea la ventana
ventana.resizable(False, False) #No permite que se cambie el tamano de la ventana
ventana.title("Calculadora de Heinrich") #Titulo de la ventana
ventana.iconbitmap("Imagenes/Imagen icono.ico") #Icono de la ventana
ventana.config(bg = '#FFF2E1') #Color de fondo
ventana.state('zoomed') #Hace que se ejecute en modo ventana

opcion = tk.StringVar() #Crear la variable para guardar la opcion escogida del menu

crear_widgets(ventana) #Crea los botones, entry's, menus, etc
graficar() #Establece la ventana graficar por defecto
crear_barra_menu(ventana) #Crea la barra superior

ventana.mainloop() #Mantiene la ventana abierta