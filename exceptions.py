
class PointerOutOfBound(Exception):

	@staticmethod
	def negative_pointer(index: int) -> "PointerOutOfBound":
		return PointerOutOfBound(f"Tried to move to negative index; pointer = {index}.")

	@staticmethod
	def too_big_pointer(index: int, size: int) -> "PointerOutOfBound":
		return PointerOutOfBound(f"Tried to move beyond last byte; pointer = {index:_} >= size = {size:_}.")

class MismatchedBrackets(Exception):
	
	@staticmethod
	def mismatched(code: str, index: int, depth: int) -> "MismatchedBrackets":

		string: str = f"Couldn't find match for bracket at {index=}; " 
		string += f"{depth} closing bracket{'s' * (depth > 1)} missing in {code=}."

		return MismatchedBrackets(string)

class InvalidMacro(Exception):

	@staticmethod
	def invalid_name(name: str) -> "InvalidMacro":
		return InvalidMacro(f"Macro \"{name}\" does not exist.")

	@staticmethod
	def mismatched_parenthesis(macro: str, index: int) -> "InvalidMacro":

		string: str = f"Couldn't match parenthesis at index={index} for macro=\"{macro}\"."

		return InvalidMacro(string)
