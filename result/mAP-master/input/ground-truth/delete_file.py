import glob
import os

d = [
    '1000.txt', '1003.txt', '1006.txt', '1046.txt', '1060.txt',
    '108.txt',  '1089.txt', '1091.txt', '1093.txt', '1104.txt',
    '1118.txt', '1124.txt', '1137.txt', '1147.txt', '1152.txt',
    '1240.txt', '1263.txt', '1314.txt', '1369.txt', '138.txt',
    '1414.txt', '1430.txt', '1434.txt', '1463.txt', '1471.txt',
    '1501.txt', '1515.txt', '1527.txt', '1579.txt', '1593.txt',
    '16.txt',   '160.txt',  '1628.txt', '164.txt',  '1646.txt',
    '1650.txt', '1657.txt', '1661.txt', '1685.txt', '1714.txt',
    '1726.txt', '1732.txt', '1747.txt', '1761.txt', '1791.txt',
    '190.txt',  '231.txt',  '245.txt',  '246.txt',  '257.txt',
    '272.txt',  '29.txt',   '292.txt',  '365.txt',  '369.txt',
    '382.txt',  '399.txt',  '401.txt',  '418.txt',  '427.txt',
    '458.txt',  '463.txt',  '474.txt',  '488.txt',  '525.txt',
    '547.txt',  '552.txt',  '583.txt',  '584.txt',  '593.txt',
    '596.txt',  '629.txt',  '667.txt',  '673.txt',  '674.txt',
    '685.txt',  '688.txt',  '701.txt',  '752.txt',  '781.txt',
    '790.txt',  '794.txt',  '803.txt',  '823.txt',  '829.txt',
    '832.txt',  '848.txt',  '865.txt',  '89.txt',   '920.txt',
    '934.txt',  '938.txt',  '953.txt',  '963.txt',  '971.txt',
    '998.txt'
]

for x in d:
    print(x)
    os.remove(x)