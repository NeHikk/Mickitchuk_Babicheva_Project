# Импорт библиотеки для создания графического интерфейса
import tkinter as tk

# Импорт тематических виджетов и диалоговых окон из tkinter
from tkinter import ttk, messagebox

# Импорт библиотеки для построения графиков
import matplotlib.pyplot as plt

# Импорт модуля для встраивания графиков matplotlib в tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Импорт библиотеки для математических вычислений
import numpy as np

# Импорт стандартной математической библиотеки
import math

# Импорт класса для создания дополнительных окон
from tkinter import Toplevel

# Основной класс приложения
class ChordMethodApp:
    # Конструктор класса, вызывается при создании объекта
    def __init__(self, root):
        # Сохранение ссылки на главное окно
        self.root = root
        
        # Установка заголовка окна
        self.root.title("Решение нелинейных уравнений методом хорд")
        
        # Установка начального размера окна (ширина x высота)
        self.root.geometry("1200x800")
        
        # Вызов методов инициализации интерфейса
        self.create_menu()
        self.create_widgets()
        self.create_tooltips()
    
    # Метод создания меню
    def create_menu(self):
        # Создание главного меню
        menubar = tk.Menu(self.root)
        
        # Создание выпадающего меню "Справка"
        help_menu = tk.Menu(menubar, tearoff=0)  # tearoff=0 отключает возможность отрыва меню
        
        # Добавление пункта "Примеры функций" с привязкой к методу show_examples
        help_menu.add_command(label="Примеры функций", command=self.show_examples)
        
        # Добавление пункта "О программе" с привязкой к методу show_about
        help_menu.add_command(label="О программе", command=self.show_about)
        
        # Добавление выпадающего меню в главное меню
        menubar.add_cascade(label="Справка", menu=help_menu)
        
        # Установка созданного меню в главное окно
        self.root.config(menu=menubar)
    
    # Метод показа примеров функций
    def show_examples(self):
        # Многострочный текст с примерами
        examples = """Примеры ввода функций:
1. Полиномы:
   x**3 - 2*x - 5
   2*x**4 - 3*x**2 + x - 5

2. Тригонометрические функции:
   math.sin(x) - 0.5
   math.cos(x) - x

3. Экспоненциальные функции:
   math.exp(-x) - math.sin(x)
   x*math.exp(-x) - 0.2

4. Логарифмические функции:
   math.log(x) - 1
   math.log10(x+1) - x/2

Примечание: используйте math. для математических функций"""
        
        # Вызов метода для отображения окна с примерами
        self.show_info_window("Примеры функций", examples)
    
    # Метод показа информации о программе
    def show_about(self):
        # Текст с информацией о программе
        about = """Программа для решения нелинейных уравнений
методом хорд (секущих)

Версия 1.0
Автор: Ваше имя"""
        
        # Вызов метода для отображения окна "О программе"
        self.show_info_window("О программе", about)
    
    # Метод создания информационного окна
    def show_info_window(self, title, message):
        # Создание нового окна
        window = Toplevel(self.root)
        
        # Установка заголовка окна
        window.title(title)
        
        # Установка размера окна
        window.geometry("500x300")
        
        # Создание текстового поля с переносом по словам
        text = tk.Text(window, wrap=tk.WORD, padx=10, pady=10)
        
        # Вставка текста в конец текстового поля
        text.insert(tk.END, message)
        
        # Блокировка редактирования текста
        text.config(state=tk.DISABLED)
        
        # Размещение текстового поля с заполнением всего пространства
        text.pack(fill=tk.BOTH, expand=True)
        
        # Создание кнопки "Закрыть"
        btn = ttk.Button(window, text="Закрыть", command=window.destroy)
        
        # Размещение кнопки с отступами
        btn.pack(pady=10)
    
    # Метод создания виджетов интерфейса
    def create_widgets(self):
        # Создание фрейма для параметров с заголовком и отступами
        input_frame = ttk.LabelFrame(self.root, text="Параметры метода", padding=10)
        
        # Размещение фрейма в сетке (0 строка, 0 столбец)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        
        # Создание метки для поля ввода функции
        ttk.Label(input_frame, text="Функция f(x):").grid(row=0, column=0, sticky="w")
        
        # Создание поля ввода функции шириной 30 символов
        self.func_entry = ttk.Entry(input_frame, width=30)
        
        # Размещение поля ввода в сетке фрейма
        self.func_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Вставка примера функции по умолчанию
        self.func_entry.insert(0, "x**3 - 2*x - 5")
        
        # Создание метки для интервала
        ttk.Label(input_frame, text="Интервал [a, b]:").grid(row=1, column=0, sticky="w")
        
        # Создание поля ввода для 'a' шириной 10 символов
        self.a_entry = ttk.Entry(input_frame, width=10)
        
        # Размещение поля 'a' с выравниванием по левому краю
        self.a_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Вставка значения по умолчанию для 'a'
        self.a_entry.insert(0, "1")
        
        # Создание поля ввода для 'b' шириной 10 символов
        self.b_entry = ttk.Entry(input_frame, width=10)
        
        # Размещение поля 'b' с выравниванием по правому краю
        self.b_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        
        # Вставка значения по умолчанию для 'b'
        self.b_entry.insert(0, "3")
        
        # Создание метки для точности
        ttk.Label(input_frame, text="Точность:").grid(row=2, column=0, sticky="w")
        
        # Создание поля ввода для точности
        self.eps_entry = ttk.Entry(input_frame, width=10)
        
        # Размещение поля точности
        self.eps_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Вставка значения точности по умолчанию
        self.eps_entry.insert(0, "1e-6")
        
        # Создание метки для максимального числа итераций
        ttk.Label(input_frame, text="Макс. итераций:").grid(row=3, column=0, sticky="w")
        
        # Создание поля ввода для итераций
        self.max_iter_entry = ttk.Entry(input_frame, width=10)
        
        # Размещение поля итераций
        self.max_iter_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        # Вставка значения по умолчанию
        self.max_iter_entry.insert(0, "100")
        
        # Создание кнопки "Решить" с привязкой к методу solve
        ttk.Button(input_frame, text="Решить", command=self.solve).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Создание кнопки "Пример" с привязкой к методу load_example
        ttk.Button(input_frame, text="Пример", command=self.load_example).grid(row=5, column=0, columnspan=2, pady=5)
        
        # Создание фрейма для результатов
        result_frame = ttk.LabelFrame(self.root, text="Результаты", padding=10)
        
        # Размещение фрейма результатов
        result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        
        # Создание текстового поля для вывода результатов
        self.result_text = tk.Text(result_frame, height=5, width=50)
        
        # Размещение текстового поля
        self.result_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Создание фрейма для графиков
        graph_frame = ttk.LabelFrame(self.root, text="Графики", padding=10)
        
        # Размещение фрейма графиков (объединение двух строк)
        graph_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        # Создание фигуры matplotlib с 1 строкой и 2 столбцами графиков
        self.figure, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Создание холста для встраивания графиков в tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=graph_frame)
        
        # Размещение холста с заполнением всего доступного пространства
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Настройка растягивания столбца 1 при изменении размеров окна
        self.root.columnconfigure(1, weight=1)
        
        # Настройка растягивания строк 0 и 1
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
    
    # Метод создания всплывающих подсказок
    def create_tooltips(self):
        # Словарь с подсказками для каждого поля ввода
        tooltips = {
            self.func_entry: "Примеры: x**3 - 2*x - 5, math.sin(x) - 0.5",
            self.a_entry: "Левая граница интервала (число)",
            self.b_entry: "Правая граница интервала (число, должно быть > a)",
            self.eps_entry: "Точность решения (например, 1e-6)",
            self.max_iter_entry: "Максимальное число итераций (целое число)"
        }
        
        # Создание объекта стиля
        style = ttk.Style()
        
        # Настройка стиля для подсказок
        style.configure("Tooltip.TLabel", 
                       background="#ffffe0",  # Цвет фона
                       relief="solid",       # Граница
                       padding=5,            # Отступы
                       borderwidth=1)        # Толщина границы
        
        # Создание подсказок для каждого виджета
        for widget, text in tooltips.items():
            # Создание метки с подсказкой
            label = ttk.Label(self.root, 
                             text=text, 
                             style="Tooltip.TLabel", 
                             wraplength=200)  # Максимальная ширина перед переносом
            
            # Функция показа подсказки при наведении
            def enter(event, lbl=label):
                # Позиционирование подсказки рядом с курсором
                lbl.place(x=event.x_root - self.root.winfo_rootx(), 
                         y=event.y_root - self.root.winfo_rooty() + 20)
            
            # Функция скрытия подсказки
            def leave(event, lbl=label):
                lbl.place_forget()
            
            # Привязка событий наведения и ухода курсора
            widget.bind("<Enter>", enter)
            widget.bind("<Leave>", leave)
    
    # Метод загрузки примера
    def load_example(self):
        # Очистка и установка примера функции
        self.func_entry.delete(0, tk.END)
        self.func_entry.insert(0, "math.sin(x) - x/2")
        
        # Очистка и установка примера для 'a'
        self.a_entry.delete(0, tk.END)
        self.a_entry.insert(0, "1")
        
        # Очистка и установка примера для 'b'
        self.b_entry.delete(0, tk.END)
        self.b_entry.insert(0, "3")
        
        # Очистка и установка примера точности
        self.eps_entry.delete(0, tk.END)
        self.eps_entry.insert(0, "1e-6")
        
        # Очистка и установка примера итераций
        self.max_iter_entry.delete(0, tk.END)
        self.max_iter_entry.insert(0, "100")
    
    # Метод решения уравнения
    def solve(self):
        try:
            # Получение строки функции из поля ввода
            func_str = self.func_entry.get()
            
            # Создание lambda-функции из строки с доступом к math
            f = lambda x: eval(func_str, {'x': x, 'math': math})
            
            # Получение параметров из полей ввода
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            epsilon = float(self.eps_entry.get())
            max_iter = int(self.max_iter_entry.get())
            
            # Проверка корректности интервала
            if a >= b:
                raise ValueError("a должно быть меньше b")
            
            # Вызов метода хорд для решения уравнения
            root, iterations = self.chord_method(f, a, b, epsilon, max_iter)
            
            # Формирование строки с результатами
            result_str = f"Найденный корень: {root:.8f}\n"
            result_str += f"Значение функции: {f(root):.3e}\n"
            result_str += f"Итераций: {len(iterations)}\n"
            result_str += f"Условие f(a)*f(b) < 0: {f(a)*f(b) < 0}"
            
            # Очистка и вывод результатов в текстовое поле
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            
            # Построение графиков
            self.plot_function(f, a, b, root, iterations)
            
        except Exception as e:
            # Показ сообщения об ошибке
            messagebox.showerror("Ошибка", str(e))
    
    # Реализация метода хорд
    def chord_method(self, f, a, b, epsilon=1e-6, max_iter=1000):
        # Проверка условия сходимости метода
        if f(a) * f(b) >= 0:
            raise ValueError("Функция должна иметь разные знаки на концах интервала")
        
        # Список для хранения истории итераций
        iterations = []
        
        # Основной цикл метода
        for i in range(max_iter):
            # Формула метода хорд
            x = a - f(a) * (b - a) / (f(b) - f(a))
            
            # Сохранение информации о текущей итерации
            iterations.append((i, x, f(x)))
            
            # Проверка достижения требуемой точности
            if abs(f(x)) < epsilon:
                return x, iterations
            
            # Выбор нового интервала
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
        
        # Если не сошлось за max_iter итераций
        raise ValueError(f"Метод не сошелся за {max_iter} итераций")
    
    # Метод построения графиков
    def plot_function(self, f, a, b, root, iterations):
        # Очистка предыдущих графиков
        self.ax1.clear()
        self.ax2.clear()
        
        # Создание массива x-значений
        x_vals = np.linspace(a, b, 400)
        
        # Вычисление y-значений для функции
        y_vals = [f(x) for x in x_vals]
        
        # Построение графика функции
        self.ax1.plot(x_vals, y_vals, label='f(x)')
        
        # Горизонтальная линия y=0
        self.ax1.axhline(0, color='black', linewidth=0.5)
        
        # Вертикальная линия корня
        self.ax1.axvline(root, color='red', linestyle='--', label=f'Корень: {root:.6f}')
        
        # Точки границ интервала
        self.ax1.scatter([a, b], [f(a), f(b)], color='green', label='Границы интервала')
        
        # Настройки первого графика
        self.ax1.set_title('График функции и найденный корень')
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('f(x)')
        self.ax1.legend()
        self.ax1.grid()
        
        # Подготовка данных для графика сходимости
        iter_nums = [it[0] for it in iterations]  # Номера итераций
        root_approx = [it[1] for it in iterations]  # Приближения корня
        
        # Построение графика сходимости
        self.ax2.plot(iter_nums, root_approx, 'o-', label='Приближение корня')
        
        # Линия истинного корня
        self.ax2.axhline(root, color='red', linestyle='--', label='Истинный корень')
        
        # Настройки второго графика
        self.ax2.set_title('Сходимость метода хорд')
        self.ax2.set_xlabel('Номер итерации')
        self.ax2.set_ylabel('Приближение корня')
        self.ax2.legend()
        self.ax2.grid()
        
        # Оптимизация расположения графиков
        self.figure.tight_layout()
        
        # Обновление холста
        self.canvas.draw()

# Точка входа в программу
if __name__ == "__main__":
    # Создание главного окна
    root = tk.Tk()
    
    # Создание экземпляра приложения
    app = ChordMethodApp(root)
    
    # Запуск главного цикла обработки событий
    root.mainloop()