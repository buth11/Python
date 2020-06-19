name='Alice'
if name=='Alice':
    print('Hi Alice')
print('Done')

passwd = 'swordfish'
if passwd == 'swordfish':
    print('Access granted')
else:
    print('Access denided')

name = 'Bob'
age = 300
if name=='Alice':
    print('Hi Alice')
elif age>200:
    print('Age ok')
elif age>100:
    print('You are not Alice, granny')

print('Enter name')
name=input()
if name: #better to use: if name!='':
    print('Thanks for your name.')
else:
    print('You didn\'t enter your name') 


# bool(0)
# False

# bool(11)
# True

# bool('')
# False

# bool('asdfd')
# True
