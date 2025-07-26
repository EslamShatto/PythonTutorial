import csv
import json
import pythontutorialmodule as pt
#data extraction phase
with open('MOCK_DATA.csv',mode='r',newline='') as file :
    uncleandata = csv.reader(file)
    clean_mail_stg_1=[]
    trusted_domain=['google.com','yahoo.com','gmail.com','outlook.com','icloud.com']
    #data filteration phase we verify mail and extract domain then we load results to clean_mail_stg_1
    for i in uncleandata :        
         if(pt.emailverify(i[1])  ):     
             if (i[1].split('@')[1] in trusted_domain):
              clean_mail_stg_1.append(i)
    print()
    #loading data into json file
    with open('jsondumb.json','w') as jsonfile:
        json.dump(dict(clean_mail_stg_1),jsonfile,indent=4)
    



        
         


