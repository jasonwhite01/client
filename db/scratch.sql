-- connect to feeds database
sqlite3 feeds.db

-- list all tables in a database
.tables

-- create feed table
CREATE TABLE feed(
feed_id INTEGER PRIMARY KEY,
feed_headline TEXT NOT NULL,
feed_description TEXT NOT NULL,
feed_podcast_url TEXT NOT NULL);

-- insert into feed table
insert into feed (feed_headline, feed_description, feed_podcast_url) 
values (,,);