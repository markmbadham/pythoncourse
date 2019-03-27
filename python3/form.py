#!/usr/bin/env python
from wsgiref.simple_server import make_server
from cgi import escape, parse_qs

html = '''
<!DOCTYPE html>
<html>
   <head>
      <title>form</title>
    </head>
    <body>
	<form>
	   <table>
	       <tr>
                  <td>
                     <label for="name">Name</label>
                  </td> 
	          <td>
               <input type="text" name="name" id="nameinput" 
		value="%(name)s" onfocus="this.value=''">
                 </td>
               </tr>
	       <tr>
                  <td><label for="surname">Surname</label></td> 
                  <td><input type="text" name="surname" value="%(surname)s"></td>
              </tr>
              <tr>
		  <td>Things I am Bringing</td>
		  <td>
                      <input type="checkbox" name="ownpc" value="Y" checked> Own PC<br>
                      <input type="checkbox" name="book" value="Y"> Book<br>
                      <input type="checkbox" name="pen" value="Y"> Pen<br>
		  </td>
              </tr>
              <tr>
		  <td>Sex</td>
		  <td>
                      <input type="radio" name="sex" value="male" checked>Male<br>
                      <input type="radio" name="sex" value="female">Female<br>
		  </td>
	      </tr>
	      <tr>
		  <td>Comment</td>
		  <td>
		      <textarea name="comment" rows="5" cols="20"></textarea>
	      </tr>
	      <tr>
		  <td>Country</td>
		  <td>
		      <select multiple name="country">
              %(options)s
		      </select>
	      </tr>
	      <tr>
                  <td colspan="2" style="text-align:center">
			<input type="submit" value="Send">
		  </td>
	      </tr>
          </table>
	</form>
        %(response)s
    </body>
</html>
'''

def simple_app(environ, start_response):
    response = ''
    options = ''
    opts_dct = {
			  '':'Choose One', 
			  "ZA":'South Africa',
			  "BW":'Botswana',
			  "NA":'Namibia',
			  "ZW":'Zimbabwe'
    }
    for key in opts_dct:
        options += '<option name="%s">%s</option>' % (key, opts_dct[key])

    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    fields = parse_qs(environ['QUERY_STRING'])

    if fields:
        for field in fields:
            response += "<p style='color:red'>%s = %s </p>" % (field, fields[field])

    ret = (html % 
       {'name':'Type in your name',
       'surname':'Bloggs',
       'options':options,
       'response':response}
       ).splitlines(True)
    return ret
httpd = make_server('', 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()
