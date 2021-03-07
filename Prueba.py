class Prueba:
    for i in range(1,3):
        print("Aprendamos a contar los numeros: " + str(i))
    edad = 22
    fecha = 25
    edad, fecha = fecha,edad
    divisionEntera = 9//2
    potencia = 2**6
    print(divisionEntera,potencia)
    s = "& abc &"
    print(s.strip("&"))


    def mensajeBienvenida (nombre:str):
        print("Bienvenido a reparapp "+nombre+", le agradecemos que nos haya elegido")
    mensajeBienvenida("LUIS")

