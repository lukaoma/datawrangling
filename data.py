#get necessary extensions
import mysql.connector
import csv

#connect to db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gameaccidents"
)

#set up cursor for db
mycursor = mydb.cursor()

#open the games csv
with open('GamesClean2018.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in myCSVReader:
        #get data from CSV
        title = "'" + row['title'] + "'"
        cleantitle = row['title']
        genre = "'" + row['genre'] + "'"
        console = "'" + row['console'] + "'"
        sales = "'" + row['na_sales'] + "'"
        date = "'" + row['release_date'] + "'"
        
        #see if title has been loaded, get its id
        sql = "SELECT id FROM games WHERE title = \"" + cleantitle + "\""
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print myresult
        
        if len(myresult) == 0:
            #unloaded titles get loaded
            print "not loaded"
            sql = "INSERT INTO games (title,genre) VALUES (" + title + "," + genre + ")"
            print sql
            mycursor.execute(sql)
            mydb.commit()
            
            #get the id
            sql = "SELECT id FROM games WHERE title = \"" + cleantitle + "\""
            print sql
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
        else:
            print "already loaded!"
        
        gameid = myresult
        #gameid[0[0]] = gameid[0[0]].str.strip(',')
        print gameid[0][0]
        gameid = str(gameid[0][0])
        
        #release data entered
        sql = "INSERT INTO releases (console,sales,date,game_id) VALUES (" + console + "," + sales + "," + date + "," + gameid + ")"
        print sql
        mycursor.execute(sql)
        mydb.commit()
        
        #get the release_id
        releaseid = str(mycursor.lastrowid)
        print releaseid
        
        #get all the days of "release week"
        day1 = date = "'" + row['release_date'] + "'"
        day2 = date = "'" + row['day2'] + "'"
        day3 = date = "'" + row['day3'] + "'"
        day4 = date = "'" + row['day4'] + "'"
        day5 = date = "'" + row['day5'] + "'"
        day6 = date = "'" + row['day6'] + "'"
        day7 = date = "'" + row['day7'] + "'"
        
        #associate releases with each day of the week
        #i went ahead and did this in excel rather than messing with date strings
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day1 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day2 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day3 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day4 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day5 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day6 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        sql = "INSERT INTO playdates (date, release_id) VALUES (" + day7 + "," + releaseid + ")"
        mycursor.execute(sql)
        print sql
        mydb.commit()

#open the storms csv
with open('StormsClean2018.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    #get the values
    for row in myCSVReader:
        date = "'" + row['Date'] + "'"
        stype = "'" + row['EVENT_TYPE'] + "'"
        lat = "'" + row['BEGIN_LAT'] + "'"
        lon = "'" + row['BEGIN_LON'] + "'"
        
        #insert the values
        sql = "INSERT INTO storms (date,type,lat,lon) VALUES (" + date + "," + stype + "," + lat + "," + lon + ")"
        print sql
        mycursor.execute(sql)
        mydb.commit()

#open accidents csv
with open('AccidentsClean2018.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    #get the values
    for row in myCSVReader:
        severity = row['Severity']
        date = "'" + row['Start_Time'] + "'"
        lat = "'" + row['Start_Lat'] + "'"
        lon = "'" + row['Start_Lng'] + "'"
        
        #insert the values
        sql = "INSERT INTO accidents (severity,date,lat,lon) VALUES (" + severity + "," + date + "," + lat + "," + lon + ")"
        print sql
        mycursor.execute(sql)
        mydb.commit()