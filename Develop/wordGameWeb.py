#!/usr/bin/python

print "Content-type: text/html\n"

import cgi

form = cgi.FieldStorage()
text_input = form.getvalue('text_input')
y = int(form.getvalue('modchoice'))
    
# a = open('/home/chris/Documents/text_file.txt')
# x = a.read()

x = text_input
    
bucket = []  
result = []

print "<html>"
print "<head>"
print "<style>"
print "body {margin-top: 50px; margin-left: 120px; font-family: Arial;}"
print "textarea {font-size: 22px;}"
print "table {font-size: 22px;}"
print "input {font-size: 26px;}"
print "</style>"
print "</head>"
print "<body>"
print "<table>"
print "<tr>"
print "<td>"
print "<h1> Python word game.</h1>"
print "</td>"
print "</tr>"    
print "<tr>"
print "<td>"
print "This is your modulated text. Show it to someone and ask if they can guess what your original was. I'm working on a Machine Learning example of reforming text so please check back soon."
print "</td>" 
print "</tr>"
print "<tr>"
print "<td>"
print "<textarea readonly rows='"'8'"' cols='"'70'"'>"

for i in x:
    result.append(i)

for k in result:

    if k == ' ': 
        print ' ', 
    elif k == '.':
        print '.',
    elif (ord(k)%2) == y:
        print k,
        bucket.append(k)
    else:
        print "_",
    
for a in x:
    if a == ' ':
        result.remove(a)

print "</textarea>"
print "</td>"
print "</tr>"
print "<tr>"
print "<td>"
print str(len(bucket)) + ' out of ' + str(len(result)) + ' input charaters showing' 
print "</td>"
print "</tr>"  
print "<tr>"
print "<td>"
print "<form action='"'http://51.140.231.162'"'><input type='"'submit'"' value='"'Back'"'/>"
print "</form>"
print "</td>"
print "</tr>"
print "</table>" 
print "</body>"
print "</html>"
















