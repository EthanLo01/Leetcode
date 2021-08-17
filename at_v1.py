import random,re,time,datetime
import numpy as np
import requests as rq
from datetime import timedelta  

def job(name,part,type):
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSdweCJpzGM42OYVvp_EjhoSWzskJ2GJ7eccMzoAaC71a8lgGA/formResponse'
    symptom =['無發燒無症狀','有發燒','有感冒症狀']
    payload ={
        'entry.774684698' : '',
        'entry.385042053': '',
        'entry.1200815830': symptom[type-1],
        'entry.1200815830_sentinel':'', 
        'fvv' : '0',
        'draftResponse' : '[null,null,"2559418594602512297"]',
        'pageHistory' : '0',
        'fbzx' : '2559418594602512297'
    }
    if part == 1:
         payload['entry.774684698']= name
    elif part == 2:
        payload['entry.385042053'] = name
   
    print (payload)
    try:
        res = rq.post(url, data=payload)
        res.raise_for_status()

    except rq.HTTPError:
        print('HTTP Error!')

    else:
        print ('打卡成功')


# 自定義延遲時間
def info(dT1,dT2):
    arr = [['曲偉皓',2,1],['張嘉芳',1,1],['江宛臻',1,1],['巫冠廷',1,1]]
    arrRand = random.shuffle(arr)
    for i in range(len(arr)):
        timeRand = random.randrange(dT1,dT2)
        nextTime = datetime.datetime.now()+timedelta (0,timeRand )
        nextTime_str = nextTime.strftime('%H:%M:%S')
        print('打卡間格:',timeRand,'s後,預計時間:',nextTime_str)
        time.sleep(timeRand)
        job(arr[i][0],arr[i][1],arr[i][2])
        print(arr[i][0][1:3],"的表單送出:",now)
#打卡名單
 
    
#開關時間
OpeningDay = datetime.time(6,30)
ClossDay = datetime.time(7,50)

OpeningNight = datetime.time(14,20)
ClossNight = datetime.time(16,40)
    

#開關
switch = 0
start = datetime.datetime.now().strftime('%H:%M:%S')
print('打卡開始執行',start)
#無限迴圈


while True:
    #更新平率可調整
    
    #取得datetime.datetime時間格式
    now = datetime.datetime.now()
    #轉換為文字格式
    now_str = now.strftime('%H:%M:%S')
    hour = int(now_str[:2]) 
    minute = int(now_str[3:5])
    #組成datetime.time格式，方便比對
    now = datetime.time(hour, minute)
    
    detectT = 600
    thisT = datetime.datetime.now()+timedelta (0,detectT)
    thisT_str = thisT.strftime('%H:%M')
    print('下次時間:',thisT_str,'間格',detectT,'s,狀態:',switch)
    time.sleep(detectT)

    # switch == 0 且 now在丟單時間內，將switch改為1
    #第一次打卡時段
    if  (ClossDay >= now >= OpeningDay) and switch == 0:
        print ('一次打卡：')
        info(600,1200)

        switch = 1
        print('2',now,'狀態:', switch)

    #第二次打卡時段
    elif (ClossNight >= now >= OpeningNight) and switch == 0:

        print ('二次打卡：')
        info(900,1800)
        switch = 1
        
        print('3',now,'狀態:',switch)
        #switch = 1 且當時間超過丟單時間，將開關打開為0

    #第一次到第二次的中間時間
    if  (OpeningNight > now > ClossDay) and switch == 1:
        switch = 0
        print('4',now, switch)
    
    # 隔夜第二次到第一次的中間時間
    elif ((now > ClossNight) or (now < OpeningDay)) and switch == 1:
        switch = 0
        print('5',now, switch)
  

