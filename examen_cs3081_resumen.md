# Examen Parcial CS3081 – Resumen Completo (2025-2)

Este documento consolida **todos los criterios, requerimientos, casos de uso y lineamientos** mostrados en las imágenes proporcionadas. Útil como guía para rendir el examen o preparar la implementación.

---

## ## 1. Criterios de Evaluación (Nota sobre 11 puntos)

### **1. Cumplimiento de RF / RNF — 2 pts**
- Implementación correcta de RF01–RF05.
- Cumplimiento de RNF01–RNF03 (límite de evaluaciones, determinismo del cálculo, manejo de casos borde).
- No existen “atajos”: datos hardcodeados, cálculos fuera de las clases correspondientes.
- Entradas y salidas bien definidas.

---

### **2. Diseño y Arquitectura OO — 2 pts**
- Separación clara de responsabilidades.
- Uso adecuado y coherente de clases como:  
  **Evaluation, GradeCalculator, AttendancePolicy, ExtraPointsPolicy**, etc.
- Bajo acoplamiento y alta cohesión entre componentes.
- UML simple y coherente con el código final.

---

### **3. Calidad del Código — 2 pts**
Aspectos evaluados:
- **Nombres significativos** (no usar x1, dato, aux, etc.).
- Ausencia de valores mágicos: uso adecuado de constantes o configuración.
- Manejo correcto de errores y validaciones.
- Comentarios relevantes (no repetitivos ni redundantes).
- Formato consistente y código legible.

La calidad será evaluada mediante **SonarQube**.

---

### **4. Pruebas Automatizadas — 2 pts**
Se evalúan:
- Tests unitarios que cubren:
  - Caso normal.
  - Caso sin asistencia mínima.
  - Caso con y sin puntos extra.
  - Casos borde (0 evaluaciones, pesos inválidos, asistencia negativa, etc.).
- Claridad en nombres (ej.: `shouldReturnXWhenY`).
- Cobertura mínima razonable:
  - ≥ 50% aceptable  
  - ≥ 60% excelente

---

## ## 2. Desarrollo e Implementación (11 pts)

Se requiere implementar un **módulo de cálculo de la nota final**, alineado a los RF y RNF.  
- Puede hacerse en cualquier lenguaje.  
- Debe ejecutarse por terminal.  
- No se necesita persistencia en base de datos.  
- No se necesita interfaz gráfica.  
- Priorizar solución **modular**, **clara** y **estructurada**.

---
hola
## ### Requerimientos Funcionales (RF)

### **RF01:**  
El docente podrá registrar las **evaluaciones** de un estudiante, indicando nota obtenida y porcentaje de peso sobre la nota final.  
Variable: `examsStudents`.

### **RF02:**  
El docente podrá registrar si el estudiante **cumplió la asistencia mínima** exigida.  
Variable: `hasReachedMinimumClasses`.

### **RF03:**  
El docente podrá registrar, por cada año académico, si los docentes del curso **están de acuerdo en otorgar puntos extra** a los estudiantes que cumplan criterios.  
Variable: `allYearsTeachers` (True/False).

### **RF04:**  
El docente podrá solicitar el **cálculo de la nota final**, considerando:
- evaluaciones,
- asistencia mínima,
- políticas de puntos extra.

### **RF05:**  
El docente podrá visualizar el **detalle del cálculo**:  
- promedio ponderado,  
- penalización por inasistencias,  
- puntos extra aplicados.  

---

## ### Requerimientos No Funcionales (RNF)

### **RNF01:**  
Máximo **10 evaluaciones** por estudiante.

### **RNF02:**  
El sistema debe soportar **50 usuarios concurrentes**.

### **RNF03:**  
El cálculo de la nota final debe ser **determinista**: dado un mismo input, siempre produce el mismo resultado.

### **RNF04:**  
El tiempo de cálculo debe ser **menor a 300 ms** por solicitud.

---

## ## Caso de Uso Principal

### **Sistema:** CS-GradeCalculator  
### **Actor:** Docente UTEC

---

### **CU0001 – Calcular nota final del estudiante**

1. El docente ingresa a la aplicación.
2. La aplicación solicita los datos del estudiante (código o identificador).
3. El docente registra o revisa las evaluaciones con sus notas y pesos.
4. El docente indica si el estudiante alcanzó la asistencia mínima.
5. La aplicación consulta la política de puntos extra (lista `allYearsTeachers`).
6. La aplicación calcula la nota final.
7. La aplicación muestra la nota final y el detalle del cálculo.

---

## ## Recomendaciones para el Examen

- Evitar hardcodear valores.
- Dividir la lógica en clases pequeñas con responsabilidades claras.
- Implementar pruebas unitarias de todos los casos.
- Cuidar nombres, validaciones, formato y constantes.
- Asegurarse de cumplir **todos** los RF y RNF.

---

Fin del documento.

