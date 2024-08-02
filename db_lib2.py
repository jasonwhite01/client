import sqlite3
 
try:
   
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('/Users/jasonwhite/Documents/development/python/client/feeds.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
 
    cursor.execute('select * from feed;')

    records = cursor.fetchall()    

    print(records)
 
    # Close the cursor
    cursor.close()
 
# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)

# Close DB Connection irrespective of success
# or failure
finally:
   
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
