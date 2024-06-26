from tkinter import ttk, messagebox, Label, StringVar,Tk,Frame,END,Entry,INSERT,Button,Menu,scrolledtext as st
import numpy
import re
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import cmath
from math import cos, sin, radians
#configuracion de la ventana
Ventana = Tk()
version = 4.5
Ventana.title(f"Calculadora Pro {version}")
Ventana.state('zoomed')
Ventana.geometry('1000x500')
Ventana.config(bg='#1A2D3E')
#hijueputa declaracion de variables ((re)innesesaria)
global Resultado
HEcuacion = StringVar()
HResultado = StringVar()
historial_textos = []
#funciones
def Borrar():
    historial_textos.clear()
    Label4.config(text="Historial:\n")
def Limpiar():
    plt.figure(facecolor='lightgreen',clear=True)
    plt.plot([0,0], [0,0])  
    plt.axvline(0, color='black', linewidth=.5)
    plt.axhline(0, color='black', linewidth=.5)  
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfica')
    plt.grid(True)
    plt.tight_layout() 
    plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
    plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
    plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
    plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
    canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
    toolbar = NavigationToolbar2Tk(canvas, Ventana)
    toolbar.update() 
    canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
    toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
    canvas.draw()    
    canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
    MenuNumero.current(0)
    EOperacion.delete(0, END)
    MenuCambio1.current(0)
    MenuCambio2.current(0)
    EResultado.configure(state='normal')
    EResultado.delete(0, END)
    EResultado.configure(state='readonly')
def Operar ():#funcion para solo operar
    Operacion = EOperacion.get()
    Estilo = MenuNumero.get()
    if (Estilo == "Complejo"):
        Resultado = eval(Operacion)
        Resultado = complex(Resultado)
    elif (Estilo == "Entero"):
        Resultado = eval(Operacion)
        Resultado = int(Resultado)
    elif (Estilo == "Decimal"):
        Resultado = eval(Operacion)
        Resultado = float(Resultado)
    else:messagebox.showerror("Error", "Por favor ingrese el tipo de numero.");return
    EResultado.config(state='normal')
    EResultado.delete(0, END)
    EResultado.insert(1, Resultado)
    EResultado.config(state='readonly')
    hora_actual = datetime.now().strftime("%H:%M:%S")
    HEcuacion = EOperacion.get()
    HResultado = EResultado.get()
    historial_textos.append(f"[{hora_actual}]\nEcuacion: {HEcuacion}; Resultado: {HResultado}")
    historial_actualizado = "\n".join(historial_textos)
    Label4.config(state='normal')
    Label4.delete(1.0, END)
    Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
    Label4.config(state='disabled')
def Graficar():
    #opera la funcion
    Operacion = EOperacion.get()
    Estilo = MenuNumero.get()
    if (Estilo == "Complejo"):
        Resultado = eval(Operacion)
        Resultado = complex(Resultado)
    elif (Estilo == "Cartesiano"):#graficar en coordenadas cartesianas
        coordenadas = EOperacion.get().strip()
        x, y = map(float, coordenadas.split(','))
        plt.figure(facecolor='lightgreen',clear=True)
        plt.plot(x, y, 'gx')
        plt.plot([0,x], [0,y], 'b-')  
        plt.plot([0,x], [y,y], 'r--')  
        plt.plot([x,x], [0,y], 'r--')
        if (x == 0):
            Pocicion = 'center'
        elif (x < 0):
            Pocicion = 'left'
        elif (x > 0):
            Pocicion = 'right'
        plt.text(x, y,f'({x},{y})',fontsize=12,color='black',ha=Pocicion)
        plt.axvline(0, color='black', linewidth=1)
        plt.axhline(0, color='black', linewidth=1)
        plt.title('Coordenadas Cartesianas')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.tight_layout() 
        plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
        plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
        plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
        plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
        canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
        toolbar = NavigationToolbar2Tk(canvas, Ventana)
        toolbar.update() 
        canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
        toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
        canvas.draw()
