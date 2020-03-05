import requests
from lib.checkDb import create_db, data_terminals
from lib.dbTerminal import Db_terminal



exit = False
while not exit:
    print("========= DB Terminal =============")
    print("""
    1. Create DB Terminal
    2. Get data by City
    3. Insert Data in to DB
    4. Select by city
    5. Select by street
    0. Exit
    """)
    choice = int(input())
    if choice == 1:
        # two = Db_terminal(("localhost", "root", "", "bank"))
        create_db()
         
            
       
    elif choice == 2:
        data_terminals()
        
        
    elif choice == 3:
        two = Db_terminal("localhost", "root", "", "bank")
        two.insert_data()
        
    elif choice == 4:
        three = Db_terminal("localhost", "root", "", "bank")
        three.get_city()
       
    elif choice == 5:
        four = Db_terminal("localhost", "root", "", "bank")
        four.get_street()
    elif choice == 0:

        exit = True
    else:
        print("read manual")
