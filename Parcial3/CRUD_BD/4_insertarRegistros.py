from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id,nombre,direccion, tel) VALUES (NULL, 'Jesús Manuel', 'col.benignomontoya', '6183650520')"

    micursor.execute(sql)
    # Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelva a intentar... mas tarde...")
else:
    print("Registro insertado correctamente")