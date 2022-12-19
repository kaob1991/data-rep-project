# install wamp on laptop 
# use mysql console 

# using python to control database
# This wil lnot work on chromebook so will need to check it on windows


# This gets imported into Flask!!!

import mysql.connector

class myDAO:
#mydb = mysql.connector.connect(
    host = "localhost",
    user = "???"
    password = "???" 
    database = "????"


    connection = ""
    cursor = ""


    def __init__(self):
        # read these in from a config file
        self.host= "localhost"
        self.user= "root"
        self.password = ""
        self.database = "database"
    

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user= self.user,
            password=self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor


    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    
    def create(self, values):
        cursor = self.getCursor()
        sql = "some sql query- insert into db (col1, col2) values (%s,%s)"
        cursor.execute(sql,values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll
        return newid

    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from db"
        cursor.execute(sql)
        result= cursor.fetchAll()
        self.closeAll()
        return result

    def findByID(self,id):
        cursor = self.getCursor()
        sql = "select * from db where x = %s"
        values = (id,)

        cursor.execute(sql,values)
        result= cursor.fetchone()
        self.closeAll()
        return result

    def update(self,values):
        cursor= self.getCursor()
        sql= "update dbname set col1 = %s, col2= % where id = %s"
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()

    def delete(self,id):
        cursor = self.getCursor()
        sql = "delete from db where id = %s"
        values = (id,)

        cursor.execute(sql,values)

        self.connection.commit()
        self.closeAll


# creates a new class each time smal m dao is class above
MyDAO= myDAO()        





'''


 # Could also do this as from a config file - prob best to read in from there 



##################
# creating a db - mydb above has no database variable with this one 

cursor = mydb.cursor()
cursor.execute("create DATABASE databasename")
mydb.close()
cursor.close()

####################
# creating a table

cursor = mydb.cursor()
sql= "CREATE TABLE tablename( column names and values)"
cursor.execute(sql)
mydb.close()
cursor.close()

###########################################
# inserting into db 
mycursor = mydb.cursor()
sql = "some sql query- insert into db (col1, col2) values (%s,%s)"
values = ("value1", "value2") # this prevents sql injection
mycursor.execute(sql, values)

mydb.commit()
mydb.close()
mycursor.close()
# Don't forget to close these or the server may block you out for continuous calls



####################
# Reading from db 

cursor = mydb.cursor()
sql = "select * from db where x = %s"
values = (1,) # this needs to have the comma

cursor.execute(sql, values)
result = cursor.fetchall() # Can use fetchOne() also
for x in result:
    print(x)
mydb.close
cursor.close()

#######################
# Updating from db 
cursor = mydb.cursor()
sql = "update dbname set col1 = %s, col2= % where id = %s"
values = ("value1", "value2", 1)

cursor.execute(sql, values)
mydb.commit()
mydb.close()
cursor.close()

####################
# delete

cursor = mydb.cursor()
sql = "delete from db where id = %s"
values = (1,) # this needs to have the comma

cursor.execute(sql, values)

mydb.commit()
mydb.close()
cursor.close()


'''