def step_dict(strings):
    dict = {}
    
    for line in strings:
        print(line)
        # ex. line -> 'Step C must be finished before step A can begin.'
        first_step = re.match( r'Step (.)', line, re.M)
        second_step = re.match( r'Step (.) .* step (.)', line, re.M)
        #print(matchObj.group())  ->  Step C
        ini_step = first_step.group(1)
        #print(ini_step) -> C
        fin_step = second_step.group(2)
        #print(fin_step) -> ...before step] A

        try:
            # if key already in dict, add fin_step to the value
            if len(dict[ini_step]) == 1:
                dict[ini_step] += fin_step
        except KeyError:
            # if key not already in dict, set value as fin_step
            dict[ini_step] = fin_step
    
    return dict

def find_next_step(available):
    available.sort()
    return available[0]

def find_prereq_step(step_dict):
    val_i = iter(step_dict.values())
    val_list = []
    for _ in range(len(step_dict)):
        val_list.append(next(val_i))
    
    counter = collections.Counter(val_list)
    prereq_step = counter.most_common()[0][0]  # counter sorts a letter by its frequency so the first is the most frequent

    return prereq_step

def test(step_dict):
    prereq_step = find_prereq_step(step_dict)
    prereq = []
    available = []
    result = 'C'
    key_i = iter(step_dict)

    for _ in range(len(step_dict)):
        
        key = next(key_i)
        step = step_dict[key]
        print("key: ",key)
        print("Steps(values):", step)

        if step == prereq_step:
            prereq.append(key)
            

        # add to available
        if len(step) == 1:
            available.append(step)
        else:  
            # if the key contains more than one step
            available.append(step[0])         # to do: note that it can contain more than two steps
            available.append(step[1])
        
        result_step = find_next_step(available)
        print("Available: ",available)
        print("Result step: ",result_step)
        available.remove(result_step)
        result += result_step
        print("Result:", result)
        print()

        #sys.exit()
    print(result)

        

if __name__ == "__main__":
    import re
    import sys
    import collections

    INPUT = 'input.txt'
    strings = [str(line.rstrip('\n')) for line in open(INPUT)]
    step_dict = step_dict(strings)
    find_prereq_step(step_dict)
    #test(step_dict)

    
