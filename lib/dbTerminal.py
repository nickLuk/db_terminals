import mysql.connector
import requests
from mysql.connector import Error
if __name__ == "__main__":
    pass


class Db_terminal():

    def __init__(self, host: str, user: str, passwd: str, database: str):
        self.__db = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )

    
    
    def insert_data(self):
    
        cursor = self.__db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS bank")
        cursor.execute("USE bank")
        choice_city = input("Enter city:  ")
        URL = ("https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city={}".format(choice_city))
        response = requests.get(URL)
        print("res Result = {0}", response)
        data = response.json()
    

        for item in data["devices"]:
            sql="INSERT INTO terminals (address,city,latitude,longitude) VALUES (%s,%s, %s, %s)"
            val = (item["fullAddressEn"],item["cityEN"],item["latitude"],item["longitude"])
            result = cursor.execute(sql,val)
            self.__db.commit()
            print(item["fullAddressEn"]+"\n"+item["cityEN"]+"\n"+item["latitude"]+"\n"+item["longitude"])
            print ("==============================================")
        return result
    
    def get_city(self):
        cursor = self.__db.cursor()
        choise_user = input("Enter city  from DB====> ")
        sql = "SELECT * FROM terminals WHERE city = %s"
        ch = (choise_user,)
        cursor.execute(sql, ch)
        result = cursor.fetchall()
        for item in result:
            print("{}\n{}\n{}\n{}\n{}" .format(item[0], item[1], item[2], item[3], item[4]))
            print ("==============================================")
        return result
    
    def get_street(self):
        cursor = self.__db.cursor()
        choise_user_street = input("Enter street  from DB====> ")
        sql = "SELECT * FROM terminals WHERE address LIKE (%s)"
        ch = ('%'+choise_user_street+'%',)
        cursor.execute(sql, ch)
        result = cursor.fetchall()
        for item in result:
            print("{}\n{}\n{}\n{}\n{}" .format(item[0], item[1], item[2], item[3], item[4]))
            print ("==============================================")
        return result

    


