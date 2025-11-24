import unittest
from src.model.evaluation import Evaluation
from src.logic.grade_calculator import GradeCalculator
from src.utils.constants import MAX_EVALUATIONS, MAX_GRADE, ATTENDANCE_PENALTY_LIMIT

class TestGradeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = GradeCalculator()

    def test_normal_case(self):
        """Caso normal: Promedio simple sin penalizaciones ni puntos extra."""
        evals = [
            Evaluation(15, 50),
            Evaluation(17, 50)
        ]
        # Promedio: (15*50 + 17*50) / 100 = 16
        result = self.calculator.calculate(evals, has_reached_minimum_classes=True, all_years_teachers=False)
        self.assertEqual(result['final_grade'], 16.0)
        self.assertEqual(result['penalty'], 0.0)
        self.assertEqual(result['extra_points'], 0.0)

    def test_attendance_penalty(self):
        """Caso sin asistencia mínima: La nota debe bajar a 10 si es mayor a 10."""
        evals = [Evaluation(18, 100)]
        # Promedio 18. Sin asistencia -> Penalización = 18 - 10 = 8. Final = 10.
        result = self.calculator.calculate(evals, has_reached_minimum_classes=False, all_years_teachers=False)
        self.assertEqual(result['average'], 18.0)
        self.assertEqual(result['penalty'], 18.0 - ATTENDANCE_PENALTY_LIMIT)
        self.assertEqual(result['final_grade'], ATTENDANCE_PENALTY_LIMIT)

    def test_attendance_penalty_low_grade(self):
        """Caso sin asistencia mínima pero nota baja: No se penaliza extra si ya es <= 10."""
        evals = [Evaluation(8, 100)]
        # Promedio 8. Sin asistencia -> Penalización 0 (ya es < 10). Final = 8.
        result = self.calculator.calculate(evals, has_reached_minimum_classes=False, all_years_teachers=False)
        self.assertEqual(result['average'], 8.0)
        self.assertEqual(result['penalty'], 0.0)
        self.assertEqual(result['final_grade'], 8.0)

    def test_extra_points(self):
        """Caso con puntos extra."""
        evals = [Evaluation(14, 100)]
        # Promedio 14. Puntos extra +1. Final = 15.
        result = self.calculator.calculate(evals, has_reached_minimum_classes=True, all_years_teachers=True)
        self.assertEqual(result['average'], 14.0)
        self.assertEqual(result['extra_points'], 1.0)
        self.assertEqual(result['final_grade'], 15.0)

    def test_extra_points_cap(self):
        """Caso con puntos extra topado a 20."""
        evals = [Evaluation(MAX_GRADE, 100)]
        # Promedio 20. Puntos extra +1 -> 21. Topado a 20.
        result = self.calculator.calculate(evals, has_reached_minimum_classes=True, all_years_teachers=True)
        self.assertEqual(result['average'], MAX_GRADE)
        self.assertEqual(result['extra_points'], 1.0)
        self.assertEqual(result['final_grade'], MAX_GRADE)

    def test_mixed_case(self):
        """Caso mixto: Puntos extra y penalización por asistencia."""
        evals = [Evaluation(15, 100)]
        # Promedio 15.
        # Puntos extra: +1 -> 16.
        # Sin asistencia: 16 -> Penalización 6 -> Final 10.
        result = self.calculator.calculate(evals, has_reached_minimum_classes=False, all_years_teachers=True)
        self.assertEqual(result['average'], 15.0)
        self.assertEqual(result['extra_points'], 1.0)
        # Nota con extra es 16. Penalización para llegar a 10 es 6.
        self.assertEqual(result['penalty'], 16.0 - ATTENDANCE_PENALTY_LIMIT)
        self.assertEqual(result['final_grade'], ATTENDANCE_PENALTY_LIMIT)

    def test_max_evaluations_error(self):
        """Debe lanzar error si hay más de 10 evaluaciones."""
        evals = [Evaluation(10, 10) for _ in range(MAX_EVALUATIONS + 1)]
        with self.assertRaises(ValueError):
            self.calculator.calculate(evals, True, False)

    def test_zero_evaluations(self):
        """Manejo de lista vacía de evaluaciones."""
        evals = []
        result = self.calculator.calculate(evals, True, False)
        self.assertEqual(result['final_grade'], 0.0)

    def test_zero_total_weight_error(self):
        """Debe lanzar error si el peso total es 0 (caso defensivo)."""
        # Creamos un objeto mock o "fake" que salte la validación de Evaluation
        class FakeEvaluation:
            def __init__(self):
                self.grade = 10
                self.weight = 0
        
        evals = [FakeEvaluation()]
        with self.assertRaises(ValueError):
            self.calculator.calculate(evals, True, False)

    def test_negative_final_grade_clamping(self):
        """Asegurar que la nota final no sea negativa (caso defensivo)."""
        # Forzamos una penalización enorme mockeando la política de asistencia
        from unittest.mock import MagicMock
        self.calculator.attendance_policy.calculate_penalty = MagicMock(return_value=100.0)
        
        evals = [Evaluation(10, 100)]
        result = self.calculator.calculate(evals, has_reached_minimum_classes=False, all_years_teachers=False)
        
        self.assertEqual(result['final_grade'], 0.0)
        self.assertEqual(result['penalty'], 100.0)

if __name__ == '__main__':
    unittest.main()
