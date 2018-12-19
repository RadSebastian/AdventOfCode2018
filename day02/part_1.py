
def result(string):
    count_twos = 0
    count_threes = 0
    dict = {}

    for word in string:
        dict[word] = 0

    for key in dict:
        for _word in string:
            if key == _word:
                dict[key] += 1

    for _key in dict:
        if dict[_key] == 2:
            count_twos = 1
        elif dict[_key] == 3:
            count_threes = 1

    return count_twos, count_threes, dict

if __name__ == "__main__":
    INPUT = 'input.txt'
    strings = [str(line.rstrip('\n')) for line in open(INPUT)]
    count_twos_ = 0
    count_threes_ = 0

    for string in strings:
        count_twos, count_threes, dict = result(string)
        count_twos_ += count_twos
        count_threes_ += count_threes
    
    print(count_twos_, count_threes_)
    print("Checksum:", count_twos_ * count_threes_)
