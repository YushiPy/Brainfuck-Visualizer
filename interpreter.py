
from typing import Callable, overload

from exceptions import InvalidMacro
from tape import Tape
from settings import TAPE_SIZE, Characters
from macros import MACROS

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

	@staticmethod
	def parse_code(code: str) -> str:

		result: str = ""

		index: int = 0
		length: int = len(code)

		while index < length:

			if code[index] not in Characters.VALID_CHARACTERS:
				index += 1
				continue

			if code[index] != Characters.MACRO_CHAR:
				result += code[index]
				index += 1
				continue
			
			marker: int = index

			index += 1

			while index < length and code[index] != '(':
				index += 1

			if index == length and code[index] != '(':
				raise InvalidMacro.no_args(code[marker + 1: index], marker)

			macro_name: str = code[marker + 1: index]

			if macro_name not in MACROS:
				raise InvalidMacro.invalid_name(macro_name, marker)
			
			index += 1

			func: Callable[..., str] = MACROS[macro_name]

			start: int = index
			count: int = 1

			while count and index < length:

				count += (code[index] == '(') - (code[index] == ')')
				index += 1
			
			if count:
				raise InvalidMacro.mismatched_parenthesis(macro_name, start)
			
			args: str = code[start: index - 1]

			try:
				macro_result: str = func(args)
			except ValueError:
				raise InvalidMacro.invalid_args(macro_name, args)

			result += macro_result

		return result


	def __init__(self, code: str, size: int = TAPE_SIZE) -> None:
		
		self.code = Interpreter.parse_code(code)
		self.tape = Tape(size)

		self.backward_map = Interpreter.make_map(self.code)
		self.forward_map = {b : a for a, b in self.backward_map.items()}


	@overload
	def run(self, _input: str | list[int], as_int: None) -> str: ...
	@overload
	def run(self, _input: str | list[int], as_int: int = 0) -> list[int]: ...

	def run(self, _input: str | list[int], as_int: int | None = None) -> str | list[int]:

		if isinstance(_input, str):
			_input = list(map(ord, _input))

		_input.reverse()
		
		output: list[int] = []

		debug: bool = False

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
			

			elif char == Characters.TOGGLE_DEBUG:
				debug = not debug
			
			elif char == Characters.SET_DEBUG:
				debug = True

			elif char == Characters.RESET_DEBUG:
				debug = False

			if debug:
				print(self.tape)

			index += 1

		if as_int is None:
			return "".join(map(chr, output))

		return output
