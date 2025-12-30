import numpy as np
import scipy.integrate as spi


# Функція для інтегрування
def f(x):
    return x**2


# Обчислення інтегралу методом Монте-Карло
def monte_carlo_simulation(a, b, f_max, num_experiments, points_per_experiment):
    average_area = 0

    # Генерація випадкових точок
    for _ in range(num_experiments):
        x = np.random.uniform(a, b, points_per_experiment)
        y = np.random.uniform(0, f_max, points_per_experiment)

        # Підрахунок точок під кривою
        M = np.sum(y <= f(x))

        # Розрахунок площі
        area = (M / points_per_experiment) * ((b - a) * f_max)
        average_area += area

    # Середнє значення площі
    average_area /= num_experiments
    return average_area


if __name__ == "__main__":

    # Межі інтегрування
    a = 0
    b = 2

    # Максимальне значення функції на відрізку
    f_max = max(f(a), f(b))

    # Кількість експериментів та точок
    num_experiments = 100
    points_per_experiment = 150_000

    # Виконання Монте-Карло
    monte_carlo_result = monte_carlo_simulation(
        a, b, f_max, num_experiments, points_per_experiment
    )
    print(f"Інтеграл за методом Монте-Карло: {monte_carlo_result:.6f}")

    # Перевірка через SciPy
    quad_result, error = spi.quad(f, a, b)
    print(f"Інтеграл з функцією quad: {quad_result:.6f}")
    print(f"Абсолютна похибка: {abs(quad_result - monte_carlo_result):.6f}")
