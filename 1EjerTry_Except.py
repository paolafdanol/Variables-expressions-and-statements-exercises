ent=input("Introduzca la temperatura Fahrenheit: ")
try:
    fahr = float(ent)
    cel=(fahr-32.0)*(5.0/9.0)
    print(cel)
except:
    print("\n** Por favor, introduzca un numero **")