import random
import numpy as np

def random_predict(number: int = np.random.randint(1, 101)) -> int:
    count = 0
    max1 = 100
    min1 = 0
    predict_number = np.random.randint(1, 101) # предполагаемое число
    while True:
        count += 1
        if predict_number > number:
            max1 = predict_number - 1
            predict_number = (max1 + min1)//2
        elif predict_number < number:
            min1 = predict_number + 1
            predict_number = (max1 + min1)//2
        else:
            break
    return(count)

def score_game(random_predict) -> int:
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(53)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)

