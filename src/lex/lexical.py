"""
Written by BCL0c, whose software is terrible and should always be checked thrice before sendind to production.


Let's get this straight now:
    1. This program will consume a lot of memory.
        To be exact, this program will load the entire .txt passed as an argument when invoking it; 
    2. This program was written after a big ass break from python for about half a year.
        Half a year not coding in python till i came back to work with python style bullshit again.
        Very fun;
    3. I will still be very unhinged during comments. If you can't work with that, you should probably Echo Sierra Alpha Delta;
    4. Not following the documentation presented in this initial comment and/or the usage instructions when calling this program as 
        such -> "program --help" will result in a MikeFoxtrot and unexpected behaviour. It might kill your sys32? maybe, i don't know.
        It might erase important data? Probably. But be sure i did not test it. And therefore this program comes without any warranty 
        whatsoever and, by using it, you assume all risks, documented or not :) 
        (just kidding, i do not believe it will fuckup your system. Except for the warranty and risk part, that there is very serious);
    
Documents to be read by the programmer (IGNORE UNTIL NEXT TOPIC IF YOU'RE SEARCHING FOR USEFUL DOCUMENTATION)
    < https://realpython.com/python-command-line-arguments/#the-command-line-interface > (yeah, i know, i'm not a very good programmer)

    
"""
import sys
def canOpener(somefile) -> list:
    pass

def bigAssAnalyzer(filelines: list) -> list:
    pass

def main(pathtopas: str) -> None:
    pass #TODO

##basic nofuckup method1 :
if __name__ == "__main__" and len(sys.argv) < 2:
    print("NO FILE")
    quit()
#here is the actual program:
elif __name__ == "__main__" and sys.argv[1] != "--debug":
    flag = 0
    for arg in sys.argv:
        if ".pas" in arg: #consequence is that the last argument the program will ever read is the .pas file. 
            pathtopas = arg
            flag = 1
            break
    if flag == 0: #basic ass flag check
        print("NO FILE")
        quit()
    
    main(pathtopas)
    


##################!!!DEBUG BELLOW. CALL PROGRAM --DEBUG TO START DEBUG PROCEEDURE!!!#############################
else: #runs when no arguments passed 
    print("program called as main")
    print("running test battery 1!")

