# модуль 6 - викторина

right_answer = 0
wrong_answer = 0
new_game = 'yes'

dictionary_of_writers = {'А.С. Пушкин': 1799,
                         'М.Ю. Лермонтов': 1814,
                         'А.П. Чехов': 1904,
                         'Л.Н. Толстой': 1828,
                         'М.А. Булгаков': 1940,
                         }
while new_game == 'yes':

    year_ = None

    for i in range(len(list(dictionary_of_writers.keys()))):

        name_writers = list(dictionary_of_writers.keys())[i]
        birthday_writers = list(dictionary_of_writers.values())[i]

        while year_ != str(birthday_writers):

            year_ = input('введите год рождения ' + f'{name_writers}' + ' : ')

            if year_ == str(birthday_writers):
                right_answer += 1

                if year_ == list(dictionary_of_writers.values())[-1]:
                    break
            else:
                wrong_answer += 1

    print('количество правильных ответов : ', right_answer)
    print('количество ошибок : ', wrong_answer)
    print('процент правильных ответов : ', right_answer * 100 / (right_answer + wrong_answer))
    print('процент неправильных ответов : ', wrong_answer * 100 / (right_answer + wrong_answer))

    new_game = input('начать игру сначала? ввести yes/no : ')
