import requests
from requests_ntlm import HttpNtlmAuth
import pyodbc

# Define connection parameters
server = 'servername'
database = 'database'
username = 'username'
password = 'password'

 

# Create a connection string
conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}" #name according to organization needs

 

# Establish a connection
connection = pyodbc.connect(conn_str)

 

# Create a cursor
cursor = connection.cursor()

 

# Define your SQL query
sql_query = "SELECT * FROM table"

 

# Execute the query
cursor.execute(sql_query)

 

# Fetch the results
results = cursor.fetchall()

 

# Process the results
for row in results: #row is a tuple (postion of values according to the select queries)
    #change username to your username
    filename = f'C:\\Users\\anp\\report_generated\\report.pdf'

    #change username and password to your network login
    username = "network_username"
    password = "network_password"
    #url needs to be the special url found by going to the ReportServer, the one with &rs:Command=Render
    url = f"http://reportservername/ReportServer%2fReportFolder%2fReportName&rs:Command=Render&rs:Format=PDF"
    print(url)
    r = requests.get(url, auth=HttpNtlmAuth(username, password))

    print(r.status_code)

    if r.status_code == 200:
        with open(filename, 'wb') as out:
            for bits in r.iter_content():
                out.write(bits)

 

# Close the cursor and connection
cursor.close()
connection.close()


