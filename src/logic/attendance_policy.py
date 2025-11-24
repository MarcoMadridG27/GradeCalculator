from src.utils.constants import ATTENDANCE_PENALTY_LIMIT

class AttendancePolicy:
    def calculate_penalty(self, current_grade: float, has_reached_minimum: bool) -> float:
        """
        Calcula la penalización por inasistencia.
        Si no cumple la asistencia mínima, la nota se limita a 10 (o menos si ya era menor).
        """
        if has_reached_minimum:
            return 0.0
        
        # Si la nota es aprobatoria (> 10), se penaliza para bajarla a 10.
        # Si ya está desaprobada, no se penaliza adicionalmente (o se podría, pero asumiremos tope 10).
        if current_grade > ATTENDANCE_PENALTY_LIMIT:
            return current_grade - ATTENDANCE_PENALTY_LIMIT
        
        return 0.0
