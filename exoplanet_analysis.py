"""
Proyecto de Caracterización de Exoplanetas

Asignatura: Exoplanetas y Astrobiología
Planeta: GJ 436 b

Autor: Kevin Perez

Este programa analiza datos reales de tránsito y
velocidad radial para estimar parámetros físicos
del exoplaneta, incluyendo:

- Radio planetario
- Distancia orbital
- Masa
- Densidad
- Temperatura de equilibrio
- Habitabilidad

"""
import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("data/Transito_Spitzer.txt", sep=r"\s+",names=["HJD", "Flux", "Noise"],comment="#")
#print(data)
#print(data.columns)

time= data["HJD"]
flux = data["Flux"]
noise = data["Noise"]

Rs =0.46
Ms=0.45
p_days=2.6439
e = 0.16
Ts=3350
# =====================================
# EJERCICIO 1 - Curva de luz
# =====================================

plt.plot(time,flux)
plt.title("Curva de Luz del Tránsito")
plt.xlabel("HJD")
plt.ylabel("Flux")

plt.grid(True)
plt.show()
# =====================================
# EJERCICIO 2 - Profundidad De Transito y Radio Planetario
# =====================================
print("flujo minimo",flux.min())
print("flujo maximo ",flux.max())

depth = flux.max() - flux.min()
print("profundidad de transito: ",depth*100,"%")


Rp =Rs*(depth**0.5)
print("Radio planetario(R☉): ",Rp)

# =====================================
# EJERCICIO 3 - Distancia del Planeta a la Estrella
# =====================================

p_years=p_days/365.25

a3= (p_years**2)*Ms
a=a3**(1/3)
print("Semieje mayor (UA): ",a)
# =====================================
# EJERCICIO 4 - Curva de velocidad radial
# =====================================
data2 =pd.read_csv("data/RV_HIRES.txt", sep=r"\s+",names=["Time_(days)", "RV_(m/s)", "Error", "Phase"],comment="#")
#print(data2)
#print(data2.columns)
timerv= data2["Time_(days)"]
r_velocity =data2["RV_(m/s)"]
error =data2["Error"]
fase=data2["Phase"]

plt.scatter(timerv,r_velocity)
plt.title("Curva de Velocidad Radial")
plt.xlabel("Tiempo(days)")
plt.ylabel("velocidad (m/s)")
plt.grid(True)
plt.show()

plt.scatter(fase,r_velocity)
plt.title("Velocidad Radial vs Fase Orbital")
plt.xlabel("fase orbital")
plt.ylabel("velocidad (m/s)")
plt.grid(True)
plt.show()

# =====================================
# EJERCICIO 5 - Estimando K, la semiamplitud de la velocidad radial.
# =====================================
vrmax=r_velocity.max()
vrmin=r_velocity.min()
k=(vrmax-vrmin)/2

print("semiamplitud(K) ",k,"m/s")

# =====================================
# EJERCICIO 6 - masa mínima y Real del planeta
# =====================================
constante_masa=4.92e-3
mp=(constante_masa)*((1-e**2)**0.5)*k*(p_days**(1/3))*(Ms**(2/3))
print("masa minima planetaria: ",mp,"MJ")

# =====================================
# EJERCICIO 7 - Ms incertidumbre del 10%, cómo influye en la masa del planeta
# =====================================
incertidumbre_estelar = 0.10 # 10%
incertidumbre_planetaria = (2/3) * incertidumbre_estelar

print("Incertidumbre relativa de Mp:", incertidumbre_planetaria*100,"%")

# =====================================
# EJERCICIO 8 - Densidad Planetaria
# =====================================
RSUN_a_RJUP = 9.73
Rpj=Rp*RSUN_a_RJUP
print("radio planetario en radios de jupiter: ", Rpj)

densidad=mp/(Rpj**3)
print("densidad del planeta respecto a jupiter: ",densidad)

densidad_jupiter=1.33
densidadreal = densidad_jupiter*densidad
print("densidad en g/cm³: ", densidadreal)

# =====================================
# EJERCICIO 9 - temperatura de equilibrio del planeta. albedo nulo y albedo Terrestre.
# =====================================
RSUN_a_AU = 0.00465
Rsua=Rs*RSUN_a_AU
division=Rsua/(2*a)
raiz=((division)**0.5)
Tean=raiz*Ts
print("temperatura equilibrio albedo nulo: ", Tean,"kelvin")

Atierra =0.30
Teat=(Ts*((1-Atierra)**(1/4)))*raiz
print("temperatura de equilibrio con albedo terrestre: ", Teat,"kelvin")
# =====================================
# EJERCICIO 10 - zona de Habitabilidad
# =====================================

#documento

# =====================================
# EJERCICIO 11 - de que Planeta se Trata
# =====================================
print("Planeta identificado: GJ 436 b (Gliese 436 b)")