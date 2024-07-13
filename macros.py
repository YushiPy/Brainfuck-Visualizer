
from typing import Callable

"""
Ascii names, such as `a` or `b` represent a byte.
`x` represents an arbitrary byte.
"""

def _copy(count: str) -> str:
	"""
	Returns a code snippet for copying the byte at the current location
	`count` spaces ahead. 

	Paramete
	--------
	- `count`: Must represent a base `10` integer. 
	Represents the distance between the source and result.

	Results
	-------
	Initial: `[a, ...]`.
	Final: `[a, x_1, ...,  x_count, a, x, 0]`.
	"""
	
	shift: int = int(count)

	right: str = ">" * shift
	left: str = "<" * shift

	return f"{right}[-]>>[-]<<{left}[-{right}+>>+<<{left}]{right}>>[-<<{left}+{right}>>]<<{left}"


def _or(on_stack: str) -> str:
	"""
	Returns a code snippet for computing `a || b`.
	
	Parameter
	--------
	- `on_stack == 0`: Returns a comparison on stack level.
	- `on_stack != 0`: Returns a comparison on information level.

	Results
	-------
	Initial = `[a, x, b, x, x, x]`.

	Final = {
	- `on_stack == 0`: `[a, x, b, x, a || b, x, 0, x, 0]`.
	- `on_stack != 0`: `[a, a || b, b, 0, x, 0]`.
	}
	"""

	if on_stack != "0":
		return ">[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>>>[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>>>+<<[[-]>>[-]<<]<<[[-]>>>>[-]<<<<]+>>>>[-<<<<->>>>]<<<<<"

	return ">>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>>>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>>>>>+<<<<[[-]>>>>[-]<<<<]>>[[-]>>[-]<<]<<+>>>>[-<<<<->>>>]<<<<<<<<"


def _and(on_stack: str) -> str:
	"""
	Returns a code snippet for computing `a && b`.
	
	Parameter
	--------
	- `on_stack == 0`: Returns a comparison on stack level.
	- `on_stack != 0`: Returns a comparison on information level.

	Results
	-------
	Initial = `[a, x, b, x, x, x]`.

	Final = {
	- `on_stack == 0`: `[a, x, b, x, a && b, x, 0, x, 0]`.
	- `on_stack != 0`: `[a, a && b, b, 0, x, 0]`.
	}
	"""

	if on_stack != "0":
		return ">[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>>>[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>[[-]>>+<<]<<[[-]>>>>+<<<<]+>>>>--[[-]<<<<->>>>]<<<<"

	return ">>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>>>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>[[-]>>>>+<<<<]>>[[-]>>+<<]<<+>>>>--[[-]<<<<[-]>>>>]<<<<<<<<"


def _xor(on_stack: str) -> str:
	"""
	Returns a code snippet for computing `a ^ b`.
	
	Parameter
	--------
	- `on_stack == 0`: Returns a comparison on stack level.
	- `on_stack != 0`: Returns a comparison on information level.

	Results
	-------
	Initial = `[a, x, b, x, x, x]`.

	Final = {
	- `on_stack == 0`: `[a, x, b, x, a ^ b, x, 0, x, 0]`.
	- `on_stack != 0`: `[a, a ^ b, b, 0, x, 0]`.
	}
	"""

	if on_stack == "0":
		return ">>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>>>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>[[-]>>>>+<<<<]>>[[-]>>+<<]>>[--[[-]<<<<+>>>>]]<<<<<<<<"

	return ">[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>>>[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>[[-]>>+<<]<<[[-]>>>>+<<<<]>>>>[--[[-]<<<<+>>>>]]<<<<<"


def _eq(on_stack: str) -> str:
	"""
	Returns a code for computing `a == b`.
	
	Parameter
	--------
	- `on_stack == 0`: Returns a comparison on stack level.
	- `on_stack != 0`: Returns a comparison on information level.

	Results
	-------
	Initial = `[a, x, b, x, x, x]`.

	Final = {
	- `on_stack == 0`: `[a, x, b, x, a == b, x, 0, x, 0]`.
	- `on_stack != 0`: `[a, a == b, b, 0, x, 0]`.
	}
	"""

	flag: bool = on_stack == "0"

	if not flag:
		return ">[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>>>[-]>>[-]<<<[->+>>+<<<]>>>[-<<<+>>>]<<<>[-<<->>]+<<[[-]>>-<<]>>[-<<+>>]<<<"

	return ">>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>>>>>[-]>>[-]<<<<<<[->>>>+>>+<<<<<<]>>>>>>[-<<<<<<+>>>>>>]<<<<<<>>[->>-<<]+>>[[-]<<->>]<<<<<<"



MACROS: dict[str, Callable[[str], str]] = {
	"copy": _copy,
	"or": _or,
	"and": _and,
	"xor": _xor,
	"eq": _eq,
}
