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
keywords = ["and","array","begin","div","do","else","end","function","goto","if",
            "label","not","of","or","procedure","program","then","type","var",
            "while","read","write"]
delimiters = ["(" , ")" , "[" , "]" , " " , ";" , ":" , "," , "." ]
operators = ["+", "-", "*", "/", "<", ">", "="]
cOperators = [":=", "<=", ">=", "<>"]
ignorelist = ["\n",  "(" , ")" , "[" , "]" , " " , ";" , ":" , "," , ".", "*", "+", "-", "*", "/", "<", ">", "="]

def canOpener(somefile) -> list: 
    """
    canOpener does just that. It gets a file (the so called can) and reads its contents;

    Input: a file path
    """
    newWord: str
    words: list 
    filehandler = open(somefile)
    f = filehandler.read()
    for char in f:
        if char not in ignorelist:
            newWord += char
        else:
            if newWord != "":
                words.append(newWord)
            words.append(char)
            newWord = ""
    commentaries = 0
    for i in range(len(words)):
        if(i >= len(words)): break
        if words[i] == "(" and words[i+1] == "*":
            commentaries += 1
            for j in range(i, len(words)):
                print(j)
                if words[j] == "*" and words[j+1] == ")":
                    print("found commentary end!")
                    for zetta in range(i, j+2, 1):
                        #print("POPPING WORD ->", words[i])
                        words.pop(i)
                    break
        
    print(words)
    while(True): #This could be a very dumb dumb way to do this, but i do believe it'll work out.
        try:
            words.remove("\n")
        except:
            break

    while(True):
        try:
            words.remove(" ")
        except:
            break
    filehandler.close()
    return words     

def bigAssAnalyzer(allwords: list, comments: int) -> dict:
    '''
        bigAssAnalyzer -> a tokenizer which relies on a bunch of list popping and a bunch of ifs
        input: allwords -> a list of words to be processed, already without comments, which might fuckup the analyzer.
            aaand the number of comments, since they were removed, they get counted as such.
    '''
    analysis: dict = {
            'KEYWORD': 0,
            'IDENTIFIER': 0,
            'NUMBER': 0,
            'OPERATOR': 0,
            'COMPOUND OPERATOR': 0,
            'DELIMITER': 0,
            'COMMENTS': 0,
            'UNKNOWN': 0 
        }
    while(len(allwords) > 0): #we gotta check for all possibilities.
        #print("fetching next word")
        try:
            thisword : str = allwords.pop(0)
            #print("Word fetched: ", thisword)
            #print("word fetch successfull")
        except:
            break
        if thisword in keywords: #checks for keywords
            #print("word of analysis in keywords!")
            analysis['KEYWORD'] += 1
            continue
        elif thisword.isidentifier():
            #print("Word in analysis is identifier!")
            analysis['IDENTIFIER'] += 1
            continue
        elif thisword.isalnum():
            #print("Word in analysis is allnumbers!")
            analysis['NUMBER'] += 1
            continue
        elif thisword in operators:
            #print("Word in operators")
            #print("Checking for compound!")
            if len(allwords) > 1:
                nextword = allwords[0]
                #print("NextWord is ", nextword)
            else:
                #print("Length of allwords not enough!")
                #print("Finishing up execution...")
                continue
            possiblecompound = thisword + nextword
            #print("Possible compound operator is", possiblecompound)
            if possiblecompound in cOperators:
                #print("Possible compound found to be actual cOperator!")
                analysis['COMPOUND OPERATOR'] += 1
                #print("Wiping second operator of compound to assure consistence!")
                allwords.pop(0) #accounts for next word being part of this operator, already pops it so next iteration got a fresh word.
                continue
            else:
                #print("Possible compound found to be inadequate")
                analysis['OPERATOR'] += 1
                continue
        elif thisword in delimiters:
            #print("Word in analysis found to be a delimiter!")
            if thisword == ":" and allwords[0] == "=":
                analysis['COMPOUND OPERATOR'] += 1
                allwords.pop(0)
                continue
            analysis['DELIMITER'] += 1
            continue
        else:
            analysis['UNKNOWN'] += 1

def basicAssError(*argv):
    if len(argv) < 1:
        print("NO FILE") #default 
        quit()
    else:
        for msg in argv:
            print(msg)
            quit()
##basic nofuckup method1 :
if __name__ == "__main__" and len(sys.argv) < 2:
    basicAssError()
#here is the actual program:
elif __name__ == "__main__" and sys.argv[1] != "--debug":
    flag = 0
    for arg in sys.argv:
        if ".pas" in arg: #consequence is that the last argument the program will ever read is the .pas file. 
            pathtopas = arg
            flag = 1
            break
    if flag == 0: #basic ass flag check
        basicAssError()
    try:
        betta = open(pathtopas)
    except:
        basicAssError()
    zetta = canOpener(betta)
    zetta = bigAssAnalyzer(zetta)

##################!!!DEBUG BELLOW. CALL PROGRAM --DEBUG TO START DEBUG PROCEEDURE!!!#############################
else: #runs when no arguments passed 
    print("program called as main")
    print("running test battery 1!")

