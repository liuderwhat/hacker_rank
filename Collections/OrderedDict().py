'''
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
from collections import OrderedDict

def trac(num, meal):
    for _ in range(num):
        meal_info = list(i for i in input().split())
        if len(meal_info) > 2:
            meal_name = ' '.join(meal_info[:-1])
            if meal_name in meal.keys():
                meal[meal_name] += int(meal_info[-1])
            else:
                meal[meal_name] = int(meal_info[-1])
        else:
            meal_name = meal_info[0]
            if meal_name in meal.keys():
                meal[meal_name] += int(meal_info[-1])
            else:
                meal[meal_name] = int(meal_info[-1])

    [print(*i) for i in meal.items()]

def trac2(num, meal):
    for _ in range(num):
        meal_info = list(i for i in input().split())
        if len(meal_info) > 2:
            meal_name = ' '.join(meal_info[:-1])
        else:
            meal_name = meal_info[0]
        meal[meal_name] = meal.get(meal_name, 0) + int(meal_info[-1])

    [print(*i) for i in meal.items()]


num = int(input())
meal = OrderedDict()
trac2(num, meal)