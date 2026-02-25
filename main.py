import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

import numpy as np

#здесь будут поля ввода для матриц
entries_matrix_a= []
entries_matrix_b= []
entries_matrix_d= []





#функция которая будет отчищать окно от старых матриц
def clear_old_matrices():
    global result_label
    if result_label is not None:
        result_label.destroy()
    # Удаляем ВСЕ фреймы
    #цикл прохдит по всем элементам окна
    for widget in root.winfo_children():
        #если объяект это фрейм то он удаляется (isinstance - встроеная функция которая проверяет является ли объект экземпляром класса)
        #если объект является виджетом и его класс тк фрейм то объект удаляется, то есть у нас класс тк фрейм только поля ввода, а у кнопок класс -button, у меток класс- label, у выпадающего списка класс - combobox по этому они не удаляться
        if isinstance(widget, tk.Frame):
            widget.destroy()




def create_matrices():
    global entries_matrix_a, entries_matrix_b, result_label

    if result_label is not None:
        result_label.destroy()
        #вообще как бы избыточно тк до первого вызова функции ниже перед калькулейт я ее уже обнуляю но пусть будет
        #если ты это читаешь и тебе не нравится лишнее обнуление можешь удалить
        result_label = None

    #обнуляем на всякий случай вдруг до этого были созданы матрицы
    entries_matrix_a = []
    entries_matrix_b = []

#при вызове функции все старые поля будут удаляться и создаваться новые на их месте
    clear_old_matrices()

    print('кнопка нажата')
    selected_size=combo.get()
    #разбиваем строку по букве 'x'
    size_parts=selected_size.split('x')

    #преобразуем в числа
    #строки
    rows=int(size_parts[0])
    #столбцы
    cols=int(size_parts[1])

    print(f'выбран размер: {selected_size}')
    print(f'Строк: {rows}, столбцов: {cols}')

    #создаем контейнер для матрицы A


    #Frame() это просто прямоугольная область для полей матрицы А
    #Frame - просто невидимая прямоугольная область для организации виджетов
    frame_matrix_a= tk.Frame(root)
    # pack(pady=10) - размещаем эту область в окне с отступом 10px сверху/снизу
    frame_matrix_a.pack(pady=10)

    #подпись "матрица А"
    label_a = tk.Label(frame_matrix_a,text='Матрца A')
    # grid() - указываем КОНКРЕТНОЕ место для надписи ВНУТРИ frame
    label_a.grid(row=0,column=0,columnspan=cols)

# Создаем поля ввода в виде таблицы rows x cols
#Цикл перебирает каждую строку и вложенный цикл перебирает каждый столбец, то есть для пересечения конкретной строки и конкретного столбца будет создано поле ввода
    for i in range(rows):          # для каждой строки
        row_entries_a=[] # временный список для строки
        for j in range(cols):      # для каждого столбца
            #Каждый элемент становится объектом entry
            #аргументы тут
            entry = tk.Entry(frame_matrix_a, width=5)  #  это конструктор (создает новый объект-поле-ввода)
            #аргумент row=i+1 номер строки в сетке grid начиная с 0)
            #аргумент column=j Номер столбца в сетке grid (начинается с 0)
            #padx и pady это расстояние в пикселях между ячейками
            entry.grid(row=i+1, column=j, padx=2, pady=2)  # размещаем в сетке (entry.grid() это метод у уже созданного объекта)
            row_entries_a.append(entry) #сохраняем поле
        entries_matrix_a.append(row_entries_a) #сохраняем строку

#матрица B
#прямоугольная область для матрицы b
    frame_matrix_b= tk.Frame(root)
    #область будет находиться с отступом 10 пикселей по y
    frame_matrix_b.pack(pady=10)

    #далее надпись 'матрица b' будет создана в frame_matrix_b
    label_b=tk.Label(frame_matrix_b,text='Матрица B')
    #конкретное место это 0 строка 0 столбец (заголовок матрицы это как бы тоже часть матрицы
    label_b.grid(row=0,column=0,columnspan=cols)

    #цикл полей ввода элементов
    for i in range(rows):
        row_entries_b=[]
        for j in range(cols):
            #все эти поля будут создаваться исключительно внутри frame_matrix_b
            #width это ширина поля ввода
            entry = tk.Entry(frame_matrix_b, width=5)
            #размещаем в сетке типо столбец за столбцом сначала первая строка i затем i+1 а столбец не меняется значит сначала один столбец затем второй и тд
            entry.grid(row=i+1, column=j, padx=2, pady=2)
            row_entries_b.append(entry)
        entries_matrix_b.append(row_entries_b)








#функция для считывания чисел из полей ввода матриц
#определяем функцию гет в аргументы которой передаем значения объектов полей ввода в которых уже что то есть
def get_entrys_matrix(enries_matrix_a,enries_matrix_b):
#определяем для них глобальные переменные но это уже лишнее тк они все равно передаются извне как аргументы
    global entries_matrix_a, entries_matrix_b
#создаем списки в которых будем хранить итоговые значения
    matrix_a=[]
    matrix_b=[]

    #row- строка col-столбец

