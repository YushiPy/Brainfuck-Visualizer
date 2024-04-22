
from typing import Callable, Literal, overload

from tape import Tape
from exceptions import MismatchedBrackets

import settings

type Routine = list[tuple[Callable[[], None]] | 
                    tuple[Callable[[int], None], int] | 
                    tuple[Callable[[int, int], None], int, int] |
                    tuple[Callable[[Routine], None], Routine]]


class Interpreter(Tape):
    
    def __init__(self, code: str, size: int = settings.SIZE) -> None:
        super().__init__(size)
        
        self.code = "".join(filter(set("><+-[],.").__contains__, code))

        self.input: list[int] = [0] # input is popped from the top until reaching 0
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
        start = index
        
        for index, char in enumerate(self.code[index + 1:], start + 1):
            
            count += (char == '[') - (char == ']')
        
            if not count: break
        
        if count:
            raise MismatchedBrackets.mismatched(self.code, start, count)
        
        return index
    
    
    def execute_routine(self, routine: Routine) -> None:
        
        for a, *b in routine: 
            
            if settings.PRINT_LINE:
                print(self)
            
            a(*b) # type: ignore
    
    
    def do_while(self, routine: Routine) -> None:
        
        while self.byte:
            self.execute_routine(routine)
    
    
    def __parse(self, start: int | None = None, end: int | None = None) -> Routine:
        
        if start is None: start = 0
        if end is None: end = len(self.code) # end represents an exclusive index
        
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
            inside_routine = self.__parse(index + 1, inside_end) # +1 remove brackets, end is exclusive already
            
            routine.append((self.do_while, inside_routine))
            
            index = inside_end + 1
        
        return routine

    
    @overload
    def run(self, _input: list[int | str] | str) -> list[int]: ...
    @overload
    def run(self, _input: list[int | str] | str, to_string: Literal[1, True]) -> str: ...
    
    def run(self, _input: list[int | str] | str, to_string: Literal[1, True] | None = None) -> list[int] | str:
        
        self.input = [0] + [i if isinstance(i, int) else ord(i) for i in _input][::-1]
        self.output = []

        self.__run()

        return "".join(map(chr, self.output)) if to_string else self.output


    def __run(self) -> list[int]:

        self.execute_routine(self.__parse())
        
        return self.output
