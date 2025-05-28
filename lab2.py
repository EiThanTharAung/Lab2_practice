import statistics
def display_main_menu():
    print("display_main_menu")

def get_user_input():
    temp_val = []
    temp = str(input("Enter temperature values (use commas to seperate): "))
    split = temp.split(",")

    for i in split:
        temp_val.append(float(i))
    
    print("Temperature values: " + str(temp_val))
    return temp_val

def calc_average_temperature(temp_val):
    """total = 0
    for i in temp_val:
        total = total + i
    avg = total/len(temp_val)
    return avg"""
    return round(sum(temp_val)/len(temp_val), 2)

def calc_min_max_temperature(temp_val):
    min_val = min(temp_val)
    max_val = max(temp_val)
    return [min_val, max_val]

def sort_temperature(temp_val):
    temp_val.sort()
    return temp_val

def calc_median_temperature(temp_val):
    n = len(temp_val)
    mid = n//2
    if n % 2 == 1:      # Odd 
        return temp_val[mid]
    else:               # Even 
        return round((temp_val[mid-1]+temp_val[mid])/2, 2)


def main():
    display_main_menu()
    temp_list = get_user_input()

    average = calc_average_temperature(temp_list)
    print("Average: " + str(average))

    min_max_list = calc_min_max_temperature(temp_list)
    print("Minimum value: " + str(min_max_list[0]))
    print("Maximum value: " + str(min_max_list[1]))

    temp_sorted = sort_temperature(temp_list)
    print("Sorted temperature values: " + str(temp_sorted))

    median = calc_median_temperature(temp_sorted)
    print("Median: " + str(median))

if __name__ == "__main__":
    main()