import re
import os
import xml.etree.ElementTree as ET
import mysql.connector
import pandas as pd

class Consultas:
    def __init__ (self,bbdd,tabla,query):
        self.bbdd=bbdd
        self.tabla=tabla
        self.query=query
    
    def consulta_bbdd(self):
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                    host='127.0.0.1',
                                    database="INFORMATION_SCHEMA")
        mycursor = cnx.cursor()
        
        mycursor.execute("SHOW DATABASES")
        for i in mycursor:
            print(i)
        return mycursor.close()
    
    def consulta_tablas(self):
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                host='127.0.0.1',
                                database=self.bbdd)
        mycursor = cnx.cursor()
        mycursor.execute("SHOW TABLES")
        for i in mycursor:
            print(i)
        return mycursor.close()
    
    def consulta_columnas(self):
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                host='127.0.0.1',
                                database="INFORMATION_SCHEMA")
        mycursor = cnx.cursor()
        
        mycursor.execute(F"SELECT * FROM COLUMNS WHERE TABLE_NAME='{self.tabla}'")
        for i in mycursor:
            print(i)
        return mycursor.close()
    
    def consultas_datos(self):
        from mysql.connector import errorcode
        cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                                    host='127.0.0.1',
                                    database=self.bbdd)
        mycursor = cnx.cursor()
        try:
            consulta= pd.read_sql_query(self.query,cnx)
            print(consulta)
            #Se le pregunta al usuario si quiere guardar su consulta
            respuesta=input("¿Deseas guardar tu consulta en un archivo csv? S/N")
            if "S" == respuesta.upper():
                archivo=input("Escribe el nombre con el que quieres guardar tu consulta")
                consulta.to_csv(f"{archivo}.csv")
                print(f"Tu consulta se ha guardado en el archivo '{archivo}.csv' con éxito")
            else:
                print("Consulta no guardada")    
        except mysql.connector.DatabaseError as err:
            print("No se puede realizar tu consulta verifica tu query")
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        except :
            print("No se puede realizar tu consulta verifica tu query. Pista... ¿escribiste bien el nombre de la tabla o la BBDD?")
        return mycursor.close()