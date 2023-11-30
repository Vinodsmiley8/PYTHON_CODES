# Check if a number is prime
def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

is_prime(11)