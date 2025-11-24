import sys
import os

# Add the current directory to sys.path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.utils.constants import MAX_EVALUATIONS, MIN_GRADE, MAX_GRADE, MIN_WEIGHT, MAX_WEIGHT
from src.model.evaluation import Evaluation
from src.logic.grade_calculator import GradeCalculator

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def get_bool_input(prompt: str) -> bool:
    while True:
        response = input(prompt).strip().lower()
        if response in ['s', 'si', 'y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print("Por favor, responda 's' o 'n'.")

def main():
    print("=== CS-GradeCalculator ===")
    
    student_id = input("Ingrese el código del estudiante: ")
    print(f"Registrando notas para el estudiante: {student_id}")
    
    evaluations = []
    
    while True:
        if len(evaluations) >= MAX_EVALUATIONS:
            print(f"Se ha alcanzado el límite máximo de {MAX_EVALUATIONS} evaluaciones.")
            break
            
        print(f"\nEvaluación #{len(evaluations) + 1}")
        try:
            grade = get_float_input(f"  Ingrese la nota ({MIN_GRADE}-{MAX_GRADE}): ")
            weight = get_float_input(f"  Ingrese el peso ({MIN_WEIGHT}-{MAX_WEIGHT}): ")
            
            evaluation = Evaluation(grade, weight)
            evaluations.append(evaluation)
            
            if len(evaluations) < MAX_EVALUATIONS:
                cont = get_bool_input("  ¿Desea agregar otra evaluación? (s/n): ")
                if not cont:
                    break
        except ValueError as e:
            print(f"  Error: {e}")
            continue

    print("\n--- Información Adicional ---")
    has_min_attendance = get_bool_input("¿El estudiante cumplió con la asistencia mínima? (s/n): ")
    all_teachers_agree = get_bool_input("¿Los docentes acuerdan otorgar puntos extra? (s/n): ")
    
    calculator = GradeCalculator()
    
    try:
        result = calculator.calculate(evaluations, has_min_attendance, all_teachers_agree)
        
        print("\n=== Resultados ===")
        print(f"Promedio Ponderado: {result['average']}")
        print(f"Puntos Extra:       +{result['extra_points']}")
        print(f"Penalización:       -{result['penalty']}")
        print("-------------------------")
        print(f"NOTA FINAL:         {result['final_grade']}")
        
    except Exception as e:
        print(f"\nError al calcular la nota: {e}")

if __name__ == "__main__":
    main()
