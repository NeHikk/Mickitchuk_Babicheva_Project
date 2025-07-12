"""модификация программы для создания графика функциии, 
графика сходимости метода и ввода пользователем данных"""
import matplotlib.pyplot as plt
import numpy as np 

def chord_method(f, a, b, epsilon=1e-6, max_iter=1000):
    """
    Решение нелинейного уравнения методом хорд
    
    Параметры:
    f - функция, корень которой ищем
    a, b - границы интервала, на котором ищем корень
    epsilon - точность
    max_iter - максимальное число итераций
    
    Возвращает:
    x - найденный корень
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")
    
    iterations = []
    for i in range(max_iter):
        x = a - f(a) * (b - a) / (f(b) - f(a))
        iterations.append((i, x, f(x)))
        
        if abs(f(x)) < epsilon:
            return x, iterations
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    
    raise ValueError(f"Метод не сошелся за {max_iter} итераций")

def plot_function(f, a, b, root, iterations):
    """Построение графика функции и процесса поиска корня"""
    x_vals = np.linspace(a, b, 400)
    y_vals = [f(x) for x in x_vals]
    
    plt.figure(figsize=(12, 6))
    
    # График функции
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(root, color='red', linestyle='--', label=f'Корень: {root:.6f}')
    plt.scatter([a, b], [f(a), f(b)], color='green', label='Границы интервала')
    plt.title('График функции и найденный корень')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    
    # График сходимости
    plt.subplot(1, 2, 2)
    iter_nums = [it[0] for it in iterations]
    root_approx = [it[1] for it in iterations]
    plt.plot(iter_nums, root_approx, 'o-', label='Приближение корня')
    plt.axhline(root, color='red', linestyle='--', label='Истинный корень')
    plt.title('Сходимость метода хорд')
    plt.xlabel('Номер итерации')
    plt.ylabel('Приближение корня')
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    plt.show()

def input_float(prompt):
    """Ввод числа с проверкой"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

def main():
    print("Решение нелинейного уравнения методом хорд")
    print("----------------------------------------")
    
    # Ввод функции
    while True:
        try:
            func_str = input("Введите функцию f(x) (например, 'x**3 - 2*x - 5'): ")
            f = lambda x: eval(func_str, {'x': x, 'math': __import__('math')})
            break
        except:
            print("Ошибка в функции. Попробуйте еще раз.")
    
    # Ввод интервала
    print("\nВведите интервал [a, b], где ищем корень:")
    a = input_float("a = ")
    b = input_float("b = ")
    
    # Ввод параметров метода
    epsilon = input_float("\nВведите точность (по умолчанию 1e-6): ") or 1e-6
    max_iter = int(input_float("Введите максимальное число итераций (по умолчанию 100): ") or 100)
    
    # Решение уравнения
    try:
        root, iterations = chord_method(f, a, b, epsilon, max_iter)
        print(f"\nНайденный корень: {root:.8f}")
        print(f"Значение функции в корне: {f(root):.3e}")
        print(f"Количество итераций: {len(iterations)}")
        
        # Построение графиков
        plot_function(f, a, b, root, iterations)
        
    except ValueError as e:
        print(f"\nОшибка: {e}")

if __name__ == "__main__":
    main()