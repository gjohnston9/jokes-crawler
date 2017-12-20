import praw
import psycopg2

import json


credentials = json.load(open('credentials.json'))
    
db_creds = credentials['db']
reddit_creds = credentials['reddit']

db_user = db_creds.get('user', 'postgres')
db_password = db_creds['password']

reddit_username = reddit_creds['reddit_username']
client_id = reddit_creds['client_id']
client_secret = reddit_creds['client_secret']

try:
    connect_str = "dbname='hgp' host='localhost' user='{}' password='{}'".format(db_user, db_password)
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    crawler = praw.Reddit(user_agent='Python r/Jokes crawler (u/{})'.format(reddit_username),
                  client_id=client_id,
                  client_secret=client_secret)

    subreddit = crawler.subreddit('jokes')
    posts = subreddit.stream.submissions()

    for i, post in enumerate(posts):
        cursor.execute(
            'INSERT INTO reddit_jokes VALUES (%s, %s, %s, %s, %s, NOW()) ON CONFLICT DO NOTHING',
            (post.id, post.title, post.selftext, post.ups, post.downs))
        if i % 20 == 0:
            print('saving 20 jokes')
            conn.commit()

except psycopg2.Error as e:
    print('database connection error')
    print(e)
except praw.exceptions.PRAWException as e:
    print('PRAW exception')
    print(e)