#перебираем все строки матрицы А
#цикл фор перебирает последовательность полей ввода матрицы а
    for i in range(len(enries_matrix_a)):
        #создаем список в котором будем хранить значение символов каждой строки каждую итерацию
        row=[]
        #перебираем все столбцы в текущей матрице
        for j in range(len(enries_matrix_a[i])):
            #entry_obj это конкретный объект поля ввода
            entry_obj=entries_matrix_a[i][j]#координаты текущего объекта такая то строка такой то столбец

            value=entry_obj.get()#берем значение с этого поля  и даем это значение переменной value
            #если строка пустая то добавляем 0.0
            if value=='':
                row.append(0.0)
            #иначе пробуем выплонить row.append(float(value)) хотя как мне кажется трай тут излишнее ведь что может пойти не так
            else:
                try:
                    row.append(float(value))
                except ValueError:
                    row.append(0.0)
        #в список матрицы а добавляем строку которую только что перебрали затем цикл пойдет перебирать уже новую строку снова for i и все тоже самое
        matrix_a.append(row)


    for i in range(len(enries_matrix_b)):
        row=[]
        #перебираем все столбцы в текущей матрице
        for j in range(len(enries_matrix_b[i])):
            entry_obj=entries_matrix_b[i][j]
            value=entry_obj.get()
            if value=='':
                row.append(0.0)
            else:
                try:
                    row.append(float(value))
                except ValueError:
                    row.append(0.0)
        matrix_b.append(row)






    return np.array(matrix_a), np.array(matrix_b)



#функция для работы с одной матрицей

def create_one_matrix():
    global result_label,entries_matrix_d
    if result_label is not None:
        result_label.destroy()
        #вообще как бы избыточно тк до первого вызова функции ниже перед калькулейт я ее уже обнуляю но пусть будет
        #если ты это читаешь и тебе не нравится лишнее обнуление можешь удалить
        result_label = None

    entries_matrix_d = []

    # при вызове функции все старые поля будут удаляться и создаваться новые на их месте
    clear_old_matrices()

    print('кнопка нажата')
    selected_size = combo.get()
    # разбиваем строку по букве 'x'
    size_parts = selected_size.split('x')
    # преобразуем в числа
    # строки
    rows = int(size_parts[0])
    # столбцы
    cols = int(size_parts[1])

    print(f'выбран размер: {selected_size}')
    print(f'Строк: {rows}, столбцов: {cols}')

    # создаем контейнер для матрицы D

    # Frame() это просто прямоугольная область для полей матрицы А
    # Frame - просто невидимая прямоугольная область для организации виджетов
    frame_matrix_d = tk.Frame(root)
    # pack(pady=10) - размещаем эту область в окне с отступом 10px сверху/снизу
    frame_matrix_d.pack(pady=10)

    # подпись "матрица А"
    label_d = tk.Label(frame_matrix_d, text='Матрца D')
    # grid() - указываем КОНКРЕТНОЕ место для надписи ВНУТРИ frame
    label_d.grid(row=0, column=0, columnspan=cols)

    # Создаем поля ввода в виде таблицы rows x cols
    # Цикл перебирает каждую строку и вложенный цикл перебирает каждый столбец, то есть для пересечения конкретной строки и конкретного столбца будет создано поле ввода
    for i in range(rows):  # для каждой строки
        row_entries_d = []  # временный список для строки
        for j in range(cols):  # для каждого столбца
            # Каждый элемент становится объектом entry
            # аргументы тут
            entry = tk.Entry(frame_matrix_d, width=5)  # это конструктор (создает новый объект-поле-ввода)
            # аргумент row=i+1 номер строки в сетке grid начиная с 0)
            # аргумент column=j Номер столбца в сетке grid (начинается с 0)
            # padx и pady это расстояние в пикселях между ячейками
            entry.grid(row=i + 1, column=j, padx=2,
                       pady=2)  # размещаем в сетке (entry.grid() это метод у уже созданного объекта)
            row_entries_d.append(entry)  # сохраняем поле
        entries_matrix_d.append(row_entries_d)  # сохраняем строку



def get_entrys_matrix_one(enries_matrix_d):
    matrix_d=[]
    for i in range(len(enries_matrix_d)):
        row=[]
        for j in range(len(enries_matrix_d[i])):
            entry_obj=entries_matrix_d[i][j]
            value=entry_obj.get()
            if value=='':
                row.append(0.0)

            else:
                try:
                    row.append(float(value))
                except ValueError:
                    row.append(0.0)
        matrix_d.append(row)

    return np.array(matrix_d)


result_label = None



