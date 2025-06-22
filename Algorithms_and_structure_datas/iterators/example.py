

def iter_function(array):
    for element in array:
        if element:
           yield element
        continue


for i in iter_function([1,2,3,None,4]):
    print(i)