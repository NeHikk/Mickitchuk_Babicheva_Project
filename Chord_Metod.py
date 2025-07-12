"""модификация программы для функции ввода и графика в одном окне"""

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math

class ChordMethodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Решение нелинейных уравнений методом хорд")
        self.root.geometry("1200x800")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Фрейм для ввода данных
        input_frame = ttk.LabelFrame(self.root, text="Параметры метода", padding=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        
        # Поля ввода
        ttk.Label(input_frame, text="Функция f(x):").grid(row=0, column=0, sticky="w")
        self.func_entry = ttk.Entry(input_frame, width=30)
        self.func_entry.grid(row=0, column=1, padx=5, pady=5)
        self.func_entry.insert(0, "x**3 - 2*x - 5")
        
        ttk.Label(input_frame, text="Интервал [a, b]:").grid(row=1, column=0, sticky="w")
        self.a_entry = ttk.Entry(input_frame, width=10)
        self.a_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.a_entry.insert(0, "1")
        
        self.b_entry = ttk.Entry(input_frame, width=10)
        self.b_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        self.b_entry.insert(0, "3")
        
        ttk.Label(input_frame, text="Точность:").grid(row=2, column=0, sticky="w")
        self.eps_entry = ttk.Entry(input_frame, width=10)
        self.eps_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.eps_entry.insert(0, "1e-6")
        
        ttk.Label(input_frame, text="Макс. итераций:").grid(row=3, column=0, sticky="w")
        self.max_iter_entry = ttk.Entry(input_frame, width=10)
        self.max_iter_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.max_iter_entry.insert(0, "100")
        
        # Кнопки
        ttk.Button(input_frame, text="Решить", command=self.solve).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Фрейм для вывода результатов
        result_frame = ttk.LabelFrame(self.root, text="Результаты", padding=10)
        result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        
        self.result_text = tk.Text(result_frame, height=5, width=50)
        self.result_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Фрейм для графиков
        graph_frame = ttk.LabelFrame(self.root, text="Графики", padding=10)
        graph_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.figure, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Настройка растягивания
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        
    def solve(self):
        try:
            # Получаем данные из полей ввода
            func_str = self.func_entry.get()
            f = lambda x: eval(func_str, {'x': x, 'math': math})
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            epsilon = float(self.eps_entry.get())
            max_iter = int(self.max_iter_entry.get())
            
            # Проверка корректности интервала
            if a >= b:
                raise ValueError("a должно быть меньше b")
            
            # Решение уравнения
            root, iterations = self.chord_method(f, a, b, epsilon, max_iter)
            
            # Вывод результатов
            result_str = f"Найденный корень: {root:.8f}\n"
            result_str += f"Значение функции: {f(root):.3e}\n"
            result_str += f"Итераций: {len(iterations)}\n"
            result_str += f"Условие f(a)*f(b) < 0: {f(a)*f(b) < 0}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            
            # Построение графиков
            self.plot_function(f, a, b, root, iterations)
            
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def chord_method(self, f, a, b, epsilon=1e-6, max_iter=1000):
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
    
    def plot_function(self, f, a, b, root, iterations):
        # Очищаем предыдущие графики
        self.ax1.clear()
        self.ax2.clear()
        
        # Подготовка данных для графиков
        x_vals = np.linspace(a, b, 400)
        y_vals = [f(x) for x in x_vals]
        
        # График функции
        self.ax1.plot(x_vals, y_vals, label='f(x)')
        self.ax1.axhline(0, color='black', linewidth=0.5)
        self.ax1.axvline(root, color='red', linestyle='--', label=f'Корень: {root:.6f}')
        self.ax1.scatter([a, b], [f(a), f(b)], color='green', label='Границы интервала')
        self.ax1.set_title('График функции и найденный корень')
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('f(x)')
        self.ax1.legend()
        self.ax1.grid()
        
        # График сходимости
        iter_nums = [it[0] for it in iterations]
        root_approx = [it[1] for it in iterations]
        self.ax2.plot(iter_nums, root_approx, 'o-', label='Приближение корня')
        self.ax2.axhline(root, color='red', linestyle='--', label='Истинный корень')
        self.ax2.set_title('Сходимость метода хорд')
        self.ax2.set_xlabel('Номер итерации')
        self.ax2.set_ylabel('Приближение корня')
        self.ax2.legend()
        self.ax2.grid()
        
        # Обновляем холст
        self.figure.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChordMethodApp(root)
    root.mainloop()