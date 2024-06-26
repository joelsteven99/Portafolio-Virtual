from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as num
import sympy as sym
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as TkAgg, NavigationToolbar2Tk as ToolBar
import math as mt
from datetime import datetime
import customtkinter

ventana = tk.Tk() #Crea la ventana
ventana.resizable(False, False) #No permite que se cambie el tamano de la ventana
ventana.title("Calculadora de Heinrich") #Titulo de la ventana
#ventana.iconbitmap("Imagenes/Imagen icono.ico") #Icono de la ventana
ventana.config(bg = '#FFF2E1') #Color de fondo
ventana.state('zoomed') #Hace que se ejecute en modo ventana

#Historial
#historial = customtkinter.CTkLabel(ventana, font = Fuente_Botones, fg_color = '#D1BB9E', corner_radius = 15, text_color = '#76453B', text = "Historial")
#historial.place(relx = .02, rely = .35, relwidth = .4, relheight = .04)
#borrar_his = customtkinter.CTkButton(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', text = "Borrar historial")
#borrar_his.place(relx = .02, rely = .93, relwidth = .1, relheight = .04)

def destruir():
    global graf, resol, resul, oper, esp_graf, borrar, opc_polar #Variables que se pueden usar en distintas partes del codigo

    graf.destroy() #Eliminar el boton que grafica
    resol.destroy() #Eliminar el boton que realiza la operacion
    resul.destroy() #Eliminar el entry donde se pone el resultado
    oper.destroy() #Eliminar el entry donde se pone la operacion
    esp_graf.destroy() #Eliminar el espacio donde va el grafico
    borrar.destroy() #Eliminar el boton de limpiar
    opc_polar.destroy() #Eliminar el boton de seleccion de la parte de conversion polar

