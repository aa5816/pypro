#takes customer info of 3 customers and prints it
i=0
while (i<3):
  print("for customer :", i+1)
  cust_id=int(input("enter 4 digit the customer id"))
  bill_id=int(input("enter 3 digit bill id"))
  if_minor=bool(input("is it a minor enter False or True"))
  cust_name=str(input("enter customer name"))
  bill_amt=float(input("enter bill amount"))
  i+=1

while (i>0):
  print ("customerc info is",cust_id,'\n',bill_id,'\n',if_minor,'\n',cust_name,'\n',bill_amt,'\n')
  i-=1

  
