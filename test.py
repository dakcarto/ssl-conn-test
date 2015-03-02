import os
import sys
import site
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), '/libs')))
import httplib2
import requests
import ssl

'''
Usage:

python test.py [geoserver_catalog_url] [key_file] [cert_file] [ca_cert file]
'''
if __name__ == "__main__":
	key = sys.argv[2]
	cert = sys.argv[3]
	ca_certs = sys.argv[4]
	url = sys.argv[1] + "/rest/workspaces"

	#Try connecting using patched httplib2 library
	http = httplib2.Http(ca_certs = ca_certs, disable_ssl_certificate_validation = False, ssl_protocol = ssl.PROTOCOL_TLSv1)
	http.add_certificate(key, cert, '')
	response, content = http.request(url, "GET")
	if response.status == 200:
		print "Connection suceeded using httplib2"
		print content
	else:
		print "Connection failed using httlib2"
		print (content or response.status)

	#Try connecting using requests library
	response = requests.get(url, cert=(cert,key), verify=ca_certs)
	try:
		response.raise_for_status()
		print "Connection suceeded using requests"
	except:
		print "Connection failed using request"
	finally:
		print response.text