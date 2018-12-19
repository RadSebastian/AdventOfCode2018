if __name__ == "__main__":

    INPUT = 'input.txt'
    num = [int(line.rstrip('\n')) for line in open(INPUT)]

    print(sum(num))