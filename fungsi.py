# Pengganti fungsi len hanya untuk array
def len_arr(arr):
    counter = 0
    temp = []
    while(temp != arr):
        counter += 1
        temp = [0 for i in range(counter)]
        for i in range(counter):
            temp [i] = arr [i]
    return counter
            

# Pengganti fungsi append array
def konso(arr,lmnt):
    count = len_arr(arr)
    temp = ['' for i in range(count+1)]
    for i in range (count):
        temp [i] = arr [i]
    
    temp[count] = lmnt
    return temp

def konso_string(string,lmnt):
    count = len(string)
    temp = ['' for i in range(count+1)]
    for i in range(count):
        temp[i] = string[i]

    temp[count]=lmnt
    a = ''
    for i in range(count+1):
        a += temp[i]
    return a

# Pengganti fungsi split untuk tipe data string
def split(kata,delimiter):
    a = kata
    b = delimiter
    count = len(a)
    tampung = []
    word = ''
    for i in range(count):
        if(a[i] == b):
            c = konso(tampung,word)
            tampung = c
            word = ''
        else:
            d = konso_string(word,a[i])
            word = d
    e = konso(tampung,word)
    return e

'''a=[]
b='joshua'
print(konso(a,b))
'''
a='josh;ua'
print(split(a,';'))