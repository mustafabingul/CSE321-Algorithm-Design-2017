
"""

explanation:

referans: https://www.youtube.com/watch?v=tmu50Fs4v54
buradaki videodan yardım aldım hocam..

bir önceki sorunun aynısı sadece karmaşıklığı logk da istenmiş.
logk zaten bir nevi log(m+n) dir.(çünkü k en fazla m+n olur.
zaten bunun worst-case durumudur.)

probleme tek bir taraftan yaklaştım, aksi taktirde eğer
birinci arrayimin size ı ikinci arrayimin size ından büyükse
yerlerini değiştirdim. base case lerimden birtanesi bu.
diğer durumlar da, eğer 1. kitabı arıyorsam iki data arrayiminde
ilk elemanlarının küçük olanıdır.
eğer birinci arrayimin size ı 0 olur ise de, ikinci arrayde
aranan kitabı bulurum.
recursive kollarda da sürekli aranan kitab indisnin yarısını(logk)
arraylerde birbirleri ile karşılaştırıp tekrardan
recursive kol yapıyorum.
recursive kollarda arraylarımi elemanımın olduğu
kısımları tekrardan gönderiyorum.
((k/2) hesabı -> logk)..!


"""
def find_kth_book_2(array1,array2,wantedBook):
    s1=len(array1)
    s2=len(array2)
    if((wantedBook>s1+s2) or wantedBook<=0):
        return -1
    if(s1>s2):
        return find_kth_book_2(array2,array1,wantedBook)
    if(s1==0):
        return array2[wantedBook-1]
    if(wantedBook==1):
        return min(array2[0],array1[0])
    i=int(min(s1,wantedBook/2))
    j=int(min(s2,wantedBook/2))
    #print(i,j)
    if(array1[i-1]<array2[j-1]):
        #print("11")
        return find_kth_book_2(array1[i:],array2,wantedBook-i)
    else:
        # print("22")
        return find_kth_book_2(array1,array2[j:],wantedBook-j)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming", "oop"]
a=find_kth_book_2(m,n,4)
print(a)