
class Characters:

	RIGHT: str = '>'
	LEFT: str = '<'

	INCREASE: str = '+'
	DECREASE: str = '-'

	START_LOOP: str = '['
	END_LOOP: str = ']'

	PRINT: str = '.'
	READ: str = ','


	TOGGLE_DEBUG: str = '?'
	SET_DEBUG: str = '*'
	RESET_DEBUG: str = '!'


	MACRO_CHAR: str = "@"

	VALID_CHARACTERS: set[str] = {
		
		RIGHT, LEFT, 
		INCREASE, DECREASE, 
		START_LOOP, END_LOOP, 
		PRINT, READ,

		TOGGLE_DEBUG, SET_DEBUG, RESET_DEBUG,
		MACRO_CHAR
	}


TAPE_SIZE: int = 30_000
