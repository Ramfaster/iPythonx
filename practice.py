stack2 = Stack()
del stack2

def flatten_list(alist, flatten_result=None):
    
    if flatten_result is None:
        flatten_result = []
    
    for a in alist:
        if isinstance (a, list):
            flatten_list(a, flatten_result)
        else:
            flatten_result.append(a)

    return flatten_result

print(flatten_list ([[1,2,[3,4]],[5,6],7]))