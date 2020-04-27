import sqlite3
import requests
import time

response=requests.get("https://covid19.th-stat.com/api/open/today")
data=response.json()

timeis = time.localtime()
date = time.strftime('%M',timeis)


def create():
    with sqlite3.connect("databasecovidtoday2.sqlite") as con:
        sql_cmd = """
        create table covidtoday(
            UpdateDate text primary key,
            Confirmed text,
            Recovered text,
            Hospitalized text,
            Deaths text);
        """
        con.execute(sql_cmd)

def delete_all():
    with sqlite3.connect("databasecovidtoday2.sqlite") as con:
                sql_cmd = """
                    delete from covidtoday
                """
                con.execute(sql_cmd)

def insert(params):
    with sqlite3.connect("databasecovidtoday2.sqlite") as con:
                sql_cmd = """
                    insert into covidtoday(UpdateDate,Confirmed,Recovered,Hospitalized,Deaths) values(?,?,?,?,?);
                """
                con.execute(sql_cmd,params)


def select():
    with sqlite3.connect("databasecovidtoday2.sqlite") as con:
                sql_cmd = """
                    select * from covidtoday
                """
                for row in con.execute(sql_cmd):
                    print(row)
def loop():
    select()
    time.sleep(3000)
    try:
        print("ทำงาน1")
        insert((data["UpdateDate"],data["Confirmed"],data["Recovered"],data["Hospitalized"],data["Deaths"]))    
        loop()
    except:
        print("ทำงาน2")
        loop()

loop()