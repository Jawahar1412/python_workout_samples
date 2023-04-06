x = int(input("Enter the number" + "\n"))
def calculation():
    print (int(x/10))
calculation()
x=10
calculation()
x=50
calculation()

base = int(input("Enter the base"+"\n"))
height = int(input("Enter the height"+"\n"))

def tri_area(base,height):
    area = (base*height)/2
    return (area)
print int((tri_area(base,height)))