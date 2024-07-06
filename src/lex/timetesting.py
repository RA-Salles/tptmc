"""
    I'll go on a little tangent on how much i hate myself and my DELTA ALPHA.
    I named the now named test3 as test5 nospaces and tested out 3 and 4 and was like
    DAMN, THESE DON'T ADD UP.
    Guess what.
    OF FUCKING COURSE IT DOESN'T ADD UP, 3 AND 4 ARE COMPLETELY FUCKING DIFFERENT FILES!
    NOT A SIMPLE MATTER OF SPACE CHANGING AND SWITCHAROO LIKE WITH 3MANY AND 3SIMPLE.
    Really, Foxtrot Mike Sierra.

    notes of testing: 
    passed test1_pas
    passed test2_simple
    passed test2_withcomments
    passed test3_simple

"""
import time
start_time = time.time()

import os 
import sys
keywords = ["and","array","begin","div","do","else","end","function","goto","if",
            "label","not","of","or","procedure","program","then","type","var",
            "while","read","write"]
delimiters = ["(" , ")" , "[" , "]" , " " , ";" , ":" , "," , "." ]
operators = ["+", "-", "*", "/", "<", ">", "="]
cOperators = [":=", "<=", ">=", "<>"]
ignorelist = ["\n",  "(" , ")" , "[" , "]" , " " , ";" , ":" , "," , ".", "*", "+", "-", "*", "/", "<", ">", "=", "'", "\"", "!"] #this are all the stuff we don't want getting tangled up with others.
archivepath = os.path.dirname(os.path.abspath(sys.argv[0]))
if len(sys.argv) < 2:
    print("NO FILE")
    quit()
testingname = str(sys.argv[1])
archivepath = os.path.join(archivepath, testingname)
file = open(archivepath, 'r')
f = file.read()
words: list = []
newWord: str = ""


debug = 0 #make this naught to ommit debug messages at the and.
debuglog: list = [] #useful if you wanna access it from a simple 


#word separator routine
for i in range(len(f)):
    #debuglog.append("content of reading: " +  str(f[i]))
    if f[i] not in ignorelist:
        newWord += f[i]
    else:
        if newWord != "":
            debuglog.append("word detected as: " + newWord)
            words.append(newWord)
        debuglog.append("identified ignorelist character as " + str(f[i]))
        words.append(f[i])
        newWord = ""
debuglog.append("processing of words successfull...")

if debug == 1:
    #debuglog.append("Debuglog next space contains all words and ignorelist chars found in processing")
    #for word in words:
    #    debuglog.append(str(word))
    print(words)

#Commentary killer routine
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
i = 0
while(True):
    flag = 0
    if(i < 0): i = 0 #this is a Mike Foxtrot Uniform Avoider (MiFUA, for short). We might need to send the iterator back in some kind of circunstance. This avoid whatever monkey logic implemented later Foxtrots Uniform the program.
    if(i >= len(words)): break
    debuglog.append("WORD: < " + str(words[i]) + " >- POSITION:" + str(i))
    if words[i] == "(" and words[i+1] == "*":
        flag = 1
        debuglog.append("found commentary in position " + str(i) + "!")
        for j in range(i, len(words)):
            debuglog.append(j)
            if words[j] == "*" and words[j+1] == ")":
                debuglog.append("found commentary end!")
                for zetta in range(i, j+2, 1):
                    debuglog.append("POPPING WORD ->" + str(words[i]))
                    words.pop(i)
                debuglog.append("comment successfully expurgated of further processing!")
                break
    if flag == 1:
        debuglog.append("found a complete comment and added it to sum of contents found.")
        analysis["COMMENTS"] += 1
        i -= 1
        continue
    i += 1
debuglog.append("all possible comments expurgated. Next position contain final words after expurgation.")
#if debug == 1:
#    #for word in words:
#    #    debuglog.append(str(word))
#    print(words)
debuglog.append("running space expurgation routine!")
while(True):
    try:
        words.remove("\n")
    except:
        debuglog.append("Removed all posible newlines.")
        break

while(True):
    try:
        words.remove(" ")
    except:
        debuglog.append("Removed all possible blanks")
        break

if debug == 1:
    print(words)

while(len(words) > 0): #we gotta check for all possibilities.
        try:
            thisword : str = words.pop(0)
            debuglog.append("Word fetched: " + str(thisword))
            #print("word fetch successfull")
        except:
            break
        if thisword in keywords: #checks for keywords
            debuglog.append("KEYWORD")
            analysis['KEYWORD'] += 1
            continue
        elif thisword.isidentifier():
            debuglog.append("IDENTIFIER")
            analysis['IDENTIFIER'] += 1
            continue
        elif thisword.isalnum():
            debuglog.append("NUMBER")
            analysis['NUMBER'] += 1
            continue
        elif thisword in operators:
            debuglog.append("OPERATOR")
            debuglog.append("Checking for compound!")
            if len(words) > 1:
                nextword = words[0]
                debuglog.append("NextWord is " + str(nextword))
            else:
                debuglog.append("Length of words not enough!")
                debuglog.append("OPERATOR")
                analysis['OPERATOR'] += 1
                continue
            possiblecompound = thisword + nextword
            debuglog.append("Possible compound operator is" + str(possiblecompound))
            if possiblecompound in cOperators:
                debuglog.append("Possible compound found to be actual cOperator!")
                analysis['COMPOUND OPERATOR'] += 1
                debuglog.append("Wiping second operator of compound to assure consistence!")
                words.pop(0) #accounts for next word being part of this operator, already pops it so next iteration got a fresh word.
                continue
            else:
                debuglog.append("Possible compound found to be inadequate")
                analysis['OPERATOR'] += 1
                continue
        elif thisword in delimiters:
            if(thisword == ":" and words[0] == "="):
                debuglog.append("This word is : and next =, forming up := compound!")
                debuglog.append("This and next word form a cOperator!")
                analysis['COMPOUND OPERATOR'] += 1
                debuglog.append("Wiping second operator of compound to assure consistence...")
                words.pop(0)
                continue
            debuglog.append("Word found to be a delimiter!")
            analysis['DELIMITER'] += 1
            continue
        else:
            debuglog.append("Word in analysis unknown...")
            analysis['UNKNOWN'] += 1

#formatted print routine:

if debug == 1:
    for debugmessage in debuglog:
        print(debugmessage)

for key in analysis:
    print(key + ": " + str(analysis[key]))

file.close()

print("--- %s seconds ---" % (time.time() - start_time))



            

    