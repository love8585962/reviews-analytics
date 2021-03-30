data = [] #創建一個空列表
count = 0 #創建計數初始值
with open("reviews.txt","r") as f :  #讀取名為"reviews"的檔案,並且儲存到 f 這個變數
	for line in f :   #循環f這個變數的值 並賦值為 line
		data.append(line) #將 line的值加到 data 這個列表
		count += 1  #為計數每次循環 +1
		if count % 1000 == 0 : #如果 count 除 1000 餘數剛好為0
			print(len(data)) #印出 data 列表的總長度
print("檔案讀取完了, 總共有" , len(data), "筆資料")

sum_len = 0
for d in data :
	sum_len += len(d)
print("留言平均長度為",sum_len/len(data))