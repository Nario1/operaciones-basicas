"""
Módulo para realizar operaciones matemáticas básicas y cálculo de promedios.

Este script define dos clases:
1. `OperacionesBasicas`: Permite realizar sumas y restas.
2. `CalculadoraPromedio`: Calcula el promedio de una lista de valores.

El código también incluye una ejecución principal con ejemplos de uso.

Clases:
- OperacionesBasicas: Realiza suma y resta de dos números.
- CalculadoraPromedio: Calcula el promedio de una lista de números.

Variables globales:
- NUMEROS (list[int]): Lista de números de ejemplo para calcular el promedio.
- NUM1 (int): Primer número de ejemplo para operaciones básicas.
- NUM2 (int): Segundo número de ejemplo para operaciones básicas.

Ejemplo de uso:
    - Crear una instancia de `OperacionesBasicas` y usar los métodos `sumar` y `restar`:
        operaciones = OperacionesBasicas()
        operaciones.sumar(10, 20)
        print(operaciones.obtener_resultado())  # 30

        operaciones.restar(10, 20)
        print(operaciones.obtener_resultado())  # -10

    - Crear una instancia de `CalculadoraPromedio` y calcular el promedio:
        calculadora = CalculadoraPromedio([1, 2, 3, 4, 5])
        print(calculadora.calcular_promedio())  # 3.0
"""

class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas."""

    def __init__(self):
        """Inicializa la clase con un resultado en cero."""
        self.resultado = 0

    def sumar(self, a: float, b: float) -> float:
        """
        Retorna la suma de dos números y actualiza el resultado interno.

        Args:
            a (float): Primer número.
            b (float): Segundo número.

        Returns:
            float: Resultado de la suma.
        """
        self.resultado = a + b
        return self.resultado

    def restar(self, a: float, b: float) -> float:
        """
        Retorna la resta de dos números y actualiza el resultado interno.

        Args:
            a (float): Primer número.
            b (float): Segundo número.

        Returns:
            float: Resultado de la resta.
        """
        self.resultado = a - b
        return self.resultado

    def obtener_resultado(self) -> float:
        """
        Retorna el último resultado calculado.

        Returns:
            float: Último resultado almacenado.
        """
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de números."""

    def __init__(self, valores: list[float]):
        """
        Inicializa la clase con una lista de valores numéricos.

        Args:
            valores (list[float]): Lista de valores para calcular el promedio.
        """
        if not valores:
            raise ValueError("La lista de valores no puede estar vacía.")
        self.valores = valores

    def calcular_promedio(self) -> float:
        """
        Calcula y retorna el promedio de la lista de valores.

        Returns:
            float: Promedio de los valores.
        """
        return sum(self.valores) / len(self.valores)


# Variables globales
NUMEROS: list[int] = [1, 2, 3, 4, 5]
NUM1: int = 10
NUM2: int = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    print(f"El resultado de la suma es: {operaciones.sumar(NUM1, NUM2)}")
    print(f"El resultado de la resta es: {operaciones.restar(NUM1, NUM2)}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    print(f"El promedio de los números es: {calculadora_promedio.calcular_promedio()}")
