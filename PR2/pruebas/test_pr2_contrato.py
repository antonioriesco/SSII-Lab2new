"""Bloque 1 — contrato: qué devuelven `q_learning` y `politica_de`."""

import pytest

from ayuda_pr2 import entorno_pasillo
from ssii_estacion.modelo import ACCIONES

ACCIONES_VALIDAS = {a[0] for a in ACCIONES}


def test_q_learning_devuelve_tabla_y_curva(q_learning):
    entorno = entorno_pasillo()
    salida = q_learning(entorno, 200, semilla=0)
    assert isinstance(salida, tuple) and len(salida) == 2, "devuelve (Q, curva)"
    Q, curva = salida
    assert isinstance(Q, dict) and Q, "la tabla Q no puede estar vacía"
    assert len(curva) == 2, "con 200 episodios y ventana de 100 hay 2 puntos de curva"
    assert all(isinstance(x, (int, float)) for x in curva)


def test_la_tabla_q_tiene_todas_las_acciones(q_learning):
    entorno = entorno_pasillo()
    Q, _ = q_learning(entorno, 200, semilla=0)
    for estado, valores in Q.items():
        assert set(valores) == ACCIONES_VALIDAS, f"{estado}: {sorted(valores)}"
        assert all(isinstance(v, (int, float)) for v in valores.values())


def test_politica_de_devuelve_acciones_validas(q_learning, politica_de):
    entorno = entorno_pasillo()
    Q, _ = q_learning(entorno, 200, semilla=0)
    politica = politica_de(Q)
    assert isinstance(politica, dict) and politica
    assert set(politica) == set(Q), "una acción por cada estado de la tabla"
    assert set(politica.values()) <= ACCIONES_VALIDAS


def test_politica_de_no_falla_con_una_tabla_vacia(politica_de):
    assert politica_de({}) == {}


def test_misma_semilla_mismo_resultado(q_learning):
    """El entrenamiento tiene que ser reproducible: es lo que se corrige."""
    a = q_learning(entorno_pasillo(semilla=3), 200, semilla=7)[1]
    b = q_learning(entorno_pasillo(semilla=3), 200, semilla=7)[1]
    assert a == b, "dos entrenamientos con la misma semilla dan la misma curva"


def test_decaimiento_desconocido_lanza_error(q_learning):
    with pytest.raises(ValueError):
        q_learning(entorno_pasillo(), 10, decaimiento="cuadratico")


def test_los_dos_decaimientos_se_usan(q_learning):
    """Lineal y exponencial exploran distinto: las curvas no pueden coincidir."""
    lineal = q_learning(entorno_pasillo(p_exito=0.8, semilla=3), 300, semilla=7,
                        decaimiento="lineal")[1]
    exponencial = q_learning(entorno_pasillo(p_exito=0.8, semilla=3), 300, semilla=7,
                             decaimiento="exponencial", factor_decaimiento=0.9)[1]
    assert lineal != exponencial, "el decaimiento exponencial da lo mismo que el lineal"
