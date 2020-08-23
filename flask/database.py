import psycopg2

if __name__ == '__main__':
    connection = psycopg2.connect(user="postgres", password="postgres")
