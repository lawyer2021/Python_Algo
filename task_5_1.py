# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from statistics import mean

quantity_companies = int((input('Введите количество компаний: ')))
companies = {}
max_comp = {}
min_comp = {}
all_profit = []
max_profit, min_profit = (0,) * 2
while quantity_companies > 0:
    name = input("Введите " + str(quantity_companies) + " Наименования: ")
    profit = list(map(int, (input('Введите прибыль за 4 квартала через пробел: ').split())))
    quantity_companies -= 1
    companies[name] = profit
for k, v in companies.items():
    print(f' Средний размер прибыли компании {k} - {round(mean(v), 2)}')
    all_profit += v
    if mean(v) > mean(all_profit):
        max_comp[k] = k, mean(v)
    else:
        min_comp[k] = k, mean(v)
print(
    f' Средний размер прибыли всех компаний составил:  {mean(all_profit)} \n Прибыль выше среднего у {", ".join(map(str, [k for k in max_comp.keys()]))} \n Прибыль ниже среднего у {", ".join(map(str, [k for k in min_comp.keys()]))}')
