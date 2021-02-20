import pymysql.cursors


print('data base connection')

        #connect to server
conection_rent=pymysql.connect(
            host='127.0.0.1',
            port=8889,
            user='root',
            password='root',
            db='rents',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
)
    
cursor=conection_rent.cursor()


#inserir dados
sql='INSERT INTO rents (ID_Car, ID_Client, Days, Price, Status) VALUES'\
            '(%s, %s, %s, %s, %s)'
cursor.execute(sql,(1,1,2,200,'Open'))
conection_rent.commit()

cursor.close
conection_rent.close()