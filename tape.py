
from constants import SIZE


class Tape(list[int]):
    
    def __init__(self, size: int = SIZE) -> None:
        super().__init__([0] * size)
        
        self.__pointer = 0
        self.__maximum = 0
    
    @property
    def byte(self) -> int:
        return self[self.__pointer]
    
    
    @byte.setter
    def byte(self, value: int) -> None:
        self.set_value(value, self.__pointer)
        
    
    def set_value(self, value: int, index: int | None = None) -> None:
        self[index if index is not None else self.__pointer] = value & 255
        
    
    def increase(self, ammount: int, index: int | None = None) -> None:
        self.set_value((self[index] if index is not None else self.byte) + ammount, index)
       
        
    def move_by(self, ammount: int = 1) -> None:
        self.move_to(self.__pointer + ammount)
        
    
    def move_to(self, index: int) -> None:

        self.__pointer = index
        self.__maximum = max(self.__pointer, self.__maximum)
    
    
    def __str__(self) -> str:

        string = str(self[:self.__maximum + 1])

        pointer_index = (self.__pointer and len(str(self[:self.__pointer]))) + (len(str(self.byte)) + 1) // 2

        string += '\n' + ' ' * (pointer_index) + '^'

        return string


    def __repr__(self) -> str:
        return f"Tape: size={len(self)}, pointer={self.__pointer}, byte={self.byte}"