# This program demonstrates various set operations.
file1= set(open("txt1"))
file2 = set(open("txt2"))

# Display members of the baseball set.
print('The following students are on the baseball team:')
for name in file1:
    print(name)

# Display members of the basketball set.
print()
print('The following students are on the basketball team:')
for name in file2:
    print(name)

# Demonstrate intersection
print()
print('The following students play both baseball and basketball:')
for name in file1.intersection(file2):
    print(name)

# Demonstrate union
print()
print('The following students play either baseball or basketball:')
for name in file1.union(file2):
    print(name)

# Demonstrate difference of baseball and basketball
print()
print('The following students play baseball, but not basketball:')
for name in file1.difference(file2):
    print(name)

# Demonstrate difference of basketball and baseball
print()
print('The following students play basketball, but not baseball:')
for name in file2.difference(file1):
    print(name)

# Demonstrate symmetric difference
print()
print('The following students play one sport, but not both:')
for name in file1.symmetric_difference(file2):
    print(name)
