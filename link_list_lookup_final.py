import csv
f1 = open ("link_list_lookup.csv","r") # open input file for reading 
users_dict = {}
with open('link_list_lookup_final.csv', 'wb') as f: # output csv file
    writer = csv.writer(f)
    with open('link_list_lookup.csv','r') as csvfile: # input csv file
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            writer.writerow([row['file'],row['movie_id'].split('.0')[0]])
            users_dict.update(row)
            
    print users_dict

f1.close()
