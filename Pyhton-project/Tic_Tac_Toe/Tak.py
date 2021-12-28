theboard={"7":" ","8":"","9":"",
         "4":" ","5":"","6":"",
           "1":" ","2":"","3":""
}


def Board(theboard):
    print(theboard["7"] + "|"+ theboard["8"] + " |"+ theboard["9"]+" |")
    print("-+-+-+-")

    theboard["4"]+ "|" + theboard["5"] + " |" + theboard["6"]+" |"
    print("-+-+-+-")

    theboard["1"]+ "|" + theboard["2"] + " |" + theboard["3"]+" |"
    print("-+-+-+-")
    # theboard["7"]+ "|" + theboard["8"] + "|" + theboard["9"]+"|")

Board(theboard)