num = 17
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
if is_prime:
    print("prime")
else:
    print("not prime")

    #explanation of this Code

#is_prime = True — We first assume the number is prime
#The loop runs from 2 up to num - 1
#If we ever find that num % i == 0 (meaning some number divides it evenly), we set is_prime = False
#After the loop ends, we check whether is_prime is still True or has become False