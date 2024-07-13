
from typing import Callable

def _copy(count: str) -> str:
    
	shift: int = int(count)

	right: str = ">" * shift
	left: str = "<" * shift

	return f"{right}[-]>>[-]<<{left}[-{right}+>>+<<{left}]{right}>>[-<<{left}+{right}>>]<<{left}"

MACROS: dict[str, Callable[[str], str]] = {

	# [a, x, x, x, x] -> [a, x, a, x, 0]
	r"copy": _copy,
}
