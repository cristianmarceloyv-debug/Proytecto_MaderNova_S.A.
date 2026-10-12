# Análisis Operativo y Comercial: MaderNova S.A.

## Objetivo
Evaluar comportamiento productivo y de desempeño de la red de distribución de tableros de madera, correlacionando consumo de energía, tiempos de despacho, tipo de material y volúmenes de merma.

## Datos
Se utiliza el archivo `dataset_set_B_madernova.xlsx`, el que documenta variables de las tres plantas operativas y tres canales comerciales a lo largo de diversos periodos.

## Metodología
- **Carga y segregación:** División del dataset primario para separar contexto de Producción del área Comercial utilizando `pandas`.
- **Análisis Estadístico:** Cálculo de indicadores críticos de eficiencia y dispersión guardados mediante `joblib`.
- **Visualización:** Generación de un dashboard gerencial multifacético utilizando `matplotlib` y `seaborn`.

## Resultados
Se detecta una alta variabilidad en los tiempos de despacho asociados a los canales, variando fuertemente según la planta. El volumen no muestra relación perfectamente escalonada con la merma, lo cual indica que las pérdidas de material pueden obedecer a incidentes en la línea de producción y no meramente a la cantidad de tableros fabricados.
