def leap_year(y):
    if(y%100==0 and y%400==0):
        return True
    if(y%100==0 and y%400!=0):
        return False
    if(y%4==0):
        return True
    else:
        return False

    
def first_day_of_year(y):
    if y>=2000:
        sum=1
        for i in range(2001,y):
            x= leap_year(i)
            if(x==True):
                sum=sum+2
            else:
                sum=sum+1
        l=sum%7
        return l
    
    if(y<2000):
        sum=0
        for i in range(1999,y-1,-1):
            if leap_year(i)==True:
                sum=sum-2
            else:
                sum=sum-1

        if sum<-6:
            sum=sum%7
        l=sum
        return (l+7)-1
    

def length_of_month(m,y):
    i=m
    if(i==1):
        return 31
    if(i==2):
            if leap_year(y):
                return 29
            else:
                return 28
    if(i==3):
            return 31    
    if(i==4):
            return 30
    if(i==5):
            return 31
    if(i==6):
            return 30
    if(i==7):
            return 31
    if(i==8):
            return 31
    if(i==9):
            return 30
    if(i==10):
            return 31
    if(i==11):
            return 30
    if(i==12):
            return 31


def first_day_of_month(y,m):
    sum=first_day_of_year(y)
    for i in range(m):
        if(i==1):
            sum=sum+31
        if(i==2):
            if leap_year(y):
                sum=sum+29
            else:
                sum=sum+28
        if(i==3):
            sum=sum+31    
        if(i==4):
            sum=sum+30
        if(i==5):
            sum=sum+31
        if(i==6):
            sum=sum+30
        if(i==7):
            sum=sum+31    
        if(i==8):
            sum=sum+31
        if(i==9):
            sum=sum+30
        if(i==10):
            sum=sum+31
        if(i==11):
            sum=sum+30
        if(i==12):
            sum=sum+31
    return sum%7


def month_calender(a,b):
    x=first_day_of_month(a,b)
    str='{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}'
    str2=str[:]
    print(str2.format('Sat','Sun','Mon','Tue','Wed','Thu','Fri'))

    m=-x-1
    list=['','','','','','','']
    length=length_of_month(b,a)
    while m<length:
        list=['','','','','','','']
        for i in range(0,7):
            m=m+1
            if(m>0):
                list[i]=m
            
            if(m>=length):
                break
        print(str.format(list[0],list[1],list[2],list[3],list[4],list[5],list[6]))


def year_calender(y):
    year_name='{0:>19}'
    print(year_name.format('Year :'),'[',y,']')
    print()
    print()
    print()
    month_name='{0:>20}'
    for i in range(1,13):
        if(i==1):
            print(month_name.format('January'),',',y)
        if(i==2):
            print(month_name.format('February'),',',y)
        if(i==3):
            print(month_name.format('March'),',',y)
        if(i==4):
            print(month_name.format('April'),',',y)
        if(i==5):
            print(month_name.format('May'),',',y)
        if(i==6):
            print(month_name.format('June'),',',y)
        if(i==7):
            print(month_name.format('July'),',',y)
        if(i==8):
            print(month_name.format('August'),',',y)
        if(i==9):
            print(month_name.format('September'),',',y)
        if(i==10):
            print(month_name.format('October'),',',y)
        if(i==11):
            print(month_name.format('November'),',',y)
        if(i==12):
            print(month_name.format('December'),',',y)
        print()

        month_calender(y,i)
        print()
        print()

    
def day(d,m,y):
    sum=first_day_of_year(y)
    for i in range(1,m):
        if(i==1):
            sum=sum+31
        if(i==2):
            if leap_year(y):
                sum=sum+29
            else:
                sum=sum+28
        if(i==3):
            sum=sum+31    
        if(i==4):
            sum=sum+30
        if(i==5):
            sum=sum+31
        if(i==6):
            sum=sum+30
        if(i==7):
            sum=sum+31    
        if(i==8):
            sum=sum+31
        if(i==9):
            sum=sum+30
        if(i==10):
            sum=sum+31
        if(i==11):
            sum=sum+30
        if(i==12):
            sum=sum+31

    sum=sum+d
    return sum%7-1



d_m_y=str(input('Please Enter(DD-MM-YYYY):'))
z=d_m_y.split('-')


if(len(z)==3):
    if(int(z[0])>0 and int(z[0])<=31 and int(z[1])>0 and int(z[1])<=12 and int(z[2])>0):
        c=day(int(z[0]),int(z[1]),int(z[2]))+1
        print('The date you entered is: ',end='')
        if(c==0):
            print('Saturday')
        if(c==1):
            print('Sunday')
        if(c==2):
            print('Monday')
        if(c==3):
            print('Tuesday')
        if(c==4):
            print('Wednesday')
        if(c==5):
            print('Thursday')
        if(c==6):
            print('Friday')
    else:
        print('Sorry. Incorrect input. Try again.')

        
if(len(z)==2):
    if(int(z[0])>0 and int(z[0])<=12 and int(z[1])>0):
        print()
        month_name='{0:>20}'
        if(int(z[0])==1):
            print(month_name.format('January'),',',int(z[1]))
        if(int(z[0])==2):
            print(month_name.format('February'),',',int(z[1]))
        if(int(z[0])==3):
            print(month_name.format('March'),',',int(z[1]))
        if(int(z[0])==4):
            print(month_name.format('April'),',',int(z[1]))
        if(int(z[0])==5):
            print(month_name.format('May'),',',int(z[1]))
        if(int(z[0])==6):
            print(month_name.format('June'),',',int(z[1]))
        if(int(z[0])==7):
            print(month_name.format('July'),',',int(z[1]))
        if(int(z[0])==8):
            print(month_name.format('August'),',',int(z[1]))
        if(int(z[0])==9):
            print(month_name.format('September'),',',int(z[1]))
        if(int(z[0])==10):
            print(month_name.format('October'),',',int(z[1]))
        if(int(z[0])==11):
            print(month_name.format('November'),',',int(z[1]))
        if(int(z[0])==12):
            print(month_name.format('December'),',',int(z[1]))
        print()
        month_calender(int(z[1]),int(z[0]))
    else:
        print('Sorry. Incorrect input. Try again.')

   
if(len(z)==1):
    if(int(z[0])>0):
        print()
        year_calender(int(z[0]))
    else:
        print('Sorry. Incorrect input. Try again.')







