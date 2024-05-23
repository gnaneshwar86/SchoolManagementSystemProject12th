#Function definitions

import mysql.connector as CON

#Menu

def menu():
        print("Logging in.......")
        print()
        print("MENU FOR FUNCTIONS TO BE PERFORMED:")
        print()
        print("Enter 1 to DISPLAY data")
        print("Enter 2 to INSERT data")
        print("Enter 3 to UPDATE data")
        print("Enter 4 to DELETE data")
        print("Enter 5 for SALARY related operations")
        print("Enter 6 for DELETION of a username")
        print()
        choice=int(input("Enter your choice : "))
        print()
        if choice in (1,2,3,4,5,6):
                return choice
        else:
                print("Invalid choice")

#Login or register

def login():
        O = CON.connect(host="localhost",user="root",password="123456",database="sms")
        c = O.cursor()
        B=input("Enter your username : ")
        C=int(input("Enter your 4-digit password :"))
        c.execute("select * from Login")
        D=c.fetchall()
        dic={}
        for i in range(len(D)):
                dic[D[i][0]]=D[i][1]
        choice1='y'
        Q=0
        List=[]
        for i in D:
                List.append(i[0])
        while choice1.lower()=='y':
                while True:
                        if B in List:
                                if C==dic[B]:
                                        z=menu()
                                        if z==1:
                                                display()
                                                Q=1
                                                break
                                                
                                        elif z==2:
                                                insert()
                                                Q=1
                                                break
                                                
                                        elif z==3:
                                                update()
                                                Q=1
                                                break
                                                
                                        elif z==4:
                                                a=1
                                                delete(a)
                                                Q=1
                                                break
                                                
                                        elif z==5:
                                                salary()
                                                Q=1
                                                break
                                                
                                        elif z==6:
                                                a=2
                                                delete(a)
                                                Q=1
                                                break
                                                
                                        elif z==7:
                                                Q=3
                                                choice1='n'
                                                break
                                               
                                        else :
                                                print("Invalid Choice")
                                                Q=2
                                                
                                else:
                                        print("Invalid password")
                                        Q=2
                                        break
                        
                        else:
                                print("Invalid Username")
                                Q=2
                                break
                                
                if Q==1:
                        print()
                        choice1=input("Do you want to perform any other operation(y/n):")
                elif Q==2:
                        break
        else:
                print("Thank you😀😀😀😀🙏🙏🙏🙏")

def register():
        global dic
        O = CON.connect(host="localhost",user="root",password="123456",database="sms")
        c = O.cursor()
        B=input("Enter a username :")
        C=int(input("Enter your 4-digit password : "))
        c.execute("select * from Login")
        D=c.fetchall()
        L=[]
        dic={}
        for i in range(len(D)):
                L.append(D[i][0])
                dic[D[i][0]]=D[i][1]
        if B in L:
                print("Username already exists")
                return 0
                
        else:
                dict1={B:C}
                c.execute("Insert into Login (Username,Password) values('{}',{})".format(B,C))
                O.commit()
                dic.update(dict1)
                print("User added successfully")
                return 1
                
        
        
#Inserting data

def insert():
    O = CON.connect(host="localhost",user="root",password="123456",database="sms")
    c = O.cursor()
    st=int(input("""Select the Table
Enter 1 for Personal_Details
Enter 2 for Staff_Details
Your Choice(1/2)...? """))
    ch="y"
    if st==1:
        while ch.lower()=="y":
            A=input("Enter the employee code : ")
            c.execute('Select Emp_code from personal_details')
            X=c.fetchall()
            code=[]
            for i in X:
                for j in i:
                    code.append(j)
            if A not in code:
                    B=input("Enter the employee name : ")
                    C=input("Enter the DOB (YYYY-MM-DD) : ")
                    D=input("Enter the account number : ") 
                    E=int(input("Enter the phone number : "))
                    F=input("Enter the Gender (M/F) : ")
                    G=int(2022-int(C[:4]))
                    c.execute('''Insert into Personal_Details Values("{}","{}","{}","{}",{},"{}",{})'''.format(A,B,C,D,E,F,G))
            else :
                    print("Employee code already exists. Change your employee code")
            ch=input("Do you want to continue INSERTION(y/n).....")
            O.commit()
    elif st==2:
        while ch.lower()=="y":
            A=input("Enter the employee code : ")
            B=input("Enter the Date of Joining(YYYY-MM-DD) : ")
            C=input("Enter the Department Name : ")
            D=float(input("Enter the Salary : "))
            E=int(2022-int(B[:4]))
            F=input("Enter the Qualification : ")
            G=input("Enter the Designation : ")
            c.execute('''Insert into Staff_Detail 
            Values("{}","{}","{}",{},{},"{}","{}")'''.format(A,B,C,D,E,F,G))
            ch=input("Do you want to continue INSERTION(y/n).....")
            O.commit()
    else:
        print("Invalid choice")

    O.close()



