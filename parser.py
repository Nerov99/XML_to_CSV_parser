#
# Script for parsing xml to csv with using Regular Expressions
#
import re
import csv
with open('sample.xml', 'r') as file_xml:
    data = file_xml.read().replace('\n', '')
csv_fields = ['Name','Phone','Email','City','Description','ID', 'Salary'] # tags to parse
# (?P<name>...) saves data into variable "name" when .+? determines the data. 
# '?' means that its gonna match until the first occurence of what`s coming next
xml_data = re.findall(r"<Name>(?P<name>.+?)</Name>.{0,5}?"
                      r"<Phone>(?P<phone>.+?)</Phone>.{0,5}?"
                      r"<Email>(?P<email>.+?)</Email>.{0,5}?"
                      r"<City>(?P<city>.+?)</City>.{0,5}?"
                      r"<Description>(?P<description>.+?)</Description>.{0,5}?"
                      r"<ID>(?P<id>\d+?)</ID>.{0,5}?"
                      r"<Salary>(?P<salary>\d+?)</Salary>"
                      , data)
with open('csv_file', 'w') as file_csv:
    write = csv.writer(file_csv)
    write.writerow(csv_fields)
    write.writerows(xml_data)
# used to test script
print(xml_data)
