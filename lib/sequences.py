# #!/usr/bin/env python3

# def print_fibonacci(length):
#     pass

# def print_fibonacci():
def print_fibonacci(length):
    fibonacci_sequence = []
    
    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_value = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)

print_fibonacci(9)
