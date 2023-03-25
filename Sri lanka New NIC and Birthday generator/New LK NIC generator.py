nic = input("Enter your Current NIC:") 
newnic=""

# convert old nic to new nic number
# old number has 10 digits including the letter X or V . new number has 12 digits
if len(nic) == 10: #check length of old NIC
 idtype = "Old"
 # Put 19 to the front , put 0 to the 6 th place of the ID and remove the letter X or V
 newnic = "19"+ nic[:6] + "0" + nic[6:9] 
 print("NIC type : " + idtype)
 print("Your New NIC : " + newnic)

if len(nic) == 12: #check legnth of new NIC
 idtype = "New"
 print("NIC type : " + idtype)
 newnic = nic 

#check if new nic has valid length
if len(newnic) == 12 : 
 
#check gender by 5th digit (above 5 is female , Below 5 is male)
 gender_value = int (newnic[4]) 
 
 if gender_value >= 5:
  gender = "Female"
  month_value = int(newnic[4:7]) - 500
 else:
  gender = "Male"
  month_value = int(newnic[4:7])
 print("Gender : "+ gender)

 #get year
 year = newnic[:4]
 
 #get month & day

 #check good year or not
 if float(year) % 4 == 0:
 #good year number of days in a month - 31 29 31 30 31 30 31 31 30 31 30 31
 #Good year number of days to the birth month end from first 1st day of the year - 31 60 91 121 152 182 213 243 274 305 335 366
  djan,dfeb,dmar,dapr,dmay,djun,djul,daug,dsep,doct,dnov,ddec = 31,60,91,121,152,182,213,243,274,305,335,366
 else:
 #normal year number of days in a month - 31 28 31 30 31 30 31 31 30 31 30 31
 #number of days to the birth month end from 1st day of the year -  31 59 90 120 151 181 212 242 273 304 334 365 
  djan,dfeb,dmar,dapr,dmay,djun,djul,daug,dsep,doct,dnov,ddec = 31,59,90,120,151,181,212,242,273,304,334,365

 if 0< month_value <= djan : 
  month ="Jan"
  #get thd day of birth
  date = month_value
 elif djan < month_value <=dfeb:
  month ="Feb"
  date = month_value - djan
 elif dfeb < month_value <=dmar:
  month ="Mar"
  date = month_value - dfeb
 elif dmar < month_value <=dapr:
  month ="Apr"
  date = month_value - dmar
 elif dapr < month_value <=dmay:
  month ="May"
  date = month_value - dapr
 elif dmay < month_value <=djun:
  month ="Jun"
  date = month_value - dmay
 elif  djun < month_value <=djul:
  month ="Jul"
  date = month_value - djun
 elif  djul < month_value <=daug:
  month ="Aug"
  date = month_value - djul
 elif  daug < month_value <=dsep:
  month ="Sep"
  date = month_value - daug
 elif  dsep < month_value <=doct:
  month ="Oct"
  date = month_value - dsep
 elif  doct < month_value <=dnov:
  month ="Nov"
  date = month_value - doct
 elif  dnov < month_value <=ddec:
  month ="Dec"
  date = month_value - dnov

 print("Birthday : " + year +"-"+ month +"-"+str(date))
else:
 print("Wrong NIC Entered")