#historial de la grafica
        hora_actual = datetime.now().strftime("%H:%M:%S")
        HResultado = EResultado.get()
        historial_textos.append(f"[{hora_actual}]\nGrafica: {coordenadas}; En ejes (X={x}, Y={y})")
        historial_actualizado = "\n".join(historial_textos)
        Label4.config(state='normal')
        Label4.delete(1.0, END)
        Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
        Label4.config(state='disabled')
        return
    elif (Estilo == "Polar"):#graficar en coordenadas Polares
        Valor = EOperacion.get()
        r, theta = map(float, Valor.split(','))
        theta = numpy.deg2rad(theta)
        x = r * numpy.cos(theta)
        y = r * numpy.sin(theta)
        plt.figure(facecolor='lightgreen',clear=True)
        plt.plot(x, y, 'gx')
        plt.plot([0,x], [0,y], 'b-')  
        plt.plot([0,x], [y,y], 'r--')  
        plt.plot([x,x], [0,y], 'r--')
        if (x == 0):
            Pocicion = 'center'
        elif (x < 0):
            Pocicion = 'left'
        elif (x > 0):
            Pocicion = 'right'
        plt.text(x, y,f'({x},{y})',fontsize=12,color='black',ha=Pocicion)
        plt.axvline(0, color='black', linewidth=1)
        plt.axhline(0, color='black', linewidth=1)
        plt.title('Coordenadas Polares')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.tight_layout() 
        plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
        plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
        plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
        plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
        canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
        toolbar = NavigationToolbar2Tk(canvas, Ventana)
        toolbar.update() 
        canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
        toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
        canvas.draw()
        #historial de la grafica
        hora_actual = datetime.now().strftime("%H:%M:%S")
        HResultado = EResultado.get()
        historial_textos.append(f"[{hora_actual}]\nGrafica: {HResultado}; En ejes (X={x}, Y={y})")
        historial_actualizado = "\n".join(historial_textos)
        Label4.config(state='normal')
        Label4.delete(1.0, END)
        Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
        Label4.config(state='disabled')
        return
    elif (Estilo == "Exponencial"):#graficar en coordenadas Exponenciales
        coordinates = EOperacion.get()
        coordinates = coordinates.split(",")
        coordinates = [complex(coord) for coord in coordinates]
        
        x = [coord.real for coord in coordinates]
        y = [coord.imag for coord in coordinates]
        
        plt.figure(facecolor='lightgreen',clear=True)
        plt.plot(x, y, 'ro')
        
        plt.axvline(0, color='black', linewidth=1)
        plt.axhline(0, color='black', linewidth=1)
        plt.title('Coordenadas Exponenciales')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.tight_layout() 
        plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
        plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
        plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
        plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
        canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
        toolbar = NavigationToolbar2Tk(canvas, Ventana)
        toolbar.update() 
        canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
        toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
        canvas.draw()
        #historial de la grafica
        hora_actual = datetime.now().strftime("%H:%M:%S")
        HResultado = EResultado.get()
        historial_textos.append(f"[{hora_actual}]\nGrafica: {HResultado}; En ejes (X={x}, Y={y})")
        historial_actualizado = "\n".join(historial_textos)
        Label4.config(state='normal')
        Label4.delete(1.0, END)
        Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
        Label4.config(state='disabled')
        return
    elif (Estilo == "Entero"):
        Resultado = eval(Operacion)
        Resultado = int(Resultado)
    elif (Estilo == "Decimal"):
        Resultado = eval(Operacion)
        Resultado = float(Resultado)
    else:messagebox.showerror("Error", "Por favor ingrese el tipo de numero.");return
    EResultado.config(state='normal')
    EResultado.delete(0, END)
    EResultado.insert(1, Resultado)
    EResultado.config(state='readonly')
    try:
        result = evaluate_function(Operacion)
        if result is not None:
            draw_matplotlib_graph(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))
