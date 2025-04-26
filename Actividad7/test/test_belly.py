# test/test_belly.py
import pytest
from features.steps.belly_steps import convertir_tiempo_a_horas
from src.belly import Belly
from unittest.mock import Mock

@pytest.mark.parametrize("entrada,esperado", [
    ("90 minutos", 1.5),
    ("3600 segundos", 1.0),
    ("1 hora y 30 minutos", 1.5),
    ("1 hora y 30 minutos y 45 segundos", 1.5125),
    ("media hora", 0.5),
])
def test_convertir_tiempo_a_horas(entrada, esperado):
    resultado = convertir_tiempo_a_horas(entrada)
    assert round(resultado, 4) == round(esperado, 4)

def test_estomago_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_estomago_no_gruñe_si_no_espera_suficiente():
    belly = Belly()
    belly.comer(20)
    belly.esperar(1)
    assert belly.esta_gruñendo() == False

def test_pepinos_comidos():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15

def test_predecir_gruñido():
    belly = Belly()
    assert belly.predecir_gruñido(12, 2) == True
    assert belly.predecir_gruñido(12, 1) == False

def test_clock_simulado():
    clock_simulado = Mock()
    clock_simulado.return_value = "2025-02-22 12:00"

    # "2025-02-22 10:00" como los 12 pepinos
    belly = Belly(clock_simulado)
    belly.comer(12)
    belly.esperar(2)

    assert belly.esta_gruñendo()
    assert belly.clock() == "2025-02-22 12:00"
