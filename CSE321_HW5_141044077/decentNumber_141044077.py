

"""

5 lerin sayısı 3 e bölünebilecek ve
3 lerin sayısıda 5 e bölünebilecek
Önce 5 lerin sayısına baktım, ondan sonra
duruma göre 3 lerin sayısını handle ettim.
verilen inputtan birer birer azaltarak
duruma göre işlemleri gerçekleştirdim.
eğer durumu sağlayacak input verilmemiş ise
o zaman -1 print ettim

analiz istenmemiş.

"""

def decentNumber(number):
    arr =[]
    i=number
    while(i>=0):
        #print(i)
        if((number-i)%5==0 and i%3==0):
            x=0
            while(x<i):
                arr.append(5)
                x+=1
            #print(i,"II",x)
            y=x
            while(y<number):
                #print(y)
                arr.append(3)
                y+=1
            break
        i-=1
    if(len(arr)==0):
        return -1

    return ''.join(map(str,arr))

aa=decentNumber(5)
print(aa)