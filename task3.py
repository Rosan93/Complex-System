'''The user enters a string and a substring. You have to print the number of times 
that the substring occurs in the given string. String traversal will take place from left to right, 
not from right to left.'''

# class CountSubtring:
#     def countSub(self):
#         userin=input("Enter a string: ")
#         check=input("Enter substring of last string to be counted: ")

#         result = userin.count(check)

#         print(result)

# if __name__=="__main__":
#     test = CountSubtring()
#     test.countSub()

class  CountSubstring:

    def countSub(self):
        count=0
        userin=input("Enter a string: ")
        check=input("Enter substring of last string to be counted: ")
        a=len(userin)
        b=len(check)
         

        for i in range(0,a):
            if userin[i]==check[0]:
                if userin[i:i+b]==check:
                    count+=1

        print(count)

        

if __name__=="__main__":
    test = CountSubstring()
    test.countSub()