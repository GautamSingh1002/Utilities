import sys
import cx_Oracle

args = sys.argv
username = args[1]
pwd = args[2]
hostname = args[3]

connection_details = username + '/' + pwd + '@' + hostname
connection = cx_Oracle.connect(conn_str)
cursor = conn.cursor()

query=u'select * from table'

cursor.execute(query)

for row in cursor:
	print(row)
	
	
