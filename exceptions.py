
class PointerOutOfBound(Exception):

    @staticmethod
    def negative_pointer(index: int) -> "PointerOutOfBound":
        return PointerOutOfBound(f"Tried to move to negative index; pointer = {index};")

    @staticmethod
    def too_big_pointer(index: int, size: int) -> "PointerOutOfBound":
        return PointerOutOfBound(f"Tried to move beyond last byte; pointer = {index:_} >= size = {size:_}")

class MismatchedBrackets(Exception):
    
    @staticmethod
    def mismatched(code: str, index: int, depth: int) -> "MismatchedBrackets":

        string = f"Couldn't find match for bracket at {index=}; " 
        string += f"{depth} closing bracket{'s' * (depth > 1)} missing in {code=};"

        return MismatchedBrackets(string)
