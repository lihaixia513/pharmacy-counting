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
#===========read the file
with open(fname) as f:
    first_char = f.read(1) 
    if not first_char or first_char == '\n': 
        print('check the file, the file might be empty')
    else:
        next(f) #start from the next line, the second line
        for line in csv.reader(f,quotechar='"', delimiter=',', skipinitialspace=True):   
            if len(line) == 5:
                prescriber_last_name,prescriber_first_name,drug_name,drug_cost = line[1:5]
                name = prescriber_last_name + " " + prescriber_first_name 
                if drug_name in d:
                    total_cost = d[drug_name][1] + float(drug_cost) #d[drug_name][1] is the first value related to the key drug_name
                    name_l = d[drug_name][2] 
                    if name in name_l: #check if the name is in the name list name_l or not, if it is, do not increase the num_prescriber
                        num_prescriber = d[drug_name][0]
                    else:
                        num_prescriber = d[drug_name][0] + 1
                        name_l.append(name) #update the name list name_l
                    d[drug_name] = [num_prescriber, total_cost, name_l] #update the dictionary
                else:
                    d[drug_name] = [1, float(drug_cost), [name]] 
            else:
                pass
#=============sort the results 
for keys, values in d.items():  
    out = (keys, values[0], values[1])
    out_l.append(out)
sort_l = sorted(out_l,key=lambda x:(-x[2],x[0])) #-x[2] means the negative valus of total_cost, descend it, x[0] ascends based on the first chracter of the drug_name
#=============write the results in the txt file
fout = open(output_file, 'w') 
fout.write('drug_name,num_prescriber,total_cost\n') 
for items in sort_l: 
    fout.write('%s,%d,%.0f\n' % (items[0],items[1],round(items[2],0)))
fout.close()
