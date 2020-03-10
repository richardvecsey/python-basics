"""
How to speed up for cycle with break and continue
-------------------------------------------------
continue:   Jump to the next iteration, the remain part of the actual iteration
            won't be executed
break:      Jump out from the for loop, the remain part of the whole for cycle
            won't be executed
"""
print('This is a normal for loop')
for i in range(4):
    print(i)

print('\nThis is an example for continue')
for i in range(4):
    if i == 2:
        continue
    print(i)

print('\nThis is an example for break')
for i in range(4):
    if i == 2:
        break
    print(i)

print('\nEnd of examples')