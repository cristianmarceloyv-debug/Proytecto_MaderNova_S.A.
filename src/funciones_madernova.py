import numpy as np
from joblib import dump

def calcular_kpis_logisticos(df, ruta_salida):
    """Calcula indicadores logísticos clave y guarda usando joblib."""
    # Uso de NumPy para cálculos
    despacho_prom = np.mean(df['tiempo_despacho_dias'])
    despacho_std = np.std(df['tiempo_despacho_dias'], ddof=1)
    ventas_totales = np.sum(df['ventas_unidades'])
    
    metricas = {
        'Despacho_Promedio_Dias': round(despacho_prom, 2),
        'Desviacion_Despacho': round(despacho_std, 2),
        'Ventas_Totales_Unidades': int(ventas_totales)
    }
    
    # Uso de Joblib para persistencia
    dump(metricas, ruta_salida)
    
    return metricas
