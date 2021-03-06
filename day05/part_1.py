
def react_reduction(string):

    pos_dict = {}
    _index = 0
    for word in string:
        pos_dict[_index] = word
        _index += 1

    for index in range(len(string)-1):
        if (string[index] == string[index].lower())\
            and (string[index+1] == string[index+1].capitalize())\
            and (string[index] == string[index+1].lower()):
            pos_dict[index] = ''
            pos_dict[index+1] = ''
            break

        if (string[index] == string[index].capitalize())\
            and (string[index+1] == string[index+1].lower())\
            and (string[index] == string[index+1].capitalize()):
            pos_dict[index] = ''
            pos_dict[index+1] = ''
            break
    
    _string = []
    r_string = ''
    for i in range(len(string)):
        _string.append(pos_dict[i])
    
    result = r_string.join(_string)
    same_result = False
    if result == string:
        same_result = True

    return result, same_result

if __name__ == "__main__":

    string = open('input.txt').read()
    same_result = False

    while same_result == False:
        print("Remaining units: ",len(string))
        string, same_result = react_reduction(string)
    