try:
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print('''Please install matplotlib with:''' + '''
    ''' + '''pip install matplotlib''' + '''
    ''')
xvalv = input("Enter number of x to display (min:5, max:7): ")
yvalv = input("Enter number of values to display (min:5, max:7): ")
print("Make sure that both a's are in 0 for speed log.")
print("x values:")
if xvalv == '5':
    a = input('a: ')
    b = input('b: ') 
    c = input('c: ')
    d = input('d: ')
    e = input('e: ')
    x_values = [a, b, c, d, e]
if xvalv == '6':
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    d = input('d: ')
    e = input('e: ')
    f = input('f: ')
    x_values = [a, b, c, d, e, f]
if xvalv == '7':
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    d = input('d: ')
    e = input('e: ')
    f = input('f: ')
    g = input('g: ')
    x_values = [a, b, c, d, e, f, g]
print("Values:")
if yvalv == '5':
    a = input('a:')
    b = input('b:')
    c = input('c:')
    d = input('e:')
    e = input('f:')
    squares = [a, b, c, d, e]
if yvalv == '6':
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    d = input('d: ')
    e = input('e: ')
    f = input('f: ')
    squares = [a, b, c, d, e, f]
if yvalv == '7':
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    d = input('d: ')
    e = input('e: ')
    f = input('f: ')
    g = input('g: ')
    squares = [a, b, c, d, e, f ,g]
title = input('Title: ')
xlab = input('x label: ')
ylab = input('y label: ')
plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.plot(x_values, squares)
plt.show()
