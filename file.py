n1 = 1
n2 = 5
n3 = 0

# def largest(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         if n2>n1 and n2>n3:
#             return n2
#         return n1
#     else:
#         return n3
    
# print(largest(n1,n2,n3))


# def largest1(n1,n2,n3):
#     largest = 0
#     if largest<n1:
#         largest = n1
#     if largest<n2:
#         largest = n2
#     if largest<n3:
#         largest = n3 
#     return largest

# print(largest1(n1,n2,n3))


def largest2(n1,n2,n3):
    if n1>n2 and n1>n3:
        if n2>n1 and n2>n3:
            return n2
        else:
            return n3
    return n1
    
print(largest2(n1,n2,n3)) 