# Day 1
def load_data(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))
    
    return left_list, right_list

def calculate_difference(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    diff_list = [abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))]
    return sum(diff_list)

def main():
    left_list, right_list = load_data('./Day 1/input.txt')
    result = calculate_difference(left_list, right_list)
    print(result)

if __name__ == "__main__":
    main()