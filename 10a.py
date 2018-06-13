#Mystring is a user-defined Package. find the files countvowel and palin to understand what the package modules do

################################################################################################################################
import Mystring
print(dir())
word=(raw_input("Enter a string : "))
Mystring.countvowel.count(word)
Mystring.palindrome.palin(word)
