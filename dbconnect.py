import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="nflapp",
                           passwd="nflroot",
                           db="nfl")
    c = conn.cursor()
    return c, conn

