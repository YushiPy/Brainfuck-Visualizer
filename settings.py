
class Characters:

	RIGHT: str = '>'
	LEFT: str = '<'

	INCREASE: str = '+'
	DECREASE: str = '-'

	START_LOOP: str = '['
	END_LOOP: str = ']'

	PRINT: str = '.'
	READ: str = ','

	VALID_CHARACTERS: set[str] = {
		RIGHT, LEFT, INCREASE, DECREASE, START_LOOP, END_LOOP, PRINT, READ
	}


TAPE_SIZE: int = 30_000
