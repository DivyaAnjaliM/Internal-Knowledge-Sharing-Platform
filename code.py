import random
details={}
web_developer={}
web_design={}
data_science={}
cyber={}
dlt_list={}
artcl={'Web Developer':'https://medium.com/javarevisited/10-articles-every-web-developer-should-read-2efca81d0696',
'Web Designer':'https://www.linkedin.com/pulse/best-article-web-designing-alfatechindustries',
'Cyber Security':'https://www.simplilearn.com/introduction-to-cyber-security-article',
'Data Science':'https://www.ibm.com/topics/data-science'}
ttrl={'Web Developer':'https://youtu.be/HVjjoMvutj4',
      'Web Designer':'https://youtu.be/Q8NPQ2RgWyg',
      'Cyber Security':'https://youtu.be/i4Uk7D_csLg',
      'Data Science':'https://youtu.be/LHBE6Q9XlzI'}
QA={'Web Developer':'https://radixweb.com/blog/python-for-web-development',
    'Web Designer':'https://medium.com/design-bridges/design-docs-6bb34589f7a9',
    'Cyber Security':'https://www.geeksforgeeks.org/cyber-security-types-and-importance/',
    'Data Science':'https://learn.microsoft.com/en-us/fabric/data-science/'}
tagng={'coding':{'Web Developer':{artcl['Web Developer'],ttrl['Web Developer']}},
       'design':{'Web Designer':{artcl['Web Designer'],ttrl["Web Designer"]}},
       'cyber':{'Cyber Security':{artcl["Cyber Security"],ttrl["Cyber Security"]}},
       'ds':{'Data Science':{artcl["Data Science"],ttrl["Data Science"]}}}
#create profile
def add(nm,email,ph_nmbr,usr_id,expert):
    details[nm]={'usr_id':usr_id,'expert':expert,'E-mail':email,"ph_nmbr":ph_nmbr}
    if expert=="Web Developer":
        web_developer[nm]={'usr_id':usr_id,'E-mail':email,"ph_nmbr":ph_nmbr}
    elif expert=="Web Designer":
        web_design[nm]={'usr_id':usr_id,'E-mail':email,"ph_nmbr":ph_nmbr}
    elif expert=="Cyber Security":
        cyber[nm]={'usr_id':usr_id,'E-mail':email,"ph_nmbr":ph_nmbr}
    elif expert=="Data Science":
        data_science[nm]={'usr_id':usr_id,'E-mail':email,"ph_nmbr":ph_nmbr}
    print("Profile is added successfully")
