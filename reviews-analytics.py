data = [] #創建一個空列表
count = 0 #創建計數初始值
#讀取名為"reviews"的檔案,並且儲存到 f 這個變數
with open("reviews.txt","r") as f :
	for line in f :   #循環f這個變數的值 並賦值為 line
		data.append(line)  #將 line的值加到 data 這個列表
		count += 1  #為計數每次循環 +1
		if count % 10000 == 0 : #如果 count 除 1000 餘數剛好為0
			print(len(data)) #印出 data 列表的總長度
print("檔案讀取完了, 總共有" , len(data), "筆資料")

sum_len = 0
for d in data :  #每一筆資料命名為 d(字串) , data為全部列表 把每一筆資料拿出來
    sum_len += len(d) #len(d)為每一筆的長度
print("留言平均長度為",sum_len/len(data))

new = []
for d in data :
    if len(d) < 100 :  #如果長度<100
        new.append(d)  #就把它裝進new這個新的清單
print("一共有",len(new),"筆留言長度小於100")
print(new[0])