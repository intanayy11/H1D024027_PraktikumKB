# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Input
suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')

# Output
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')

# Suhu
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

# Kelembapan
kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['basah'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

# Kecepatan kipas
kecepatan['lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['sedang'] = fuzz.trimf(kecepatan.universe, [25, 50, 75])
kecepatan['cepat'] = fuzz.trimf(kecepatan.universe, [50, 100, 100])

#rule
rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kecepatan['lambat'])
rule2 = ctrl.Rule(suhu['normal'] & kelembapan['lembap'], kecepatan['sedang'])
rule3 = ctrl.Rule(suhu['panas'] | kelembapan['basah'], kecepatan['cepat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
kipas = ctrl.ControlSystemSimulation(kipas_ctrl)

kipas.input['suhu'] = 30
kipas.input['kelembapan'] = 70

kipas.compute()

# Output
print("Kecepatan kipas:", kipas.output['kecepatan'])

suhu.view()
kelembapan.view()
kecepatan.view(sim=kipas)

plt.show()