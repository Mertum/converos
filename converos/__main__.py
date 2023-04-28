
class Numero:
    """
        Clase que representa un número en cualquier base definida.

        :parametro valor: El valor del número (por defecto 0).
        :parametro base: La base del número (por defecto 10, es decir, decimal).
    """
    def __init__(self, valor: str = 0, base: int = 10):
        self.__valor = valor
        self.__base = base
        if self.__base < 2 or self.__base > 36:
            raise ValueError('La base debe estar entre 2 y 36.')
        if self.hasLetter() and self.__base < 11:
            raise ValueError('La base debe ser mayor a 10 para contener letras.')

    def hasLetter(self) -> bool:
        '''
            Verifica si el número tiene letras.

            :return: True si el número tiene letras, False si no.
        '''
        return any(c.isalpha() for c in self.__valor)
    
    def __str__(self) -> str:
        '''
            Representación del número en la base definida.

            :return: El número en la base definida.
        '''
        return f'{self.__valor}({self.__base})'

    def decimal(self) -> int:
        '''
            Representación del número en decimal.

            :return: El número en decimal.
        '''
        if self.__base != 10:
            return int(self.__valor, self.__base)
        return int(self.__valor)
    
    def binario(self) -> str:
        '''
            Representación del número en binario.

            :return: El número en binario.
        '''
        if self.__base != 2:
            return bin(self.decimal())[2:]
        return self.__valor
    
    def octal(self) -> str:
        '''
            Representación del número en octal.

            :return: El número en octal.
        '''
        if self.__base != 8:
            return oct(self.decimal())[2:]
        return self.__valor
    
    def hexadecimal(self) -> str:
        '''
            Representación del número en hexadecimal.

            :return: El número en hexadecimal.
        '''
        if self.__base != 16:
            return hex(self.decimal())[2:]
        return self.__valor
    
