"""http://103.6.80.113:3333/
http://39.116.31.133:3333/

39.116.31.167
39.116.31.207

103.6.80.77
103.6.80.33

36, 38, 57, 58 """

import urllib.request
from bs4 import BeautifulSoup as bs
import struct
import time

class Extract:
    def __init__(self):
        self.dataToSend = b''
        self.myName = input('Enter your nickname: ')
        while len(self.myName) > 11:
            print("Please enter less than 12 characters: ")
            self.myName = input('Enter your nickname: ')
            if len(self.myName) < 12:
                break
        self.myName = self.myName + ' '

    def findGPU(self):
        my_name_byte = bytes(self.myName, encoding='utf-8')
        #url에 피닉스 마이너가 송출하는 주소를 담아 전달하여 data에 채굴 정보를 담습니다.
        url = urllib.request.urlopen('http://127.0.0.1:3333')
        data = url.read()
        #뷰티풀솝에 전달하여 텍스트를 추출합니다.
        soup = bs(data, "html.parser")
        text = soup.get_text()
        #리스트로 변경하여 필요한 정보를 추출합니다.
        textS = text.split()


        # 원하는 정보가 있는 위치를 발견합니다.
        try:
            gpuN = textS.index('GPUs:')
        # 가끔 GPUs: 정보가 나오지 않을때가 있으므로 3초의 여유를 두고 예외처리를 하여 다시 채굴정보를 받습니다.
        except ValueError:
            time.sleep(3)
            url = urllib.request.urlopen('http://127.0.0.1:3333')
            data = url.read()
            soup = bs(data, "html.parser")
            text = soup.get_text()
            textS = text.split()
            gpuN = textS.index('GPUs:')

        # textAll에 필요한 채굴 정보만 담기 위한 준비를 합니다.
        textAll = []



        # 컴퓨터 자원을 아끼기위해 앞부분만 검색해도 충분하므로, GPU 1개당 33문자이므로 GPU가 최대 12개까지 있다고 가정할때 넉넉하게 500문자까지만 검색을 합니다.
        for i in range(500):
            # 만약 Eth:등의 리스트 구성요소가 나오면, 거기까지가 필요한 채굴정보이므로 거기까지만 추출합니다.
            if textS[gpuN + i + 1] != 'Eth:' and textS[gpuN + i + 1] != 'Eth' and textS[gpuN + i + 1] != 'GPU1:' and \
                    textS[gpuN + i + 1] != '***' and textS[gpuN + i + 1] != 'Available':
                # textAll에 필요한 채굴 정보를 담습니다.
                # print(textS[gpuN+i])
                textAll.append(textS[gpuN + i + 1])
            else:
                # print(textAll)
                break
        # GPU 하나당 4개의 리스트 구성요소를 가지므로 4로 나누어 줘서 총 GPU 개수를 구해서 gpuA에 담아줍니다.
        gpuA = int(len(textAll) / 4)

        # 리스트를 스트링으로 변환하여 송출할 준비를 해 줍니다.
        textAll_str = str(textAll)

        # 송출하기 위해 바이트로 변경해 줍니다.
        textAll_byte = bytes(textAll_str, encoding='utf-8')

        # 빅엔디안(>)으로 패킹을 합니다.
        self.dataToSend = struct.pack('> 12s 500s I', my_name_byte, textAll_byte, gpuA)












        """
        #패킹을 하기 위한 준비를 합니다.
        values = (textAll_byte, gpuA)
        #패킹의 형식을 빅 엔디안(>)으로 지정해 줍니다.
        fmt = '>{}s I'.format(len(textAll_str))
        #패킹의 구조를 설정해 줍니다.
        packer = struct.Struct(fmt)
        #패킹을 해 줍니다.
        textAll_Num = len(textAll_byte)


        #테스트용으로 출력해 봅니다.
        #print(dataToSend)

        #패킹한 데이터를 송출합니다.
        #client_socket.send(sendData)
        """
    """
    연습코드
    try:
        a = textS.index('fdk')
    except ValueError:
        print("su")
    
    for i in range(200):
    
        if textS[gpuN+i] != 'Eth':
            print(textS[gpuN+i])
        else:
            break
    """