def crear():
    global graf, resol, resul, oper, esp_graf, borrar, opc_polar #Variables que se pueden usar en distintas partes del codigo

    #Establecer fuentes de letra
    Fuente_Letra = customtkinter.CTkFont(family='sans serif', size = 20)
    Fuente_Botones = customtkinter.CTkFont(family='sans serif', size = 12)

    #Crear el entry donde se pondra la operacion
    oper = customtkinter.CTkEntry(ventana, font = Fuente_Letra, fg_color = '#D1BB9E', border_color = '#A79277', corner_radius = 15, text_color = '#76453B')
    oper.place(relx = .02, rely = .02, relwidth = .4,relheight = .1)

    #Crear el boton para graficar
    graf = customtkinter.CTkButton(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', text = "Graficar", command = grafica)
    graf.place(relx = .28, rely = .15, relwidth = .06, relheight = .04)

    #Crear el boton que realizara la operacion
    resol = customtkinter.CTkButton(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', text = "Calcular", command = matematicas_especiales_menu)
    resol.place(relx = .03, rely = .15, relwidth = .1, relheight = .04)

    #Crear el entry donde se pondra el resultado
    resul = customtkinter.CTkEntry(ventana, font = Fuente_Letra, fg_color = '#D1BB9E', border_color = '#A79277', corner_radius = 15, text_color = '#76453B', state = 'readonly')
    resul.place(relx = .02, rely = .22, relwidth = .4,relheight = .1)

    #Crear el espacio para la grafica
    esp_graf = tk.Label(ventana, background = "#A79277")
    esp_graf.place(relx = .47, rely = .05, relwidth = .5, relheight = .85)

    #Crear el boton para borrar todo
    borrar = customtkinter.CTkButton(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', text = "Limpiar", command = limpiar)
    borrar.place(relx = .35, rely = .15, relwidth = .06, relheight = .04)

    #Seleccionar el procedimiento de la funcion de conversion polar
    opc_polar = customtkinter.CTkOptionMenu(ventana, font = Fuente_Botones, button_color = '#EAD8C0', fg_color = '#EAD8C0', dropdown_font = Fuente_Botones, dropdown_fg_color = '#EAD8C0', text_color = '#76453B', dropdown_text_color = '#76453B', corner_radius = 15, values = ["Conversion Complejo/Polar", "Conversion Polar/Complejo"], state = 'readonly')
    opc_polar.set("Conversion Complejo/Polar")
    opc_polar.place(relx = .15, rely = .15, relwidth = .12, relheight = .04)

def limpiar():  
    try:
        if opcion.get() == "Graficar" and canvas == None:
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se pone el resultado
        elif opcion.get() == "Graficar" and canvas != None:
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se pone el resultado
            canvas.get_tk_widget().destroy() #Elimina el grafico
            toolbar.destroy() #Elimina la barra de herramientas del grafico
        elif opcion.get() == "Grafica de onda" and canvas == None:
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se pone el resultado
        elif opcion.get() == "Grafica de onda" and canvas != None:
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se pone el resultado
            canvas.get_tk_widget().destroy() #Elimina el grafico
            toolbar.destroy() #Elimina la barra de herramientas del grafico
        elif opcion.get() != "Graficar" and canvas == None: #Verificar si el grafico esta vacio
            resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se pone el resultado
            resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
            oper.delete(0, 'end') #Elimina lo que haya en el entry donde se pone la operacion
        elif opcion.get() != "Graficar" and canvas != None: #En caso de que el grafico no este vacio
            canvas.get_tk_widget().destroy() #Elimina el grafico
            toolbar.destroy() #Elimina la barra de herramientas del grafico
            resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
            oper.delete(0, 'end') #Elimina lo que haya en el entry donde se pone la operacion
    except Exception as e:
        messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error

def graficar():
    ventana.title("Calculadora de Heinrich (Graficar)") #Cambiar el nombre de la ventana

    opcion.set("Graficar") #Define la opcion seleccionadac del menu

    destruir() #Destruir todos los entry, botones, labels y graficas
    crear() #Crear todos los entry, botones, labels y graficas

    resol.destroy() #Eliminar el boton que realiza la operacion
    oper.destroy() #Eliminar el entry donde se pone la operacion
    opc_polar.destroy() #Eliminar las opciones de polar y complejo
    graf.place(relx = .03, rely = .15, relwidth = .1, relheight = .04) #Mover el boton para graficar
    resul.place(relx = .02, rely = .02, relwidth = .4,relheight = .1) #Mover el entry donde se pone el resultado
    resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable

def oper_basicas():
    ventana.title("Calculadora de Heinrich (Operaciones Basicas)") #Cambiar el nombre de la ventana

    opcion.set("Operaciones Basicas") #Define la opcion seleccionadac del menu

    destruir() #Destruir todos los entry, botones, labels y graficas
    crear() #Crear todos los entry, botones, labels y graficas

    opc_polar.destroy()

def valor_abs():
    ventana.title("Calculadora de Heinrich (Valor Absoluto)") #Cambiar el nombre de la ventana

    opcion.set("Valor Absoluto") #Define la opcion seleccionada del menu

    destruir() #Destruir todos los entry, botones, labels y graficas
    crear() #Crear todos los entry, botones, labels y graficas

    opc_polar.destroy()

def polar():
    ventana.title("Calculadora de Heinrich (Polar)") #Cambiar el nombre de la ventana

    opcion.set("Polar") #Define la opcion seleccionada del menu

    destruir() #Destruir todos los entry, botones, labels y graficas
    crear() #Crear todos los entry, botones, labels y graficas

def limites():
    ventana.title("Calculadora de Heinrich (Limites)")

    opcion.set("Limites")

    destruir()
    crear()

    graf.destroy()
    opc_polar.destroy()

def derivadas():
    ventana.title("Calculadora de Heinrich (Derivadas)")

    opcion.set("Derivadas")

    destruir() #Destruir todos los entry, botones, labels y graficas
    crear() #Crear todos los entry, botones, labels y graficas

    opc_polar.destroy()
    graf.destroy()
    resol.configure(text = "Derivar")

def graficar_onda():
    ventana.title("Calculadora de Heinrich (Grafica de la onda)")

    opcion.set("Grafica de onda")

    destruir()
    crear()

    resol.destroy() #Eliminar el boton que realiza la operacion
    oper.destroy() #Eliminar el entry donde se pone la operacion
    opc_polar.destroy() #Eliminar las opciones de polar y complejo
    graf.place(relx = .03, rely = .15, relwidth = .1, relheight = .04) #Mover el boton para graficar
    resul.place(relx = .02, rely = .02, relwidth = .4,relheight = .1) #Mover el entry donde se pone el resultado
    resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable

def limpiar_grafica_auto(canvas):
    
    if canvas != None:
        canvas.get_tk_widget().destroy() #Elimina el grafico
        toolbar.destroy() #Elimina la barra de herramientas del grafico
    else:
        pass

def grafica():
    global canvas, toolbar, r, theta

    canvas.get_tk_widget().destroy() #Elimina el grafico
    toolbar.destroy() 

    if opcion.get() == "Grafica de onda":
        t = num.arange(-30, 30, 0.001)
        x = resul.get()
        palabrasc = {"sin":"num.sin","cos":"num.cos","tan":"num.tan","log":"num.log","e":"num.exp","pi":"num.pi"}

        for i in palabrasc:
            if i in x :
                x = x.replace(i, palabrasc[i])

        y = eval(x)

        lista = [] #Crear una lista para guardar los numeros
        longitud = 200 #Establecer la longitud de la lista
        for lon in range(-longitud, longitud + 1): #Calcular los numeros desde el negativo hasta el positivo del numero mayor
            if lon != 0:
                lista.append(lon) #Guardara en la lista todos los numeros, a excepcion del cero
        
        plt.rc('font', family = 'sans-serif', size = 6) #Cambiar la fuente de todo el grafico y el tamanio
        plt.figure(figsize = (20, 8)) #Cambiar el tamanio del grafico
        plt.subplot().spines['left'].set_position('zero') #Poner la margen izquierda en el centro y hacer que no se mueva
        plt.subplot().spines['bottom'].set_position('zero') #Poner la margen inferior en el centro y hacer que no se mueva
        plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
        plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
        plt.subplot().set_xticks(lista) #Poner los numeros en el eje x de acuerdo a la lista
        plt.subplot().set_yticks(lista) #Poner los numeros en el eje y de acuerdo a la lista
        plt.xlim(-9.5, 9.5) #Limitar el eje x entre -20 y 20
        plt.ylim(-9.5, 9.5) # Limitar el eje y entre -20 y 20
        plt.subplot().set_aspect('equal', adjustable = 'box') #Hacer que el aspecto entre los puntos del eje x y y sean completamente simetricas
        plt.tight_layout() #Ajustar la grafica al tamanio del cuadro
        plt.grid(True, alpha = 0.4)
        plt.axvline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje x
        plt.axhline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje y
        plt.plot (t, y)
        canvas = TkAgg(plt.gcf(), master = ventana) #Crear un canvas con el grafico del matplolib
        toolbar = ToolBar(canvas, ventana) #Crear una barra de herramientas
        toolbar.update() #Llama a la barra de herramientas
        canvas.get_tk_widget().place(relx = .47, rely = .05, relwidth = .5, relheight = .85) #Ubica el canvas en la ventana
        toolbar.place(relx = .47, rely = .9, relwidth = .5, relheight = .05) #Ubica la barra de herramientas en la ventana
        canvas.draw() #Dibuja el canvas en la ventana
    elif opcion.get() != "Grafica de onda":
        if opcion.get() == "Polar":
            if opc_polar.get() == "Conversion Complejo/Polar":
                z = oper.get() #Obtener el string ingresado
                z = "".join(z) #Elimina los espacios
                z = z.replace(")j", ")*I")
                z = sym.sympify(z)
                print(z)
            elif opc_polar.get() == "Conversion Polar/Complejo":
                z = resul.get() #Obtener el string ingresado
        elif opcion.get() != "Polar":
            z = resul.get() #Obtener el string ingresado

        try:
            z = complex(z) #Convertirlo a forma compleja
            print(z)
            real_int = int(z.real) #Dividir la parte real en un entero
            imag_int = int(z.imag) #Dividir la parte imaginaria en un entero

            #Crear una lista, que servira para guardar los numeros que graficaremos en los ejes x y y, teniendo en cuenta la longitud
            lista = [] #Crear una lista para guardar los numeros
            longitud = 200 #Establecer la longitud de la lista
            for x in range(-longitud, longitud + 1): #Calcular los numeros desde el negativo hasta el positivo del numero mayor
                if x != 0:
                    lista.append(x) #Guardara en la lista todos los numeros, a excepcion del cero
            
            plt.rc('font', family = 'sans-serif', size = 6) #Cambiar la fuente de todo el grafico y el tamanio
            plt.figure(figsize = (20, 8)) #Cambiar el tamanio del grafico
            plt.subplot().spines['left'].set_position('zero') #Poner la margen izquierda en el centro y hacer que no se mueva
            plt.subplot().spines['bottom'].set_position('zero') #Poner la margen inferior en el centro y hacer que no se mueva
            plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
            plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
            plt.subplot().set_xticks(lista) #Poner los numeros en el eje x de acuerdo a la lista
            plt.subplot().set_yticks(lista) #Poner los numeros en el eje y de acuerdo a la lista
            plt.xlim(-20.5, 20.5) #Limitar el eje x entre -20 y 20
            plt.ylim(-20.5, 20.5) # Limitar el eje y entre -20 y 20
            plt.subplot().set_aspect('equal', adjustable = 'box') #Hacer que el aspecto entre los puntos del eje x y y sean completamente simetricas
            plt.tight_layout() #Ajustar la grafica al tamanio del cuadro
            plt.grid(True, alpha = 0.4) #Crear una rejilla con transparencia 0.4
            plt.quiver(0, 0, z.real, z.imag, color = "black", angles = 'xy', scale_units = 'xy', scale = 1, width = 0.002) #Ubicar la funcion en el plano
            plt.plot([0, -z.real], [0, -z.imag], color = "white", alpha = 0) #Ubicar la funcion en el plano pero en el otro eje, de manera invisible para hacer visible los otros 3 ejes
            plt.plot([0, z.real], [z.imag, z.imag], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje x hasta el punto 
            plt.plot([z.real, z.real], [0, z.imag], color = 'black', linestyle = '--', linewidth = 0.5) #Hacer la linea que ira desde el eje y hasta el punto
            plt.axvline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje x
            plt.axhline(0, color = "black", linewidth = 0.5) #Crear las lineas que iran por todo el punto cero del eje y
            plt.get_current_fig_manager().set_window_title("Grafico") #Poner titulo a la ventana del grafico
        
            #Funciones que ponen la funcion compleja en el punto dependiendo de en que cuadrante se encuentra
            if opcion.get() == "Polar":
                if opc_polar.get() == "Conversion Complejo/Polar":
                    if real_int > 0 and imag_int > 0:
                        plt.text(z.real, z.imag, f'  {r}', verticalalignment = 'bottom', horizontalalignment = 'left')

                    if real_int < 0 and imag_int > 0:
                        plt.text(z.real, z.imag, f'  {r}', verticalalignment = 'bottom', horizontalalignment = 'right')

                    if real_int < 0 and imag_int < 0:
                        plt.text(z.real, z.imag, f'  {r}', verticalalignment = 'top', horizontalalignment = 'right')

                    if real_int > 0 and imag_int < 0:
                        plt.text(z.real, z.imag, f'  {r}', verticalalignment = 'top', horizontalalignment = 'left')

                    radio = 3
                    punto_inicio = 0
                    valor_theta = theta
                    theta = float(theta.evalf())
                    theta = round(theta, 2)
                    angulo = num.linspace(0, theta , 100)
                    angulo_ejex = punto_inicio + radio * num.cos(angulo)
                    angulo_ejey = punto_inicio + radio * num.sin(angulo)

                    plt.subplot().plot(angulo_ejex, angulo_ejey, color = 'red', linewidth = 0.8)
                    plt.text(3, 1, f'  {valor_theta}', verticalalignment = 'bottom', horizontalalignment = "left")
                else:      
                    if real_int > 0 and imag_int > 0:
                        plt.text(z.real, z.imag, f'  {z}', verticalalignment = 'bottom', horizontalalignment = 'left')

                    if real_int < 0 and imag_int > 0:
                        plt.text(z.real, z.imag, f'{z}  ', verticalalignment = 'bottom', horizontalalignment = 'right')

                    if real_int < 0 and imag_int < 0:
                        plt.text(z.real, z.imag, f'{z}  ', verticalalignment = 'top', horizontalalignment = 'right')

                    if real_int > 0 and imag_int < 0:
                        plt.text(z.real, z.imag, f'  {z}', verticalalignment = 'top', horizontalalignment = 'left')

            canvas = TkAgg(plt.gcf(), master = ventana) #Crear un canvas con el grafico del matplolib
            toolbar = ToolBar(canvas, ventana) #Crear una barra de herramientas
            toolbar.update() #Llama a la barra de herramientas
            canvas.get_tk_widget().place(relx = .47, rely = .05, relwidth = .5, relheight = .85) #Ubica el canvas en la ventana
            toolbar.place(relx = .47, rely = .9, relwidth = .5, relheight = .05) #Ubica la barra de herramientas en la ventana
            canvas.draw() #Dibuja el canvas en la ventana
        except Exception as e:
            resul.delete(0, 'end') #Elimina lo que haya en el entry donde se ingresa la funcion
            messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error

def matematicas_especiales_menu():
    global r, theta

    opc_sel = opcion.get() #Obtiene la opcion seleccionada del menu

    #Verifica cual opcion fue seleccionada
    if opc_sel == "Operaciones Basicas":
        try:
            entrada = oper.get() #Obtiene la operacion
            entrada = "".join(entrada) #Elimina los espacios y saltos de linea
            entrada = eval(entrada) #Convierte la operacion en una funcion
            entrada = complex(entrada) #Convierte la funcion en una funcion compleja y la resuelve
            red_real = round(entrada.real, 4) #Redondea la parte real a 4 digitos
            red_imag = round(entrada.imag, 4) #Redondea la parte imaginaria a 4 digitos 
            entrada = complex(red_real, red_imag) #Junta la parte real e imaginaria, ya redondeadas en una funcion compleja

            resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            resul.insert(0, entrada) #Inserta el resultado
            resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
        except Exception as e:
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error
    elif opc_sel == "Valor Absoluto":
        try:
            entrada = oper.get() #Obtiene la operacion
            entrada = "".join(entrada) #Elimina los espacios y saltos de linea 
            entrada = eval(entrada) #Convierte la operacion en una funcion
            entrada = complex(entrada) #Convierte la funcion en una funcion compleja y la resuelve
            entrada = mt.sqrt(entrada.real**2 + entrada.imag**2) #Se realiza la funcion del valor absoluto de un complejo 
            entrada = round(entrada, 4) #Se redondea el resultado a 4 digitos
            
            resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            resul.insert(0, entrada) #Inserta el resultado
            resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
        except Exception as e:
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error
    elif opc_sel == "Polar":
        if opc_polar.get() == "Conversion Complejo/Polar":        
            try:
                entrada = oper.get() #Obtiene la operacion
                entrada = "".join(entrada) #Elimina los espacios
                entrada = entrada.replace(")j", ")*I")
                entrada = sym.sympify(entrada)
                real = sym.re(entrada)
                imag = sym.im(entrada)
                string_real = str(real)
                print(string_real)
                string_imag = str(imag)
                print(string_imag)
                r = sym.sqrt(real**2 + imag**2) #Se saca la raiz cuadrada de la parte real al cuadrado mas la parte imaginaria al cuadrado
                print(r)
                string_r = str(r)
                print(string_r)

                if "." in string_r:
                    r = round(r, 4) 
                else: 
                    r = sym.sqrt(real**2 + imag**2)
                                  
                if imag == 0:
                    theta = 0
                elif real == 0 and imag < 0: #Caso si la parte real es cero y la imaginaria es negativa
                    theta = sym.atan(-sym.oo)
                    theta = 2*sym.pi + theta
                elif real == 0 and imag > 0: #Caso si la parte real es cero y la imaginaria es positiva
                    theta = sym.atan(sym.oo)
                elif real > 0 and imag > 0: #Caso si la parte real e imaginaria son positivas
                    theta = sym.atan(imag/real)
                    string_theta = str(theta)

                    if "pi" in string_theta:
                        theta = sym.atan(imag/real)                 
                    elif "pi" not in string_theta:
                        theta = sym.atan(imag/real).evalf() 
                        theta = round(theta, 4) 
                elif real < 0 and imag < 0: #Caso si la parte real e imaginaria son negativas
                    theta = sym.atan(imag/real)
                    string_theta = str(theta)

                    if "pi" in string_theta:
                        theta = sym.atan(imag/real)
                        theta = abs(theta)                  
                        theta = theta + sym.pi
                    elif "pi" not in string_theta:
                        theta = sym.atan(imag/real).evalf()
                        theta = abs(theta)                  
                        theta = (theta + sym.pi).evalf() 
                        theta = round(theta, 4) 
                elif real < 0 and imag > 0: #Caso si la parte real es negativa y la imaginaria positiva
                    theta = sym.atan(imag/real)
                    string_theta = str(theta)

                    if "pi" in string_theta:
                        theta = sym.atan(imag/real)
                        theta = abs(theta)                  
                        theta = sym.pi - theta
                    elif "pi" not in string_theta:
                        theta = sym.atan(imag/real).evalf()
                        theta = abs(theta)                  
                        theta = (sym.pi - theta).evalf() 
                        theta = round(theta, 4) 
                elif real > 0 and imag < 0: #Caso si la parte real es positiva y la imaginaria negativa
                    theta = sym.atan(imag/real)
                    string_theta = str(theta)

                    if "pi" in string_theta:
                        theta = sym.atan(imag/real)
                        theta = abs(theta)                  
                        theta = 2*sym.pi - theta
                    elif "pi" not in string_theta:
                        theta = sym.atan(imag/real).evalf()
                        theta = abs(theta)                  
                        theta = (2*sym.pi - theta).evalf() 
                        theta = round(theta, 4)
                resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
                resul.delete(0, 'end') #Elimina lo que haya en el entry
                resul.insert(0, f'{r}(Cos({theta}) + jSen({theta}))') #Inserta el resultado
                resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
            except Exception as e:
                resul.delete(0, 'end') #Elimina lo que haya en el entry
                messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error
        elif opc_polar.get() == "Conversion Polar/Complejo":
            try:
                entrada = oper.get() #Obtiene la operacion
                entrada = entrada.lower() #Vuelve la entrada en minuscula
                entrada = entrada.replace("(", "").replace(")", "").replace("cos", "").replace("sen", "") #Elimina parentesis, cos y sen, dejando solo los angulos y r
                entrada = entrada.split('*') #Separa r de los angulos
                r = entrada[0] #Guarda r
                r = eval(r) #Vuelve r funcion
                complejo = entrada[1] #Guarda el angulo
                complejo = list(complejo) #Convierte los dos angulos en lista
                complejo.remove("j") #Elimina j de la parte de sen
                complejo = "".join(complejo) #Junta todo en un string
                complejo = eval(complejo) #Vuelve el string una funcion y la resuelve
                complejo = float(complejo/2) #Como el angulo quedo duplicado se divide por 2
                complejo = num.radians(complejo) #Pasa el angulo a radianes
                parte_real = num.cos(complejo) #Saca el cos del angulo
                parte_imag = num.sin(complejo) #Saca el sen del angulo
                funcion_compleja = complex(round(r*parte_real, 4), round(r*parte_imag, 4)) #Multiplica r con el resultado de sen y cos, luego lo convierte en funcion compleja
                                               
                resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
                resul.delete(0, 'end') #Elimina lo que haya en el entry
                resul.insert(0, funcion_compleja) #Inserta el resultado
                resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
            except Exception as e:
                resul.delete(0, 'end') #Elimina lo que haya en el entry
                messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error
    elif opc_sel == "Derivadas":
        try:   
            z = sym.symbols('z')
            
            entrada = oper.get()
            
            palabrasc = {"sin":"sym.sin","cos":"sym.cos","tan":"sym.tan","log":"sym.log","e":"sym.exp","pi":"sym.pi"}

            for i in palabrasc:
                if i in entrada :
                    entrada = entrada.replace(i, palabrasc[i])

            entrada = eval(entrada)

            derivada = sym.diff(entrada, z)

            print(derivada)

            resul.configure(state = 'normal') #Configura el entry del resultado para que sea editable
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            resul.insert(0, derivada) #Inserta el resultado
            resul.configure(state = 'readonly') #Configura el entry del resultado para que no sea editable
        except Exception as e:
            resul.delete(0, 'end') #Elimina lo que haya en el entry
            messagebox.showerror("Error", f'{e}') #Captura e imprime cualquier error

crear() #Crea todos los botones, entry y label (tienen que crearse siempre para poder hacer funcionar los comandos que eliminan los botones uwu)

opcion = tk.StringVar() #Crea una variable que guarda la opcion del menu

#Crear el menu
barra_menu = tk.Menu(ventana)
ventana.config(menu = barra_menu)

#Definir la zona de archivo
Archivo = tk.Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Archivo", menu = Archivo)
Archivo.add_command(label = "Salir", command = ventana.destroy)

#Definir la zona de ajustes
Ajustes = tk.Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Ajustes", menu = Ajustes)
Ajustes.add_command(label = "Pantalla Completa",command = lambda:ventana.attributes('-fullscreen', True)) #Pone pantalla completa
Ajustes.add_command(label = "Pantalla normal",command = lambda:ventana.attributes('-fullscreen', False)) #Pone modo ventana

#Menu matematicas especiales
mat_esp = tk.Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Matematicas Especiales", menu = mat_esp)
mat_esp.add_command(label = "Graficar", command = graficar)
mat_esp.add_command(label = "Operaciones Basicas", command = oper_basicas)
mat_esp.add_command(label = "Valor Absoluto", command = valor_abs)
mat_esp.add_command(label = "Conversión a Polar", command = polar)
#mat_esp.add_command(label = "Rango y Dominio", command = polar)
#mat_esp.add_command(label = "Operaciones polares", command = polar)
#mat_esp.add_command(label = "Funciones Complejas", command = funciones_complejas)
#mat_esp.add_command(label = "Polinomio Complejo", command = polinomio_complejo)
mat_esp.add_command(label = "Limites", command = limites)
mat_esp.add_command(label = "Derivadas", command = derivadas)
#mat_esp.add_command(label = "Numeros complejos de forma exponencial", command = numeros_exponenciales)
#mat_esp.add_command(label = "Logaritmos", command = logaritmos)
#mat_esp.add_command(label = "Funciones Trigonometricas Inversas e Hiperbolicas", command = inversa_hiperbolica)
#mat_esp.add_command(label = "Integración", command = integracion)
#mat_esp.add_command(label = "Analisis de Fourier", command = fourier)

#menu ondas y señales
ond_sen = tk.Menu(barra_menu, tearoff = 0)
barra_menu.add_cascade(label = "Ondas y Señales", menu = ond_sen)
ond_sen.add_command(label = "Graficar", command = graficar_onda)
#Establecer fuentes de letra
Fuente_Botones = customtkinter.CTkFont(family='sans serif', size = 12)

#Historial
historial = customtkinter.CTkLabel(ventana, font = Fuente_Botones, fg_color = '#D1BB9E', corner_radius = 15, text_color = '#76453B', text = "Historial")
historial.place(relx = .02, rely = .35, relwidth = .4, relheight = .04)
zona_historial = customtkinter.CTkLabel(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', text = "Aqui va el historial")
zona_historial.place(relx = .02, rely = .4, relwidth = .4, relheight = .5 )
borrar_his = customtkinter.CTkButton(ventana, font = Fuente_Botones, fg_color = '#EAD8C0', corner_radius = 15, text_color = '#76453B', hover_color = '#D1BB9E', text = "Borrar historial")
borrar_his.place(relx = .02, rely = .93, relwidth = .1, relheight = .04)

graficar() #Grafica ejecutada por defecto

ventana.mainloop(0) #Bucle para que no se cierre la ventana