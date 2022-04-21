from pykiwoom.kiwoom import *

## 종목받아와서 sql에 던지기 

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)










