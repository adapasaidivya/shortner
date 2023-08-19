import time
username = {"divya": '12345',"pavan":'6789',"praveen":'847584'}
list_of_trains ={"chennai_express":12345,"tripathi_express":6789,"east cost_express":3847358}
user_name=input ("enter your name:")
password_train=input("enter your password:")
if user_name in username:
    if password_train in username[user_name]:
        print("yes valid")
        for k,v in list_of_trains.items():
            print("trainname",k,"trainnum:",v)
ticketrate={"chennai_express":'230',"tripathi_express":'340',"east cost_express":'245'}
select=input("select train:")
for t,r in ticketrate.items():
    print("select_train:",t, "ticketrates",r)
tra = input("enter your required train:")
pas=int(input("enter number of passengers:"))
if tra in ticketrate:
    print("ticket_rate:",ticketrate[tra])
    print("totalprice;",int(ticketrate[tra]*pas))
seatselect=("front_coner:" ,"front_middle:","last:")
select=input("select_seats:")
print("yes, your ticket is confirmed")    