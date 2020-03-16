def str_to_int(string):
    digits=0
    count=len(string)-1
    for i in string:
        digits+=(int(i)*(10**count))
        count-=1 
    return digits

print(str_to_int('1134'))
