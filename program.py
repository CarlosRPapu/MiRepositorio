def función_devolver(valor1: int, valor2: int, valor3: int):
        result_suma = valor1 + valor2 + valor3
        
        if result_suma > 15:
            if valor1 > valor2 and valor1 > valor3:
                return "numero mayor: ",valor1
            elif valor2 > valor1 and valor2 > valor3:
                return "numero mayor: ",valor2
            else:
                return "numero mayor: ",valor3
        elif result_suma < 10:
            if valor1 < valor2 and valor1 < valor3:
                return "numero menor: ",valor1
            elif valor2 < valor1 and valor2 < valor3:
                return "numero menor: ",valor2
            else:
                return "numero menor: ",valor3

        else:
            if valor1 < valor2 and valor1 > valor3:
                return "numero intermedio: ",valor1
            elif valor2 < valor1 and valor2 > valor3:
                return "numero intermedio: ",valor2
            else:
                return "numero intermedio: ",valor3
            
numero1 = int(input("Ingrese numero 1:"))
numero2 = int(input("\nIngrese numero 2:"))
numero3 = int(input("\nIngrese numero 3:"))

result = función_devolver(numero1,numero2,numero3)
print("\n",result)