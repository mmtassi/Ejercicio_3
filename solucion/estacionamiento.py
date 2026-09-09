from abc import ABC, abstractmethod


class ModificadorTarifa(ABC):

    @abstractmethod
    def aplicar(self, total, horas):
        pass


class Nocturna(ModificadorTarifa):

    def aplicar(self, total, horas):
        return total + 200 * horas


class FinDeSemana(ModificadorTarifa):

    def aplicar(self, total, horas):
        return total * 1.5


class Estadia:

    def __init__(self, patente, horas):
        if patente == "":
            raise ValueError("La patente no puede estar vacia")

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        self.patente = patente
        self.horas = horas
        self._modificadores = []

    @property
    def modificadores(self):
        return tuple(self._modificadores)

    def agregar_modificador(self, modificador):
        try:
            modificador.aplicar
        except AttributeError:
            raise TypeError("El modificador no cumple el contrato")

        self._modificadores.append(modificador)

    def total(self, tarifa_por_hora):
        total = tarifa_por_hora * self.horas

        for modificador in self._modificadores:
            total = modificador.aplicar(total, self.horas)

        return total


class EstadiaMensual(Estadia):

    def __init__(self, patente, horas, descuento):
        super().__init__(patente, horas)

        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        self.descuento = descuento

    def total(self, tarifa_por_hora):
        total = super().total(tarifa_por_hora)

        descuento = total * self.descuento / 100

        return total - descuento


def facturar(estadias, tarifa_por_hora):
    total = 0

    for estadia in estadias:
        total += estadia.total(tarifa_por_hora)

    return total