
from convert import str_to_float

def gather_numbers() -> list[float]:
    nums = []
    should_continue = True
    quit_string = "done"
    while should_continue:
        input_str = input("Enter a number (type 'done' to finish): ")
        if input_str.lower() == quit_string:
            should_continue = False
        else:
            float_input = str_to_float(input_str)
            if not float_input is None:
                nums.append(float_input)

    return nums

if __name__ == "__main__":
    nums = gather_numbers()
    print(sum(nums))

'''
Testing 
Console Output:

Enter a number (type 'done' to finish): 5
Enter a number (type 'done' to finish): e
Enter a number (type 'done' to finish): 2
Enter a number (type 'done' to finish): -9
Enter a number (type 'done' to finish): 2
Enter a number (type 'done' to finish): done
0.0
'''