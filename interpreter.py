
from typing import Callable, Literal, overload
from constants import SIZE
from tape import Tape

type Routine = list[tuple[Callable[[], None]] | 
                    tuple[Callable[[int], None], int] | 
                    tuple[Callable[[int], None], int, int]]

class Interpreter(Tape):
    
    def __init__(self, code: str, size: int = SIZE) -> None:
        super().__init__(size)
        
        self.code = "".join(filter(set("><+-[],.").__contains__, code))

        self.input: list[int] = []
        self.output: list[int] = []


    def read_byte(self) -> None:
        self.byte = self.input.pop()
    
    
    def output_byte(self) -> None:
        self.output.append(self.byte)
    
    
    def find_match(self, index: int) -> int:
        
        count = 1
        
        while count:
            index += 1
            count += (self.code[index] == '[') - (self.code[index] == ']')
        
        return index
    
    
    
    @overload
    def run(self, _input: list[int | str] | str) -> list[int]: ...
    @overload
    def run(self, _input: list[int | str] | str, to_string: Literal[1, True]) -> str: ...
    
    def run(self, _input: list[int | str] | str, to_string: Literal[1, True] | None = None) -> list[int] | str:
        
        self.input = [i if isinstance(i, int) else ord(i) for i in _input]

        output = self.__run()

        return "".join(map(chr, output)) if to_string else output


    def __run(self) -> list[int]:
        return []
