# COLUMNAS - CONCLUSIONES (texto)

## Conclusiones Generales
- **Seniority and turnover**: la mayoría de empleados tiene menos de 10 años en la empresa → sugiere una fuerza laboral relativamente joven.
- **Promotions**: muchos empleados llevan 1–3 años sin promoción, algunos hasta 15 → puede influir en la rotación si se sienten estancados.
- **Age**: empleados desde ~20 años (2005) hasta ~60 años (1963). Promedio ~39 años en 2025.
- **Satisfaction and options**: satisfacción media-alta, pero *stock options* bajas → posible desmotivación.
- **Training**: todos reciben igual cantidad de entrenamiento → no diferencia perfiles.

## Panorama resumido
- Plantilla joven-adulta, rotación previa moderada (2–3 empresas).
- Antigüedad promedio 7 años, pocos superan los 10.
- Promociones limitadas.
- Satisfacción aceptable, pero beneficios bajos.

## Variables principales (columnas en inglés, texto en español)
- **Age**: Edad. 1678 empleados. Los jóvenes suelen irse más rápido, edad media permanece más.
- **Attrition**: Variable clave (Yes/No). Depende de salario, viajes, distancia, satisfacción.
- **PercentSalaryHike**: Incremento % salario. Media ~15%, rango 11–25%. Poca variabilidad.
- **YearsAtCompany**: Media ~7.1 años. Rango 0–40. P75=9 → pocos >10.
- **BusinessTravel**: La mitad no viaja. ~25% rara vez, ~25% con frecuencia.
- **DailyRate**: Promedio 668.08, desv. 470.79. Min 104.10, Mediana 556.26, Q3 971.96, Máx 2063.39.
- **Department**: Distribución en Sales, HR, Research.
- **DistanceFromHome**: Promedio 4.5 km, desv. 14.65. Rango -49 (error) a 29 km. Mayoría entre 2 y 11 km.
- **Education**: Mayoría nivel 3–4. Pocos nivel 5 o 1. Influye en salario/rol.
- **EducationField**: Principalmente Life Sciences y Medical (~40%). HR y Other poco frecuentes.
- **EmployeeCount**: Constante “1” → cada fila es un empleado.
- **EmployeeNumber**: ID 1–1614. Mediana ~813.
- **EnvironmentSatisfaction**: Escala 1–4. Errores (ej. 41 → debería ser 4).
- **Gender**: Codificado 0/1. Normalizar a Male/Female.
- **HourlyRate**: Derivado de DailyRate/8. Muchos nulos → drop.
- **JobInvolvement**: Escala 1–4. Mantener. Nulos = “Unknown”.
- **JobLevel**: Escala 1–5. Mantener.
- **JobRole**: Inconsistencias de mayúsculas → normalizar con `.str.lower().str.strip()`.
- **JobSatisfaction**: Escala 1–4. Mantener.
- **MaritalStatus**: 500–600 nulos. Normalizar con `str.title()`.
- **MonthlyIncome**: Sin nulos. Convertir a float. Quitar “$”.
- **MonthlyRate**: Variable continua relacionada con salario. Mantener.
- **NumCompaniesWorked**: Nº empresas previas. Int. Sin nulos. Mantener.
- **Over18**: Drop.
- **OverTime**: Yes/No. Normalizar a booleano.
- **PerformanceRating**: Convertir a int. Renombrar si procede.
- **RelationshipSatisfaction**: Escala 1–4. Mantener. Renombrar.
- **StandardHours**: Full Time / Part Time. Nulos = Full Time.
- **StockOptionLevel**: Drop. Baja relevancia.
- **TotalWorkingYears**: Años totales de experiencia. Convertir a int. Mantener.
- **TrainingTimesLastYear**: Nº entrenamientos. Mantener.
- **WorkLifeBalance**: Escala 1–4. Convertir a int. Mantener.
- **YearsInCurrentRole**: Muchos nulos. Convertir a int. Posible drop.
- **YearsSinceLastPromotion**: Mantener. Métrica de promociones.
- **YearsWithCurrManager**: Mantener.
- **DateBirth**: Drop (ya existe Age).
- **Salary**: Convertir a float. Quitar “$”.
- **RoleDepartment**: Muchos nulos. Normalizar o drop.
- **NumberChildren**: Sin datos. Drop.
- **RemoteWork**: Yes/No. Normalizar a booleano.
