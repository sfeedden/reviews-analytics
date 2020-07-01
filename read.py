data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，共有',len(data),'筆資料！')

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均：',sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有：',len(new),'筆留言長度小於100')
print(new[0])
print(new[1])


#文字計數
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有：',len(good),'筆留言提及good')
print(good[0])

good = [d for d in data if 'good' in d] #26~30
print('總共有--',len(good),'個留言含有good')

wc = {} #word_count
for d in data:
	words = d.split() #預設值，為空白鍵
	for w in words:
		if w in wc:
			wc[w] += 1
		else:
			wc[w] = 1
for w in wc:
	if wc[w] >= 1000000:
		print(w, wc[w])

while True:
	w = input('請輸入想查詢的字：')
	if w == 'q':
		break
	if w in wc:
		print('您所查詢的字是：', w, '；共出現', wc[w], '次 ')
	else:
		print('很抱歉，您所查詢的字並未出現')
print('感謝使用')
