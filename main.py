def calculos(accion, a, b):
  
  if accion == "1":
    print("La suma es: ", a + b)
    agradecimiento()
    reiniciar()
  elif accion == "2":
    print("La resta es: ", a - b)
    agradecimiento()
    reiniciar()
  elif accion == "3":
    print("La multiplicacion es: ", a * b)
    agradecimiento()
    reiniciar()
  elif accion == "4":
    if b == 0:
      print("No se puede dividir por 0")
    else:
      print("La division es: ", a / b)
      agradecimiento()
      reiniciar()
  elif accion == "5":
    print(a ** b)
    agradecimiento()
    reiniciar()
  else:
    print("Operacion no valida")
    print("Debe Ingresar, solo numeros naturales (positivos): ")
    reiniciar()
    
def bienvenida ():
  print("************************************************")
  print("Bienvenido, le saluda la CalculadoraMaxProv600")
  print("************************************************")
  print("Esta calculadora solo admite numeros naturales(positivos)")
  print("************************************************")

def ingreso_numeros():
  resp1 = input("Por favor, ingresar primer digito: ")
  ingreso_numeros.num1 = int(resp1)
  if ingreso_numeros.num1 < 0:
    print("Debe Ingresar, solo numeros naturales (positivos): ")
    reiniciar()
  else:
    #print(num1)
    print("************************************************")

  resp2 = input("Por favor, ingresar ultimo digito: ")
  ingreso_numeros.num2 = int(resp2)
  if ingreso_numeros.num2 < 0:
    print("Debe Ingresar, solo numeros naturales (positivos): ")
    reiniciar()    
  else:
    #print(num2)
    print("************************************************")

def ingreso_operacion():
  print("Que operacion quiere realizar? ")
  print("1.Suma") 
  print("2.Resta ")
  print("3.Multiplicacion ")
  print("4.Division") 
  print("5.Potencia")
  ingreso_operacion.operacion = input("Respuesta: ")
  print("************************************************")

def reiniciar():
  restart = input("Desea iniciar nuevamente? (Y/N): ")
  if restart == "Y" or restart == "y":
    main()
  else:
    print("Bye")
    exit()
    
def agradecimiento():
  print("Gracias por usar la CalculadoraMaxProv600")

def main():

  bienvenida()
  
  try:
    ingreso_numeros()
    
    ingreso_operacion()

    calculos(ingreso_operacion.operacion, ingreso_numeros.num1, ingreso_numeros.num2)  
      
  except Exception as e:
    print("Debe Ingresar, solo numeros naturales (positivos): ")
    print(e)
    reiniciar()
#Ejecutar el codigo main
main()
