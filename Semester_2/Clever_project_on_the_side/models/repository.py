
import sqlite3
import ladestander

class Repository:
    def __init__(self):
        self.ladestanderList = []



    
    def load_database(self):
        with sqlite3.connect("Semester_2/Clever_project_on_the_side/static/CleverLokationtest.db") as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM cleverLokationertest;"
            Lokationer = cursor.execute(query)

    
        for d in Lokationer:
            nyladestander = ladestander(d[0], d[1])
            self.ladestanderList.append(nyladestander)
        
        


        pass





myrep = Repository()
myrep.load_database()



print(myrep.ladestanderList)