Scripts to debug SSL/PKI connections for QGIS core and OpenGeo Explorer plugin
==============================================================================

ssl-conn-qt.[py|bat] scripts
----------------------------

Script launches a Qt-based test Web browser, with connection log output. This
mirrors how QGIS handles connections (though not identically, since QGIS uses a
custom QNetworkAccessManager subclass).

Usage (Linux/Mac):

`python ssl-conn-qt.py`

On WINDOWS: Run the `.bat` script, which to set up the environment (relative to
a Boundless QGIS install), that then launches the `.py` script:

`ssl-conn-qt.bat`

The test browser has the following features:

* `Auth select...` opens a dialog for selection/creation of auth configurations.
* `Auth editor...` opens a dialog for auth database editing of configurations.
* `SSL protocol` allows selection of the Qt-specific-named protocol.
  See: http://qt-project.org/doc/qt-4.8/qssl.html#SslProtocol-enum
* `Reset` will reset the Web page object of the test browser, thereby clearing
  the authentication cache. Useful for clearing accepted auth configs before
  testing another one (otherwise, the config will continue to be used by network
  manager). This is automatically called when selecting/clearing an auth config
  or changing the SSL protocol.

.. warning:: The auth database accessed is the same as used in QGIS. It is NOT a
   temp database.

.. note:: The test browser is very bare-bones. It will generally freeze the GUI
   while it loads pages, and includes only modest support for URL redirection.


ssl-conn-plugin.[py|bat] scripts
--------------------------------

Script tests a modified `httplib2` Python module to allow for specifying the SSL
protocol, as well as default SSL connection handling for the `requests` module
(as a preliminary review towards substituting `requests` over `httplib2` in the
`gsconfig` module).

Usage (Linux/Mac):

`python ssl-conn-plugin.py geoserver_url key_file cert_file ca_file`
  NOTE: key_file should not be passphrase-protected for this test

On WINDOWS: Run the `.bat` script, which to set up the environment (relative to
a Boundless QGIS install), that then launches the `.py` script:

`ssl-conn-plugin.bat geoserver_url key_file cert_file ca_file`

Samples::

python ssl-conn-plugin.py https://localhost:8443/geoserver pki/rod_key.pem pki/rod_cert.pem pki/ca.pem

ssl-conn-plugin.bat https://localhost:8443/geoserver pki/rod_key.pem pki/rod_cert.pem pki/ca.pem



PKI (pki) folder
----------------

These sample PKI components are culled from:
http://suite.opengeo.org/opengeo-docs/geoserver/security/tutorials/cert/index.html

They can be used to test a similarly set up OpenGeo Suite GeoServer.

See also community docs:
http://docs.geoserver.org/latest/en/user/security/tutorials/cert/index.html
