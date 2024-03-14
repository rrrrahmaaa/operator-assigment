#!/usr/bin/env python
# coding: utf-8

# Nilai Statis dan Dinamis

# In[1]:


bil1 = input('isikan bilangan 1')
bil2 = input('isikan bilangan 2')
hasil = int(bil1) + int(bil2)
print("hasil penjumlahan dari",bil1,"+",bil2,"=",hasil)


# Buatlah Luas dan Persegi Panjang

# In[2]:


panjang = input("masukan nilai panjang : ")
lebar = input("masukan nilai lebar: ")

luas = int(panjang) * int(lebar)
keliling = 2 * int(panjang) + int(lebar)

print("luas", luas)
print("keliling", keliling)


# In[3]:


print("A","B","C","D", sep='@_@') #sep=seperator atau pembatas


# In[4]:


print("A","B","C","D", sep='\n', end='>_<')


# Format Index

# In[6]:


num_1 = 8
num_2 = 10

# Hasil dari 8 modulus 10 = 8
#str.format()
print('hasil dari {} modulus {} ={}'.format(num_1,num_2,num_1%num_2))


# In[8]:


fname = "rahma"
mname = "nur"
lname = "sapitri"

print('nama anda {0} {1} {2}'.format(fname,mname,lname))


# In[11]:


print('Nama anda {nama}, nilai anda {nilai}'.format(nama='rahma',nilai=100))


# In[13]:


univ = "Universitas Nusa Putra"

print("karakter pertama : ",univ[0])
print("karakter terakhir :",univ[-1])
#universitas
print(univ[0:11])
print(univ[-5:-11])
print(univ[17:])
print(univ[::-1])


# In[14]:


f_name = 'adam'
l_name = 'yandi'

print(f'Nama saya {f_name} {l_name}')

first = 100
second = 20
print(f'Hasil jumlah {first} + {second} ={first+second}')


# In[19]:


nama = "Rahma,lala,Nabela"
nama2 = "Rahma lala Nabela"
print(nama.split())
print(nama.split(','))

#join
print('@'.join(nama.split(',')))
      
#input tanggal lahir ->18/oktober/2010
#input nama -> Bill Gate
#output:
#Tgl : 18, bulan:oktober, tahun :2010
#nama inisial : bg


# In[7]:


tgl = input ('masukan tanggal : ')
nama = input ('masukan nama : ')

pemisah = tgl.split('/')
print(f'tgl: {pemisah[0]},{pemisah[1]},{pemisah[2]}')
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f'Nama inisial: {nama_pertama[0]}{nama_terakhir[0]}')


# In[ ]:




