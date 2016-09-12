import csv
import sqlparse
# import sys

table_list = []
table_found = False
word = '<begin_table>'
lines = open('./metadata.txt', 'r')
for line in lines:
    if table_found:
        table_list.append(line.strip())
        table_found = False
    if word in line:
        table_found = True
lines.close()
print table_list

table_start = False
field_start = False
field_list = []
for i in range(len(table_list)):
    field_list.append([])
start_word = '<begin_table>'
end_word = '<end_table>'
table_number = 0
lines = open('./metadata.txt', 'r')
for line in lines:
    if field_start and (end_word in line) is False:
        field_list[table_number].append(line.strip())
    if end_word in line:
        field_start = False
        table_number = table_number + 1
    if line.strip() in table_list:
        field_start = True
lines.close()
print field_list

table_dict = {}
for i in range(len(table_list)):
    table_dict[table_list[i]] = field_list[i]
print table_dict

table_field = {}
for table in table_list:
    filename = table + '.csv'
    table_field[table] = []
    # print table_dict[table]
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, table_dict[table])
        for row in reader:
            table_field[table].append(row)
            # print row
    # print table_field[table]
for table in table_field:
    print table
    for row in table_field[table]:
        print row

print(sqlparse.format('select * from foo', reindent=True))
