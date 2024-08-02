import sqlite3
 
def saveFeed(title, description, podcasturl):
 
    try:
    
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('feeds.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')
    
        # Create table if it doesn't exist yet
        cursor.execute('CREATE TABLE IF NOT EXISTS feed(feed_id INTEGER PRIMARY KEY, feed_headline TEXT NOT NULL, feed_description TEXT NOT NULL, feed_podcast_url TEXT NOT NULL);')

        # Write a query and execute it with cursor
        cursor.execute('INSERT INTO FEED (feed_headline, feed_description, feed_podcast_url) VALUES (?,?,?)', (title, description, podcasturl))
    
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