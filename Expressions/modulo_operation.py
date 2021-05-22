from .binary_operation import BinaryOperation


class ModuloOperation(BinaryOperation):
    """
    Операция остаток от деления
    """

    def calculate(self):
        """
        Метод вычисляет численное значение выражения

        :return: значение выражения как целое число
        """
        # raises ZeroDivisionError automatically
        return int(self._left.calculate() % self._right.calculate())