#Updating data

def update():
        O = CON.connect(host="localhost",user="root",password="123456",database="SMS")
        c = O.cursor()
        st=int(input("""Select the Table
Enter 1 for Personal_Details
Enter 2 for Staff_Details
Your Choice(1/2)...? """))
        ch="y"
        if st==1:
                while ch.lower()=="y":
                        B=input("Enter the employee code to be updated : ")
                        c.execute('Select * from Personal_Details where Emp_Code="{}"'.format(B))
                        F1=c.fetchone()
                        if F1==None:
                                print("NO records matched")
                                break
                        A=int(input("Enter number of columns to be updated(Total no. of columns = 6) : "))
                        C={1:"Emp_Name",2:"DOB",3:"ACC_No",4:"Phone_No",5:"Gender",6:"Age"}
                        L=[]
                        print('''Select the column(s)
Enter 1 for Emp_Name
Enter 2 for DOB
Enter 3 for Account number
Enter 4 for Phone_No
Enter 5 for Gender
Enter 6 for Age''')
                        for i in range(A):
                                H=int(input("Enter choice "+str(i+1)+" : "))
                                if H in (1,2,3,4,5,6):
                                        L.append(H)
                                else:
                                        print("Invalid choice")
                        for i in range(A):
                                D=L[i]
                                if D in (4,6):
                                        E=int(input("Enter "+C[D]+" : "))
                                        c.execute('''UPDATE Personal_Details 
                    SET {}={} WHERE Emp_Code="{}"'''.format(C[D],E,B))
                                        O.commit()
                                elif D in (1,2,3,5) :
                                        if D==2:
                                                E=input("Enter "+C[D]+" (YYYY-MM-DD) : ")
                                        elif D==5:
                                                E=input("Enter "+C[D]+" (M/F) : ")
                                        else:
                                                E=input("Enter "+C[D]+" : ")
                                        c.execute('''UPDATE Personal_Details 
                    SET {}="{}" WHERE Emp_Code="{}"'''.format(C[D],E,B))
                                        O.commit()
                        c.execute('Select * from Personal_Details where Emp_Code="{}"'.format(B))
                        F2=c.fetchone()
                        print("Before Updating the Record: ")
                        print(F1)
                        print("After Updating the Record: ")
                        print(F2)
                        ch=input("Do you want to continue UPDATION(y/n).....")
        elif st==2:
                while ch.lower()=="y":
                        B=input("Enter the employee code to be updated : ")
                        c.execute('Select * from Staff_Detail where Emp_Code="{}"'.format(B))
                        F1=c.fetchone()
                        if F1==None:
                                print("NO records matched")
                        A=int(input("Enter number of columns to be updated(Total no. of columns = 6) : "))
                        C={1:"DOJ",2:"DEPT",3:"Salary",4:"Experience",5:"Qualification",6:"Designation"}
                        L=[]
                        print('''select the column(one column at a time)
Enter 1 for Date of Joining
Enter 2 for Department
Enter 3 for Salary
Enter 4 for Experience
Enter 5 for Qualification
Enter 6 for Designation''')
                        for i in range(A):
                                H=int(input("Enter choice "+str(i+1)+" : "))
                                if H in (1,2,3,4,5,6):
                                        L.append(H)
                                else:
                                        print("Invalid choice")
                        for i in range(A):
                                D=L[i]
                                if D in (3,4):
                                        E=int(input("Enter "+C[D]+" : "))
                                        c.execute('''UPDATE Staff_Detail 
                    SET {}={} WHERE Emp_Code="{}"'''.format(C[D],E,B))
                                        O.commit()
                                elif D in (1,2,5,6) :
                                        if D==1:
                                                E=input("Enter "+C[D]+" (YYYY-MM-DD) : ")
                                        else:
                                                E=input("Enter "+C[D]+" : ")
                                        c.execute('''UPDATE Staff_Detail 
                    SET {}="{}" WHERE Emp_Code="{}"'''.format(C[D],E,B))
                                        O.commit()
                        c.execute('Select * from Staff_Detail where Emp_Code="{}"'.format(B))
                        F2=c.fetchone()
                        print("Before Updating the Record: ")
                        print(F1)
                        print("After Updating the Record: ")
                        print(F2)
                        ch=input("Do you want to continue UPDATION(y/n).....")
        else:
                print("Invalid choice")
        
        O.close()


