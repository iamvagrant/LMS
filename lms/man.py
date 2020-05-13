from datetime import date,timedelta
from function_csv import *
import os,csv,shutil
from random import randrange
from tabulate import tabulate

filename1="text.csv"
filename2="record.csv"
filename3="books.csv"
filename4="category.csv"
filename5="Fine.csv"
def log():
        global filename1
        c2=['User_Id',
        'User_Name',
        'Father_Name',
        'User_Addr',
        'User_Email',
        'User_Contact',
        'Book_Issued',
        'Fine_Amount',
        'User_Password',
        'Join_Date']
        num=int(input('how many numbers of student progile you want to add:'))
        d={}
        # if not file1:
        #     s.writeheader()
        # Csv_format(filename1,'a+',c2)
        if num!=0:
            for i in range(num):
                ids=randrange(111111,999999)
                Username=input('Enter the username:')
                FatherName=input("Enter the Father's Name:")
                UserAddress=input("Enter the  House Address:")
                userEmail=input('Enter Email Address:')
                Contact=input('Enter the Contact:')
                BookIssued=0
                Fine=0
                passw=int(input('Enter 8-Digit Password:'))
                joindate=date.today()
                d={
                    'User_Id':ids,
                    'User_Name':Username,
                    'Father_Name':FatherName,
                    'User_Addr':UserAddress,
                    'User_Email':userEmail,
                    'User_Contact':Contact,
                    'Book_Issued':BookIssued,
                    'Fine_Amount':Fine,
                    'User_Password':passw,
                    'Join_Date':joindate
                }
                Csv_format(filename1,'a+',d)
        else:
                print('Must Enter one student data')
                exit                                
#############################################################################################                
def update():
    Updatein=Csv_format(filename1,'r',dict_=None)
    UserId=input('Enter the User Id:')
    for i in Updatein:
        if UserId in i['User_Id']:
            print('ACCOUNT EXIST!!!')
            Username=input('ENTER THE NEW USERNAME:')
            FatherName=input("ENTER THE FATHER'S NAME:")
            UserAddress=input('ENTER THE NEW USER ADDRESS:')
            userEmail=input('ENTER THE NEW EMAIL:')
            Contact=input('ENTER THE NEW CONTACT NUMBER:')
            if Username!='' and Username!=' ' and Username!='\n':
                i['User_Name']=Username
            if FatherName!='' and FatherName!=' ' and FatherName!='\n':
                    i['Father_Name']=FatherName   
            if UserAddress!='' and UserAddress!=' ' and UserAddress!='\n':
                    i['User_Addr']=UserAddress
            if userEmail!='' and userEmail!=' ' and userEmail!='\n':
                    i['User_Email']=userEmail
            if Contact!='' and Contact!=' ' and Contact!='\n':
                    i['User_Contact']=Contact                                           
        else :
            print('Check your password and Id') 
        d={'User_Id':i['User_Id'],'User_Name':i['User_Name'],'Father_Name':i['Father_Name'],'User_Addr':i['User_Addr'],'User_Email':i['User_Email'],'User_Contact':i['User_Contact'],'Book_Issued':i['Book_Issued'],'Fine_Amount':i['Fine_Amount'],'User_Password':i['User_Password'],'Join_Date':i['Join_Date']}
        Csv_format('Update.csv','a+',d)     
    shutil.move('update.csv',filename1)             
#*********************************************************************************
def delete():
    global filename1
    while True:
        UserId=input('Enter The User Id:')
        data_info,data,head_info=[],[],[]
        records=0
        dict_={}
        objData=Csv_format(filename1,'r',dict_=None)
        for i in objData:
            if UserId==i['User_Id']:
                head_info=[b for b in i.keys()]
                data_info.append([b for b in i.values()])
                print(tabulate(data_info,headers=head_info,tablefmt='pretty'))   
                output=input('Do you really want to delete:[Y/N]~:')
                if output=='Y' or output=='y':
                    pass
                else:
                    status=Csv_format("text_temp.csv","a+",dict(i))
            else:
                status=Csv_format("text_temp.csv","a+",dict(i))
            records=records+1
        
        if(records <= 1):
            for a in head_info:
              dict_.update({a:"Null"})
            status=Csv_format("text_temp.csv","a+",dict_)
            
        # os.remove(filename1)
        # os.rename("text_temp.csv",filename1)    

        shutil.move('text_temp.csv',filename1)         
