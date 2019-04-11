from ..Common import HOST,EID
from ..AccessToken import AccessToken
import json
import random
import requests
'''
    云之家人员操作接口调用
'''
class ModifyPerson:
    
    '''
        分页查询全部的人员
        eid：圈子号
        begin：开始位置
        count：数量
    '''
    def getall(self,eid = EID,begin = 0, count = 100):
        data = {'eid':eid,'begin':begin,'count':count}
        param = {'nonce':str(random.randint(100,10000)),'eid':eid,'data':json.dumps(data)}
        url = HOST+'gateway/openimport/open/person/getall?accessToken='+ AccessToken().getAccessToken('resGroupSecret')  #理论上accesstoken应该保存备用
        response = requests.post(url,data=param)
        print(response.text)

