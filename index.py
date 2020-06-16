from dateGenerator import *
from koneksiCrud import *
from getpass import getpass
import datetime
import os
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
    print("Bejjo Application")
    print("━━━━━━━━━━━━━━━━━")
def main():
    cls()
    print("Hello World :)\n")
    asd=input("Enter...")
    while True:
        cls()
        print("1. Library\n2. Login")
        print("Note : Type 0 for back")
        n=int(input("\nChoose Program : "))
        cls()
        if n==1:
            while True:
                print("1. View books\n2. Borrow a book")
                print("Note : Type 0 for back")
                n=int(input("\nChoose Program : "))
                cls()
                if n==1:
                    print("Library List")
                    print("------------")
                    select()
                    asd=input("\nEnter...")
                    cls()
                elif n==2:
                    print("Borrow it!!!")
                    print("------------")
                    jmlh,nama=select()
                    tday=datetime.date.today()
                    brw=int(input("\nNumber of book : "))
                    if brw==0:
                        break
                    crDate="Current date : "+tday.strftime("%d/%m/%Y")
                    print(crDate)
                    duration=int(input("Duration(Day) : "))
                    if duration==0:
                        break
                    dy,mt,yr = hitungtanggal(tday.day,tday.month,tday.year,duration)
                    lsDate="Return limit : {}/{}/{}".format(dy,mt,yr)
                    print(lsDate)
                    name=input("Name : ")
                    if name=="0":
                        break
                    hasil1=insrtOrder(nama[brw],name,crDate,duration,lsDate)
                    jmlNext=int(jmlh[brw])-1
                    hasil=update(jmlNext,nama[brw])
                    print(hasil1)
                    print(hasil)
                    break
                elif n==0:
                    break
                else:
                    print("Input is not recognized")
        elif n==2:
            while True:
                print("Form Admin")
                print("----------")
                user=input("Username : ")
                if user=="0":
                    break
                pswd=getpass('Password :')
                if pswd=="0":
                    break
                if user=="Bejjoeqq" and pswd=="Aldhiyarozak":
                    cls()
                    print("1. Insert\n2. Delete\n3. Ordered")
                    print("Note : Type 0 for back")
                    n=int(input("\nChoose Program : "))
                    cls()
                    if n==1:
                        print("Insert new book to library")
                        print("--------------------------")
                        nama=input("Title : ")
                        if nama=="0":
                            break
                        jumlah=input("Amount : ")
                        if jumlah=="0":
                            break
                        hasil = insert(nama,jumlah)
                        print(hasil)
                        break
                    elif n==2:
                        print("Delete a book from library")
                        print("--------------------------")
                        jmlh,nama=select()
                        dlt=int(input("\nNumber of book : "))
                        if dlt==0:
                            break
                        hasil = delete(nama[dlt])
                        print(hasil)
                        break
                    elif n==3:
                        print("Ordered List")
                        print("------------")
                        slctOrder()
                        asd=input("Enter...")
                        break
                    elif n==0:
                        break
                    else:
                        print("Input is not recognized")
                else:
                    print("\nUsername or password incorrect")
                    asd=input("Enter...")
                    cls()
        elif n==0:
            break

        else:
            print("Input is not recognized")

    # tanggal=list(map(int, input("dd/mm/yyyy : ").split("/")))
    # lama=int(input("Lama hari = "))
    # h,b,t=hitungtanggal(tanggal[0],tanggal[1],tanggal[2],lama)
    # print(h,b,t)
if __name__ == '__main__':
    main()
