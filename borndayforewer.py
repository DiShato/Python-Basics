# модуль 5 - замена цикла for (модуля3)  на while

year_ = None
day_ = None

while year_ != str(1799):

    year_ = input('введите год рождения А.С. Пушкина : ')

    if year_ == str(1799):

        while day_ != str(6):

            day_ = input('введите день рождения А.С. Пушкина : ')

            if day_ == str(6):
                print('верно')
