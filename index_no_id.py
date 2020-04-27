#!python
print("content-type: text/html; charset=utf-8\n")
print()
import cgi
form=cgi.FieldStorage()

pageId="Welcome"

print('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index_no_id.py">WEB<h1>
    <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
<h2>{title}</h2>
<p> The World Wide Web(abbreviated WWW or Web) is an information
space where documents and other web resources are indetified
by Uniform Resource Locators(URLs), interlinked by hypertext
links, and ca be accessed via the Internet.[1] English scientist
Tim Berners-Lee invented the World Wide Web in 1989. He wrote 
the first web browsercomputer program in 1990 while employed at CERN 
in Switzerland.[2][3]The Web browser was released outside of CERN
in 1991, first to other research institutions starting
in Junuary 1991 and to the general public on the Internet 
in August 1991.
</body>
</html>'''.format(title=pageId))