#функция для кнопки вычислить для одной матрицы
def calculate_for_1_matrix():
    global result_label
    if result_label is not None:
        result_label.destroy()
    print('вычисляем одну матрицу')

    matrix_d = get_entrys_matrix_one(entries_matrix_d)

    if combo_operations.get() == 'determinant':
        try:
            result = np.linalg.det(matrix_d)
            result_label = tk.Label(root, text=f'Результат: \n {result}')
            result_label.pack(pady=10)
        except np.linalg.LinAlgError:
            print('Ошибка')

    elif combo_operations.get() == 'invertible':
        try:
            result = np.linalg.inv(matrix_d)
            result_label = tk.Label(root, text=f'Результат: \n {result}')
            result_label.pack(pady=10)
        except np.linalg.LinAlgError:
            print('Ошибка')


    elif combo_operations.get() == 'transposition':
        try:
            result = matrix_d.T
            result_label = tk.Label(root, text=f'Результат: \n {result}')
            result_label.pack(pady=10)
        except np.linalg.LinAlgError:
            print('Ошибка')





    #print(f'матрица D:\n {matrix_d}')



















#функция для кнопки вычислить
def calculate():
    global result_label
    if result_label is not None:
        result_label.destroy()
    print('вычисляем')




    matrix_a,matrix_b=get_entrys_matrix(entries_matrix_a,entries_matrix_b)

    print(f'матрица A \n {matrix_a}')
    print(f'матрица B \n {matrix_b}')
    if combo_operations.get() == '+':
        result=matrix_a+matrix_b
        result_label=tk.Label(root, text=f'Результат: \n {result}')
        result_label.pack(pady=10)

    elif combo_operations.get() == '-':
        result=matrix_a-matrix_b
        result_label = tk.Label(root, text=f'Результат: \n {result}')
        result_label.pack(pady=10)
    #elif combo_operations.get() == 'multiplication scalar':
    #    result=matrix_d*КАКОЕ ТО ЧИСЛО

    elif combo_operations.get() == 'multiplication':
        result=matrix_a@matrix_b
        result_label = tk.Label(root, text=f'Результат: \n {result}')
        result_label.pack(pady=10)



    #elif combo_operations.get() == 'invertible':
    #    try:
    #        result=np.linalg.inv(matrix_d)
    #    except np.linalg.LinAlgError:
    #        print('Ошибка')

    #else:
       # messagebox.showwarning("Предупреждение", "Выберите операцию")
     #   return  # просто выходим без return значения

    print(f'Результат операции: \n {result}')





    #получаем размер матрицы
    #selected_size=combo.get()



#окно
#создаем объект класса Tk - главное окно. Tk() это конструктор он создает экзеспляр класса
root = Tk()
#вызываем метод класса Tk у объекта root (заголовок)
root.title('matix_calculator')
#размер
root.geometry('700x700')

#создаем объект-метку (надпись) класса label
#label() это конструктор класса меток
#аргументы это root это родительское окно где будет размещена метка, text = текст который будет показан
#tk.label потому что из модуля tkinter as tk
label =tk.Label(root, text='выберите размер матрицы/введите свой размер: ')
# pack() - метод всех виджетов tkinter для размещения в окне
# pady=10 - вертикальные отступы (сверху и снизу по 10 пикселей)
# padx - горизонтальные отступы (слева и справа)а pady - вертикальные для этой надписи вертикальные например
label.pack(pady=10)

#выпадающий список с размерами
sizes=['2x2','3x3','4x4']
#создаем объект combo с помощью конструктора выпадающего списка ttk.Combobox (объект класса Combovox)
#ttk. потому что combobox из модуля ttk
#аргументы root значит что создаем выпадающий список в родительском окне, а values выпадающие значения
combo= ttk.Combobox(root,values=sizes)
#вертикальные отступы
combo.pack(pady=5)









label_op=tk.Label(root, text='Выберите операцию: ')
label_op.pack()

#выпадающий список с операциями

operations = ['determinant','transposition','invertible','multiplication','multiplication scalar #недоступно','+','-']
combo_operations=ttk.Combobox(root,values=operations)
combo_operations.pack(pady=5)

#Режим одной матрицы

btn_one_matrix=tk.Button(root, text='создать одну матрицу', command=create_one_matrix)
btn_one_matrix.pack(pady=5)









#кнопка создаения матриц
#объект button класса Button
#tk.Button() конструктор кнопки
#root - где будет кнопка, text= текст отобразиться, command - функция, которая вызовется при нажатии кнопки( БЕЗ СКОБОК)
button=tk.Button(root, text='Создать две матрицы', command=create_matrices)
button.pack(pady=10)



btn_one_matrix_calculate=tk.Button(root, text='Вычислить для ОДНОЙ матрицы', command=calculate_for_1_matrix)
btn_one_matrix_calculate.pack(pady=5)


#кнопка вычислить
button_calculate= tk.Button(root, text= 'вычислить для ДВУХ матриц',command=calculate)
button_calculate.pack(pady=10)


button_clear_all=tk.Button(root, text='отчистить всё', command=clear_old_matrices)
button_clear_all.pack(pady=5)



# Загружаем иконку (добавь перед mainloop)
icon = tk.PhotoImage(file="assets/tomoko_math.png")
root.iconphoto(True, icon)





# Запускаем главный цикл обработки событий
# Программа переходит в режим ожидания действий пользователя
# (клики, ввод текста, перемещение окна и т.д.)
# Без mainloop() окно появится и сразу закроется
root.mainloop()