##################################################################################    
def showpro():
    global filename1
    head_info=''
    data_info=[]
    s=Csv_format(filename1,'r',dict_=None)
    for i in s:
        head_info=[b for b in i.keys()]
        data_info.append([b for b in i.values()])
    print(tabulate(data_info,headers=head_info,tablefmt="pretty")) 
    #     print("User's Id:",i['User_Id'])
    #     print("User's name:",i['User_Name'])
    #     print("User's Father name:",i['Father_Name'])
    #     print("User's Address:",i['User_Addr'])
    #     print("User's Email:",i['User_Email'])
    #     print("User's Contact:",i['User_Contact'])
    #     print("Book Issued:",i['Book_Issued'])
    #     print("Fine :",i['Fine_Amount'])
    #     print("Password:",i['User_Password'])
    #     print("Date of Joining::",i['Join_Date'])
#####################################################################################         
def UserShown():
    global filename1
    s=Csv_format(filename1,'r',dict_=None)
    User_login={}
    head_info=''
    data_info=[]
    UserId=input('Enter the Id You want to search:')
    password=input('Enter Your Password:')
    for i in s:
        if UserId==i['User_Id'] and password==i['User_Password']:
            head_info=[b for b in i.keys()]
            data_info.append([b for b in i.values()])
    print(tabulate(data_info,headers=head_info,tablefmt="pretty"))
    #     Login_Check=i['User_Id']
    #     User_Data=[i['User_Name'],
    #     i['User_Addr'],
    #     i['Father_Name'],
    #     i['User_Email'],
    #     i['User_Contact'],
    #     i['Book_Issued'],
    #     i['Fine_Amount'],
    #     i['Join_Date']]
    #     User_login.update({Login_Check:User_Data})
    # userid=str(input('Enter Your UserId:'))
    # password=str(input('Enter your paasword:'))
    # if userid in  User_login:
    #     print("Id:",userid)
    #     print("Name:",User_login[userid][0])
    #     print("Address:",User_login[userid][1])
    #     print("Father'sName:",User_login[userid][2])
    #     print("User's Email:",User_login[userid][3])
    #     print("User's Contact:",User_login[userid][4])
    #     print("Book Issued:",User_login[userid][5])
    #     print("Fine :",User_login[userid][6])
    #     print("Date of Joining::",User_login[userid][7])
#############################################################################################
def cate():
    global filename2
    record_list=['Category_Id','Category_Name']
    num1=int(input('Enter the total number of categories you want to add:'))    
    if num1!=0:
        for i in range(num1):
            CategoryID=randrange(1111,9999)
            CategoryName=input('Enter the categories:')
            Categories_Data={'Category_Id':CategoryID,'Category_Name':CategoryName}
            Csv_format(filename2,'a+',Categories_Data)
    else:
        print('Must enter one data!!')
        exit                                  
###########################################################################################
def Delete_Category():
    global filename2
    while True:
        UserId=input('Enter The Name OF Category Id:')
        data_info,head_info=[],[]
        records=0
        dict_={}
        objData=Csv_format(filename2,'r',dict_=None)
        for i in objData:
            if UserId==i['Category_Name']:
                head_info=[b for b in i.keys()]
                data_info.append([b for b in i.values()])
                print(tabulate(data_info,headers=head_info,tablefmt='pretty'))   
                output=input('Do you really want to delete:[Y/N]~:')
                if output=='Y' or output=='y':
                    pass
                else:
                    status=Csv_format("DuplicateCategory.csv","a+",dict(i))
            else:
                status=Csv_format("DuplicateCategory.csv","a+",dict(i))
            records=records+1
        
        if(records <= 1):
            for a in head_info:
              dict_.update({a:"Null"})
            status=Csv_format("DuplicateCategory.csv","a+",dict_)
            
        # os.remove(filename1)
        # os.rename("text_temp.csv",filename1)    

        shutil.move('DuplicateCategory.csv',filename2)
###########################################################################################
def showcate():
     global filename2
     head_info=''
     data_info=[]
     s=Csv_format(filename2,'r',dict_=None)
     for i in s:
         head_info=[b for b in i.keys()]
         data_info.append([b for b in i.values()])    
         print(tabulate(data_info,headers=head_info,tablefmt='pretty'))                   
