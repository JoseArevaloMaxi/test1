#Definicion de variables
print("CALCULADORA!\n")
while True:
    try:

        num1 = float(input("Introduzca el primer valor: \n>"))
        op = input("Estriba el simbolo de la operacion que desea realizar, sumar (+), restar(-), multiplicar (*), dividir (/): \n>")
        num2 = float(input("Introduzca el segundo valor: \n>"))

        if op == "+":
            res = num1 + num2
            print("RESULTADO: " + str(res))
        elif op == "-":
            res = num1 - num2
            print("RESULTADO: " + str(res))
        elif op == "*":
            res = num1 * num2
            print("RESULTADO: " + str(res))
        elif op == "/":
            res = num1 / num2
            print("RESULTADO: " + str(res))
        else:
            print("ooops hay un error, en el operador debe ser + - * /")

    except ValueError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)

    print("\n------------0------------\n")
    continua = input("Quieres hacer otra operacion? (s) para aceptar: \n>")


    if continua != "s":
        print("Bye, orina antes de dormir :P")
        break













