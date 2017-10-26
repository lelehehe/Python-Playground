"""tuple practice
"""

def printOut(items):
    print()
    print('=================')
    for item in items:
        print(item, end=",")

t = ("abc", 4.2, 3)
print(t)

#partition()
#1. tuple unpacking
#2. use underscore as a dummy name for the separator
origin, _, destination = "Seattle-Boston".partition('-')

#range
printOut(range(5, 10))

#enumerate() yields (index, value) tuples
t = [6, 23, 15, 18]
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))

#list
s = "a quick brown fox jumps over the lazy dog".split()
printOut(s)
printOut(s[1:4]) #quick brown fox

printOut(s[1:-1])

printOut(s[:3])

#multiple ways to re-build another copy
full_slice = s[:]
full_slice == s  #True
u = s.copy()
v = list(s) # full_slice, u, v 

#copy function is shallow
a = [[1, 2], [3, 4]]
b = a[:]
a == b #True
a[0] == b[0]  #True
a[0] = [8, 9] #b[0] is still holding the old value [1,2], not [8, 9]
a[1].append(5) 
a[1] #[3, 4, 5]
b[1] #b[1] is also changed, because they are both the same object due to shallow copy :)

#initialize with size
d = [1,2] * 3  #[1,2,1,2,1,2]

#repition is shallow
s = [[1,2]] * 2 #[1, 2],[1, 2]
printOut(s) 
s[0][0] = 5  #[5, 2],[5, 2],
printOut(s)

#delete from list: del
s = "a quick brown fox jumps over the lazy dog".split()
del s[0]
s.remove('quick')
printOut(s)  # 'brown fox jumps over the lazy dog'