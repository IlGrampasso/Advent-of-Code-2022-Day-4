with open('input.txt') as f:
    data = f.readlines()
count = 0
for i in data:
    #split the the line into two parts using "," as separator
    vect = i.split(",")
    x = vect[0]
    y = vect[1]
    #split substring int two parts using "-" as separator
    a, b = x.split('-')
    c, d = y.split('-')
    #string conversion into integer
    a, b = int(a), int(b)
    c, d = int(c), int(d)
    #range creation with upper and lower bound
    r1 = range(a, b + 1)
    r2 = range(c, d + 1)
    #conversion from range to list
    r1 = list(r1)
    r2 = list(r2)
    z=list(set(r1)&set(r2))
    print(z)
    #check if one range fully contains the other
    if (len(z)==len(r1) or len(z)==len(r2)):
        count += 1
print(count)