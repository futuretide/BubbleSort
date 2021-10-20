

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      
      if array[j] > array[j + 1]:

        # swapping elements if elements
        
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


req = [-2, 4, 0, 10, -6]

bubbleSort(req)

print('Sorted Array is following :')
print(req)
