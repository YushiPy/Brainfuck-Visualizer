
from typing import Callable, overload

from tape import Tape
from settings import TAPE_SIZE, Characters

class Interpreter:
	
	code: str
	tape: Tape

	forward_map: dict[int, int]
	backward_map: dict[int, int]

	@staticmethod
	def make_map(code: str) -> dict[int, int]:

		result: dict[int, int] = {}

		indeces: list[int] = []

		for i, a in enumerate(code):

			if a == Characters.START_LOOP:
				indeces.append(i)
			
			elif a == Characters.END_LOOP:
				result[i] = indeces.pop()

		return result

	def __init__(self, code: str, size: int = TAPE_SIZE) -> None:
		
		self.code = "".join(filter(Characters.VALID_CHARACTERS.__contains__, code))
		self.tape: Tape = Tape(size)

		self.backward_map = Interpreter.make_map(self.code)
		self.forward_map = {b : a for a, b in self.backward_map.items()}

		self.actions: list[Callable[[int], None]] = []
	
	@overload
	def run(self, _input: str | list[int], as_int: None) -> str: ...
	@overload
	def run(self, _input: str | list[int], as_int: int = 0) -> list[int]: ...

	def run(self, _input: str | list[int], as_int: int | None = None) -> str | list[int]:

		if isinstance(_input, str):
			_input = list(map(ord, _input))

		_input.reverse()
		
		output: list[int] = []

		index: int = 0
		length: int = len(self.code)

		while index < length:
			
			char: str = self.code[index]

			if char == Characters.RIGHT:
				self.tape.move_by(1)

			elif char == Characters.LEFT:
				self.tape.move_by(-1)
			
			elif char == Characters.INCREASE:
				self.tape.increase(1)
			
			elif char == Characters.DECREASE:
				self.tape.increase(-1)
			
			elif char == Characters.START_LOOP:
				if not self.tape.byte:
					index = self.forward_map[index]
			
			elif char == Characters.END_LOOP:
				index = self.backward_map[index] - 1
			
			elif char == Characters.PRINT:
				output.append(self.tape.byte)

			elif char == Characters.READ:
				self.tape.set_value(_input.pop())
			
			index += 1

		if as_int is None:
			return "".join(map(chr, output))

		return output
