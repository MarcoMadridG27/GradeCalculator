from src.utils.constants import MIN_GRADE, MAX_GRADE, MIN_WEIGHT, MAX_WEIGHT

class Evaluation:
    def __init__(self, grade: float, weight: float):
        if not (MIN_GRADE <= grade <= MAX_GRADE):
            raise ValueError(f"La nota debe estar entre {MIN_GRADE} y {MAX_GRADE}.")
        if not (MIN_WEIGHT < weight <= MAX_WEIGHT):
            raise ValueError(f"El peso debe estar entre {MIN_WEIGHT} y {MAX_WEIGHT} (exclusivo 0).")
        
        self.grade = grade
        self.weight = weight
