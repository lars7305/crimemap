import dbconfig
import pymysql

conection = pymysql.connect(host='192.168.178.28',
                            user='root',
                            passwd='ShAme69'
                            )

try:
    with conection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
                id int NOT NULL AUTO_INCREMENT,
                latitude FLOAT(10,6),
                longitude FLOAT(10,6),
                date DATETIME,
                category VARCHAR(50),
                description VARCHAR(1000),
                updated_at TIMESTAMP,
                PRIMARY KEY (id)
                )"""
        cursor.execute(sql)
        conection.commit()
finally:
        conection.close()