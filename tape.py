
from random import randint
from exceptions import PointerOutOfBound
from settings import TAPE_SIZE

class Tape(list[int]):

	size: int

	__pointer: int
	__maximum: int
	
	def __init__(self, size: int = TAPE_SIZE) -> None:
		super().__init__([0] * size)
		
		self.size = size
		
		self.__pointer = 0
		self.__maximum = 0
	
	@property
	def byte(self) -> int:
		return self[self.__pointer]
	
	
	@byte.setter
	def byte(self, value: int) -> None:
		self.set_value(value, self.__pointer)
		
	
	def set_value(self, value: int, index: int | None = None) -> None:
		"""
		Sets the value at `index` to `value`.
		If `index` is `None`, uses the value of `self.__pointer`.
		"""
		self[index if index is not None else self.__pointer] = value & 255
		
	
	def increase(self, ammount: int, index: int | None = None) -> None:
		"""
		Increases the value at `index` by `ammount`.
		If `index` is `None`, uses the value of `self.__pointer`.
		"""
		self.set_value((self[index] if index is not None else self.byte) + ammount, index)
	   
		
	def move_by(self, ammount: int = 1) -> None:
		"""
		Increases the value of `self.__pointer` by `ammount`.
		"""
		self.move_to(self.__pointer + ammount)
		
	
	def move_to(self, index: int) -> None:
		"""
		Sets `self.__pointer` to `index`.
		"""

		self.__pointer = index
		self.__maximum = max(self.__pointer, self.__maximum)
		
		if self.__pointer < 0:
			raise PointerOutOfBound.negative_pointer(self.__pointer)
	
		if self.__pointer >= self.size:
			raise PointerOutOfBound.too_big_pointer(self.__pointer, self.size)
	
	
	def trash(self, start: int = 0, end: int | None = None, step: int = 1) -> None:
		"""Adds random numbers (trash) to the sepecified slice. Serves mostly for testing."""

		if end is None:
			end = len(self)
		
		for i in range(start, end, step):
			self.set_value(randint(0, 255), i)

	def __str__(self) -> str:

		pointer_index: int = (self.__pointer and len(str(self[:self.__pointer]))) + (len(str(self.byte)) + 1) // 2

		return str(self[:self.__maximum + 1]) + '\n' + ' ' * (pointer_index) + '^'


	def __repr__(self) -> str:
		return f"Tape: size={len(self)}, pointer={self.__pointer}, byte={self.byte}"
