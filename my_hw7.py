with open("syslog.txt") as file1:
    if "ERROR" in file1.read():
        file = open("syslog.txt")
        lines = file.readlines()
        for line in lines:
            if "ERROR" in line:
                print(line)
        exit(1)
    else:
        exit(0)

        

