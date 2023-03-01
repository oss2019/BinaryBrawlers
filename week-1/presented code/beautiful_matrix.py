def make_it_beautiful(arr:list[int]):
    """
    Returns TRUE if array can be made beautiful and prints its beautiful version.
    ELSE returns FALSE if array can not be made beautiful.
    """

    # MAIN IDEA: AN ARRAY CAN BE BEAUTIFUL AS LONG AS ALL THE ELEMENTS OF  
    #THE ARRAY ARE NOT THE SAME.

    # For that, we can compare any two arbitrary elements
   
    if arr[0] == arr[1]: # Comparing first and second element
        # Are we missing a case here... I think so
        # CAN YOU TELL WHICH INPUT CAN HALT OUR CODE....?
        return False


    # HINT:
    # ^^^^

    # See which of the test cases can cause an issue:

    # [3, 2, 5, 10]
    # [2, 2, 4, 8]
    # [3, 5, 6, 8]
    # [47]
    # [8, 8, 6, 9]
    # [7, 6, 5]
    # [39, 1000]




    # YA, [47] will cause us some trouble, Can you tell why?






       

    # Think what will happen if single elment array is passed?
    # How should we tackle it

    # One way is to write an explicit case for a single like:

    if len(arr) <= 1:
        print(arr)
        return True

    # We can do better than that by comparing the first and last element,
    #this way we can avoid giving explicit condition for single element array

    if arr[0] == arr[len(arr)-1]: # for cpp, we will pass array length as an argument
        return False

    # Modulo Operation(%), a%b will return the remainder when a was divided by b,
    #returned value will always be >= 0 but <b.
    #looks like we can use it to access elements of the array without causing any errors.

    # But this again creates one problem, it will return false for [a]
    #which is already beautiful, giving us wrong answer.

    # Another alternative could be:
    m = 108
    n = 22
    if arr[m%len(arr)] == arr[n%len(arr)]: #comparing two random elements, no condition for m and n
        return False

    #  It has its own set of issues, can you guess what?

    # Moral of the story: we can not avoid giving explicit condition in this case.

    # NOW WE ARE LEFT WITH THE TASK TO PRINT THE BEAUTIFUL VERSION AND RETURN TRUE

    # The first approach that hits the mind is printing the array in
        # DECREASING Order.
    arr.sort()
    print(arr[::-1])
    # Guess what, it will not always give always correct answer
    # like for arr = [4, 7, 7, 3]











    # The Solution I propose is to print the biggest element first
    #followed by the smallest element and then print the remaining
    #elements in which ever way you want, sorting the array beforehand will make things easy
    arr.sort()
    size = len(arr)

    print(arr[size-1], end=" ")
    print(arr[0], end=" ")
    print(*arr[1:size-1])
