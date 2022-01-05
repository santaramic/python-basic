def palindrome(z):
    x = list(str(z))
    if(x[::-1] == x):
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    a=1
    while a!=0 :
        a = int(input())
        
        if a==0:
            
            break
        palindrome(a)
