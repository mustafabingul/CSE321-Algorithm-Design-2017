
"""

explanation:
Problemde istenen çözüm logn+logm de olduğu için verilerimi
uygun şartlarda ortadan bölerek recursive fonksiyonu
tekrardan çağırmalıyım. Yani kısaca verilerin birbirlerinin
ortalarındaki değerlerini karşılaştırıp recursive kolları tekrar
çağırıyorum.

Eğer birinci arrayimin ortasındaki eleman ikinci arrayimin
ortasındaki elemandan büyükse ikinci arrayimin artık sağ
tarafından yarıya bölerek gönderiyorum. Çünkü birinci arrayimde
oratadaki elemanı ile ikinci arrayimdeki ortadan önceki
olan elemanlarını elemiş oluyorum.
Aynı durumu birinci array içinde yapıyorum. Bu sefer birinci
arrayimin ortadan önceki elemanlarını eliyorum.
(tabi bu durumlarda bir sonraki recursive kola
uygun k.ıncı kitap sayısını gönderiyorum..)

Problem de eğer birinci arrayimin uzunluğu sıfır olur ise
aranan kitap ikinci arrayimin k.ıncı elemanı olur,
eğer ikinci arrayimin uzunluğu sıfır olur ise kitap birinci
arrayimin k.ıncı elemanı olur.

"""

def findBookHelper(array1,array2,wantedBook):
    if(len(array1)==0):
        return array2[wantedBook]
    if(len(array2)==0):
        return array1[wantedBook]
    m1 = int(len(array1)/2)
    m2 = int(len(array2)/2)
    #print("M1",m1,"M2",m2)
    if(m1+m2<wantedBook and array1[m1]>array2[m2]):
        #print(array2[m2+1:],"11")
        return findBookHelper(array1,array2[m2+1:],wantedBook-1-m2)
    elif(array1[m1]>array2[m2]):
        # print("33")
        return findBookHelper(array1[:m1], array2, wantedBook)
    elif(m1+m2<wantedBook and array1[m1]<array2[m2]):
        # print("22")
        return findBookHelper(array1[m1+1:],array2,wantedBook-1-m1)
    else:
        #print("44")
        return findBookHelper(array1,array2[:m2],wantedBook)

def find_kth_book_1(_array1,_array2,_wantedBook):
    if(_wantedBook<=0):
        book = "there is not book."
    elif(len(_array1)+len(_array2)<_wantedBook):
        book = "there is not book.."
    else:
        book = findBookHelper(_array1,_array2,_wantedBook-1)
    return book


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming", "oop"]
boook=find_kth_book_1(m,n,4)
print(boook)

