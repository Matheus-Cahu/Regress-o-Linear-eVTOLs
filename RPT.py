import pandas as pd
import matplotlib.pyplot as plt

rpt = pd.read_csv('datasets/VAH01_impedance.csv')
df = pd.read_csv('datasets/VAH01.csv')

ciclos = rpt['cycle numbers'].tolist()
print(f"CICLOS:\nN° de elementos: {len(ciclos)} \n {ciclos}")
df_filtrando = df[df['cycleNumber'].isin(ciclos)]
df_filtrado = df_filtrando.drop_duplicates(subset='cycleNumber', keep='last')

df_discharge = df_filtrado[['cycleNumber','QDischarge_mA_h']].sort_values('cycleNumber')
print(f"DF_DISCHARGE: \nN° de elementos: {len(df_discharge)} \n {df_discharge}")

plt.figure(figsize=(10, 6))
plt.plot(df_discharge['cycleNumber'], df_discharge['QDischarge_mA_h'], marker='o', linestyle='-', color='b', label='Capacidade de descarga')

plt.title('Capacidade de descarga por ciclo (VAH01)', fontsize=14)
plt.xlabel('Número do ciclo', fontsize=12)
plt.ylabel('Capacidade de descarga', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Adiciona a legenda
plt.legend()

# Exibe o gráfico na tela
plt.show()
