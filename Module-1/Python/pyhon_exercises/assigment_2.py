##Write a function that finds the places in the Turkish alphabet of the letters in the expression whose input is a string,
adds the values of all of them, and prints True if the result is even and False if it is odd.##

def even_word(sentence):
    uppers = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    lowers = "abcçdefgğhıijklmnoöprsştuüvyz"
    toplam = 0
    for i in sentence:
        if i in uppers:
            toplam += uppers.index(i)+1
        elif i in lowers:
            toplam += lowers.index(i)+1
            
    if toplam%2 == 0 :
        return True
    else:
        return False
    
even_word("Merhaba")    
False
