# import dependencies
import matplotlib.pyplot as plt
import mysql.connector

# connect to mysql server and select relevant database
mydb=mysql.connector.connect(host="localhost",user="root",password="*****",database="screaming_swifts")

# store a cursor of the current database
mycursor=mydb.cursor()

# SQL query as arguement to store the result using mycursor
mycursor.execute("select year, individual_count from ssp_data")
result = mycursor.fetchall()

#store values for year of sighting & individual count of birds within the screaming party as seperate lists for plotting downstream
year = []
individual_count = []

for i in mycursor:
    year.append(i[0])
    individual_count.append(i[1])

print ("Year", year)
print ("Individual Count", individual_count)


# bar chart with given values from above, y axis limits of between 2 and 50 indiviuals, x axis limits of between 1913 and 2021
plt.bar(year, individual_count)
plt.ylim(2, 50)
plt.xlim(1913, 2021)
plt.xlabel("Year")
plt.ylabel("Individual Count")
plt.title("Screaming Party Individual Count per Year")
plt.show()

# close connection with database
mydb.close()