# ###########################################################################################3
def reco():
    global filename2,filename3
    s=Csv_format(filename2,'r',dict_=None)
    Category_record={}
    lat={}
    for i in s:
        print(i['Category_Name'])
        c={i['Category_Id']:i['Category_Name']}
        Category_record.update(c)   
    j=Category_record.values()

    keys=input('Enter the Category in which You want to add Books:')         
    if keys in j:
        print('you have chosen',keys)
        Book_lst=["Category",'Book_Id','Book_Name','Publisher','Edition','Book_Price','Book_Stock']
        while True:
            BookId=randrange(1,500)
            BookName=str(input('Enter the name of book:'))
            BookAuthor=str(input('Enter the Author of the book:'))
            BookPublisher=str(input('Enter the Publisher:'))
            BookEdition=int(input('Enter the year:'))
            Stock=int(input('Enter the Stock Of the book:'))
            price=int(input('Enter the Cost of per. book:'))

            c={"Category":keys,'Book_Id':BookId,'Book_Name':BookName,'Publisher':BookPublisher,'Edition':BookEdition,'Book_Price':price,'Book_Stock':Stock}

            Csv_format(filename3,'a+',c)
            
            Conti=str(input('do you want to continue(y/n):'))
            if Conti=='Y' or Conti=='y':
                pass
            else:
                print('There are ')
                exit(1)                                                                                                                     
#************************************************************************************* 
def recopro():
    s=Csv_format(filename3,'r',dict_=None)
    Info=[]
    head=''
    for j in s:
        head=[b for b in j.keys()]
        Info.append([b for b in j.values()])
        print(tabulate(Info,headers=head,tablefmt='pretty'))   
# recopro()
#***************************************************************************************
def Delete_Books():
    global filename3
    while True:
        UserId=input('ENTER The ID OF BOOK YOU WANT TO DELETE:')
        info,head=[],[]
        records=0
        dict_={}
        objData=Csv_format(filename3,'r',dict_=None)
        for i in objData:
            if UserId==i['Book_Id']:
                head=[b for b in i.keys()]
                info.append([b for b in i.values()])
                print(tabulate(info,headers=head,tablefmt='pretty'))   
                output=input('Do you really want to delete:[Y/N]~:')
                if output=='Y' or output=='y':
                    pass
                else:
                    status=Csv_format("DuplicateBooks.csv","a+",dict(i))
            else:
                status=Csv_format("DuplicateBooks.csv","a+",dict(i))
            
            records=records+1
        if(records <= 1):
            for a in head:
              dict_.update({a:"Null"})
            status=Csv_format("DuplicateBooks.csv","a+",dict_)    
        shutil.move('DuplicateBooks.csv',filename3)      
########################################################################################            
# def viewlist():
#         for book,name,yr in c1.values():
#             print("Book's name:{}".format(book))
#             print("publisher's name:{}".format(name))
#             print("year:{}".format(yr))
##########################################################################3###
def lent():
    global filename5,filename1,filename3
    tab=Csv_format(filename3,'r',dict_=None)

    head=''
    info=[]
    for i in tab:
        head=[b for b in i.keys()]
        info.append([b for b in i.values()])
        print(tabulate(info,headers=head,tablefmt='pretty'))

    title={}
    BookList=[]
    
    output=input("enter the Student's id:")
    for i in Csv_format(filename1,'r',dict=None):
        if  output in i['User_Id']:
            if i['Book_Issued']<3:
                while True:
                    IssueBook=input('enter the name of the books you want to issue:')
                    c=''
                    for j in Csv_format(filename3,'r',dict=None):
                        head=''
                        info=[]
                        if IssueBook == j['Book_Name']:
                            head=[b for b in j.keys()]
                            info.append([b for b in j.values()])
                            s=input('IS THIS BOOK YOU WANT TO ISSUE[y/N]~:')
                            if s=='Y' or s=='y':
                                Decre=j['Book_Stock']-1
                                issue=i['Book_Issued']+1
                                deck={'Category':j['Category'],'Book_Id':j['Book_Id'],'Book_Name':j['Book_Name'],'Publisher':j['Publisher'],'Edition':j['Edition'],'Book_Price':j['Book_Price'],'Book_Stock':Decre} 
                            Csv_format('UpdateBook.csv','a+',deck)
                    shutil.move('UpdateBook.csv',filename3)

                    Date_oF_Issue=date.today()
                    Detail_Student_fine={
                        'User_Id':output,
                        'User_Name':i['User_Name'],
                        'Issued_Book':IssueBook,
                        'Issued_Date':Date_oF_Issue,
                        'User_Contact':i['User_Contact'],
                        'User_Email':i['User_Email'],
                        'User_Addr':i['User_Addr'],
                        'Fine_Amount':i['Fine_Amount']
                        }
                    Csv_format(filename5,'a+',Detail_Student_fine)
                    c2={
                        'User_Id':output,
                        'User_Name':i['User_Name'],
                        'Father_Name':i['Father_Name'],
                        'User_Addr':i['User_Addr'],
                        'User_Email':i['User_Email'],
                        'User_Contact':i['User_Contact'],
                        'Book_Issued':issue,
                        'Fine_Amount':Fine,
                        'User_Password':i['User_Password'],
                        'Join_Date':i['Join_Date']
                        }
                    Csv_format('UpdateLog.csv','a+',c2)


            else:
                print('This Book is Unavailable!!!')     
        else:
            print('you had already issued three books!!')
