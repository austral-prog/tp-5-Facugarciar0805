# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    if x > y:  
        return x
    elif x < y:
        return y
    else:
        return x



def max_of_three(x, y, z): 
    if x!=y and x!=z and y!=z:

        if (x > y) and (x > z):
            return x
        elif (y > x) and (x > z):
            return y 
        elif (z > x) and (z > y):
            return z  
    elif x==y and x!=z:
        if x > z:  
            return x
        elif x < z:
            return z
    elif x==z and y!=x:
        if x > y:  
            return x
        elif x < y:
            return y
    elif z==y and x!=z:
        if x > z:  
            return x
        elif x < z:
            return z
    else:
        return x
