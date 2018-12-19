def result(numbers_list):
    result = 0 #the first number cannot be zero 
    result_list = []
    twice_found = False
    
    for number in numbers_list:
        result += number
        if str(result) in result_list :
            print("Twice: ", result)
            twice_found = True
            sys.exit()
        result_list.append(str(result))
    
    return result, result_list, twice_found

if __name__ == "__main__":
    import re
    import sys

    INPUT = 'input.txt'
    num = [int(line.rstrip('\n')) for line in open(INPUT)]
    result_n, result_list, twice_found = result(num)
    while twice_found == False:
        #num_repeat += num
        #numbers_rep = numbers_list(num_repeat)
        _result, _result_list, twice_found = result(num)


    