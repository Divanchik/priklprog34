# сумма всех умерших
import pandas as pd
from multiprocessing import Pool
from time import sleep, monotonic
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # считать таблицу
    df = pd.read_csv("data.csv", sep=',', encoding='windows-1251')
    # вывести в консоль число столбцов и их названия, типы данных, число строк
    print("Кол-во столбцов:", len(df.columns))
    print(df.dtypes, end='\n\n')
    print("Кол-во строк:", len(df['Страна']), end='\n\n')
    # изучить таблицу
    print(df.isnull().sum(), end='\n\n')
    # избавиться от нежелательных данных
    df.fillna(-1)

    # dead_list = list(df['Умерли'])
    fig = plt.figure()
    plt.title("Время выполнения")
    plt.ylabel("Время, сек")
    plt.xlabel("Количество процессов")
    xvals = []
    yvals = []
    for i in range(1, 9):
        t_s = monotonic()
        with Pool(i) as pl:
            print(pl.apply(sum, [df['Умерли']]))
        print(i, "time:", monotonic()-t_s)
        xvals.append(i)
        yvals.append(round(monotonic()-t_s, 3))
    # plt.plot(xvals, yvals, color='teal', linestyle='--', marker='.', linewidth=1, markersize=10)
    plt.plot(xvals, yvals, marker='.', markersize=10)
    plt.savefig("graph.png")
    plt.show()


