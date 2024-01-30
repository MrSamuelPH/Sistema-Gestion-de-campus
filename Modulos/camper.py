from.variable import save,getAll
import os
def create ():
    os.system('clear')
    print("""          
        ----------------------------
        +++ Formularo del camper +++
        ----------------------------
          """)
    save({
        "Nombre": input("ingrese su nombre camper :"),
        "Apellido": input("ingrese su apellido camper :"),
          "Edad": input("ingrese su edad camper :")
    })
    os.system("pause")



def read():
    print("""          
        ------------------------
        +++ Tabla del camper +++
        ------------------------
          """)
    for i,val in enumerate(getAll()):
        plantilla += f"""
        {val}
        """
    print("""          
        --------------------------
        * NOMBRE * APELLIDO * EDAD
        --------------------------
          """)

    os.system("pause")
def update():
    print("El camper se actualizo")
def delete ():
    print("el camper se borro")
def menu():
    
    
    menu = ["\n1.Guardar:  \n2.Buscar: \n3.Actualizar: \n4.Borrar: \n5.salir: "]

    
    while(True):
        os.system('clear')
        print("""          
        -----------------------
        +++ Menu del camper +++
        -----------------------  
          """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input())
            if(opc<=len(menu)and opc>0):
               match(opc):
                   case 1:
                       create()
                   case 2:
                       read()
                   case 3:
                       update()
                   case 4:
                       delete()
                   case 5:
                       break
                           
        except ValueError:
            print("la opcion no es valida por favor" "digite un numero")

   