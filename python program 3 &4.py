#finding area of rectangle ,triangle,circle,square
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breath of the rectangle:"))
rec=l*b
print("Area of the rectangle is ",rec)

x=int(input("Enter the side of the square:"))
s=x*x
print("Area of the square is ",s)

r=int(input("Enter the radius of the circle:"))
d=3.14*r*r
print("Area of the circle is ",d)

b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
t=1/2*b*h
print("Area of the triangle is ",t)

#Fibonacci series
x=int(input("Enter the number:"))
n1=0
n2=1
count=0
while count<x:
    n1,n2=n2,n1+n2
    count+=1
    print(n1,end=" ")
