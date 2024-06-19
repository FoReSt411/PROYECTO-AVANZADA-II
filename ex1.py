input("BIENVENIDO A LA DIVISION, PRESIONA ENTER PARA CONTINUAR :)")
num1= int(input("INGRESE EL PRIMER NUMERO:  "))
num2= int(input("INGRESE EL SEGUNDO :  "))

if num1 == 0:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("ERROR")
    exit()
    input ("PRESIONA ENTER PARA CONTINUAR")
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    if num2 == 0:
        
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("ERROR")
        input ("PRESIONA ENTER PARA CONTINUAR")
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
    else:
        div= (num1/num2)
        print (div)
    input ("PRESIONA ENTER PARA CONTINUAR")
import os
os.system('cls' if os.name == 'nt' else 'clear')
