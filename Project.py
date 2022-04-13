SOURCE CODE
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='123',database='project')
mycur=mycon.cursor()
from datetime import date
#======================================================
def p1():
    l1=[]
    mycur.execute('select * from pinfo')
    r=mycur.fetchall()
    for row in r:
        for col in row:
            l1.append(col,)
    #print(l1)
    a=float(input('Enter pNo For Information Diplay: '))
    b=l1.index(a)
    i=int(b)
    #print(i)
    return(l1[i:i+8])
#======================================================
def Delete():
    a=input('Enter The pNo to Delete The Data')
    sql="DELETE FROM pinfo WHERE pNo={}".format(a)
    mycur.execute(sql)
    mycon.commit()	
#======================================================
def UpdateN():
    a=input('Enter Which column to update')
    b=input('Enter New value')
    c=input('Enter pNo')
    st="UPDATE pinfo SET {}='{}' WHERE pNo={}".format(a,b,c)
    mycur.execute(st)
    mycon.commit()
#=======================================================
def UpdateN1():
    a=input('Enter Which column to update')
    b=input('Enter New value')
    c=input('Enter pNo')
    st="UPDATE ward SET {}={} WHERE pno={}".format(a,b,c)
    mycur.execute(st)
    mycon.commit()
#======================================================
def wardE():
    l2=[]
    q1='select * from ward'
    mycur.execute(q1)
    r=mycur.fetchall()
    for i in r:
        for j in i:
            l2.append(j)
    print(l2)
    a=int(input('enter pNo'))
    k=a;d=0
    c=len(l2)
    for n in range(k*4+1,k*4+4,1):
        d=d+(l2[n])
        print(n)
        return d
    mycon.commit()
#======================================================
def wardIN():
    w1='select * from ward'
    mycur.execute(w1)
    r1=mycur.fetchall()
#======================================================
def wardCHEK():
     a=['OPD','AC','nonAC']
     l1=[]
     q='select * from pinfo'
     mycur.execute(q)
     r=mycur.fetchall()
     for i in r:
        for j in i:
            l1.append(j)
     #print(l1)
     a=int(input('Enter pNo'))
     d=8*a
     c=l1[d-1]     
     return c
#======================================================
def Head():
        print('RASHTRIYE SWAYAM SEVAK HOSPITAL')
        print('Greater Noida Extension')
        print('          201009')
        print('                                      Ph:01124345656 Mobile:09876543214')
        print('                                       E-mail:RSSH@gmail.com')
        print('                                       Date:',date.today())
        return('-------------------------------------------------------')
#======================================================
def view():
        mycur.execute('select * from pinfo')
        records=mycur.fetchall()
        print('pno\tName\tAge\tContact\t\tAddress\tBloodGroup DOA\tWARD')
        for row in records:
                for col in row:
                    print(col,end='\t')
                print()
        mycon.close
#====================================================
def view1():
        mycur.execute('select * from ward')
        records=mycur.fetchall()
        print('pno\tOPD\tAC\tnonAC')
        for row in records:
                for col in row:
                    print(col,end='\t')
                print()
        mycon.close
    

