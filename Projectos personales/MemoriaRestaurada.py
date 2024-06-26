import os
DirectorioUSB = 'unidad usb que desea recuperar'
DirectorioDestino = 'Archivos_Recuperados'
Contador = 0
if not os.path.exists(DirectorioDestino):
    os.makedirs(DirectorioDestino)
with open(DirectorioUSB, 'rb') as Usb:
    while True:
        Datos = Usb.read(1024)
        if not Datos:
            break
        Inicio = Datos.find(b'\xFF\xD8\xFF\xE0\x00\x10')
        while Inicio != -1:
            Fin = Datos.find(b'\xFF\xD9', Inicio)
            if Fin != -1:
                LongitudArchivo = Fin + 2 - Inicio
                with open(os.path.join(DirectorioDestino, f'{Contador}.jpg'),'wb')as ImgFile:
                    ImgFile.write\
                        (Datos[Inicio:Inicio+LongitudArchivo])
                Contador += 1
                Inicio = Datos.find(b'\xFF\xD8\xFF\xE0\x00\x10',Fin + 2)
            else:
                DatosExtra = Usb.read(1024)
                if not DatosExtra:
                    break
                Datos += DatosExtra
                continue
# JPG
# encabezado:\xFF\xD8\xFF\xE0\x00\x10
# terminal:\xFF\xD9

# PNG
# encabezado:\x89\x50\x4E\x47\x0D\x0A\x1A\x0A
# terminal:\x49\x45\x4E\x44\xAE\x42\x60\x82