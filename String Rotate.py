string=input()
rotateNum=int(input())

def rotate_string(string,rotateNum):
    length=len(string)
    print('left rotate: '+string[rotateNum:]+string[:rotateNum])
    print('right rotate: '+string[length-rotateNum:]+string[:length-rotateNum])

rotate_string(string,rotateNum)