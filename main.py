import csv
import statistics
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd


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
            genre[currentGenre].append(float(row["na_sales"]) * 10)
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


def mapAccidnets():
    df = pd.read_csv('AccidentsClean2018.csv')
    limit = 5000
    fig = go.Figure(data=go.Scattergeo(
        lon=df['Start_Lng'][1:limit],
        lat=df['Start_Lat'][1:limit],
        text=df['Severity'][1:limit],
        mode='markers',
        marker_color='red',
    ))

    fig.update_layout(
        title='Accidents<br>',
        geo_scope='usa',
    )
    fig.show()


def lineGraphClean():
    with open('StormsClean2018.csv') as csvfile:
        myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        dates = {}
        for row in myCSVReader:
            if row["Date"] not in dates:
                dates[row["Date"]] = 1
            else:
                dates[row["Date"]] += 1
        keys = sorted(dates.keys())
        scoreArray = []
        for each in keys:
            scoreArray.append(dates[each])
        plt.plot(keys, scoreArray)
        plt.ylabel('Storm events per day')
        plt.show()

def lineGraphAccident():
    with open('accidentcsv.csv') as csvfile:
        myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        accidents = {}
        for row in myCSVReader:
            if row["Start_Time"] not in accidents:
                accidents[row["Start_Time"]] = 1
            else:
                accidents[row["Start_Time"]] += 1
        keys = sorted(accidents.keys())
        scoreArray = []
        for each in keys:
            scoreArray.append(accidents[each])
        plt.plot(keys, scoreArray)
        plt.ylabel('Accidents events per day')
        plt.show()


def lineGraphGameShow():
    with open('GamesClean2018.csv') as csvfile:
        myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        games = {}
        notValid = ["title","console","genre","na_sales"]
        for row in myCSVReader:
            for col in row:
                if col not in notValid:
                    if row[col] not in games:
                        games[row[col]] = float(row["na_sales"])
                    else:
                        games[row[col]] += float(row["na_sales"])
        keys = sorted(games.keys())
        salesArray = []
        for each in keys:
            salesArray.append(games[each])
        plt.plot(keys, salesArray)
        plt.ylabel('Sales per day')
        plt.show()


if __name__ == '__main__':
    lineGraphGameShow()
