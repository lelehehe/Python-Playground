# from video https://www.youtube.com/watch?v=ZoWgzG_r2qo

# setup an array of integer [0, 1, 2, 3, 4]
xyz = [i for i in range(5)]  #list expression
print(xyz)
#generator expression, not in memory 
xyz = (i for i in range(5))
for i in xyz:
    print(i)