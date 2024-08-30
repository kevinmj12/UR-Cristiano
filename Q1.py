errorCounter = 0

while True:
    string = input()
    try:
        num = int(string)
        flag = False

        if(string[0] == "-"):
            flag = True
            string = string[1:]

        output = ""

        for i in range(len(string), len(string)%3, -3):
            if(i-3 <= 0):
                output = string[i-3:i] + output
            else:
                output = "," + string[i-3:i] + output

        output = string[0:(len(string)%3)] + output

        print(output if not flag else "-" + output)
        errorCounter = 0
    except:
        errorCounter+=1
        print("응 탈락")

    if errorCounter == 3:
        print("응 수듄")
        break

