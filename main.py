import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics

def barGraph():
    plt.rcdefaults()
    fig, ax = plt.subplots()
    genre = {}
    with open('GamesClean2018.csv') as csvfile:
        myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in myCSVReader:
            currentGenre = row['genre']
            if row['genre'] not in genre:
                genre[row['genre']] = []
            genre[currentGenre].append(float(row["na_sales"])*10)
    genreLables = []
    averageSales = []
    for singleGenre in genre:
        if singleGenre not in "Sandbox":
            genreLables.append(singleGenre)
            averageSales.append(statistics.mean(genre[singleGenre]))
    y_pos = np.arange(len(genreLables))
    ax.barh(y_pos, averageSales, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(genreLables)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Sales (millions)')
    ax.set_title('How well did each genre do?')
    plt.show()



if __name__ == '__main__':
    barGraph()


