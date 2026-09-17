# exercise 3-10

randomthings= ['lagos', 'shoe', 'car', 'chicken', 'pepsi']

randomthings.sort()
print(randomthings)

randomthings.sort(reverse = True)
print(randomthings)

print(sorted(randomthings))
print(sorted(randomthings, reverse = True))

randomthings.reverse()
print(randomthings)

print(len(randomthings))

randomthings.remove('car')
print(randomthings)

randomthings.append('bicycle')
print(randomthings)

randomthings.pop(1)
print(randomthings)

del randomthings[0]
print(randomthings)

randomthings.insert(0, 'macbook pro')
print(randomthings)


randomthings[0] = 'macbook air'
print(randomthings)
