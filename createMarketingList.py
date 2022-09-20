# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.


import csv

# open the vendorlist file
infile = open('VendorList.csv','r')

# create a csv object from the file object
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)
#vendorlines = infile.readlines()
# create an output file
outfile = open('marketinglistFinal.csv','w')



# create an empty dictionary
marketing_dict = {}


# iterate through the csv object
for rec in csvfile:
    marketing_dict['full_name']= ([rec[1]],[rec[2]])
    email = [rec[4]]
    phone = [rec[5]]
    #print(full_name)
    #print(email)
    #print(phone)

    # add the key-value pair to the dictionary
    #if rec in marketing_dict:
    marketing_dict={'full_name':{'email': email,'phone' :phone}}
      

# print the dictionary after the loop is finished
    print(marketing_dict)

# iternate through the dictionary and write to the output file

    outfile.write(str(marketing_dict)+'\n')


# close your output file
outfile.close
