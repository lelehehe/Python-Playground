# from video https://www.youtube.com/watch?v=ZoWgzG_r2qo

# setup an array of integer [0, 1, 2, 3, 4]
xyz = [i for i in range(5)]  # list expression
print(xyz)
# generator expression, not in memory
xyz = (i for i in range(5))
for i in xyz:
    print(i)

# https://www.youtube.com/watch?v=MJUbUDa-YCA&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=5
input_list = [5, 6, 7, 8, 10, 12, 15, 20, 22, 24, 30, 2, 5, 1]


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))

[print(i) for i in xyz]

[[print(i, j) for i in range(3)] for j in range(2)]
x = [[(i, j) for i in range(3)] for j in range(2)]
print('x=')
print(x)
print('[i for i in x]=')
print([i for i in x])