def evaluate_function(function):
    pattern = r"[-+]?\d+\.?\d*j?|\d*\.?\d+j"
    matches = re.findall(pattern, function)
    complex_numbers = [complex(match) for match in matches]
    return complex_numbers
def draw_matplotlib_graph(complex_numbers):
    Resultado = complex(EResultado.get())
    plt.figure(facecolor='lightgreen',clear=True)  
    plt.plot(Resultado.real, Resultado.imag, 'gx')  
    plt.plot([0,Resultado.real], [0,Resultado.imag], 'b-')  
    plt.plot([0,Resultado.real], [Resultado.imag,Resultado.imag], 'r--')  
    plt.plot([Resultado.real,Resultado.real], [0,Resultado.imag], 'r--')
    if (Resultado.real == 0):
        Pocicion = 'center'
    elif (Resultado.real < 0):
        Pocicion = 'left'
    elif (Resultado.real > 0):
        Pocicion = 'right'
    plt.text(Resultado.real, Resultado.imag,f'({Resultado.real},{Resultado.imag})',fontsize=12,color='black',ha=Pocicion)  
    plt.axvline(0, color='black', linewidth=1)
    plt.axhline(0, color='black', linewidth=1)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.title('Gráfico de Números Complejos')
    plt.grid(True)
    plt.tight_layout() 
    plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
    plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
    plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
    plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible
    canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
    toolbar = NavigationToolbar2Tk(canvas, Ventana)
    toolbar.update() 
    canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
    toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
    canvas.draw()
    #historial de la grafica
    hora_actual = datetime.now().strftime("%H:%M:%S")
    HResultado = EResultado.get()
    historial_textos.append(f"[{hora_actual}]\nGrafica: {HResultado}; En ejes (X={Resultado.real}, Y={Resultado.imag})")
    historial_actualizado = "\n".join(historial_textos)
    Label4.config(state='normal')
    Label4.delete(1.0, END)
    Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
    Label4.config(state='disabled')
def CambiarRepresentación():
    HEcuacion = EOperacion.get()
    Representacion1 = MenuCambio1.get()
    Representacion2 = MenuCambio2.get()
    if (Representacion1 == 'Complejo' and Representacion2 == 'Carteciano'):
        try:
            Valor = complex(EOperacion.get())
            Valor = "{:.2f} + {:.2f}j".format(Valor.real, Valor.imag)
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Complejo' and Representacion2 == 'Polar'):
        try:
            Valor = complex(EOperacion.get())
            Valor = "{:.2f} ∠ {:.2f}°".format(abs(Valor), numpy.angle(Valor, deg=True))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Complejo' and Representacion2 == 'Exponencial'):
        try:
            Valor = complex(EOperacion.get())
            Valor = "{:.2f} * e^({:.2f}j)".format(abs(Valor), numpy.angle(Valor, deg=True))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Carteciano' and Representacion2 == 'Complejo'):
        try:
            Valor = complex(HEcuacion.replace("i", "j"))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Carteciano' and Representacion2 == 'Polar'):
        try:
            Valor = cmath.polar(complex(HEcuacion.replace("i", "j")))
            modulo = Valor[0]
            argumento = Valor[1]
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, f"(Mod={modulo},Arg={argumento})")
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Carteciano' and Representacion2 == 'Exponencial'):
        try:
            Valor = cmath.exp(complex(HEcuacion.replace("i", "j")))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Polar' and Representacion2 == 'Complejo'):
        try:
            r, theta = map(float, HEcuacion.split(','))
            real_part = r * cos(radians(theta))
            imaginary_part = r * sin(radians(theta))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, f"{round(real_part, 2)}j+{round(imaginary_part, 2)}i")
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Polar' and Representacion2 == 'Carteciano'):
        try:
            r, theta = map(float, HEcuacion.split(','))
            x = r * cos(radians(theta))
            y = r * sin(radians(theta))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, f"({round(x, 2)},{round(y, 2)})")
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Polar' and Representacion2 == 'Exponencial'):
        try:
            r, theta = map(float, HEcuacion.split(','))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, f"{round(r, 2)} * e^(i{round(theta, 2)})")
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Exponencial' and Representacion2 == 'Complejo'):
        try:
            Valor = complex(HEcuacion)
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Exponencial' and Representacion2 == 'Carteciano'):
        try:
            Valor = complex(HEcuacion.replace("i", "j"))
            Valor = "{:.2f} + {:.2f}j".format(Valor.real, Valor.imag)
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly')
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    elif (Representacion1 == 'Exponencial' and Representacion2 == 'Polar'):
        try:
            valor_complejo = complex(HEcuacion.replace("i", "j"))
            Valor = "{:.2f} ∠ {:.2f}".format(abs(valor_complejo), cmath.phase(valor_complejo))
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, Valor)
            EResultado.config(state='readonly') 
        except ValueError:
            EResultado.config(state='normal')
            EResultado.delete(0, END)
            EResultado.insert(1, "Entrada inválidad")
            EResultado.config(state='readonly')
    else:messagebox.showerror("Error", "Por favor elija una opcion valida.");return
    hora_actual = datetime.now().strftime("%H:%M:%S")
    HResultado = EResultado.get()
    historial_textos.append(f"[{hora_actual}]\nRepresentación {Representacion1} cambio a {Representacion2};\nOperacion: {HEcuacion}, Cambio a: {Valor}")
    historial_actualizado = "\n".join(historial_textos)
    Label4.config(state='normal')
    Label4.delete(1.0, END)
    Label4.insert(INSERT,"Historial:\n" + historial_actualizado)
    Label4.config(state='disabled')
