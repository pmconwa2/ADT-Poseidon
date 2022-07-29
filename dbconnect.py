import psycopg2


def connection():
    conn = psycopg2.connect(host="localhost",
                           database="nfl",
                           user="postgres",
                           password="oceanic46&!",
                            )
    c = conn.cursor()
    return c, conn
