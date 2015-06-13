# example of a cgi script that will work with both apache and nginx + cherrypy. 
import cgi
import cgitb
cgitb.enable()

def main(env=None):
    # compatability with apache 
    if env is None:
        import os
        env = os.environ
    # get the cgi data
    form = cgi.FieldStorage(environ=env)
    # continue the work of the app
    ...
    # return response (this can't be printed to stdout from here
    # as the response has to be returned by cherrypy. 
    return "was succesful"

# more apache compatibility (and just generally useful)
if __name__ == '__main__':
    # for apache, we can just output to stdout. don't forget the newline
    print() # newline, end of http headers
    print(main())
