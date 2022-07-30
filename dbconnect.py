import psycopg2


def connection():
    conn = psycopg2.connect(host="ec2-44-208-88-195.compute-1.amazonaws.com",
                           database="d20atckuunjd6a",
                           user="btifnirlvheggd",
                           password="456dae0c256c66d5f8b454351412c5dedd3cfa6f9e696a8c229954549fe2c166",
                            )
    c = conn.cursor()
    return c, conn
