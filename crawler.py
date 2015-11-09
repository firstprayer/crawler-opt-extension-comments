
import requests
import simplejson as json

def main():
	fs = open('data.txt', 'w')
	po = 0
	while True:
		#payload = '7|0|18|http://www.regulations.gov/Regs/|2C25B267A99A93A13416C63BF89CA32C|com.gwtplatform.dispatch.rpc.shared.DispatchService|execute|java.lang.String/2004016611|com.gwtplatform.dispatch.rpc.shared.Action|6tAGq535PEN3pRM35g0tIRyr|gov.egov.erule.regs.shared.dispatch.LoadSearchResultsAction/3614113675|gov.regulations.common.models.SearchQueryModel/1665573539|java.util.HashSet/3273092938|ICEB-2015-0002||java.util.ArrayList/4159755760|gov.regulations.common.models.DocumentType/3342328439|java.lang.Boolean/476441737|ICEB-2015-0002-0011|gov.regulations.common.models.DataFetchSettings/4209605978|java.lang.Integer/3438268394|postedDate|DESC|1|2|3|4|2|5|6|7|8|9|0|0|10|0|11|12|12|13|0|13|1|14|5|0|0|15|0|0|12|13|0|16|3|12|17|18|25|18|{PO}|12|12|-7|15|1|'
		payload = '7|0|20|http://www.regulations.gov/Regs/|E6F50CFBCCBC536D17649C8BEBE8D36B|com.gwtplatform.dispatch.rpc.shared.DispatchService|execute|java.lang.String/2004016611|com.gwtplatform.dispatch.rpc.shared.Action|citRtw5cTFlmmjD4yPVr7PRk|gov.egov.erule.regs.shared.dispatch.LoadSearchResultsAction/3614113675|gov.regulations.common.models.SearchQueryModel/1665573539|java.util.HashSet/3273092938|ICEB-2015-0002||java.util.ArrayList/4159755760|gov.regulations.common.models.DocumentType/3342328439|java.lang.Boolean/476441737|ICEB-2015-0002-0011|gov.regulations.common.models.DataFetchSettings/4209605978|java.lang.Integer/3438268394|postedDate|ASC|1|2|3|4|2|5|6|7|8|9|0|0|10|0|11|12|12|13|0|13|1|14|5|0|0|15|0|0|12|13|0|16|3|12|17|18|25|18|{PO}|19|20|-7|15|1|'
		payload = payload.replace('{PO}', str(po))

		cookie_string = '_gat=1; JSESSIONID=6tAGq535PEN3pRM35g0tIRyr; _ga=GA1.2.1171580541.1446740999; fsr.s.session=%7B%22v%22%3A1%2C%22rid%22%3A%22de358f8-93999825-bb10-b02a-70d90%22%2C%22to%22%3A3%2C%22c%22%3A%22http%3A%2F%2Fwww.regulations.gov%2F%23!docketBrowser%3Brpp%3D25%3Bpo%3D25%3Bdct%3DPS%3BD%3DICEB-2015-0002%3BrefD%3DICEB-2015-0002-0011%22%2C%22pv%22%3A2%2C%22lc%22%3A%7B%22d0%22%3A%7B%22v%22%3A2%2C%22s%22%3Afalse%7D%7D%2C%22cd%22%3A0%2C%22f%22%3A1446741003343%7D'
		cookies = {}
		for pair in cookie_string.split(';'):
			[key, value] = pair.split('=')
			cookies[key] = value

		headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
			'content-type': 'text/x-gwt-rpc; charset=UTF-8',
			'X-GWT-Permutation': '0D852FF1ACA93B2BC78AEA5C45EC518B',
			'X-NewRelic-ID': 'UAQEUV5bGwcDU1NbDwM=',
			'X-GWT-Module-Base': 'http://www.regulations.gov/Regs/'
		}
		cnt = 0
		while True:
			try:
				res = requests.post('http://www.regulations.gov/dispatch/LoadSearchResults', \
					headers=headers, data=payload, cookies=cookies)
				break
			except Exception as e:
				if cnt < 3:
					cnt += 1
					continue
				else:
					raise e

		if res.status_code != 200:
			print res
			continue

		jsontext = res.text[4: ]
		start_idx = jsontext.find('["gov.egov.erule.regs.shared.dispatch.LoadSearchResultsResult')
		end_idx = jsontext.rfind('"]')

		if end_idx <= start_idx or start_idx < 0 or end_idx < 0:
			print "Invalid response"

		jsontext = jsontext[start_idx: end_idx + 2].replace('\\x', "\\u00")
		texts = json.loads(jsontext)
		if len(texts) <= 11:
			# Empty response.
			break
		fs.write(json.dumps(texts) + '\n')

		po += 25
		if po % 100 == 0:
			print po

		# if po > 10000:
		# 	break

	fs.close()

if __name__ == '__main__':
	main()
