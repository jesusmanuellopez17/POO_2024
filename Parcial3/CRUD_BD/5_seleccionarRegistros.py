from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="SELECT * FROM clientes"

    micursor.execute(sql)
    resultado=micursor.fetchall()

    
    for fila in resultado:
        print(f"Id:{fila[0]} | Nombre:{fila[1]} | Direccion:{fila[2]} | Telefono:{fila[3]}")

except:
    print(f"Ocurrio un error por favor vuelva a intentar... mas tarde...")
else:
    print("Registro insertado correctamente")