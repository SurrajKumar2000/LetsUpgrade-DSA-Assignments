pos=-1
def search(list,n):
    i=0
  
    while i<len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i=i+1
    return False
            
list=[1,2,3,4,5]
n=1

if search (list,n):
    print("Found at:",pos)
else:
    print("Not found")
            
