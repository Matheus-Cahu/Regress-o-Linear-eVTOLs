import pandas as pd
import matplotlib.pyplot as plt

# Importação dos datasets
rpt = pd.read_csv('datasets/VAH01_impedance.csv')
rpt = rpt.rename(columns={'cycle numbers': 'cycleNumber'})
df = pd.read_csv('datasets/VAH01.csv')

# Declaração da tabela de filtros a partir de ciclos de RTP
ciclos = rpt['cycleNumber'].tolist()
print(f"CICLOS:\nN° de elementos: {len(ciclos)} \n {ciclos}")

# Filtra VAH a partir dos ciclos de RTP
df_filtrando = df[df['cycleNumber'].isin(ciclos)]
df_filtrado = df_filtrando.drop_duplicates(subset='cycleNumber', keep='last')

# Busca Resistências RTP
df_discharge = pd.merge(df_filtrado[['cycleNumber','QDischarge_mA_h']].sort_values('cycleNumber'), rpt[['cycleNumber','60%_30_second']], on='cycleNumber', how='inner')

# Calcula proporção entre R e QD para estimar as QD em demais RTPs
df_discharge['proporcao'] = df_discharge['QDischarge_mA_h'] / df_discharge['60%_30_second']

print(f"DF_DISCHARGE: \nN° de elementos: {len(df_discharge)} \n {df_discharge} \n {df_discharge['QDischarge_mA_h']/df_discharge['60%_30_second']}")

# Traça gráfico
plt.figure(figsize=(10, 6))
plt.plot(df_discharge['cycleNumber'], df_discharge['QDischarge_mA_h'], marker='o', linestyle='-', color='b', label='Capacidade de descarga')

plt.title('Capacidade de descarga por ciclo (VAH01)', fontsize=14)
plt.xlabel('Número do ciclo', fontsize=12)
plt.ylabel('Capacidade de descarga', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend()

plt.show()
