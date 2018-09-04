''' Q. You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.'''

class Swap:
    def swapStrings(self):
        a='This is mE 123'
        b=''

        for i in a:
            if(i.isupper()):
                b+=i.lower()
            else:
                b+=i.upper()

        print("The swapped String is:",b)

if __name__=="__main__":
    test = Swap()
    test.swapStrings()

