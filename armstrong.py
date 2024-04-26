# number=int(input('Enter any number: '))
# dup_num=number
# length=len(str(number))

# sum=0
# while number>0:
#     last_num=number%10
#     sum += last_num**length
#     number=number//10
   
# if sum==dup_num:
#     print(f'The number {dup_num} is Armstrong')

# else:
#     print('The number {} is not Armstrong'.format(dup_num))    


number=int(input('enter number '))
length=len(str(number))


digits = [int(digit) for digit in str(number)]

sum=sum([ digit**length for digit in digits])


if sum==number:
    print('Armstrong')
else:
    print("not armstrong")    

