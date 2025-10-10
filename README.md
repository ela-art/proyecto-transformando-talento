# Proyecto Transformando Talento – Enfoque: Empleados que se Van

## 🎯 Objetivo
Analizar el perfil de los empleados que abandonan la empresa (Attrition = Yes) para detectar patrones comunes y posibles factores de riesgo asociados al abandono laboral.

## 📅 Avance final

- **Día 1**: carga del dataset `hr_tratado.csv`, planificación del enfoque analítico y creación del diccionario de variables.
- **Día 2**: análisis exploratorio enfocado en la variable `attrition`, segmentación de los empleados que se van y revisión de sus características generales.
- **Día 3**: limpieza y estandarización de columnas relevantes (`businesstravel`, `worklifebalance`, `horas_extra`, etc.).
- **Día 4**: análisis descriptivo de variables numéricas y categóricas para el grupo de empleados con attrition.
- **Día 5**: elaboración de conclusiones y recomendaciones específicas para mitigar la rotación.

## 📂 Organización

- `notebooks/` → notebooks con el análisis del grupo "attrition = yes".  
- `data/` → dataset tratado: `hr_tratado.csv`.  
- `docs/` → diccionario de datos y documentación del análisis.  

## 🧠 Perfil del empleado que se va

- Edad promedio: **35 años**
- Antigüedad en la empresa: **5 años**
- Experiencia total previa: **~9 años**
- Salario mensual medio: **~4.300 €**
- Alta representación en roles **técnicos y comerciales**
- Mayoría con **jornada parcial** y **trabajo remoto**
- Satisfacción laboral e involucramiento: **nivel medio**
- Frecuente presencia de campos `Unknown`, especialmente en variables como **viajes, horas extra y estado civil**

## 💡 Conclusiones

- El grupo que abandona la empresa muestra un patrón claro: empleados jóvenes, con experiencia, pero posiblemente sin oportunidades claras de crecimiento o con condiciones poco estables.
- La falta de datos en variables clave podría estar ocultando factores estructurales que afectan la fidelización del talento.
- Se recomienda priorizar mejoras en:
  - Claridad de carrera profesional
  - Seguimiento personalizado desde RRHH
  - Reducción de contratos parciales o poco definidos
  - Detección temprana de señales de desconexión

## ⚙️ Requisitos técnicos

- Python 3.10+  
- Librerías: pandas, numpy  
