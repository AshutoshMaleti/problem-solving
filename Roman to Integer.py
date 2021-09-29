s = "MCDLXXVI"

value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
length = len(s)

p1 = length-1
p2 = length-2

total = 0

if length%2 == 1:
    while p1>=1:
        if p2>=0:
            if value[s[p1]] > value[s[p2]]:
                total += value[s[p1]]-value[s[p2]]
            else:
                total += value[s[p1]]+value[s[p2]]
            p1 -= 1
            p2 -= 1
        elif p2<0:
            total += value[s[p1]]
else:
    while p1>-1:
        if p2>=0:
            if value[s[p1]] > value[s[p2]]:
                total += value[s[p1]]-value[s[p2]]
            else:
                total += value[s[p1]]+value[s[p2]]
            p1 -= 1
            p2 -= 1
        elif p1<0:
            break   
print(total)