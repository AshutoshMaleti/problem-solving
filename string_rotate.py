string=input()
rotateNum=int(input())

def rotate_string(string,rotateNum):
    output_string=[None for _ in range(len(string))]
    for rotation in range(len(string)):
        output_string[rotation-rotateNum]=string[rotation]

    return ''.join(output_string)

print(rotate_string(string,rotateNum))