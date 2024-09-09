import os
#def ejercitario():
# Ejercitario 3
while(True):
    ejercicio = int(input(f"""                    
Elija del 1 al 9 que ejercitario desea probar
O presione "0" para salir!: 
                          
"""))
    if (ejercicio == 1):

        """
        1- En una tienda se ha establecido la siguiente oferta: por 
        compras menores a 100.000 se hace un descuento de 8%, pero 
        para compras a partir de 100.000 el descuento es de 10%. Se 
        pide ingresar la cantidad y el precio del producto que se compra 
        y determinar cuánto se descontará y cuanto se cobrará.
        """
        compra = int(input("Ingrese el valor de la compra: "))
        if (compra >= 0):
            print("Valor incorrecto!")
        elif (compra > 100000):
            descuento = compra * 0.08
            pago = compra - descuento
            print("El descuento sera del 8%: ",descuento)
            print("El total a pagar sera de: ",pago)
        else:
            descuento = compra * 0.1
            pago = compra - descuento
            print("El descuento sera del 10%: ",descuento)
            print("El total a pagar sera de: ",pago)

    elif (ejercicio == 2):
        
        """
        2- Una empresa quiere hacer una compra de varias piezas de la 
        misma clase en una fábrica de refacciones. La empresa 
        dependiendo del monto total de la compra decidirá qué hacer 
        para pagar al fabricante.
        Si el monto total de la compra excede de 500000 la empresa 
        tendrá la capacidad de invertir de su propio dinero un 55% del 
        monto de la compra, pedir prestado al banco un 30% y el resto lo 
        pagará solicitando un crédito al fabricante.
        Si el monto total de la compra no excede de 500000 la empresa 
        tendrá capacidad de invertir de su propio dinero un 70% y el 
        restante 30% lo pagará solicitando crédito al fabricante.
        El fabricante cobra por concepto de intereses un 20% sobre la 
        cantidad que se le pague a crédito.
        """

        MONTO_MAXIMO = 500000
        compra = int(input("Ingrese el monto total de la compra: "))
        if (compra > MONTO_MAXIMO):
            inversion = compra * 0.55
            prestamo = compra * 0.30
            credito = compra - (inversion + prestamo)
            interes = credito * 0.20
            total = inversion + prestamo + credito + interes
        else:
            inversion = compra * 0.70
            prestamo = compra * 0
            credito = compra - (inversion + prestamo)
            interes = credito * 0.20
            total = inversion + prestamo + credito + interes
        print(f"""
        El total de la compra es: {compra},
        La empresa hara una inversion de: {inversion},
        El prestamo al banco sera de: {prestamo},
        Se solicitara al fabricante un credito por: Gs. {credito} que se cobrara 
        con un interes del 20% en: Gs. {interes};
        El total a gastar por la empresa sera de: Gs. {total}
        """)

    elif (ejercicio == 3):

        """
        3- Un vendedor recibe un sueldo base más un 10% extra por 
        comisión de sus ventas, el vendedor desea saber cuánto dinero 
        obtendrá por concepto de comisiones por las tres ventas que 
        realiza en el mes y el total que recibirá en el mes tomando en 
        cuenta su sueldo base más comisiones.
        """

        venta1 = int(input("Valor de la venta: "))
        venta2 = int(input("Valor de la venta: "))
        venta3 = int(input("Valor de la venta: "))
        SUELDO = 2798309
        comision = (venta1 + venta2 + venta3) * 0.1
        print("El valor total de las comisiones sera de: Gs. ",comision)
        print(f"""
    Teniendo en cuenta el salario base de: Gs. {SUELDO}, se estipula
    el cobro de su sueldo bruto de: Gs. ",{SUELDO + comision}
    """)

    elif (ejercicio == 4):

        """
        4- Una tienda ofrece un descuento del 15% sobre el total de la 
        compra, y un cliente desea saber cuánto deberá pagar finalmente 
        sobre su compra.
        """

        compra = int(input("Ingrese el valor de su compra: "))
        descuento = compra * 0.15
        total = compra - descuento
        print(f"""
    El total de su compra es de: Gs. {compra},
    el descuento aplicado es del 15%: Gs. {descuento},
    el total a abonar en caja es de: Gs. {total}
        Gracias por su compra!!
    """)
        
    elif (ejercicio == 5):

        """
        5- Calcular el nuevo salario de un obrero si obtuvo un incremento 
        del 25% sobre su salario anterior.
        """

        salario = int(input("Ingrese el salario del obrero: "))
        incremento = salario * 0.25
        salario_final = salario + incremento
        print(f"""
    El salario base del obrero tendra un incremento de: Gs. {incremento};
    su salario final sera de: Gs. {salario_final}
    """)
        
    elif (ejercicio == 6):

        """
        6- Leer dos números, si son iguales que se multipliquen, si el 
        primero es mayor que el segundo que se resten y sino que se 
        sumen.
        """
        num1 = int(input("Introduzca un numero cualquiera: "))
        num2 = int(input("Introduzca un numero cualquiera: "))
        if (num1 == num2):
            print("Los numeros son iguales, se multiplican: ",num1 * num2)
        elif (num1 > num2):
            print("El primer valor es mayor, se realizara un resta: ",num1 - num2)
        else:
            print("El primer valor es menor, se realizara una suma: ",num1 + num2)

    elif (ejercicio == 7):

        """
        7- El IPS quiere clasificar a las personas que se jubilarán en el año 
        2017. Existen tres tipos de jubilaciones, por edad, por antigüedad 
        joven y por antigüedad adulta. Las personas para la jubilación por 
        edad deben tener 60 años o más y una antigüedad en su empleo 
        de menos de 25 años.
        Las personas para la jubilación por antigüedad joven deben tener 
        menos de 60 años y una antigüedad en su empleo de 25 años o 
        más.
        Las personas para antigüedad adulta deben tener 60 años o más 
        y una antigüedad en su empleo de 25 años o más.
        """
        edad = int(input("Ingrese su edad: "))
        antiguedad = int(input("Ingrese su antiguedad: "))
        if (edad >= 60) and (antiguedad < 25):
            print("Se le dara una jubilacion por edad")
        elif (edad < 60) and (antiguedad >=25):
            print("Se le dara una jubilacion por antiguedad joven")
        elif (edad >= 60) and (antiguedad >=25):
            print("Se le dara una jubilacion por antiguedad adulta")

    elif (ejercicio == 8):

        """
        8- En una tienda se efectúa una promoción en la cual se hace un 
        descuento sobre el valor de la cuenta total, según el color de la 
        bolilla que el cliente saque al pagar en caja. Si la bolilla es de 
        color blanco no se hará descuento alguno, si es verde se le hará 
        un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si 
        es roja un 100%. Determinar la cantidad final que el cliente 
        deberá pagar por su compra. Se sabe que sólo hay bolillas de los 
        colores mencionados.
        """

        import random
        compra = int(input("Ingrese el valor de la compra: "))
        bolillas = ["blanco","verde","amarillo","azul","rojo"]
        descuento = [ 0, 0.1, 0.25, 0.5, 1]
        sorteo = random.randint(0,4)
        total = compra * (1 - descuento[sorteo])
        print(f"""
        El color de la bolilla es: {bolillas[sorteo]}
        El descuento sera de: {100 * descuento[sorteo]}%
        El monto original de la compra fue de: Gs. {compra}
        El monto a abonar en caja es de: Gs. {total}
        """)

    elif (ejercicio == 9):

        """
        9- Ingresar dos valores en las variables “maximo” y “minimo” y 
        luego ingresar un valor en la variable “temperatura”. Imprime un 
        mensaje si el valor de temperatura no está dentro del rango de 
        marcado por minimo y maximo
        """

        maximo = int(input("Ingrese un valor maximo: "))
        minimo = int(input("Ingrese un valor minimo: "))
        temperatura = int(input("Ingrese la temperatura: "))
        if (temperatura >= minimo) and (temperatura <= maximo):
            print(f"""
        La temperatura actual se encuentra dentro del rango entre
        el maximo ingresado: {maximo}, y el minimo indicado {minimo}    
        """)
        else:
            print("El valor de la temperatura no se encuentra dentro del rango indicado!")

    elif (ejercicio == 0):
        print("Hasta pronto!")
        exit()

        os.system("PAUSE")