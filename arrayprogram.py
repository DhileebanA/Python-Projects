
def first_letter(s):
    return s[0]



def last_letter(s):
    return s[-1]



arr = ["road", "elephant", "onion", "tiger", "nine"]
print(arr)

arr2 = []
identified = False

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and first_letter(arr[i]) != last_letter(arr[j]):
            identified = True

    if identified and len(arr2) <= len(arr):
        arr2.append(arr[i])

    identified = False
    print(arr2)


