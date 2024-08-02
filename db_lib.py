import sqlite3
 
try:
   
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('/Users/jasonwhite/Documents/development/python/client/feeds.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
 
    # Write a query and execute it with cursor
    #query = 'select sqlite_version();'
    # cursor.execute('select count(*) from feed;')
    # cursor.execute(query)
    cursor.execute('CREATE TABLE IF NOT EXISTS feed(feed_id INTEGER PRIMARY KEY, feed_headline TEXT NOT NULL, feed_description TEXT NOT NULL, feed_podcast_url TEXT NOT NULL);')

    sqliteConnection.commit()

    a='a'
    b='b'
    c='c'
    cursor.execute('INSERT INTO FEED (feed_headline, feed_description, feed_podcast_url) VALUES (?,?,?)', (a,b,c))

    sqliteConnection.commit()
 
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
