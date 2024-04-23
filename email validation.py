email = input(" Enter your email : ")  #g@g.in , shuvamsaha2000@gmail.com
k,j,d= 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if "@" in (email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):    # (^) operator is used  as if the result is true or false in both cases the result will be false and true
               for i in email:
                   if i==i.isspace():  # for conditon 5
                      k=1
                   elif i.isalpha():
                      if i==i.upper():  # for condtion 5
                        j=1
                   elif i.isdigit():    # for condtion 5
                       continue
                   elif i=="_" or i=="." or i=="@":     #  for conditon 5
                       continue
                   else:
                       d=1
               if k==1 or j==1 or d==1:
                    print("Wrong Email (5)")
               else:
                print("The Email is Right")
            else:
                print("Wrong email (4)")
        else:
            print("Wrong Email (3)")
    else:
        print("Wrong Email (2)")
else:
    print("The email is wrong (1)")
