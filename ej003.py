import matplotlib.pyplot as plt

turistas = [89.6, 81.8, 75.3, 60.7, 58.3, 39.4, 37.4, 34.5, 33.7, 37.6]
paises = ["Francia", "Estados Unidos", "España", "China", "Italia", "Mexico", "Reino Unido", "Turquia", "Alemania", "Tailandia"]
explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]

plt.pie(turistas, labels=paises,explode=explode, autopct="%1.1f%%", shadow=True, startangle=90)
plt.title("TOP 10 DESTINOS TURISTICOS EN EL 2017")
plt.show()
