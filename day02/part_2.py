
def pos_dict(string):
    #print(string)    -> xrecqmdonskvzupalfkwhjctdb
    #print(pos_dict)   -> {0: 'x', 1: 'r', 2: 'e', 3: 'c'

    pos_dict = {}
    index = 0
    for word in string:
        pos_dict[index] = word
        index += 1

    return pos_dict

def common(list1, list2):
    for string_1 in list1:
        for string_2 in list2:
    
            pos_dict_1 = pos_dict(string_1)
            pos_dict_2 = pos_dict(string_2)

            dif_words = 0           #number of differing words
            pos_dif_words = []      #position of differing words
            
            for index in range(26):
                if pos_dict_1[index] != pos_dict_2[index]:  #compare every word
                    dif_words += 1
                    pos_dif_words.append(index)

            if dif_words == 1:
                if len(pos_dif_words) == 1:
                    print(string_1)
                    print(string_2)
                    print("Different words: ", dif_words)
                    print("Position of different words", pos_dif_words)

                    pos_dict_1[pos_dif_words[0]] = ''
                    string_ = []
                    string = ''
                    for i in range(26):
                        string_.append(pos_dict_1[i])
                    
                    print("Final result: ", string.join(string_))
                    sys.exit()

if __name__ == "__main__":
    import sys
    INPUT = 'input.txt'
    strings_1 = [str(line.rstrip('\n')) for line in open(INPUT)]
    strings_2 = [str(line.rstrip('\n')) for line in open(INPUT)]

    common(strings_1, strings_2)
    