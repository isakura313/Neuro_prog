"""
здесь у нас будет урок  по тому, как у нас будет работать самая первая наша нейросеть
Итак, мы пытаемся узнать коэфицент перевода между милям и километрами
"""

mili = 62.37
kilometri = 100

#мы можем без проблем расчитать это формулой. Но положим, что мы делаем алгоритм, подбирающий правильные значения
#Итого, мы делаем коэфицент перевода

coe = 0.5

#Запускаем расчет нашей ошибки в нашем коде

def assor(coef):
    Error = mili - (kilometri * coef)
    print(Error)
# assor(coe)
#Окей, наша ошибка типа 12.369999999999997
# Попробуем другое значение
coe = 0.6
assor(coe)
#Отлично, наша ошибка многократно уменьшилась. Теперь попробуем ее увеличить
coe = 0.63
assor(coe)
#Очень плохо, теперь ошибка у нас отрицательная! Что-то явно не то.
#Однако чем подбирать руками, давайте напишем на все это дело функцию


def assert_auto(main_cond, second_cond, learning_rate, coe, epoch):
    for i in range(epoch):
        error = second_cond - (main_cond * coe)
        coe += learning_rate
        print(error)
        print(coe)
        if(error<0.02):
            print("our final result: ")
            print(coe)
            return

lr = 0.001
coefic = 0.5

assert_auto(kilometri, mili, lr, coefic, 500)

#пускай немного неточно, но нам удалось добраться до тех значений которые мы хотели
#Теперь попробуем эту штуку в вычислении коэфицента фаренгейта

dium = 2.54
cent = 1
lr = 0.001

assert_auto(cent, dium, lr, coefic, 5000)

print(0.6250000000000001*100)
print(0.5*300)



