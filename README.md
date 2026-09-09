## Explicación

### Contrato de los modificadores

`ModificadorTarifa` define el contrato que tienen que cumplir los distintos modificadores de tarifa. Cada modificador debe implementar el método `aplicar(total, horas)`, aunque cada uno puede realizar un cálculo diferente. De esta forma se pueden agregar distintos tipos de modificadores sin tener que cambiar la forma en la que `Estadia` calcula el total.

### EstadiaMensual como especialización

`EstadiaMensual` es una especialización de `Estadia` porque una estadía mensual sigue siendo una estadía, pero agrega la característica del descuento. Por eso hereda de `Estadia` y reutiliza su comportamiento mediante `super()`, en lugar de implementarse como un modificador de tarifa.