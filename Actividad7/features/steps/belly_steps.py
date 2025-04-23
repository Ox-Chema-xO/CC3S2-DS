from behave import given, when, then
import re
import random
import time
# Función para convertir palabras numéricas en ingles y espanol a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra)
    except ValueError:
        palabra = palabra.lower()
        #es
        numeros_es = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5
        }
        #en
        numeros_en = {
            "zero": 0, "one": 1, "a": 1, "an": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
            "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
            "half": 0.5
        }
        if palabra in numeros_es:
            return numeros_es[palabra]
        elif palabra in numeros_en:
            return numeros_en[palabra]

        return 0
    
def generar_tiempo_aleatorio(texto):
    texto = texto.lower().strip()
    match = re.match(
    r"(?:un\s+tiempo\s+aleatorio\s+)?(entre|between)\s+([\d\.]+)\s+(y|and)\s+([\d\.]+)\s+(horas?|hours?)",texto)
    if match:
        min_horas = float(match.group(2)) or "0"
        max_horas = float(match.group(4)) or "0"
        return round(random.uniform(min_horas+0.5,max_horas), 2)
    return None  
    
def convertir_tiempo_a_horas(time_description):
    tiempo_random = generar_tiempo_aleatorio(time_description)
    if tiempo_random is not None:
        return tiempo_random

    time_description = time_description.strip('"').lower()
    time_description = time_description.replace(",", " ")
    time_description = time_description.replace(" y ", " ")
    time_description = time_description.replace(" and ", " ")
    time_description = time_description.strip()

    if time_description in ['media hora', 'half an hour']:
        return 0.5

    pattern = re.findall(r'(\w+(?:\.\d+)?)\s*(horas?|hours?|minutos?|minutes?|segundos?|seconds?)', time_description)

    total_time_in_hours = 0.0
    for cantidad, unidad in pattern:
        try:
            valor = convertir_palabra_a_numero(cantidad)
        except ValueError as e:
            raise ValueError(f"Error al interpretar la cantidad: {e}")

        if "hora" in unidad or "hour" in unidad:
            total_time_in_hours += valor
        elif "minuto" in unidad or "minute" in unidad:
            total_time_in_hours += valor / 60
        elif "segundo" in unidad or "second" in unidad:
            total_time_in_hours += valor / 3600
        else:
            raise ValueError(f"Unidad no reconocida: {unidad}")

    return round(total_time_in_hours, 4)



@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context, cukes):
    try: 
        context.error = None
        context.belly.comer(float(cukes))
    except Exception as e:
        context.error = e
        
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = convertir_tiempo_a_horas(time_description)
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('deberia producirse un error')
def step_then_should_error(context):
    assert context.error is not None, "Se esperaba un error pero no ocurrio."

@then('deberia haber comido {esperado:g} pepinos')
def step_then_verificar_pepinos(context, esperado):
    assert context.belly.pepinos_comidos == float(esperado), \
        f"Se esperaban {esperado} pepinos, pero se comieron {context.belly.pepinos_comidos}"
    

@given('que quiero saber si gruñire tras comer {pepinos:g} pepinos')
def step_given_predecir_comida(context, pepinos):
    context.pepinos_a_predecir = pepinos

@given('espero {tiempo} horas')
def step_given_predecir_tiempo(context, tiempo):
    context.tiempo_a_predecir = float(tiempo)

@then('deberia predecirse que el estomago gruñira')
def step_then_predecir_gruñido_positivo(context):
    prediccion = context.belly.predecir_gruñido(context.pepinos_a_predecir, context.tiempo_a_predecir)
    assert prediccion, "Se esperaba que gruñera, pero no se predijo gruñido."

@then('deberia predecirse que el estomago no gruñira')
def step_then_predecir_gruñido_negativo(context):
    prediccion = context.belly.predecir_gruñido(context.pepinos_a_predecir, context.tiempo_a_predecir)
    assert not prediccion, "No se esperaba gruñido, pero se predijo que si gruñiria."


@when('pregunto cuantos pepinos mas puedo comer antes de gruñir')
def step_when_pregunto_cuantos_faltan(context):
    context.pepinos_restantes = context.belly.pepinos_faltantes_antes_de_gruñir()

@then('deberia decirme que puedo comer {esperado:d} pepinos mas')
def step_then_verificar_faltantes(context, esperado):
    assert context.pepinos_restantes == esperado, \
        f"Se esperaban {esperado} pepinos restantes, pero se obtuvo {context.pepinos_restantes}"

@then('deberia registrar la fecha actual 2025-02-22 12:00')
def step_then_clock_simulado(context):
    fecha = context.belly.clock()
    print(f"[DEBUG] fecha simulada: {fecha}")
    assert fecha == "2025-02-22 12:00"
