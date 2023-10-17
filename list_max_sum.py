def list_max_two_num_sum(numbers):
    sum = []
    for number in numbers:
        for add_number in numbers:
            if add_number != number:
                sum.append(number + add_number)
    return max(sum)           

if __name__ == '__main__':
    print(list_max_two_num_sum([3,5,9,11]))
    

