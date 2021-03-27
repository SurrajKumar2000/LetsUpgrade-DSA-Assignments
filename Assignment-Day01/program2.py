num_list = [3,10,33,40,66,99,100,101,200]
res = list(filter(lambda x: (x % 3 == 0), num_list))
print("Numbers divisible by 3 are:",res)

