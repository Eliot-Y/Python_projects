from random import *

answers_list = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
                'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
                'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
                'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',
                'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.\nКак тебя зовут?')
print('Привет', input())

user_answer = 'да'
while user_answer == 'да':
    input('Задайте вопрос: ')
    print(choice(answers_list))
    user_answer = input('Желаете снова задать вопрос? Введите \"да\"\nда')

print('Возвращайся если возникнут вопросы!')