#Deleting records
def delete(n):
        if n==1:
                O = CON.connect(host="localhost",user="root",password="123456",database="sms")
                c = O.cursor()
                ch="y"
                while ch.lower()=="y":
                            A=input("Enter the employee code to be deleted : ")
                            c.execute('Delete from Personal_details where Emp_Code = "{}"'.format(A))
                            O.commit()
                            ch=input("Do you want to continue DELETION(y/n).....")
        elif n==2:
                O = CON.connect(host="localhost",user="root",password="123456",database="sms")
                c = O.cursor()
                A=input("Enter username to be deleted : ")
                c.execute('select * from Login')
                D=c.fetchall()
                L=[]
                for i in D:
                        L.append(i[0])
                if A in L:
                        c.execute('Delete from Login where Username=\'{}\''.format(A))
                        O.commit()
                        print("Username deleted successfully")
                else:
                        print("Username not found")
                

                        
#Displaying records
def display():
        O = CON.connect(host="localhost",user="root",password="123456",database="sms")
        c=O.cursor()
        print("""SELECT THE TABLE
Enter 1 for Personal_Details
Enter 2 for Staff_Details
Enter 3 for department related operations""")
        st=int(input("Your choice..."))
        print()
        ch="y"
        if st==1:
                while ch.lower()=='y':
                        print("""Select from the below
Enter 3 for all the records to be display
Enter 4 if you have employee code to be dispalyed""")
                        A=int(input("Your choice(3/4)...?"))
                        print()
                        if A==3:
                                c.execute('Select * from Personal_Details')
                                B=c.fetchall()
                                T=("Emp_Code","Emp_Name","DOB","ACC_No","Phone_No","Gender","Age")
                                print(T)
                                for i in B:
                                        print(i)
                        elif A==4:
                                D=input("Enter the employee code to be dispalyed :")
                                c.execute('Select * from Personal_Details where Emp_Code=\'{}\''.format(D))
                                B=c.fetchall()
                                T=("Emp_Code","Emp_Name","DOB","ACC_No","Phone_No","Gender","Age")
                                print(T)
                                if B!=None:
                                        for i in B:
                                            print(i)
                                else:
                                        print("NO records found")
                        else :
                                print("Inappropriate input!!!!")
                        ch=input("Do you want to DISPLAY further(y/n).....")
        if st==2:
                while ch.lower()=='y':
                    print("""Select from the below
Enter 3 for all the records to be display
Enter 4 if you have employee code to be dispalyed""")
                    A=int(input("Your choice(3/4)...?"))
                    print()
                    if A==3:
                        c.execute('Select * from Staff_Detail')
                        B=c.fetchall()
                        T=("Emp_Code","Emp_Name","DOB","ACC_No","Phone_No","Gender","Age")
                        print(T)
                        for i in B:
                            print(i)
                    elif A==4:
                        D=input("Enter the employee code to be dispalyed :")
                        c.execute('Select * from Staff_Detail where Emp_Code=\'{}\''.format(D))
                        B=c.fetchall()
                        T=("Emp_Code","DOJ","DOB","DEPT","Salary","Experience","Qualification","Designation")
                        print(T)
                        for i in B:
                            print(i)
                    else :
                        print("Inappropriate input!!!!")
                    ch=input("Do you want to DISPLAY further(y/n).....")
        if st==3:
            while ch.lower()=='y':
                print('''Enter 1 to view records of a particular department
Enter 2 to view number of employees in every department''')
                A=int(input("Your choice....?"))
                print()
                if A==1:
                        print('''Enter 1 for Admin
Enter 2 for English
Enter 3 for Physiscs
Enter 4 for Biology
Enter 5 for Sports
Enter 6 for Tamil
Enter 7 for Science
Enter 8 for Economics''')
                        F={1:"Admin",2:"English",3:"Physics",4:"Biology",5:"Sports",6:"Tamil",7:"Science",8:"Economics"}
                        E=int(input("Enter your choice : "))
                        print()
                        G=F[E]
                        B=c.execute('Select * from Personal_details as P,staff_detail as s where P.Emp_Code=s.Emp_Code and DEPT=\'{}\''.format(G))
                        D=c.fetchall()
                        if len(D)==0:
                                print("No record found")
                        else:
                                for i in D:
                                        print(i)
                if A==2:
                        B=c.execute('Select DEPT,count(*) from Staff_Detail GROUP BY DEPT')
                        C=c.fetchall()
                        print(("Department","Number of employees"))
                        for i in C:
                                print(i)
                ch=input("Do you want to DISPLAY further(y/n) : ")
        O.close()