lent()                                             
# ###############################################################################    
def retr():
    f=open(filename5,'r')
    s=csv.DictReader(f)
    Fine_List={}
    for i in s:
        book_Issued_record=[i['Student_Name'],i['Issued_Book'],i['Issued_Date'],i['Student_Addr']]
        Fine_List.update({i['Student_Id']:book_Issued_record})
        print(Fine_List) 
    la=Fine_List    
    Return_Data=str(input('Enter the Student Id:'))
    if Return_Data in la:
         temp=(la[Return_Data][2]).days
         print(temp)
        # dt1=d+timedelta(5)
        #  rem=dt1-ma
        # print(rem,ma,dt1)
        # return rem,ma,dt1  
##################################################################################
# def fine():
#      ls=list(lent())
#      if ls[1]<=ls[2]:
#           print("you have to submit this book in {} days".format(ls[0].days))
#      else:
#           fine=0
#           fine+=20
#           print("you have to pay fine of {}".format(fine))
# fine()
# ##################################################################################
# MAIN MENU
# def main_menu():
#     print('****LIBRARY MANAGEMENT****') 
#     print('1.Check available books')
#     print('2.Check books status')
#     print('3.Check your fine')
#     print("4.Student's profile")
#     print("5.Admin's login")
#     print("6.Exit")
#     print("7.Back")

# # ##################################################################################
# def center_menu():
#     print('1.Add Student')       #log()   
#     print('2.Add Books Category')  #cate()
#     print('3.Add Books')   #reco()
#     print('4.Add lent')     #lent 
#     print('5.return book')   #retr()
#     print('6.View fine list')  #fine() 
#     print('7.Exit')   
#     print('8.Back')

# ##################################################################################
# def val1(outp):
#     status=0
#     if outp==1:
#         log()   
#     elif outp==2:cate()
#     elif outp==3:reco()
#     elif outp==4:lent()  
#     elif outp==5:retr()
#     elif outp==6:fine()
#     elif outp==7:log()
#     elif outp==8:exit()
 
# ####################################################################################
# def val(output):
#     status=0
#     if output==1:
#         log()    
#     elif output==2:print("2")
#     elif output==3:print(3)
#     elif output==4:
#         f1=open('text.txt','r')
#         s=json.load(f1)
#         s.read()
#         for i in s:
#             print(i)
#         print("the details are:{}".format(s) ,end="\n") 
#         f1.close() 
    # elif output==5:
    #     password=str(input('enter the password:'))
    #     if password=='AAKASH':
    #         print('')
    #         while True:
    #             print("*****ADMIN'S DATA*****")
    #             center_menu()
    #             outp=int(input('choose the option:'))
    #             val1(outp)
#     elif output==6:exit()  

#******************************************************************************************
    
# #STATEMENT FOR CHOOSING OPTION# 
# while True:
#     main_menu()
#     v=int(input('choose the option:'))
#     val(v)
          