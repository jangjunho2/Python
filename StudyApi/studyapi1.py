import API_KEYS as KEY
import requests
import xmltodict
import json

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
params = {'serviceKey': KEY.apartDealApiKey, 'pageNo': '1',
          'numOfRows': '10', 'LAWD_CD': '11110', 'DEAL_YMD': '201512'}

response = requests.get(url, params=params)
contents = response.text

dict_data = xmltodict.parse(contents)  # XML 데이터를 딕셔너리로 변환
json_data = json.dumps(dict_data, indent=2,
                       ensure_ascii=False)  # 딕셔너리를 JSON 형식으로 변환

print(json_data)
