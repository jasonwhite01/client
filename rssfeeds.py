import sqlite3
 
def saveFeed(title, description, podcasturl):

    try:
    
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('feeds.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')
    
        # Create table if it doesn't exist yet
        cursor.execute('CREATE TABLE IF NOT EXISTS feed(feed_id INTEGER PRIMARY KEY, feed_headline TEXT NOT NULL, feed_description TEXT NOT NULL, feed_podcast_url TEXT NOT NULL);')

        sqliteConnection.commit()

        # Write a query and execute it with cursor
        print('title to persist: ' + title)
        cursor.execute('INSERT INTO FEED (feed_headline, feed_description, feed_podcast_url) VALUES (?,?,?)', (title, description, podcasturl))

        sqliteConnection.commit()

        cursor.execute('select * from feed;')

        records = cursor.fetchall()    

        for row in records:
            print("title: ", row[1])
    
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

def getSavedFeeds():

    try:
    
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('/Users/jasonwhite/Documents/development/python/client/feeds.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')
    
        cursor.execute('select * from feeds;')

        records = cursor.fetchall()    
        # Close the cursor
        cursor.close()

        print(records)

        return records
    
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)
    
    # Close DB Connection irrespective of success
    # or failure
    finally:
    
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')
