from django.http import HttpResponse


def pokeserverv7(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        html = '''
        <response>
        <message>ok</message>
        </response>
        '''
        response = HttpResponse(html, content_type="text/xml;charset=UTF-8")
        response['comp_version'] = '9.10.0'
        response['server_version'] = '9.0.0'
        response['comp_status'] = '0'
        response['permitNum'] = 100000
        response['msgSize'] = 100000
        response['storeSpace'] = 100000
        response['permitSpace'] = 100000
        response['realName'] = 'linsl0001'
        response['rightcode'] = '20110360'
    else:
        html = '''<html><head><title>Apache Tomcat/7.0.52 (Ubuntu) - Error report</title><style><!--H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}HR {color : #525D76;}--></style> </head><body><h1>HTTP Status 401 - An Authentication object was not found in the SecurityContext</h1><HR size="1" noshade="noshade"><p><b>type</b> Status report</p><p><b>message</b> <u>An Authentication object was not found in the SecurityContext</u></p><p><b>description</b> <u>This request requires HTTP authentication.</u></p><HR size="1" noshade="noshade"><h3>Apache Tomcat/7.0.52 (Ubuntu)</h3></body></html>'''
        response = HttpResponse(html, status=401)
        response['WWW-Authenticate'] = 'Digest realm="MetaCamp Server", qop="auth", nonce="MTUxNTIyMjU1MjA0ODo5Mjc5NjdjODM4MjM2ZjA2N2U5NGE3OTU3MTE2NDg4Mg=="'
    return response


def brower(request):
    html =  """
<html>
	<head><title>MetaCamp Home</title></head>
	<script>
		function redirect() {
			window.location="http://www.gooseeker.com";
		}
	</script>

	<body onload="redirect()">
		<h2>Hello</h2>
		<p>The page should be redirected to another page. If not, there must be something wrong</p>
	</body>
</html>
"""
    return HttpResponse(html)