def documentacion():
    messagebox.showinfo("Calculadora Pro v2.0",
    "Esta aplicación es una calculadora avanzada con capacidades para operar con números complejos, enteros y decimales, así como para graficar funciones matemáticas en un plano cartesiano."
    "\nFuncionalidades principales:"
    "\n1. Operaciones matemáticas:"
    "\n- Suma, resta, multiplicación, división, potenciación, etc."
    "\n- Admite números complejos, enteros y decimales."
    "\n2. Graficación de funciones:"
    "\n- Visualización de funciones matemáticas en un plano cartesiano."
    "\n- Soporta funciones con números complejos."
    "\n3. Historial de cálculos:"
    "\n- Registro de las operaciones realizadas, incluyendo ecuaciones y resultados."
    "\n4. Opciones de ayuda:"
    "\n- Documentación: Información sobre el funcionamiento de la aplicación."
    "\n- Actualizaciones: Verificación de nuevas versiones disponibles."
    "\n- Reportar problema: Envío de comentarios o problemas encontrados."
    "\n- Licencia y privacidad: Información legal sobre la aplicación."
    "\n- Acerca de: Detalles de derechos de autor y versión."
    "\n- Integrantes: Muestra la lista de integrantes."
    "\n"
    "\nComponentes principales del código:"
    "\n1. Funciones:"
    "\n- Operar(): Evalúa la operación ingresada por el usuario."
    "\n- Graficar(): Grafica la función matemática ingresada."
    "\n- evaluate_function(): Evalúa una función matemática y maneja errores."
    "\n- draw_complex_number(): Dibuja un número complejo en el plano cartesiano."
    "\n- Historial(): Actualiza el historial de cálculos."
    "\n- update(), fuck_off(), licencia(), privacidad(), acerca_de(), Integrantes(): Funciones de ayuda y barra de menú."
    "\n2. Interfaz de usuario:"
    "\n- Campos de entrada para ingresar la operación y ver el resultado."
    "\n- Botones para realizar cálculos y graficar funciones."
    "\n- Lienzo para mostrar la gráfica de funciones."
    "\n3. Barra de menú:"
    "\n- Opciones de archivo y ayuda para acceder a diversas funcionalidades y recursos de la aplicación."
    "\n"
    "\nUso:"
    "\n1. Ingresar la operación matemática en el campo correspondiente."
    "\n2. Seleccionar el tipo de número (complejo, entero o decimal) para realizar el cálculo."
    "\n3. Hacer clic en el botón 'Calcular (=)' para obtener el resultado."
    "\n4. Opcionalmente, se puede graficar la función matemática ingresada haciendo clic en el botón 'Graficar'."
    "\n5. El historial de cálculos se muestra en la ventana de la derecha."
    "\n6. Las opciones de ayuda y barra de menú proporcionan acceso a información adicional y opciones de soporte."
    "\n"
    "\nAutor: Equipo de Desarrollo de Calculadora Pro"
    "\nFecha de última actualización: Miércoles, 10 de Abril de 2024"
    "\nVersión: 2.0")
