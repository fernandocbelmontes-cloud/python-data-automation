import pandas as pd

# 1. Simulación de datos crudos y caóticos (como llegan en la vida real)
datos_sucios = {
    'Cliente': ['  fernando chavez ', 'ANTONIO lopez  ', ' maria RODRIGUEZ', 'fernando chavez '],
    'Ciudad': ['tijuana', ' TIJUANA ', 'Tijuana', 'tijuana'],
    'Saldo_Pendiente': [2500.50, 4300.00, 7100.20, 2500.50]
}

# Crear el DataFrame inicial
df = pd.DataFrame(datos_sucios)
print("--- DATOS ORIGINALES SUCIOS ---")
print(df)

# 2. PROCESO DE LIMPIEZA DE DATOS (Data Cleansing)
# Eliminar espacios en blanco extras y poner nombres en formato de título (Mayúscula Inicial)
df['Cliente'] = df['Cliente'].str.strip().str.title()
df['Ciudad'] = df['Ciudad'].str.strip().str.capitalize()

# Eliminar registros duplicados (Limpieza operativa)
df = df.drop_duplicates()

# 3. ANÁLISIS DE DATOS (Data Analysis & KPIs)
total_cartera = df['Saldo_Pendiente'].sum()
saldo_promedio = df['Saldo_Pendiente'].mean()

print("\n--- DATOS LIMPIOS Y PROCESADOS ---")
print(df)

print(f"\n--- METRICAS FINANCIERAS CLAVE ---")
print(f"Total de Cartera Pendiente: ${total_cartera:,.2f} MXN")
print(f"Saldo Promedio por Cliente: ${saldo_promedio:,.2f} MXN")

# 4. AUTOMATIZACIÓN DE REPORTES (Exportar el resultado)
df.to_csv('reporte_clientes_limpio.csv', index=False)
print("\n¡Éxito! Reporte optimizado exportado como 'reporte_clientes_limpio.csv'.")
