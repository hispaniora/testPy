import MainFrame


listData = []
for line in open(r'F:\testData\POI_ZoneDivide1.txt', 'r', encoding='gbk'):
    listData.append(line)
print("需写入的行数: " + str(len(listData)))