def update():
    messagebox.showinfo("¿Buscar actualizaciones?",
                        f"Actualmente no hay actualizaciones disponibles; \nUltima actualización: Lunes, 15/Abril/2024, Version: {version}")
def fuck_off():
    messagebox.showerror("¿Asi...?", "🖕🏻😘🖕🏻")
def licencia():
    messagebox.showinfo("Licencia",
                        "Pad Note "
                        "\nTÉRMINOS DE LICENCIA. "
                        "\nEstos términos de licencia son un acuerdo entre usted y CalculadoraPro (o, según el lugar donde viva, una de sus filiales). Se aplican a la empresa mencionada anteriormente. Los términos también se aplican a cualquier servicio o actualización de la CalculadoraPro para la empresa, excepto en la medida en que tengan términos diferentes.")
def privacidad():
    messagebox.showinfo("Privacidad",
                        "Pad Note"
                        "\nTÉRMINOS DE PRIVACIDAD. "
                        "\nEstos términos de privacidad son un acuerdo entre usted y la CalculadoraPro (o, según el lugar donde viva, una de sus filiales). Se aplican a la empresa mencionada anteriormente. Los términos también se aplican a cualquier servicio o actualización del CalculadoraPro para la empresa, excepto en la medida en que tengan términos diferentes.")
def acerca_de():
    messagebox.showinfo("Acerca de...", f"Copyright © 2024 Versión {version}")
def Integrantes():
    messagebox.showinfo("Integrantes",
    "Ayala Roncancio, Miguel Angelo\n"
    "\nBeltran Rubio, Jose Danilo\n"
    "\nBetancourt Prieto, Joel Steven\n"
    "\nOlave Ramirez, Juan Manolo")
