import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),'.'))

activate_this = os.path.join(os.path.abspath(os.path.dirname(__file__)),'.','env','bin','activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from jousse_blog import app as application
