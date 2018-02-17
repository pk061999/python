import string
text = str(input("tip your text to convert: "))
def rot13(text):
   rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                                "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
       
   return string.translate(text, rot13)
   
print(rot13(text))