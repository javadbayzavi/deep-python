import time


def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                
        #Swap both variables
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

   
lst = [22,54,8,12,9,56,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,1,45,267,3,23,1,45,267,3,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,6,2,5,22,54,8,12,9,56,23,6,2,5,7,39,7,4,7,39,7,4,22,54,8,22,54,8,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4,12,9,56,23,1,45,267,3,6,2,5,7,39,7,4]
start = time.time()
selection_sort(lst)
end = time.time()
print(lst)
print(end - start)