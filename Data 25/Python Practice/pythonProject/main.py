# this won't run yet because Docker isn't working
# first recording on Dec 1
import pyodbc
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
# copy and paste below
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER='+server+';DATABASE='+database+';'
                                    'UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()
cursor
# continuing another day