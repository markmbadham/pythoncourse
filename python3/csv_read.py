import csv
def read_csv(filename,field_mappings):
   with open(filename) as file:
       csv_headings=csv.reader(file).__next__()

       table_fields = []
       for key in csv_headings:
           val = field_mappings.get(key)
           print(key,val)
           table_fields.append(val)
       print(table_fields)
       contents=csv.DictReader(file,fieldnames=table_fields)
       for row in contents:
           print(row)
           row.pop(None)
           print(row)

field_mapping={"ID":"ProgramID","Name":"TaskName","Duration":"Duration","Start":"Start",
         "Finish":"Finish","Total Slack":"Slack"}
read_csv("/home/mark/Documents/Projects/PMsoftware/test.csv",field_mapping)

