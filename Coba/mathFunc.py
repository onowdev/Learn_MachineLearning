import math

x = 9
n = 8

#method 1
power = x ** n
print("%d to the power %d is %d" % (x,n,power))

# method 2
power1 = pow(x,n)
print("%d to the power %d is %d" % (x,n,power1))

# Method 3
#power 3 = math.pow(2,6.5)
#print("%d to the power %d is %5.2f" % (x,n,power3))