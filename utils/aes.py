from Crypto.Cipher import AES# 这里使用pycrypto‎demo库
class AES_ENCRYPT():
    def __init__(self, key):
        self.key = key.encode('utf-8')#一定要使用二进制
        self.mode = AES.MODE_CBC
 
        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        import base64
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
 
        # 这里密钥长度一定注意，对接方给我一个14位的，坑我好久
 
        length = 16                    # 这里只是用于下面取余前面别以为是配置
        count = len(text.encode('utf-8'))     # 这是我上传的主要目的，字符长度不同所以不能直接用，需要先编码转成字节
        print(count)               
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0             #  看看你们对接是满16的时候加上16还是0.这里注意
        text1 = text + ('\0' * add)    # 其它语言nopadding时，python还是需要‘\0’或'\x00'这里注意与其它语言对接注意
        text1=text1.encode('utf-8')
        self.ciphertext = cryptor.encrypt(text1)          # 这里就是已经加密了
        cryptedStr = str(base64.b64encode(self.ciphertext),encoding='utf-8')
 
        return cryptedStr            # 我们的加密是到这里就可以了，这里跟我们对接平台的加密方式有关
 
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
 
        print('self.ciphertext:',self.ciphertext)
        # print(len(cryptedStr.strip('\0')))     # 解密后，去掉补足的空格用strip() 去掉，注意python不是用‘’
        # b2a_hex(self.ciphertext)
        # print(cryptedStr)
        # return b2a_hex(self.ciphertext)
      
 
 
    def decrypt(self, text):
        import base64, json
        base_text = base64.b64decode(text)         # 没有用到16进制转码的我们需要base64 ,这个地方小坑
        # text = b2a_hex(base_text)    # 如果你们需要转码则用这个方法
        # new_text = a2b_hex(text)
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(base_text)
        ne = plain_text.decode('utf-8').rstrip('\0')
        # print(json.loads(ne))      #我们传输使用的json所以我直接写到了这里，对你们应该没用
        return ne
 
 
if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT('lsakdalfjsadfn45')  # 初始化密钥
    # text = '<Tyhh>064302241150429</Tyhh><Tlb>1</Tlb>'
    text = 'aidd23.测试文本'#.encode("utf-8")
    sign_data = aes_encrypt.encrypt(text)
    print(sign_data)
    data = aes_encrypt.decrypt(sign_data )
    print(data )
