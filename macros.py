
from typing import Callable

def _copy(count: str) -> str:
	"""
	Returns a code snippet for copying the byte at the current location
	`count` spaces ahead. 
	
	Will trash the byte 2 spaces ahead of the destination.

	Parameter:
	- `count`: Must represent a base `10` integer.
	"""
	
	shift: int = int(count)

	right: str = ">" * shift
	left: str = "<" * shift

	return f"{right}[-]>>[-]<<{left}[-{right}+>>+<<{left}]{right}>>[-<<{left}+{right}>>]<<{left}"

MACROS: dict[str, Callable[[str], str]] = {
	"copy": _copy,
}
