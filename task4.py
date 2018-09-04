''' Q.Write a Python program to replace last value of tuples in a list.¶
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] '''

# Using list comprehension
class Add:
    def addLast(self):
        a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        print("The input is: ",a)
        print("The output is: ",[t[:-1] + (100,) for t in a])

if __name__=="__main__":
    test =Add()
    test.addLast()


# Alternate
class Add2:
    def addLast2(self):
        a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        print("The input is: ",a)

        b=[]

        for i in a:
            n=i[:-1]+(100,)
            b.append(n)

        print("The output is: ",b)

if __name__=="__main__":
    test =Add2()
    test.addLast2()