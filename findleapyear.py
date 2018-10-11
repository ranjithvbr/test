def is_leap(year):
    if year%400==0:
       return true
    elif year%100 == 0:
       return false
    elif year%4==0:
       return true
    return true
input=int(input('enter the year: '))
call= is_leap(input)
print call
