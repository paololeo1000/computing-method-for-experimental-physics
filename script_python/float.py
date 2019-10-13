a = 0.75
num, den = a.as_integer_ratio()
num = float(num)
den = float(den)
print(num, den)
print('{:.30f}'.format(num / den))

print

b = 0.1
num, den = b.as_integer_ratio()
print(num, den)
num = float(num)
den = float(den)
print('{:.30f}'.format(num / den))
