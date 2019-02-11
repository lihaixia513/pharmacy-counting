#!/usr/bin/env python3
import sys
import csv
try:
    sys.argv[1]
except:
    print("no input file specified")
    sys.exit(1)
else:
    fname = sys.argv[1]
    try:  
        sys.argv[2]
    except: 
        output_file = 'top_cost_drug.txt'
    else:
        output_file = sys.argv[2]    
d = dict() 
out_l = list() 
i = 0
#===========read the file
with open(fname) as f:
    first_char = f.read(1) #read the charactor
    if not first_char or first_char == '\n': #if the first charactor does not exist or empty line
        print('check the file, the file might be empty')
    else: 
        next(f) #start from the next line, the second line
        for line in csv.reader(f,quotechar='"', delimiter=',', skipinitialspace=True):   #transfer every line through the file
            prescriber_last_name,prescriber_first_name,drug_name,drug_cost = line[1:5] #assign them with easily read name
            name = prescriber_last_name + " " + prescriber_first_name #name is last name space first name
            if drug_name in d: #check if the drug name is in the dictionary d or not, drug_name is the key, only can check the key, because the key is unique
                total_cost = d[drug_name][1] + float(drug_cost) #d[drug_name][1] is the first value related to the key drug_name
                name_l = d[drug_name][2] #the second value related to the key drug_name related to dictionary d
                if name in name_l: #check if the name is in the name list name_l or not, if it is, do not increase the num_prescriber
                    num_prescriber = d[drug_name][0] 
                else:
                    num_prescriber = d[drug_name][0] + 1 
                    name_l.append(name) #update the name list name_l
                d[drug_name] = [num_prescriber, total_cost, name_l] #update the dictionary
            else:
                d[drug_name] = [1, float(drug_cost), [name]] #if the drug_name appears the first time, num_prescriber is 1
#=============sort the results based on 
for keys, values in d.items():  #go through the keys values in the dictionary items
    new = (keys, values[0], values[1]) #new is a list, keys, values[0], values[1] 
    out_l.append(new) #update the list out_l
sort_l = sorted(out_l,key=lambda x:(-x[2],x[0])) #sort it -x[2] meas the negative valus of total_cost, so ascending -x[2] means desceding it, x[0] asceding based on the first chracter of the drug_name
#=============write the result in the txt file
fout = open(output_file, 'w') #write the results in the file top_cost_drug.txt
fout.write('drug_name,num_prescriber,total_cost\n') #the first line in this file
for items in sort_l: #transfer through the list and write it in the file
    fout.write('%s,%d,%.0f\n' % (items[0],items[1],items[2]))
fout.close()        