#================MAIN================================
ch='y';
while ch=='y':
    print('WELCOME TO RASHTRIYE SWAYAM SEVAK HOSPITAL')
    print('-------------------------------')
    print('Patient Information-1')
    print('Patient Ward allocation-2')
    print('Billing-3')
    print('------------------------------')
    ai=int(input('Enter Your Choice--'))
    if ai==2:
        print('----------------------------')
        print("Let's allott Ward-1")
        print('Ward updation-2')
        print('view ward table-3')
        bi=int(input('Type in your choice--'))
        if bi==1:
             str1="INSERT INTO ward values({},{},{},{})"
             print('Enter the following Record for Ward ALLOTMENT')
             c1=int(input('pno-'))
             c2=str(input('OPD-'))
             c3=int(input('AC-'))
             c4=int(input('nonAC-'))
             query=str1.format(c1,c2,c3,c4)
             mycur.execute(query)
             mycon.commit()
         
             mycur.execute('select * from ward')
             records=mycur.fetchall()
             print('pno\tOPD\tAC\tnonAC')
             for row in records:
                     for col in row:
                        print(col,end='\t')
                     print()
             mycon.close
        if bi==2:
            q=UpdateN1()
            print(q)
        if bi==3:
            h=view1()
            print(h)
    if ai==1:
        print('To view info 1')
        print('To add info 2')
        print('To update info 3')
        aiii=int(input('Enter your choice'))
        if aiii==1:
            d=view()
            print(d)
        if aiii==2:
            str1="INSERT INTO pinfo values({},'{}',{},{},\t'{}','{}','{}','{}')"
            print('Enter the following Record for PATIENT INFORMATION')
            c1=int(input('pno'))
            c2=str(input('Name'))
            c3=int(input('Age'))
            c4=int(input('contact'))
            c5=str(input('Address'))
            c6=str(input('Bloodgroup'))
            c7=str(input('Date of Appointment'))
            c8=str(input('WARD'))
            query=str1.format(c1,c2,c3,c4,c5,c6,c7,c8)
            mycur.execute(query)
            mycon.commit()

            mycur.execute('select * from pinfo')
            records=mycur.fetchall()
            print('pno Name Age Contact\t\tAddress\tBloodGroup\tDOA\tWARD')
            for row in records:
                    for col in row:
                        print(col,end='\t')
                    print()
            mycon.close
        if aiii==3:
            q=UpdateN()
            print(q)
    if ai==3:
        print("Let's Bill it UP")    
        c1,c2,c3=input('Enter the Day of allocation space seperated yyyy/mm/dd').split()
        FD=date(int(c1),int(c2),int(c3))
        i1,i2,i3=input('Enter the DAY of leaving space seperated yyyy/mm/dd').split()
        SD=date(int(i1),int(i2),int(i3))      
        c=(SD-FD).days
        a=wardCHEK()
        if a=='OPD':        
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('PATIENT INFORMATION')
            print('pNo--',g[0],'                                        Name--',g[1])
            print('Age--',g[2],'                                      Contact--',g[3])
            print('Address--',g[4],'                         BloodGroup--',g[5])
            print('DOA--',g[6],'                               Ward--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('OPD per day-84.74')
            print('AC per day-4,237.28')
            print('nonAC per day-1,694.91')
            print('18% GST on each type of Room/Bed')
            print('----------------------------------------------------------')
            print('Number of days stayed',c)
            print('ward alloted',a)
            q=100*c
            print('OPD per day charges+GST+Hospital surcharges=100')
            print('Your Outstanding Bill is', q)
        if a=='AC':        
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('PATIENT INFORMATION')
            print('pNo--',g[0],'                                        Name--',g[1])
            print('Age--',g[2],'                                      Contact--',g[3])
            print('Address--',g[4],'                       BloodGroup--',g[5])
            print('DOA--',g[6],'                              Ward--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('OPD per day-84.74')
            print('AC per day-4,237.28')
            print('nonAC per day-1,694.91')
            print('18% GST on each type of Room/Bed')
            print('--------------------------------------------------------')
            print('Number of days stayed',c)
            print('ward alloted',a)
            q=5000*c
            print('AC room per day charges+GST+Hospital surcharges=5000')
            print('Your Outstanding Bill is', q)
        if a=='nonAC':       
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('PATIENT INFORMATION')
            print('pNo--',g[0],'                                        Name--',g[1])
            print('Age--',g[2],'                                      Contact--',g[3])
            print('Address--',g[4],'                       BloodGroup--',g[5])
            print('DOA--',g[6],'                              Ward--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('OPD per day-84.74')
            print('AC per day-4,237.28')
            print('nonAC per day-1,694.91')
            print('18% GST on each type of Room/Bed')
            print('-------------------------------------------------------')
            print('Number of days stayed',c)
            print('ward alloted',a)
            q=2000*c
            print('nonAC room per day charges+GST+Hospital surcharges=2000')
            print('Your Outstanding Bill is', q)
        #print(c)
    ch=input('Want to continue(y/n)')
