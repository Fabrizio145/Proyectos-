temperatura=float(input("ingrese temperatura"))
escala=input("Es Farenheit (F) O es Celsius (C)").lower()

if escala == "f":
  celsius = (temperatura-32) * 5/9
  print(celsius)
elif escala == "c":
  farenheit = temperatura * 1.8 + 32
  print(farenheit)
else:
  print("escala incorrecta ")
