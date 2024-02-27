def selection_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]        

def bubble_sort(elements, key='name'):
    size = len(elements) - 1

    for i in range(size):
        swapped = False
        for j in range(size - i):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j][key]
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = tmp
                swapped = True
        if not swapped:
            break    


if __name__ == '__main__':

    elements = [2300, 12, 432, 45, 876.4, 55]

    # elements = [
    #     {'name': 'jawad', 'transaction_amount': 200, 'device': 'vivo'},
    #     {'name': 'bilal', 'transaction_amount': 900, 'device': 'iphone'},
    #     {'name': 'usama', 'transaction_amount': 500, 'device': 'motorolla'},
    #     {'name': 'athar', 'transaction_amount': 1000, 'device': 'lg'},
    #     {'name': 'shahzain', 'transaction_amount': 400, 'device': 'samsung'},
    # ]

    # bubble_sort(elements, 'transaction_amount')

    selection_sort(elements)

    print(elements)