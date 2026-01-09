import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o dataset
# Substitua 'seu_arquivo.csv' pelo caminho do arquivo da célula específica (ex: VAH01.csv)
df = pd.read_csv('datasets/VAH01.csv')

# 2. Agrupar por ciclo e pegar o valor máximo de cada métrica de capacidade
# O 'max()' funciona aqui porque QCharge e QDischarge são acumulativos dentro de cada ciclo
cycle_data = df.groupby('cycleNumber').agg({
    'QCharge_mA_h': 'max',
    'QDischarge_mA_h': 'max'
}).reset_index()

# 3. Calcular a Eficiência Coulômbica (Proporção)
# Nota: É importante garantir que não haja divisão por zero
cycle_data['Coulombic_Efficiency'] = cycle_data['QDischarge_mA_h'] / cycle_data['QCharge_mA_h']

# 4. Limpeza de Outliers (Opcional, mas recomendado para dados ruidosos)
# Remove ciclos onde a eficiência é fisicamente impossível (ex: > 1.05 ou < 0.8)
cycle_data = cycle_data[(cycle_data['Coulombic_Efficiency'] > 0.8) & (cycle_data['Coulombic_Efficiency'] <= 1.05)]

# 5. Visualização para conferência
plt.figure(figsize=(12, 5))

# Gráfico da Eficiência ao longo dos ciclos
plt.subplot(1, 2, 1)
plt.plot(cycle_data['cycleNumber'], cycle_data['Coulombic_Efficiency'], color='blue', alpha=0.6)
plt.title('Eficiência Coulômbica por Ciclo')
plt.xlabel('Ciclo')
plt.ylabel('QDischarge / QCharge')

# Gráfico do QDischarge (para você ver a diferença entre Missão e Referência)
plt.subplot(1, 2, 2)
plt.scatter(cycle_data['cycleNumber'], cycle_data['QDischarge_mA_h'], s=10, c='red')
plt.title('Capacidade de Descarga por Ciclo')
plt.xlabel('Ciclo')
plt.ylabel('mAh')

plt.tight_layout()
plt.show()

# Exibir os primeiros resultados
print(cycle_data[['cycleNumber', 'QCharge_mAh', 'QDischarge_mAh', 'Coulombic_Efficiency']].head())
