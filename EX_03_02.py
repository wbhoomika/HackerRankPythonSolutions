hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, input numeric data")
    quit()
if h<=40:
    print(h*r)
else:
    print(40*r +(h-40)*r*1.5)
print("XYZ", r)
