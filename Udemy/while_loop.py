#
spam =0
while spam < 5:
    print('Hello world')
    spam = spam+1

#break will exit loop
name = ''
while name != 'your name':
    print('Please type your name.')
    name=input()
    if name == 'Bart':
        break
print('Thank you!')


#continue will go to next itteration
spam =0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is " + str(spam))