planes = {
    "F001": ["Plan Básico", "mensual", 1, False, False, "libre"],
    "F002": ["Plan Full", "mensual", 1, True, True, "libre"],
    "F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
    "F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"],
    "F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"],
    "F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"]
}

inscripciones = {
    "F001": [14990, 30],
    "F002": [22990, 10],
    "F003": [39990, 0],
    "F004": [35990, 6],
    "F005": [159990, 2],
    "F006": [18990, 15]
}


def leer_opcion():
    while True:
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1. Cupos por tipo de plan")
            print("2. Búsqueda de planes por rango de precio")
            print("3. Actualizar precio de plan")
            print("4. Agregar plan")
            print("5. Eliminar plan")
            print("6. Salir")
            print("====================================")
            op = int(input("Ingrese opción: "))
            if op >= 1 and op <= 6:
                return op
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("Debe seleccionar una opción válida")


def cupos_tipo(tipo, planes, inscripciones):
    total = 0

    for codigo in planes:
        if planes[codigo][1].lower() == tipo.lower():
            total += inscripciones[codigo][1]

    print("El total de cupos disponibles es:", total)


def busqueda_precio(pmin, pmax, planes, inscripciones):
    lista = []

    for codigo in inscripciones:
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]

        if precio >= pmin and precio <= pmax and cupos != 0:
            nombre = planes[codigo][0]
            lista.append(nombre + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        print("Los planes encontrados son:")
        print(lista)


def buscar_codigo(codigo, inscripciones):
    codigo = codigo.upper()

    for c in inscripciones:
        if c.upper() == codigo:
            return True

    return False


def actualizar_precio(codigo, nuevo_precio, inscripciones):
    codigo = codigo.upper()

    if buscar_codigo(codigo, inscripciones):
        inscripciones[codigo][0] = nuevo_precio
        return True

    return False


def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return True


def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True


def validar_tipo(tipo):
    if tipo.lower() == "mensual" or tipo.lower() == "trimestral" or tipo.lower() == "anual":
        return True
    return False


def validar_duracion(duracion):
    if duracion > 0:
        return True
    return False


def validar_sn(valor):
    if valor.lower() == "s" or valor.lower() == "n":
        return True
    return False


def validar_horario(horario):
    if horario.strip() == "":
        return False
    return True


def validar_precio(precio):
    if precio > 0:
        return True
    return False


def validar_cupos(cupos):
    if cupos >= 0:
        return True
    return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    codigo = codigo.upper()

    if buscar_codigo(codigo, inscripciones):
        return False

    planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]

    return True


def eliminar_plan(codigo, planes, inscripciones):
    codigo = codigo.upper()

    if buscar_codigo(codigo, inscripciones):
        del planes[codigo]
        del inscripciones[codigo]
        return True

    return False


opcion = 0

while opcion != 6:

    opcion = leer_opcion()

    if opcion == 1:
        tipo = input("Ingrese tipo de plan a consultar: ")
        cupos_tipo(tipo, planes, inscripciones)

    elif opcion == 2:

        while True:
            try:
                pmin = int(input("Ingrese precio mínimo: "))
                pmax = int(input("Ingrese precio máximo: "))
                break
            except:
                print("Debe ingresar valores enteros")

        busqueda_precio(pmin, pmax, planes, inscripciones)

    elif opcion == 3:

        seguir = "s"

        while seguir.lower() == "s":

            codigo = input("Ingrese código del plan: ").upper()

            while True:
                try:
                    nuevo = int(input("Ingrese nuevo precio: "))
                    break
                except:
                    print("Debe ingresar un número entero")

            if actualizar_precio(codigo, nuevo, inscripciones):
                print("Precio actualizado")
            else:
                print("El código no existe")

            seguir = input("¿Desea actualizar otro precio (s/n)?: ")

    elif opcion == 4:

        codigo = input("Ingrese código del plan: ").upper()
        nombre = input("Ingrese nombre del plan: ")
        tipo = input("Ingrese tipo (mensual/trimestral/anual): ").lower()

        try:
            duracion = int(input("Ingrese duración (meses): "))
            precio = int(input("Ingrese precio: "))
            cupos = int(input("Ingrese cupos: "))
        except:
            print("Debe ingresar números enteros")
            continue

        piscina = input("¿Incluye acceso a piscina? (s/n): ").lower()
        clases = input("¿Incluye clases grupales? (s/n): ").lower()
        horario = input("Ingrese horario: ")

        if not validar_codigo(codigo):
            print("Código inválido")

        elif buscar_codigo(codigo, inscripciones):
            print("El código ya existe")

        elif not validar_nombre(nombre):
            print("Nombre inválido")

        elif not validar_tipo(tipo):
            print("Tipo inválido")

        elif not validar_duracion(duracion):
            print("Duración inválida")

        elif not validar_sn(piscina):
            print("Dato inválido")

        elif not validar_sn(clases):
            print("Dato inválido")

        elif not validar_horario(horario):
            print("Horario inválido")

        elif not validar_precio(precio):
            print("Precio inválido")

        elif not validar_cupos(cupos):
            print("Cupos inválidos")

        else:

            if piscina == "s":
                piscina = True
            else:
                piscina = False

            if clases == "s":
                clases = True
            else:
                clases = False

            if agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos, planes, inscripciones):
                print("Plan agregado")
            else:
                print("El código ya existe")

    elif opcion == 5:

        codigo = input("Ingrese código del plan: ").upper()

        if eliminar_plan(codigo, planes, inscripciones):
            print("Plan eliminado")
        else:
            print("El código no existe")

print("Programa finalizado.")