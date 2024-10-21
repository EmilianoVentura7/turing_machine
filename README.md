# Máquina de Turing

Este proyecto implementa una simulación de una Máquina de Turing utilizando Python y una interfaz gráfica simple con Tkinter. La máquina está diseñada para aceptar cadenas con la misma cantidad de `0`s y `1`s. 

## Descripción del problema

La máquina de Turing que se ha implementado sigue un conjunto de reglas que le permiten procesar cadenas en el formato `0^n 1^n`. Es decir, aceptará cualquier cadena que tenga un número igual de `0`s y `1`s, y los procesará reemplazando los `0`s con `X`s y los `1`s con `Y`s hasta que toda la cadena haya sido procesada.

### Reglas:

- La cadena debe contener solo `0`s y `1`s.
- La cantidad de `0`s debe ser igual a la cantidad de `1`s.
- Cadenas como `0011`, `000111`, o `01` serán aceptadas.
- Cadenas como `011`, `001`, o `111` serán rechazadas.

## Estructura del proyecto

Este proyecto tiene dos componentes principales:

1. **Simulación de la Máquina de Turing**: Implementada en la clase `TuringMachine`, esta clase maneja el procesamiento de la cinta y sigue las reglas definidas en el autómata de estados.
2. **Interfaz gráfica (Tkinter)**: La interfaz gráfica permite al usuario ingresar una cadena de `0`s y `1`s, ejecutar la máquina, y ver el resultado (si la cadena es aceptada o rechazada).

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las distribuciones estándar de Python)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/EmilianoVentura7/turing-machine.git
cd turing-machine



