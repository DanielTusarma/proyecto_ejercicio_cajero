# Lista para guardar los usuarios creados
usuarios = []

# función que permite crear un usuario nuevo
def crear_usuario():
    print("*** Crear usuarios ***")
    while True:
        nombre = input("Ingrese su nombre de usuario: ").strip().lower()
        
        # validamos que el usuario no exista en la lista de usuarios
        existe = False
        for usuario in usuarios:
            if usuario.get("nombre") == nombre:
                existe = True
                break
        if existe:
            print("Usuario ya existente con este nombre. Ingrese uno diferente.\n")
            continue
                
        contraseña = input("Ingrese su contraseña '4 digitos (0-9)': ")
        
        # validamos que la contraseña sea de 4 digitos
        if len(contraseña) == 4 and contraseña.isdigit():
                usuario = {"nombre": nombre, "contraseña": contraseña, "saldo": 0}
                usuarios.append(usuario)
                print("*** Usuario creado satisfactoriamente. ***") 
                break
        else:
            print("La contraseña no es correcta. Intente de nuevo")

# función que permite depositar saldo en un usuario creado     
def depositar_saldo():
    print("*** Depositar saldo ***")
    
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        encontrado = False
        
        # recorremos la lista con los usuarios ya registrados para encontrar la coincidencia 
        for usuario in usuarios:
            if usuario.get("nombre") == nombre and usuario.get("contraseña") == contraseña:
                saldo = float(input("Ingrese el saldo a depositar: "))
                if saldo < 0:
                    print("No se permite ingresar saldo negativo: ")
                else:
                    usuario["saldo"] += saldo
                    print("Ingreso de saldo correcto.\n")
                    encontrado = True   
                break

        if not encontrado:
            print("No hay usuarios con este nombre. Ingrese de nuevo")
        else:
            break

# función que permite retirar saldo de un usuario              
def retirar_saldo():
    print("*** Retirar saldo ***")    
    
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        encontrado = False
        
        # recorremos la lista con los usuarios ya registrados para encontrar la coincidencia  
        for usuario in usuarios:
            if usuario.get("nombre") == nombre and usuario.get("contraseña") == contraseña:
                retiro = float(input("Ingrese el saldo a retirar: "))
                if retiro > usuario.get("saldo"):
                    print("Fondos Insuficientes para este retiro: ")
                else:
                    usuario["saldo"] -= retiro
                    print("Retiro de saldo correcto.\n")
                encontrado = True    
                break
        
        if not encontrado:
            print("Usuario o contraseña incorrectos. Intente de nuevo.\n")
        else:
            break           

# función que permite consultar el saldo actual del usuario      
def consultar_saldo():
    print("*** Consultar saldo ***")    
    
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")      
        encontrado = False  
        
        for usuario in usuarios:
            if usuario.get("nombre") == nombre and usuario.get("contraseña") == contraseña:
                print(f"Su saldo es de: $ {usuario.get("saldo")}")
                encontrado = True
                break 
                
        if not encontrado:
            print("Usuario o contraseña incorrectos. Ingrese de nuevo\n")
        else:
            break      

# función de menú principal    
def menu():
    while True:
        print("\n*** Menú de opciones ***")
        print("1. Crear usuario")
        print("2. Depositar saldo")
        print("3. Retirar saldo")
        print("4. Consultar saldo")
        print("5. Salir")
        
        opcion = input("\nIngrese una opción (1-5): ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            depositar_saldo()
        elif opcion == "3":
            retirar_saldo()
        elif opcion == "4":
            consultar_saldo()
        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida. Ingrese una opción válida")
            
if __name__ == "__main__":
    menu()