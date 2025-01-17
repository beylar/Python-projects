class ExceedMaxTimesError(Exception):
    pass

class InputNotInteger(Exception):
    pass

def get_oddnum(max_times):
    """Get a positive odd integer from user.

    Parameters
    ----------
    max_times : int
        User given at most max_times times to enter a positive odd integer
    
    Returns
    -------
    int
         -1   An error code for not receiving a positive odd integer after max_times times
        > 0   A positive odd integer entered by user
    """
    # checks if the type of max_times is an integer
    try:
        if not isinstance(max_times, int):
            raise InputNotInteger("get_oddnum(): the input is not a number.")
    # raises an error if the input of max_times as integer
    except InputNotInteger as error:
        print(error)
        raise ExceedMaxTimesError
    # prints a message when there's no exception
    else:
        print("You can have 5 times to enter a positive odd integer.")
    
    odd_num_str = input("Enter a positive odd integer for this game >> ")
    num_try = 1

    # ask for at most max_times times
    while not odd_num_str.isnumeric() or \
          int(odd_num_str) < 0 or \
          int(odd_num_str) % 2 != 1:
        # checks if max_times exceed that might return error if they exceed
        try:
            # checks if the num_try are less than the max_times
            if num_try < max_times:
                odd_num_str = input("The input must be a positive odd integer. Please try again >> ")
                num_try += 1
            else:
                raise ExceedMaxTimesError("get_oddnum(): exceed the max number of times")
        # catches the error that is raised and raises the same error    
        except ExceedMaxTimesError as error:
            print(error)
            raise 
    
    # return a positive odd number
    return int(odd_num_str)

def main(max_times):
    # checks if the number returns an error
    try:
        number = get_oddnum(max_times)
        print("The input number is", number)
    # catches the error raised   
    except ExceedMaxTimesError:
        print("main(): fail to get an odd number")
    # printing the final message whether there's an exception or not    
    finally:
        print("This is the end of this program.")
   
    return

main(5)
print()
main('a')
