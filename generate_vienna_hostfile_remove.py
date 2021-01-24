try:
    with open("C:\Windows\System32\drivers\etc\hosts", "r") as f:
        lines = f.readlines()
except:
    print("""Can't open hosts file. Are you running as Adminitrator?""")
    input("Press enter to exit")
    exit()

skip=False
try:
    with open("C:\Windows\System32\drivers\etc\hosts", "w") as f:
        for line in lines:
            if line.strip("\n") == "#STARTPhiuCaoD1ohteephufaelaixaeJ7niix3OoBo8fa2wieX4NahbahvieF1ueRiele":
                skip=True

            if line.strip("\n") == "ENDpheex3ahy4aijohl8edeihiovee6cushe6JaighieSaijah4jaino9NahPh2oong":
                skip=False
                continue
            
            if skip!=True:
                f.write(line)
except:
    print("""Can't open hosts file. Are you running as Adminitrator?""")
    input("Press enter to exit")
    exit()
