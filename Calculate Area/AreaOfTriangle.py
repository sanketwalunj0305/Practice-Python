a = float(input("Enter the length :"))
b = float(input("Enter the breadth :"))
c = float(input("Enter the height :"))
 
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print("Area of a triangle = %.2f" %area)