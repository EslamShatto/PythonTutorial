#day 1 as a funtion--------------------------------------------------------
def vowelcntr(word):#-----------------> vowel counter        
        vowels = 'aeiou'
        counter= 0
        for i in word:
            if i in vowels:
                counter +=1
        print(f'the number of vowels is {counter}')
        
        
def mariopyr1(pyrsize):#--------------> mario pyramdid    
    for i in range (int(pyrsize)):
        print(f' '*(int(pyrsize)-i)+'*'*i)

def ilocation(word):#-------------. i location    
    counter = 0
    for i in word :
        counter += 1
        if i =='i' or i =='I':
            print(f'the i is letter number {counter}')
            break

def multtable(basenum): #---------------------------> multiplication table
    for i in range(int(basenum)+1):
        for k in range(1,i+1):
            print(f'{i}x{k} = {k*i}')

#--------------------------------------------------------------------------
#day2 as a function
def mario_pyr_list():#---------------------->mariopyramid
    baselst = [' ',' ',' ',' ',' ']
    for i in range(len(baselst)+1):
        if i != 0:
            baselst[-i]='*'
        print(baselst)

def listsorter(inp):#------------------list sorter
    bucketlist = []
    bucketlist = inp    
    print(f'The list : {bucketlist}')        
    bucketlist.sort()               
    print(f'The list in ascending order : {bucketlist}')
    bucketlist.reverse()
    print(f'The list in descending order : {bucketlist}')

def multplylist(userinpt): #------------------>list multilpy      
    multtable = []
    for i in range(int(1,userinpt)+1):        
        results = []
        for k in range(1,i+1):            
            results.append(k * i)
        multtable.append(results)
    else:
        print(multtable)

def usernamechecker(username):    #------------------------------------------>username checker
    if  username.isnumeric() or  username.isspace() or username =='' :
            print('Please use alphapet and no whitespace when entering your username')
            return False
    else:    
        print('Username accpeted')
        print(f'Wlecome {username}')
        return True
    
def emailverify(email):#--------------------------------> email verification 
 bool1 = True   
 if ('@'in email and '.' in email):  
      bool1 = email.index('.',email.index('@'))>email.index('@')
 else:
        bool1 = False        
 if email == '': return False           
 if email[0] == '@'or email[0] == '.' or email[-1]=='@'or email[-1] == '.' or not bool1 :        
     return False    
 else: return True  
    
#-----------------------------------------------------------------------
#day 3 as a function

def loginauth(usernmae,password):#----------------------->  login authenticator
    usersdate = {'ahmed':'123','ali':'456','john':'789'}    
    if usernmae in usersdate.keys():        
        if password == usersdate[usernmae]:
            print('username password accepted  welcome')
        else:
            print('The password is incorrect')
    else:
        print('this username is not registered')

def domainextractor(email_list):#-------------------------------------> domain extractor
    verifedmails = filter(emailverify,email_list)
    domainname = map(lambda x :x.split('@')[1],list(verifedmails))
    print(list(domainname))

def emailverify(email):#--------------------------------> email verification with try except raise
 try:
    bool1 = True   
    if ('@'in email and '.' in email):  
        bool1 = email.index('.',email.index('@'))>email.index('@')
    else:bool1 = False                   
    if email == '': raise('value dosent meet reqiument')          
    if email[0] == '@'or email[0] == '.' or email[-1]=='@'or email[-1] == '.' or not bool1 :        
        raise ('email dosent meet requirment')     
    else: return True 
 except:    
    print('PLease Enter mail again') 
    return False
