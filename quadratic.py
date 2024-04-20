# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = (b**2)-4*a*c
    if discriminante > 0:
        root1 = (-b+(discriminante)**(1/2))/(2*a)
        root2 = (-b-(discriminante)**(1/2))/(2*a)
        return f"{root1, root2}"
    elif discriminante == 0:
        root = (-b+(discriminante)**(1/2))/(2*a)
        return f"({root})"
    else:
        return f"( )"


def value_y(a, b, c, x):
    valorY = a*(x**2)+b*x+c
    return valorY


def to_string(a, b, c):
    if a!=0 and b!=0 and c!=0:
        funcion = f"f(x) = {a} * X^2 + {b} * X + {c}"
        return funcion #chequado
    elif a==0 and b!=0 and c!=0:
        funcion = f"f(x) = {b} * X + {c}"
        return funcion #chequeado
    elif a!=0 and b==0 and c!=0:
        funcion = f"f(x) = {a} * X^2 + {c}"
        return funcion #chequeado
    elif a!=0 and b!=0 and c==0:
        funcion = f"f(x) = {a} * X^2 + {b} * X"
        return funcion #chequado
    elif a==0 and b==0 and c!=0:
        funcion = f"f(x) = {c}"
        return funcion
    elif a==0 and b!=0 and c==0:
        funcion = f"f(x) = {b} * X"
        return funcion
    elif a!=0 and b==0 and c==0:
        funcion = f"f(x) = {a} * X^2"
        return funcion
    else:
        funcion = 0
        return funcion

def derivation(a, b, c):
    if a!=0 and b!=0 and c!=0:
        funcion = f"f'(x) = {a*2} * X + {b}"
        return funcion #chequado
    elif a==0 and b!=0 and c!=0:
        funcion = f"f'(x) = {b}"
        return funcion #chequeado
    elif a!=0 and b==0 and c!=0:
        funcion = f"f'(x) = {a*2} * X"
        return funcion #chequeado
    elif a!=0 and b!=0 and c==0:
        funcion = f"f'(x) = {a*2} * X + {b}"
        return funcion #chequado
    elif a==0 and b==0 and c!=0:
        funcion = f"f'(x) = 0"
        return funcion
    elif a==0 and b!=0 and c==0:
        funcion = f"f'(x) = {b}"
        return funcion
    elif a!=0 and b==0 and c==0:
        funcion = f"f'(x) = {a*2} * X"
        return funcion
    else:
        funcion = 0
        return funcion