#Salary related operations
def salary():
        ch='y'
        while ch.lower()=='y':
                print("""Select from the below
1.Display salary
2.Salary Increment""")
                A=int(input("Enter your choice :"))
                print()
                if A==1:
                        O = CON.connect(host="localhost",user="root",password="123456",database="sms")
                        c = O.cursor()
                        print("""Enter 1 for display of all salaries
Enter 2 if you have Employee code to be displayed""")
                        B=int(input("Enter your choice :"))
                        print()
                        if B==1:
                                c.execute('Select s.Emp_Code,Emp_Name,salary from Staff_detail as s,Personal_details as p where s.Emp_Code=p.Emp_Code')
                                D=c.fetchall()
                                T=("Employee code","Employee name","Salary")
                                print(T)
                                for i in D:
                                        print(i)
                        elif B==2:
                                D=input("Enter employee code : ")
                                print()
                                c.execute('Select s.Emp_Code,Emp_Name,Salary from Staff_detail as s,Personal_details as p where s.Emp_Code=p.Emp_Code')
                                E=c.fetchall()
                                T=("Employee code","Employee name","Salary")
                                print(T)
                                found=0
                                for i in E:
                                        if i[0]==D:
                                                print(i)
                                                found+=1
                                                break
                                if found==0:
                                        print("No match found")
                        else:
                                print("Invaild choice")
                        

                elif A==2:
                        O = CON.connect(host="localhost",user="root",password="123456",database="sms")
                        c = O.cursor()
                        print('''Enter 1 if you want to increase for a single Employee
Enter 2 if you want to increase the salary department wise''')
                        T=int(input("Enter your choice:"))
                        print()
                        if T==1:
                                B=input("Enter employee code whose salary is to incremented:")
                                C=int(input("Enter the amount by which salary is to incremented:"))
                                c.execute('Select Emp_Code,Salary from Staff_detail')
                                D=c.fetchall()
                                found=0
                                for i in D:
                                        if i[0]==B:
                                                E=int(int(i[1])+C)
                                                c.execute('Select Emp_Code,Salary from Staff_detail where Emp_Code=\'{}\'  '.format(B))
                                                F=c.fetchall()
                                                print("BEFORE incrementing")
                                                print(("Emp_Code","Salary"))
                                                print(F)
                                                c.execute('Update Staff_Detail set Salary={} where Emp_Code=\'{}\' '.format(E,B))
                                                O.commit()
                                                c.execute('Select Emp_Code,Salary from Staff_detail where Emp_Code=\'{}\'  '.format(B))
                                                F=c.fetchall()
                                                print("AFTER Incrementing")
                                                print(("Emp_Code","Salary"))
                                                print(F)
                                                found+=1
                                                break
                                if found==0:
                                        print("No match found")
                                else:
                                        print("Incremented successfully")
                        elif T==2:
                                print("SELECT the department")
                                print('''Enter 1 for Admin
Enter 2 for English
Enter 3 for Physiscs
Enter 4 for Biology
Enter 5 for Sports
Enter 6 for Tamil
Enter 7 for Science
Enter 8 for Economics''')
                                D=int(input("Enter your choice"))
                                print()
                                F={1:"Admin",2:"English",3:"Physics",4:"Biology",5:"Sports",6:"Tamil",7:"Science",8:"Economics"}
                                if D in F.keys():
                                        C=int(input("Enter the amount by which salary is to incremented:"))
                                        print("BEFORE incrementing")
                                        c.execute('Select Emp_Code,Salary from Staff_detail where DEPT=\'{}\'  '.format(F[D]))
                                        E=c.fetchall()
                                        print(E)
                                        c.execute('Update Staff_Detail set Salary=Salary+{} '.format(C))
                                        O.commit()
                                        print("AFTER incrementing")
                                        c.execute('Select Emp_Code,Salary from Staff_detail where DEPT=\'{}\'  '.format(F[D]))
                                        E=c.fetchall()
                                        print(E)
                                        print("Incremented successfully")
                                else:
                                        print("Invalid choice")

                        else :
                               print("Invalid choice")
                ch=input("Do you want to continue SALARY related Operations(y/n) : ")
        else :
                print("Invalid choice : ")
        
                
                
                
                                

                
                




    


#Main program
print("😀 ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ 😀")
print()
print("     🙏Welcome to Our PROJECT developed with PYTHON-MYSQL CONNECTIVITY🙏       ")
print()
print("                       SCHOOL MANAGEMENT SYSTEM(SMS)                          ")
print()
print("😀 ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ ⫘ 😀")
print()


O = CON.connect(host="localhost",user="root",password="123456",database="sms")
c = O.cursor()
print('''Enter 1 to LOGIN
Enter 2 to REGISTER
''')
A=int(input("Your choice(1/2)...? : "))
if A==1:
        login()
        
elif A==2:
        Z=register()
        if Z==1:
                ch=input("Do you want to login(y/n):")
                if ch.lower()=='y':
                    login()
        else:
                print()
                print("Exiting.....")
else:
        print()
        print("Invaild choice!!!!!!")
        print("Exiting.....")




        
                
                    
         
         









            
    
           
                        
                        
                    
                


                
    
    

