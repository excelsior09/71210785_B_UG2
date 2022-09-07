import time 
start = time.time()
def deret_ajaib(n):
       data = [1,2,3,4,5]
       for i in range(6, n):
              if i > 5:
                     data.append((i-2)+(i//2))
                     #x = data[i-2]
                     #y = data[i//2]
                     #data.append(x+y)
              else:
                     data.append(i)
       return data
end = time.time()

print(deret_ajaib(10),end-start,'detik')