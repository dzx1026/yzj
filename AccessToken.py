import requests
import Common
import time
import json

class AccessToken():
    '''
        获取accesstoken授权
        scope：授权级别
    '''
    def getAccessToken(self,scope):
        
        if scope=='app':
            data={'appId':Common.APPID,'secret':Common.APPID_SECRET,'scope':scope}
        elif scope == 'team':
            data={'appId':Common.APPID,'eid':Common.EID,'secret':Common.APPID_SECRET,'scope':scope}
        elif scope == 'resGroupSecret':
            data={'eid':Common.EID,'secret':Common.MODIFYPERSON_SECRET,'scope':scope}
        else:
            print('输入的授权级别有误')
            return None
        timestamp = int(round(time.time())*1000)
        data['timestamp']=timestamp

        response = requests.post(Common.HOST+'gateway/oauth2/token/getAccessToken',json=data)  #dict内部自动序列化为json
        result=response.json()
        if response.status_code == 200 and result['success']:
            return result['data']['accessToken']
        else:
            print('接口调用失败：',response.text)
            



if __name__ == '__main__':
    print(AccessToken().getAccessToken('resGroupSecret'))