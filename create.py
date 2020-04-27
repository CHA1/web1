#!python
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
form=cgi.FieldStorage()
if 'id' in form:
    title=pageId=form["id"].value
    description = open('data/'+pageId, 'r').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
else:
    title=pageId="Welcome"
    description = "Hello, web"

print('''<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h2><a href="index.py">WEB<h2>
    <ul>
       {listStr} 
    </ul>
<a href = "create.py">create</a>
<form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
</form>
</body>
</html>'''.format(title=title,
                  desc=description,
                  listStr=view.getList())
      )