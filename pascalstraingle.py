import math as m
values = []

def pascalinator(start,end):
    values = []
    start = start
    maximum = end

    for i in range(start,maximum + 1):
        print('ROW: ' + str(i))
        for j in range(0,i + 1):
            val = int(((m.factorial(i))/((m.factorial(j))*(m.factorial(i-j)))))
            val1 = str(val)
            values.append(val)
            number = []
            length = len(str(val))
            
            if (length % 2) == 1:
                leng = int(((length -1)/2))
                fnumber = ''
                enumber = ''
                for j in range(0,leng):
                    fnumber = fnumber + val1[j]

                for j in range(0,leng):
                    n = leng - j
                    enumber = enumber + val1[length - n]
                number.append(fnumber)
                number.append(val1[leng])
                number.append(enumber)

            else:
                leng = int((length/2))
                fnumber = ''
                enumber = ''
                for j in range(0,leng):
                    fnumber = fnumber + val1[j]

                for j in range(0,leng):
                    n = leng - j
                    enumber = enumber + val1[length - n]

                number.append(fnumber)
                number.append(enumber)

            input(str(number)+'\t'+str(len(val1)))
    

            
        print('------------------------------')


low = int(input('Enter the start # '))
high = int(input('Enter the end # '))

pascalinator(low,high)

