import os 
import sys
keywords = ["and","array","begin","div","do","else","end","function","goto","if",
            "label","not","of","or","procedure","program","then","type","var",
            "while","read","write"]
delimiters = ["(" , ")" , "[" , "]" , " " , ";" , ":" , "," , "." ]
operators = ["+", "-", "*", "/", "<", ">", "="]
cOperators = [":=", "<=", ">=", "<>"]
ignorelist = ["\n",  "(" , ")" , "[" , "]" , " " , ";" , ":" , "," , ".", "*", "+", "-", "*", "/", "<", ">", "="] #this are all the stuff we don't want getting tangled up with others.
archivepath = os.path.dirname(os.path.abspath(sys.argv[0]))
testingname = "somepasfile.pas"
archivepath = os.path.join(archivepath, testingname)
file = open(archivepath, 'r')
f = file.read()
words: list = []
newWord: str = ""

for i in range(len(f)):
    print("content of reading: ", f[i])
    if f[i] not in ignorelist:
        newWord += f[i]
    else:
        if newWord != "":
            words.append(newWord)
        words.append(f[i])
        newWord = ""

print(words)

for i in range(len(words)):
    if(i >= len(words)): break
    print("WORD: ",words[i], "- POSITION:", i)
    if words[i] == "(" and words[i+1] == "*":
        flag = 0
        print("found commentary in position", str(i) + "!")
        for j in range(i, len(words)):
            print(j)
            if words[j] == "*" and words[j+1] == ")":
                print("found commentary end!")
                for zetta in range(i, j+2, 1):
                    print("POPPING WORD ->", words[i])
                    words.pop(i)
                break
        
print(words)
while(True):
    try:
        words.remove("\n")
    except:
        break

while(True):
    try:
        words.remove(" ")
    except:
        break


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
while(len(words) > 0): #we gotta check for all possibilities.
        try:
            thisword : str = words.pop(0)
            print("Word fetched: ", thisword)
            #print("word fetch successfull")
        except:
            break
        if thisword in keywords: #checks for keywords
            print("word of analysis in keywords!")
            analysis['KEYWORD'] += 1
            print("\n")
            continue
        elif thisword.isidentifier():
            print("Word in analysis is identifier!")
            analysis['IDENTIFIER'] += 1
            print("\n")
            continue
        elif thisword.isalnum():
            print("Word in analysis is allnumbers!")
            analysis['NUMBER'] += 1
            print("\n")
            continue
        elif thisword in operators:
            print("Word in operators")
            print("Checking for compound!")
            if len(words) > 1:
                nextword = words[0]
                print("NextWord is ", nextword)
            else:
                print("Length of words not enough!")
                print("Finishing up execution...")
                print("\n")
                continue
            possiblecompound = thisword + nextword
            print("Possible compound operator is", possiblecompound)
            if possiblecompound in cOperators:
                print("Possible compound found to be actual cOperator!")
                analysis['COMPOUND OPERATOR'] += 1
                print("Wiping second operator of compound to assure consistence!")
                words.pop(0) #accounts for next word being part of this operator, already pops it so next iteration got a fresh word.
                print("\n")
                continue
            else:
                print("Possible compound found to be inadequate")
                analysis['OPERATOR'] += 1
                print("\n")
                continue
        elif thisword in delimiters:
            if(thisword == ":" and words[0] == "="):
                print("This word is : and next =, forming up := compound!")
                print("This and next word form a cOperator!")
                analysis['COMPOUND OPERATOR'] += 1
                print("Wiping second operator of compound to assure consistence...")
                words.pop(0)
                print("\n")
                continue
            print("Word found to be a delimiter!")
            analysis['DELIMITER'] += 1
            print("\n")
            continue
        else:
            print("Word in analysis unknown...")
            analysis['UNKNOWN'] += 1
            print("\n")
        
print(analysis)


            

    