import httplib
import urllib2
import urllib
import json

SECRET= u'6Lcz2wATAAAAAGWb7nobKto_W9I-0Q804V27Wd5m'

def verify_recaptcha(secret, response, remoteip):
	conn = httplib.HTTPSConnection('www.google.com')
	request_url = "/recaptcha/api/siteverify?"\
				"secret=%s&response=%s&remoteip=%s"%(secret, response, remoteip)
	print request_url
	conn.request("GET", request_url)
	resp = conn.getresponse()
	#print resp.status, resp.reason
	data = resp.read()
	output = json.loads(data)
	print output
	return output['success']


def verify_recaptcha3 (recaptcha_secret,
			recaptcha_response):

	def encode_if_necessary(s):
		if isinstance(s, unicode):
			return s.encode('utf-8')
		return s

	params = urllib.urlencode ({
			'secret': encode_if_necessary(recaptcha_secret),
			'response' :  encode_if_necessary(recaptcha_response),
			})
	#6Lcz2wATAAAAAGWb7nobKto_W9I-0Q804V27Wd5m
	request = urllib2.Request (
		#url = "https://%s" % "www.google.com/recaptcha/api/siteverify",
		url = "http://localhost:8100",
		data = params,
		method = "GET",
		headers = {
			"Content-type": "application/x-www-form-urlencoded",
			}
		)
	
	httpresp = urllib2.urlopen (request)
	print httpresp

	return_values = httpresp.read ().splitlines ();
	httpresp.close();

	print return_values
	



def main():



	a = {}
	a['1'] = 1
	a['dd'] = 23

	print unicode(a)

	print verify_recaptcha3(SECRET, u'03AHJ_Vut9_dovF5MUtE7y7AvOToArXT7UCKeoCXBv2xtkNo5QLxOhtvwC3pIWgpVSSW9s6lwstVbJAiKZtorem3Vp-CGcIRv5QXLZ3yCYCfo6q3Pt68nh75i4K2MwWRtZuCNVLj0TtzoSihydi10vX0YSIx5JmgfiwBsYJBSvHUPIQB8u_lC6TVRyzaH1NLnSA9kEdOJb-FScxrwevCKlJ5WLfR6i-IfTZ1_oEzP-qRmC_Ozjkv7XoX_SNv84qPijIollrShF3EMZSukfY61nTOThsqh4-0PK5UtccKfDzvOuPHNoYtN43osZWN7MPDh7E6NfRTIPgq-8MWCncl-1F1f33UbqNPLMtAW_F8R2_WN8Bn_wj7ARnM48oPi-bDL77C1KnW3NMCj8')

if __name__ == "__main__":
	main()


