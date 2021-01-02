# ASCII Chart
# Louis Doherty


print("This program will display the ASCII values from the decimal value of 65 to 122.")
print()
print()

start=65
stop=127
numElements=stop-start+1


numCols=3

numRows=numElements//numCols

if numElements%numCols>0:
    numRows+=1
    
currentCol=0
print('|', end='')
header="Dec Hex Oct Chr |"
while currentCol<numCols:
    print (header, end = '')
    currentCol+=1

print()
l=len(header)
print ("="*(l*numCols+1), end='')
print()

currentRow=0
currentEle=start



while currentRow<numRows:
    currentCol=0
    print('|', end='')
    while currentCol<numCols:
        currentEle=start+currentRow+numRows*currentCol
        if currentEle<=stop:
            print ('%3d%4x%4o%3s' %
                   (currentEle,
                    currentEle,
                    currentEle,
                    chr(currentEle)), end='')
            print('  |',end='')
        else:
            print(' '*(l-1)+'|',end='')
        currentCol+=1
        
    print()
    currentRow+=1
print ("="*(l*numCols+1), end='')

    
