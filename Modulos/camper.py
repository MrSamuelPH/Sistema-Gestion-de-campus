import os
from .variable import save, getAll, camper

def create():
        os.system ('cls')
        print("""
    +++++++++++++++++++++++++++++
    +   FORMULARIO DEL CAMPER   +
    +++++++++++++++++++++++++++++
""")
        save({
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido": input("Ingrese el apellido del camper: "),
        "Edad": int(input("Ingrese la edad del camper: ")),
        "Genero": input("Ingrese el genero del camper: ")
    })
        os.system('pause')

def read (codigo=None):
    os.system('cls')
    print("""
    ++++++++++++++++++++++++
    +   TABLA DEL CAMPER   +
    ++++++++++++++++++++++++
    """)
    if(codigo == None):
       for i, val in enumerate(getAll()):
            print(f"""
            ________________________________   
            Codigo: {i+1}
            Nombre: {val.get('Nombre')}
            Apellido: {val.get('Apellido')}
            Edad: {val.get('Edad')}
            Genero: {val.get('Genero')}
            ________________________________
            """)
    else:
        val = getAll()[codigo-1]
        print(f"""
         ________________________________   
        Codigo: {codigo}
        Nombre: {val.get('Nombre')}
        Apellido: {val.get('Apellido')}
        Edad: {val.get('Edad')}
        Genero: {val.get('Genero')}
        ________________________________
        """)
    
    os.system('pause')

def update():
    bandera = True
    while (bandera):
        os.system('cls')
        read()
        print("""
        ++++++++++++++++++++++++++++
        +   ACTUALIZAR UN CAMPER   +
        ++++++++++++++++++++++++++++
        """)
        codigo = int(input("多Cual es el codigo del camper que desea eliminar?: "))
        read (codigo)
        print("""
        多 Estas seguro que deseas actualizar el camper ?
        1. Si
        2. No
        3. Cancelar
        """)
        opc = int(input())
        match(opc):
            case 1:
                val = {
                    "Nombre": input("Ingrese el nombre del camper: "),
                    "Apellido": input("Ingrese el apellido del camper: "),
                    "Edad": int(input("Ingrese la edad del camper: "))
                }
                camper[codigo-1] = val
                os.system('cls')
                print(f"""
                El camper fue actualizado
                _______________________________   
                Codigo: {codigo}
                Nombre: {val.get('Nombre')}
                Apellido: {val.get('Apellido')}
                Edad: {val.get('Edad')}
                Genero: {val.get('Genero')}
                ________________________________
                """)
                os.system('pause')
                bandera = False 
            case 3:
                bandera = False
def delete():
    bandera = True
    while (bandera):
        os.system('cls')
        read()
        print("""
        ++++++++++++++++++++++++++
        +   ELIMINAR UN CAMPER   +
        ++++++++++++++++++++++++++
        """)
        codigo = int(input("多Cual es el codigo del camper que desea eliminar?: "))
        if 0<= codigo - 1 <len(camper):
            val = camper[codigo - 1]
        print("""
        多 Estas seguro que deseas eliminar el camper ?
        1. Si
        2. No
        3. Cancelar
        """)
        opc = int(input())
        match(opc):
            case 1: 
                val = camper.pop(codigo)
                os.system('cls')
                val = getAll()[codigo-1]
                print(f"""
                El camper fue eliminado
                _______________________________   
                Codigo: {codigo}
                Nombre: {val.get('Nombre')}
                Apellido: {val.get('Apellido')}
                Edad: {val.get('Edad')}
                Genero: {val.get('Genero')}
                ________________________________
                """)
                os.system('pause')
                bandera = False 
            case 3:
                bandera = False
        
def menu():
    menu = [" Guardar", " Buscar", " Actualizar", " Eliminar", " Salir"]
    while(True):
        os.system ('cls')
        print("""
    +++++++++++++++++++++++
    +   MENU DEL CAMPER   +
    +++++++++++++++++++++++
""")
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc<=len(menu)and opc>0):
                match(opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5: break
        except ValueError:
            print("La opcion no esta habilitada")