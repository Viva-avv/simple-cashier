import matplotlib.pyplot as plt
import numpy as np

# Definisikan rentang nilai untuk x
x = np.linspace(-5, 10, 400)

# Definisikan fungsi batas dari pertidaksamaan
y1 = (9 - x) / 3  # Untuk x + 3y < 9
y2 = (x - 6) / 2  # Untuk x - 2y > 6

# Membuat plot
plt.figure(figsize=(8, 8))

# Isi area yang memenuhi pertidaksamaan
plt.fill_between(x, y1, -10, where=(y1 > -10), color='lightblue', alpha=0.5, label=r'$x + 3y < 9$')
plt.fill_between(x, y2, 10, where=(y2 < 10), color='lightgreen', alpha=0.5, label=r'$x - 2y > 6$')

# Gambarkan garis batas
plt.plot(x, y1, 'b-', linewidth=2, label=r'$x + 3y = 9$')
plt.plot(x, y2, 'g-', linewidth=2, label=r'$x - 2y = 6$')

# Pengaturan plot
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # Garis horizontal (sumbu x)
plt.axvline(0, color='black', linewidth=0.5)  # Garis vertikal (sumbu y)
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(loc='best')

# Judul plot
plt.title('Grafik Pertidaksamaan x + 3y =< 9 dan x - 2y > 6')

# Tampilkan plot
plt.show()
