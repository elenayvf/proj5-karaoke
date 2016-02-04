import flask

from flask import request  # Data from a submitted form
from flask import url_for
from flask import render_template
import logging

app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.COOKIE_KEY  # Should allow using session variables


@app.route("/")
def run():
    flask.session["res"]= []
    flask.session["lat"]=[]
    flask.session["lon"]=[]
    flask.session["length"] = 0
    poi = open('poi.txt','r')
	
    for line in poi:
        info_list = line.strip().split(',')
        res =info_list[0]
        lat = info_list[1]
        lon = info_list[2]
        flask.session["res"].append(res)
        flask.session["lat"].append(lat)
        flask.session["lon"].append(lon)
        flask.session["length"] += 1
        flask.session.modified = True
    
    return flask.render_template('mapping.html')
		

if __name__ == "__main__":
    # Standalone. 
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    #FIXME:  Debug cgi interface 
    app.debug=False
