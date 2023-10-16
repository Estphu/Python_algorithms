def list_max_sum(numbers):
    sum = []
    max_sum = [0]
    for number in numbers:
        if number != numbers[0]:
            sum.append(numbers[0] + number)
        if number != numbers[1]:
            sum.append(numbers[1] + number)
        if number != numbers[2]:
            sum.append(numbers[2] + number)
        if number != numbers[3]:
            sum.append(numbers[3] + number)                   
    for i in sum:
        for k in max_sum:
            if (i > k):
                max_sum.append(i)
    return max_sum            


            

if __name__ == '__main__':
    print(list_max_sum([3,5,9,11]))
    