def collabration():
    qualify=input("Enter the Qualification: ").title()
    if qualify=="Web Developer":
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(web_developer.items()):
            print(" ",i+1,"\t\t%s\t\t%d\t\t\t%s\t\t%d"%(nm,j['usr_id'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
    elif qualify=="Web Designer":
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(web_design.items()):
            print(" ",i+1,"\t\t%s\t\t%d\t\t\t%s\t\t%d"%(nm,j['usr_id'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
    elif qualify=="Cyber Security":
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(cyber.items()):
            print(" ",i+1,"\t\t%s\t\t%d\t\t\t%s\t\t%d"%(nm,j['usr_id'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
    elif qualify=="Data Science":
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(data_science.items()):
            print(" ",i+1,"\t\t%s\t\t%d\t\t\t%s\t\t%d"%(nm,j['usr_id'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
def article():
    qualify=input("Enter the Qualification: ").title()
    if qualify=="Web Developer":
        print(artcl['Web Developer'])
        print("to open that link press ctrl+click")
    elif qualify=="Web Designer":
        print(artcl['Web Designer'])
        print("to open that link press ctrl+click")
    elif qualify=="Cyber Security":
        print(artcl['Cyber Security'])
        print("to open that link press ctrl+click")
    elif qualify=="Data Science":
        print(artcl['Data Science'])
        print("to open that link press ctrl+click")
    else:
        print("Stream not found..!")
def tutorial():
    qualify=input("Enter the Qualification: ").title()
    if qualify=="Web Developer":
        print(ttrl['Web Developer'])
        print("to open that link press ctrl+click")
    elif qualify=="Web Designer":
        print(ttrl['Web Designer'])
        print("to open that link press ctrl+click")
    elif qualify=="Cyber Security":
        print(ttrl['Cyber Security'])
        print("to open that link press ctrl+click")
    elif qualify=="Data Science":
        print(ttrl['Data Science'])
        print("to open that link press ctrl+click")
    else:
        print("Stream not found..!") 
def qa():
    qualify=input("Enter the Qualification: ").title()
    if qualify=="Web Developer":
        qustn=input("What is thw question: ")
        print(QA['Web Developer'])
        print("to open that link press ctrl+click")
    elif qualify=="Web Designer":
        qustn=input("What is thw question: ")
        print(QA['Web Designer'])
        print("to open that link press ctrl+click")
    elif qualify=="Cyber Security":
        qustn=input("What is thw question: ")
        print(QA['Cyber Security'])
        print("to open that link press ctrl+click")
    elif qualify=="Data Science":
        qustn=input("What is thw question: ")
        print(QA['Data Science'])
        print("to open that link press ctrl+click")
    else:
        print("Stream not found..!") 
def terminated():
    if len(dlt_list)==0:
        print("No Employee....!")
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(dlt_list.items()):
            print(" ",i+1,"\t\t%s\t\t%d\t\t\t%s\t\t%d"%(nm,j['usr_id'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
def delete():
    if len(details) == 0:
        print("No Employees.....!")
        return
    trmntd = input("Enter the name of the employee: ").title()
    if trmntd in details:
        dtls = details[trmntd]
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("user_id\t\tName\t\t\texpert\t\t\t\temail\t\t\tph_nmbr")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("%d\t\t%s\t\t%s\t\t\t%s\t\t%d" % (dtls['usr_id'], trmntd, dtls['expert'], dtls['E-mail'], dtls['ph_nmbr']))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        usrid = int(input("Enter Employee ID to confirm deletion: "))
        if usrid == dtls['usr_id']:
            if dtls['expert'] == "Web Developer":
                del web_developer[trmntd]
            elif dtls['expert'] == "Web Designer":
                del web_design[trmntd]
            elif dtls['expert'] == "Cyber Security":
                del cyber[trmntd]
            elif dtls['expert'] == "Data Science":
                del data_science[trmntd]
            dlt_list[trmntd] = details.pop(trmntd)
            print(f"Employee '{trmntd}' successfully deleted.")
        else:
            print("User ID is incorrect. Deletion failed.")
    else:
        print("Employee not found!")
#All Employee
def read_all():
    if len(details)==0:
        print("No Employee....!")
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print("sl.no\t\tuser_id\t\tName\t\t\texpert\t\t\t\temail\t\t\tph_nmbr")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for i,(nm,j) in enumerate(details.items()):
            print(" ",i+1,"\t\t%d\t\t%s\t\t\t%s\t\t\t%s\t\t%d"%(j['usr_id'],nm,j['expert'],j['E-mail'],j['ph_nmbr']))
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
def recommed_articles(usrid):
    if usrid == dtls['usr_id']:
        if dtls['expert'] == "Web Developer":
            print("Article:",artcl['Web Developer'])
            print("Tutorial:",ttrl['Web Developer'])
            print("to open that link press ctrl+click")
        elif dtls['expert'] == "Web Designer":
            print("Article:",artcl['Web Designer'])
            print("Tutorial:",ttrl['Web Designer'])
            print("to open that link press ctrl+click")
        elif dtls['expert'] == "Cyber Security":
            print("Article:",artcl['Cyber Security'])
            print("Tutorial:",ttrl['Cyber Security'])
            print("to open that link press ctrl+click")
        elif dtls['expert'] == "Data Science":
            print("Article:",artcl['data science'])
            print("Tutorial:",ttrl['data science'])
            print("to open that link press ctrl+click")
        else:
            print("Sorry,Google met help you....!")
    else:
        print("User ID is incorrect. Deletion failed.")
def tag_content(content_id,tag):
    print(tagng[tag][content_id])
authorized1=[]
password=[]
try:
    with open('authorized_permission.txt','r')as file:
        authorized=file.read()
        authorized1=[authorized]
except FileNotFoundError:
    pass
try:
    with open('password_permission.txt', 'r') as file:
        password=file.read()
        password1=[password]
except FileNotFoundError:
    pass
while True:
    print("\nEnter\n 1.Profile management \n 2.Employee \n 3.Tagging\n 4.Exit")
    ch2=int(input("Enter your choice: "))
    if ch2==1:
        while True:
            cr_prsn=input("Enter which post your in the company: ").lower()
            if cr_prsn in authorized:
                with open('password_permission.txt', 'r') as file:
                    password=file.read()
                    psswrd=(input("Enter the passward: "))
                    if psswrd in password:
                        while True:
                            print("\nEnter\n 1.ADD_profile\n 2.Employee_profile\n 3.Display_all\n 4.Articles\n 5.Tutorial\n 6.Q&A\n 7.Delete_Emp_Profile\n 8.terminated_list\n 9.change_passward\n 10.Exit")
                            ch=int(input("Enter your choice: "))
                            if ch==1:
                                nm=input("Enter the name: ").title()
                                email=input("Enter the email: ")
                                ph_nmbr=int(input("Enter the phone number: "))
                                usr_id=random.randint(1000,9999)
                                expert=input("Enter your Qualification: ").title()
                                add(nm,email,ph_nmbr,usr_id,expert)
                            elif ch==2:
                                collabration()
                            elif ch==3:
                                read_all()
                            elif ch==4:
                                article()
                            elif ch==5:
                                tutorial()
                            elif ch==6:
                                qa()
                            elif ch==7:
                                pssward2=input("Enter the passward  for verification: ")
                                if pssward2 in password:
                                    delete()
                                else:
                                    print("Invalid passward....!")
                            elif ch==8:
                                terminated()
                            elif ch == 9: 
                                permission = input("Enter the new permission: ")
                                if permission not in password:
                                    password1.append(permission)
                                    with open('password_permission.txt', 'w') as file:
                                        file.write(permission)
                                    print("passward is changed...!")
                                else:
                                    print("Password is exsisting.....!")
                            elif ch==10:
                                break
                    else:
                        print("passward is incorrect")
            else:
                print("sorry invalid post...!")
            ch1=input("Do you want to continue if yes(press y) or no(press n)").lower()
            if ch1=='n':
                print()
                print("************************* THANK YOU **************************")
                break
            else:
                print("okay............!")
    elif ch2==2:
        trmntd = input("Enter the name of the employee: ").title()
        if trmntd in details:
            dtls = details[trmntd]
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            print("user_id\t\tName\t\t\texpert\t\t\t\temail\t\t\tph_nmbr")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            print("%d\t\t%s\t\t%s\t\t\t%s\t\t%d" % (dtls['usr_id'], trmntd, dtls['expert'], dtls['E-mail'], dtls['ph_nmbr']))
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            usrid = int(input("Enter Employee ID to confirmation: "))
            recommed_articles(usrid)
        else:
            print("Employee not found!")
    elif ch2==3:
        content_id=input("Enter the stream: ").title()
        tag=input("Enter the tag name: ")
        tag_content(content_id,tag)
    elif ch2==4:
        break