#menu superior
barraMenu = Menu()
Ventana.config(menu=barraMenu, width=100, height=300)
#menu archivo
Archivo = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=Archivo)
Archivo.add_command(label="Salir", command=Ventana.destroy)
#menu About Us
AboutUs = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=AboutUs)
AboutUs.add_command(label="Documentación",command=documentacion)
AboutUs.add_command(label="¿Buscar actualizaciones?", command=update)
AboutUs.add_separator()
AboutUs.add_command(label="¡Reportar problema!", command=fuck_off)
AboutUs.add_command(label="¡Enviar comentarios!", command=fuck_off)
AboutUs.add_separator()
AboutUs.add_command(label="Ver licencia", command=licencia)
AboutUs.add_command(label="Declaracion de privacidad", command=privacidad)
AboutUs.add_separator()
AboutUs.add_command(label="Acerca de...", command=acerca_de)
AboutUs.add_command(label="Integrantes", command=Integrantes)
#menu ajustes
Ajustes = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ajustes", menu=Ajustes)
Ajustes.add_command(label="Pantalla Completa",command=lambda:Ventana.attributes('-fullscreen', True))
Ajustes.add_command(label="Pantalla normal",command=lambda:Ventana.attributes('-fullscreen', False))
#ingreso del tipo de numero
Label1 = Label(Ventana,text="Tipo de Operacion: ",bg='#1A2D3E',fg='white')
Label1.place(relx=.01, rely=0, relwidth=.1)
MenuNumero = ttk.Combobox(Ventana, values=["Complejo","Cartesiano","Polar","Exponencial","Entero","Decimal"], state='readonly')
MenuNumero.current(0)
MenuNumero.place(relx=.11, rely=0, relwidth=.1)
#label y entry de la operacion
Label2 = Label(Ventana,text="Ingrese Su Operación: ",bg='#1A2D3E',fg='white')
Label2.place(relx=.01, rely=.05, relwidth=.1)
EOperacion = Entry(Ventana,font=20,bg='dark green', fg='light green')
EOperacion.place(relx=.01, rely=.1, relwidth=.2,relheight=.1)
#botones de la interfaz
BtnCalcular = Button(Ventana,text="Calcular (=)", command=Operar)
BtnCalcular.place(relx=.01,rely=.25,relwidth=.1)
BtnGrafica = Button(Ventana,text="Graficar (X,Y)",command=Graficar)
BtnGrafica.place(relx=.11,rely=.25,relwidth=.1)
#cambiar representaciones
BtnCambiar = Button(Ventana,text="Cambiar Representación",command=CambiarRepresentación)
BtnCambiar.place(relx=.01, rely=.3, relwidth=.2)
MenuCambio1 = ttk.Combobox(Ventana, values=["Complejo","Carteciano","Polar","Exponencial"], state='readonly')
MenuCambio1.place(relx=.01, rely=.35, relwidth=.08)
Label5 = Label(Ventana, text=">a>",bg='#1A2D3E',fg='white')
Label5.place(relx=.09, rely=.35, relwidth=.04)
MenuCambio2 = ttk.Combobox(Ventana, values=["Complejo","Carteciano","Polar","Exponencial"], state='readonly')
MenuCambio2.place(relx=.13, rely=.35, relwidth=.08)
#limbiar celdas
BtnLimpiar = Button(Ventana,text="Limpiar Celdas",command=Limpiar)
BtnLimpiar.place(relx=.01,rely=.75,relwidth=.1)
#label y entry del resultado
Label3 = Label(Ventana,text="Resultado: ",bg='#1A2D3E',fg='white')
Label3.place(relx=.01, rely=.8, relwidth=.1)
EResultado = Entry(Ventana, state='readonly',font=20)
EResultado.place(relx=.01, rely=.85, relwidth=.2,relheight=.1)
#ventana de la grafica (donde se muestra la grafica)
plt.figure(facecolor='lightgreen',clear=True)
plt.plot([0,0], [0,0])  
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfica')
plt.grid(True)
plt.tight_layout() 
plt.subplot().spines['left'].set_visible(False) #Poner la margen izquierda en el centro y hacer que no se mueva
plt.subplot().spines['bottom'].set_visible(False) #Poner la margen inferior en el centro y hacer que no se mueva
plt.subplot().spines['right'].set_visible(False) #Poner la margen derecha y hacerla invisible
plt.subplot().spines['top'].set_visible(False) #Poner la margen superior y hacerla invisible

canvas = FigureCanvasTkAgg(plt.gcf(), master=Ventana)  
toolbar = NavigationToolbar2Tk(canvas, Ventana)
toolbar.update() 
canvas.get_tk_widget().place(relx=.25, rely=0, relwidth=.5, relheight=1)
toolbar.place(relx = 0.25, rely = 0.95, relwidth = 0.5)
canvas.draw()
#Historial
Label4 = st.ScrolledText(Ventana,bg='black',fg='white',state='disabled')
Label4.place(relx=.75, rely=0,relwidth=.25,relheight=.5)
BtnBorrar = Button(Ventana,text="Borrar Historial",command=Borrar)
BtnBorrar.place(relx=.85,rely=.9,relwidth=.1)
#ejecucion de la ventana en bucle
Ventana.mainloop()