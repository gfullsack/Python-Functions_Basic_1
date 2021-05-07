#1
def a():
    return 5
print(a())

#Because a is to return the number 5, it will print 5

#2
def a():
    return 5
print(a()+a())

#Because a is to return the number 5, it will print 5 + 5 for a sum total of 10 

#3
def a():
    return 5
    return 10
print(a())

#I would suspect it would return 5, this is because it will stop, there is no incentive to return 10 
#example 

Def a(x):
  If x==0:
    Return 5
  Return 10

#4
def a():
    return 5
    print(10)
print(a())

#I would suspect it would return 5, this is because it will stop, there is no incentive to print 10 

#5
def a():
    print(5)
x = a()
print(x)

#the output is 5 and none 

#it will first def a(): which will be print 5
#so line 4 is saying - we need to define a() which will be 5

#line 5 is saying we need to print x, but cause we never got a defined value, because line 4 is an equation. we got None


#6 def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))


#it will first print (1+2) = 3, then it will print 2+3 = 5. 
#However the line 3, If a function doesn�t have a return explicitly written then we will have none. printing none + none created a type error. 



#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))


#BECAUSE OF RETURN

#b = 2
#c = 5

#because we are defining C by as many B's , we are getting 5*5 = 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
	return 10
    return 7
print(a())



# Define A, A is B = 100

# and because 100 is greater then 10, we will return 10 

# 100
# 10

# return 7 is an orphaned code. 


#9
1	def a(b,c):
2	    if b<c:
3	        return 7
4	    else:
5	        return 14
6	    return 3
7	print(a(2,3))- #This generated 7
8	print(a(5,3)) - #This will generate 14
9	print(a(2,3) + a(5,3)) # 7+14 = 21 





#10
def a(b,c):
    return b+c #<- This will run first for 8 
    return 10
print(a(3,5))


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# 500
# 500
# 300
# 500


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)


# 500
# 500
# 300
# 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()


# 1
# 3
# 2

# It will first print 1, but would need to define b() which is 3, before fulfilling the last request in the function to print 2. 


def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# 1
# 3
# 5
# 10

# It will first print 1, then it would need to define b, which would be 3, then they will return 5 that will print X, and then return the 10 value