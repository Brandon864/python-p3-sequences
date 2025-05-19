def print_fibonacci(n):
    # Initialize the Fibonacci list
    fib_list = []
    
    # Handle edge cases
    if n <= 0:
        print(fib_list)  # Empty list for n <= 0
        return
    
    # Add first element for n >= 1
    fib_list.append(0)
    
    if n == 1:
        print(fib_list)  # [0] for n = 1
        return
    
    # Add second element for n >= 2
    fib_list.append(1)
    
    if n == 2:
        print(fib_list)  # [0, 1] for n = 2
        return
    
    # Generate Fibonacci numbers for n >= 3
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    # Print the Fibonacci list
    print(fib_list)