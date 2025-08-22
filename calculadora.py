num1 = float(input("Digite seu primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite seu segundo número:"))

if operador == "+":
    resultado = num1 + num2
    print(resultado)
elif operador == "-":
  resultado = num1 - num2
  print(resultado)
elif operador == "*":
  resultado = num1 * num2
  print(resultado)
elif operador == "/":
  resultado = num1 / num2
  print(resultado)
else:
  print("Operador incompativel.")
