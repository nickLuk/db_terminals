import mysql.connector
import requests


def create_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bank")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bank"
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS terminals (id INT AUTO_INCREMENT PRIMARY KEY, address VARCHAR(255), city VARCHAR(255), latitude INT(20), longitude INT(20))")

def data_terminals():
        choice_city = input("Enter city:  ")
        url = ("https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city={}".format(choice_city))
        response = requests.get(url)
        print("res Result = {0}", response)
        data = response.json()
        for item in data["devices"]:
            print(item["fullAddressEn"] + "\n" + item["cityEN"] + "\n" + item["latitude"] + "\n" + item["longitude"])
            print ("==============================================")