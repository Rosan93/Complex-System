"""
Write a class in which its one method accepts a string from console and 
another method to print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

"""

class EvenIndex:
    def __init__(self):
        self.word=""
        self.output=""

    def indexcheck(self):
        self.word=input("Enter a string to be filtered: ")
        a = len(self.word)

        for i in range(0,a):
            if i%2==0:
                self.output+=self.word[i]

        # return self.output
    

    def print_output(self):
        print("The answer is: ",self.output)

   
    
if __name__ == "__main__":
    test = EvenIndex()  
    test.indexcheck()
    test.print_output()
    
    
    