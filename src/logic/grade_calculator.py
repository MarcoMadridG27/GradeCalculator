from typing import List, Dict, Any
from src.model.evaluation import Evaluation
from src.logic.attendance_policy import AttendancePolicy
from src.logic.extra_points_policy import ExtraPointsPolicy
from src.utils.constants import MAX_EVALUATIONS, MAX_GRADE, MIN_GRADE

class GradeCalculator:
    def __init__(self):
        self.attendance_policy = AttendancePolicy()
        self.extra_points_policy = ExtraPointsPolicy()

    def calculate(self, evaluations: List[Evaluation], has_reached_minimum_classes: bool, all_years_teachers: bool) -> Dict[str, Any]:
        # RNF01: Máximo 10 evaluaciones
        if len(evaluations) > MAX_EVALUATIONS:
            raise ValueError(f"No se pueden registrar más de {MAX_EVALUATIONS} evaluaciones.")
        
        if not evaluations:
            return {
                "average": 0.0,
                "extra_points": 0.0,
                "penalty": 0.0,
                "final_grade": 0.0
            }

        # Calcular Promedio Ponderado
        total_weight = sum(e.weight for e in evaluations)
        if total_weight == 0:
             raise ValueError("El peso total no puede ser 0.")
        
        weighted_sum = sum(e.grade * e.weight for e in evaluations)
        
        # Si los pesos son porcentajes (0-100), dividimos por la suma de pesos para normalizar.
        # Si la suma es 100, es lo mismo que dividir por 100.
        average = weighted_sum / total_weight

        # Calcular Puntos Extra
        extra_points = self.extra_points_policy.calculate_extra_points(all_years_teachers)
        
        # Aplicar Puntos Extra (Topado a 20)
        grade_with_extra = average + extra_points
        if grade_with_extra > MAX_GRADE:
            grade_with_extra = MAX_GRADE

        # Calcular Penalización por Asistencia
        penalty = self.attendance_policy.calculate_penalty(grade_with_extra, has_reached_minimum_classes)
        
        # Nota Final
        final_grade = grade_with_extra - penalty
        
        # Asegurar que no sea negativa (por si acaso)
        if final_grade < MIN_GRADE:
            final_grade = MIN_GRADE

        return {
            "average": round(average, 2),
            "extra_points": round(extra_points, 2),
            "penalty": round(penalty, 2),
            "final_grade": round(final_grade, 2)
        }
