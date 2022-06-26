import os
import psycopg2
DATABASE_URL = os.environ['DATABASE_URL'] = 'postgres://gqqqlsjqlitiqn:311b27aa9011d3706abed9e7885614699c086dac290088c99b3a77c51918dde5@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d4ik1ud82kvirb'
def dbconnection():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # conn = psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print(e)
    return conn
if __name__ == '__main__':
    dbconnection()