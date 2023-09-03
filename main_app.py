# Binary search function: takes a list, and target element
def binary_search (list, element):
    middle = 0 # sets up middle variable
    start = 0 # sets up start variable
    end = len(list) # sets up end variable with the length of the list
    steps = 0 # sets up steps counter

    # while loop will reoccur until the target is found
    while (start <= end):
        print("Step ", steps, " : ", str(list[start:end + 1]))

        steps = steps + 1 # adds 1 to the step variable
        middle = (start + end) // 2 # creates a new middle length

        # if statement checks the element, if element is within the list, correctly changes the list to find element
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return - 1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2

binary_search(my_list, target)