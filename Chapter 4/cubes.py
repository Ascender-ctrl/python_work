#exercise 4-8/ 4-9

nums = []
for num in range(1,11):
    nums.append(num**3)
    print(num**3)
    
    
cubes = [num**3 for num in range(1,11)]
print(cubes)