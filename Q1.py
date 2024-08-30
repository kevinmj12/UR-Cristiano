errorCounter = 0

while True:
    string = input()
    try:
        num = int(string)
        output = ""
        for i in range(len(string), 3, -3):
            output = "," + string[i-3:i] + output

        output = string[0:(len(string)%3)] + output
        print(output)
    except:
        errorCounter+=1

    if errorCounter == 3:
        break

