 
# Database access object
# using python to control database
# 

# dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html
# This gets imported into Flask!!!

import mysql.connector
import dbconfig as cfg

class driverDAO:
# read these in from config file??

    host = "",
    user = ""
    password = "" 
    database = ""
    connection = ""
    cursor = ""


    def __init__(self):
        # read these in from a config file
        self.host= cfg.mysql['host']
        self.user= cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
    

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

    # working 
    def create(self, values):
        cursor = self.getCursor()
        sql =  "insert into f1drivers (DriverNo, LastName,FirstName,Nationality,CurrentTeam) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll
        return newid
    ## working
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from f1drivers"
        cursor.execute(sql)
        result= cursor.fetchall()
        self.closeAll()
        return result
# working
    def findBySurname(self,LastName):
        cursor = self.getCursor()
        sql = "select * from f1drivers where LastName = %s"
        values = (LastName,)

        cursor.execute(sql,values)
        result= cursor.fetchall()
        self.closeAll()
        return result

    def update(self,values):
        cursor= self.getCursor()
        sql= "update f1drivers set CurrentTeam = %s where LastName = %s"
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return

    def delete(self,id):
        cursor = self.getCursor()
        sql = "delete from f1drivers where id = %s"
        values = (id,)

        cursor.execute(sql,values)

        self.connection.commit()
        self.closeAll
        return


    def createtable(self):
            cursor = self.getcursor()
            sql="create table f1drivers (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, DriverNo int, LastName varchar(250), FirstName varchar(250), Nationality varchar (250), CurrentTeam(250))"
            cursor.execute(sql)

            self.connection.commit()
            self.closeAll()

    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()


# creates a new class each time smal m dao is class above
MyDAO= driverDAO()    

if __name__== "__main__":

    #MyDAO.createdatabase()
    #MyDAO.createtable()
    print("sanity")


