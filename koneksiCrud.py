import pymysql
import random
def connect(sql):
    con=pymysql.connect(host='localhost',user='root',password='',db='pyperpustakaan')
    a=con.cursor()
    a.execute(sql)
    return con,a

def select():
    jmlh=[0]
    nama=[0]
    con,a=connect("Select * from buku")
    con=a.fetchall()
    for x,row in enumerate(con,start=1):
        a="                                        "
        rw=row[2]
        z=40-len(row[1])
        a=a[:z]
        a=row[1]+a
        if len(str(x))==1:
            x=" "+str(x)
        if len(str(row[2]))==1:
            rw=" "+str(row[2])
        print("[{}][{}][{} Item]".format(x,a,rw))
        jmlh.append(row[2])
        nama.append(row[1])
    return jmlh,nama

def insert(nama,jumlah):
    x=random.randint(1000,9999)
    con,a=connect("Insert into buku(noid,nama,jumlah) values('{}','{}','{}')".format(x,nama,jumlah))
    con.commit()
    con.close()
    return "Inserted"

def delete(nama):
    con,a=connect("Delete from buku where nama='{}'".format(nama))
    con.commit()
    con.close()
    return "Deleted"

def update(jmlh,nama):
    con,a=connect("Update buku set jumlah='{}' where nama='{}'".format(jmlh,nama))
    con.commit()
    con.close()
    return "Updated"

def insrtOrder(nameBook,nameOrder,crDate,duration,lsDate):
    con,a=connect("Insert into list(namebook,nameorder,crdate,duration,lsdate) values('{}','{}','{}','{}','{}')".format(nameBook,nameOrder,crDate,duration,lsDate))
    con.commit()
    con.close()
    return "Inserted"

def slctOrder():
    con,a=connect("Select * from list")
    con=a.fetchall()
    for x,row in enumerate(con,start=1):
        print("[{}] \n|Name Of Book : {}\n|Ordered Name : {}\n|{}\n|Duration     : {} Days\n|{}\n".format(x,row[0],row[1],row[2],row[3],row[4]))
    return "Selected"
