#!/usr/local/bin/python3
import requests,os
from bs4 import BeautifulSoup
from getpass import getpass
from tabulate import tabulate

s = requests.Session()
url = "http://simak.stmikelrahma.ac.id"
soup = BeautifulSoup()

def loginMhs(x,y):
    data = {'username':x,
            'password':y,
            'cmdLogin':'Login'}
    r = s.post(url+"/index.php/mhs/loginmhs/cek_loginmhs", data=data)

def parsing(x):
    soup = BeautifulSoup(x,'lxml')
    return soup

def thn():
    r = s.get(url+"/index.php/mhs/simambilmk/khs")
    txt = parsing(r.text)
    txt = txt.findAll('option')
    print("Tahun KHS")
    print("---------")
    for i in txt:
        print(i.attrs['value'])
    print("---------")
    tahun = input("Masukkan Tahun KHS : ")
    return tahun

def getKuis(x):
    r = s.get(url+"/index.php/mhs/simambilmk/change_thajarankhs/" + x)
    txt = parsing(r.text)
    txt1 = txt.find_all('td',{'class':'first'})
    txt2 = txt.find_all('a')

    data = []
    for i in txt1:
        data.append(i.text)

    jum = int(len(data) / 5)
    for i in range(1,jum+1):
        globals()['data{}'.format(i)] = []
        for x in range(5):
            globals()['data{}'.format(i)].append(data.pop(0))
    
    if 'data9' in globals():
        print(tabulate([data1,data2,data3,data4,data5,data6,data7,data8,data9], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data8' in globals():
        print(tabulate([data1,data2,data3,data4,data5,data6,data7,data8], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data7' in globals():
        print(tabulate([data1,data2,data3,data4,data5,data6,data7], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data6' in globals():
        print(tabulate([data1,data2,data3,data4,data5,data6], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data5' in globals():
        print(tabulate([data1,data2,data3,data4,data5], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data4' in globals():
        print(tabulate([data1,data2,data3,data4], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data3' in globals():
        print(tabulate([data1,data2,data3], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data2' in globals():
        print(tabulate([data1,data2], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    elif 'data1' in globals():
        print(tabulate([data1], headers=['No','Kode','Nama Matakuliah','SKS','Nilai']))
    else:
        print("Anda Tidak Memiliki matakuliah Aktif")

    ids = []
    for i in txt2:
        ids.append(i.attrs['onclick'][26:-20])
    return ids


# def detailMakul(x):
#     r = s.get(url+"/index.php/mhs/quisioner/input/"+x)


def hajar(x,y,f,a,b):
    data = {'id_kelas_dosen':x,
            'nim':y,
            'thajaran':f,
            '18':a,
            '19':a,
            '20':a,
            '21':a,
            '22':a,
            '23':a,
            '24':a,
            '25':a,
            '26':a,
            '27':a,
            '28':a,
            '1':a,
            '2':a,
            '3':a,
            '4':a,
            '5':a,
            '6':a,
            '7':a,
            '8':a,
            '9':a,
            '10':a,
            '11':a,
            '12':a,
            '13':a,
            '14':a,
            '15':a,
            '16':a,
            '17':a,
            'komentar':b
            }
    r = s.post(url+"/index.php/mhs/quisioner/simpan",data = data)
    if "berhasil" in r.text:
        print("")
        print("Quisioner berhasil disimpan!")

    else:
        print("Quisioner gagal disimpan")

def clear():
    os.system('clear')

def main():
    username = input("Username : ")
    password = getpass("Password : ")
    clear()
    loginMhs(username,password)
    tahun = thn()
    clear()
    ids = getKuis(tahun)
    print("========================================================================")
    nilai = input("Input Nilai [1-5] : ")
    komentar = input("Beri Komentar : ")
    for i in ids:
        hajar(i,username,tahun,nilai,komentar)
    # hajar(3215,username,tahun,nilai,komentar)
    print("")
    print("~ Jadikan kemalasanmu bermanfaat,be lazy c0der! | @zetc0de")

if __name__ == '__main__':
    main()