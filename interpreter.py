
from typing import Callable, Literal, overload
from constants import SIZE
from tape import Tape

type Routine = list[tuple[Callable[[], None]] | 
                    tuple[Callable[[int], None], int] | 
                    tuple[Callable[[int, int], None], int, int]]

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
        """
        returns the index of the matching closing bracket
        `index` shoud be the index of the opening bracket
        """
        
        count = 1
        
        while count:
            index += 1
            count += (self.code[index] == '[') - (self.code[index] == ']')
        
        return index
    
    
    def __parse(self, start: int | None = None, end: int | None = None) -> Routine:
        
        if start is None: start = 0
        if end is None: end = len(self.code)
        
        index = start
        routine: Routine = []
        
        while index < end:
            
            char = self.code[index]
            
            if char == '>': routine.append((self.move_by, 1))
            if char == '<': routine.append((self.move_by, -1))
            if char == '+': routine.append((self.increase, 1))
            if char == '-': routine.append((self.increase, -1))
            if char == ',': routine.append((self.read_byte,))
            if char == '.': routine.append((self.output_byte,))
            
            if char != '[': 
                index += 1
                continue
            
            inside_end = self.find_match(index)
            inside_routine = self.__parse(index + 1, inside_end - 1) # +1 and -1 to remove brackets

            def inside() -> None:
                
                for a, *b in inside_routine:
                    a(*b)
            
            routine.append((inside,))
        
        return routine

    
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
