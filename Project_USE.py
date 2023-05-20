from tkinter import *
import tkinter

ScoreEx1=0
ScoreEx2=0
ScoreEx3=0
ScoreEx4=0
ScoreEx5=0

window=Tk()
window.title('ЕГЭ 2023')
window.geometry('450x350')


texttitle1 = Label(window, text='Единый Государственный Экзамен', font=('Times New Roman', 20))
texttitle2 = Label(window, text='При выполнении заданий с кратким ответом\n впишите в поле для ответа цифру, которая\n соответствует номеру правильного ответа, или\n число, слово, последовательность букв (слов)\n или цифр. Ответ следует записывать без\n пробелов и каких-либо дополнительных символов.\n Дробную часть отделяйте от целой десятичной запятой. Единицы измерений писать не нужно.',font=('Arial', 14))
def o():
    btn.destroy()
    texttitle1.destroy()
    texttitle2.destroy()
    ex1nz = Label(window, text='Задание 1', font=('Arial', 18))
    ex1v = Label(window, text='Радиусы трех шаров равны 6, 8 и 10. Найдите\n радиус шара, объем которого\n равен сумме их объемов.',font=('Arial', 14))    
    ex1ot = Entry(window, width=10)
    window.geometry('410x350')
    ex1nz.grid()
    ex1v.grid()
    ex1ot.grid()
    def o2():
        global ScoreEx1
        if ex1ot.get() == '12':
            ScoreEx1+=1
        ex1ot.destroy()
        ex1nz.destroy()
        ex1v.destroy()
        ex1btn.destroy()
        window.geometry('450x350')
        oo1()
    def oo1():
        global ex2ot
        global ex2nz
        global ex2v
        global ex2btn
        ex2nz = Label(window, text='Задание 2', font=('Arial', 18))
        ex2v = Label(window, text='На тарелке 16 пирожков: 7 с рыбой, 5 с вареньем\n и 4 с вишней. Юля наугад выбирает один пирожок.\n Найдите вероятность того, что он\n окажется с вишней.',font=('Arial', 14))
        ex2ot = Entry(window, width=10)
        ex2btn = Button(window,text='Ответить',command=oo2)
        ex2nz.pack()
        ex2v.pack()
        ex2ot.pack()
        ex2btn.pack()
    def oo2():
        global ScoreEx2
        if ex2ot.get() == '0.25':
            ScoreEx2+=1
        ex2ot.destroy()
        ex2nz.destroy()
        ex2v.destroy()
        ex2btn.destroy()
        ooo1()
    def ooo1():
        global ex3nz
        global ex3v
        global ex3ot
        global ex3btn
        ex3nz = Label(window, text='Задание 3', font=('Arial', 18))
        ex3v = Label(window, text='Найдите корень уравнения\n log₅(4+x)=2',font=('Arial', 14))
        ex3ot = Entry(window, width=10)
        ex3btn = Button(window, text='Ответить', command=ooo2)
        window.geometry('350x250')
        ex3nz.pack()
        ex3v.pack()
        ex3ot.pack()
        ex3btn.pack()
    def ooo2():
        global ScoreEx3
        if ex3ot.get() == '21':
            ScoreEx3+=1
        ex3ot.destroy()
        ex3nz.destroy()
        ex3v.destroy()
        ex3btn.destroy()
        window.geometry('450x350')
        oooo1()
    def oooo1():
        global ex4nz
        global ex4v
        global ex4ot
        global ex4btn
        ex4nz = Label(window, text='Задание 4', font=('Arial', 18))
        ex4v = Label(window, text='Из пункта A круговой трассы выехал\n велосипедист. Через 30 минут он еще не\n вернулся в пункт А и из пункта А следом за\n ним отправился мотоциклист. Через 10 минут\n после отправления он догнал велосипедиста\n в первый раз, а еще через 30 минут после этого\n догнал его во второй раз. Найдите скорость\n мотоциклиста, если длина трассы равна 30 км.\n Ответ дайте в км/ч.', font=('Arial', 14))
        ex4ot = Entry(window, width=10)
        ex4btn = Button(window, text='Ответить',command=oooo2)
        ex4nz.pack()
        ex4v.pack()
        ex4ot.pack()
        ex4btn.pack()
    def oooo2():
        global ScoreEx4
        if ex4ot.get() == '80':
            ScoreEx4+=2
        ex4ot.destroy()
        ex4nz.destroy()
        ex4v.destroy()
        ex4btn.destroy()
        ooooo1()
    def ooooo1():
        global ex5nz
        global ex5v
        global ex5ot
        global ex5btn
        ex5nz = Label(window, text='Задание 5', font=('Arial', 18))
        ex5v = Label(window, text='Найдите точку максимума функции\n y=In(x+4)²+2x+7', font=('Arial', 14))
        ex5ot = Entry(window, width=10)
        ex5btn = Button(window, text='Ответить',command=ooooo2)
        ex5nz.pack()
        ex5v.pack()
        ex5ot.pack()
        ex5btn.pack()
    def ooooo2():
        global ScoreEx5
        if ex5ot.get() == '-5':
            ScoreEx5+=2
        ex5ot.destroy()
        ex5nz.destroy()
        ex5v.destroy()
        ex5btn.destroy()
        outcome()
    def outcome():
        otcnz = Label(window, text='Экзамен завершён!', font=('Arial', 18))
        otcnx = Label(window, text='Подведём итоги', font=('Arial', 14))
        otcsc1 = Label(window, text='Задание 1 - ' + str(ScoreEx1) + ' балл(ов)', font=('Arial', 14))
        otcsc2 = Label(window, text='Задание 2 - ' + str(ScoreEx2) + ' балл(ов)', font=('Arial', 14))
        otcsc3 = Label(window, text='Задание 3 - ' + str(ScoreEx3) + ' балл(ов)', font=('Arial', 14))
        otcsc4 = Label(window, text='Задание 4 - ' + str(ScoreEx4) + ' балла(ов)', font=('Arial', 14))
        otcsc5 = Label(window, text='Задание 5 - ' + str(ScoreEx5) + ' балла(ов)', font=('Arial', 14))
        otcscommon = Label(window, text='Общее количество баллов - ' + str(ScoreEx1 + ScoreEx2 + ScoreEx3 + ScoreEx4 + ScoreEx5) + ' балл(ов)', font=('Arial', 14))
        otcnz.pack()
        otcnx.pack()
        otcsc1.pack()
        otcsc2.pack()
        otcsc3.pack()
        otcsc4.pack()
        otcsc5.pack()
        otcscommon.pack()
    ex1btn = Button(window, text='Ответить',command=o2)
    ex1btn.grid()
btn = Button(window, text='Приступить к заданиям!',bg='lightgrey',height=3,width=40, command=o)
texttitle1.pack()
texttitle2.pack()
btn.pack()
window.mainloop()