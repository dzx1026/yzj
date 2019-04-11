from Common import HOST,EID
import requests
'''
报表秀秀接口调用
'''
class Report():
    
    def getAdminTableInfos(self):
        response = requests.post(HOST+'gateway/open/linkerp/ReportDataTableapi/getAdminTableInfos',data={'eid':EID})
        print(response.text)


