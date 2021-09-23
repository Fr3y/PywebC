cubes = [i**3 for i in range(5)]
print(cubes)

#############################################

nums  = [i*2 for i in range(10)]

print(nums)

#############################################

#if statement 

evens  =[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#############################################

#memory Error


even = [2*i for i in range(10**100)]
print(even)

#############################################
