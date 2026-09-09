import pytest

from solucion.estacionamiento import (
    Estadia,
    EstadiaMensual,
    Nocturna,
    FinDeSemana,
    facturar
)


def test_calculo_estadia_nocturna():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())

    assert estadia.total(1000) == 2400


def test_horas_invalidas():
    with pytest.raises(ValueError):
        Estadia("AB123CD", 0)


def test_modificadores_no_exponen_coleccion_interna():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())

    modificadores = estadia.modificadores

    modificadores = modificadores + (FinDeSemana(),)

    assert estadia.total(1000) == 2400
    assert len(estadia.modificadores) == 1


def test_estadia_mensual_usa_validacion_de_estadia():
    with pytest.raises(ValueError):
        EstadiaMensual("XY987ZW", 0, descuento=20)


def test_calculo_estadia_mensual():
    mensual = EstadiaMensual("XY987ZW", 2, descuento=20)
    mensual.agregar_modificador(Nocturna())

    assert mensual.total(1000) == 1920


def test_facturar_estadias_mezcladas():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())

    mensual = EstadiaMensual("XY987ZW", 2, descuento=20)
    mensual.agregar_modificador(Nocturna())

    estadias = [estadia, mensual]

    assert facturar(estadias, 1000) == 4320