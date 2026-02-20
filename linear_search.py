def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   
    return -1          

my_list = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
search_element = 110

result = linear_search(my_list, search_element)

if result != -1:
    print(f"Element {search_element} is present at index {result}")
else:
    print(f"Element {search_element} is not present in array")  