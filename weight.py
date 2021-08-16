
#ライン
line = ":::::୨୧::::::::::୨୧::::::::::୨୧:::::::::::୨୧::::::::::୨୧:::::"

#種類リスト
kind = ['スコティッシュフォールド','マンチカン']
sex = ['オス','メス']

#種類選択
def q1():
	print("Q1.猫の種類を選んでください")
	num = 1

	for i in kind:
		print('['+ str(num) + ']:' + i)
		num += 1

#性別選択
def q2():
	print("Q2.性別を選んでください")
	num = 1

	for i in sex:
		print('['+ str(num) + ']:' + i)
		num += 1

#回答向け
print(line)
q1()

key1 = input('回答:')

#print(type(key1))
#print(key1.isdecimal())

if key1.isdecimal() is True:
	#print('intです')
	key1 = int(key1)

	if 1 <= key1 <= len(kind):
		q2()
	else:
		print('選択肢1~' + str(len(kind)) + 'から入力してください。')
		q1()
else:
	print('数値を入力してください。')
	q1()




key2 = input('回答:')

#print(type(key2))
#print(key2.isdecimal())

if key2.isdecimal() is True:
	#print('intです')
	key2 = int(key2)

	if 1 <= key2 <= len(sex):
		print(line)
		print('【結果】')
	else:
		print('選択肢1~' + str(len(sex)) + 'から入力してください。')
		q2()
else:
	print('数値を入力してください。')
	q2()


kekka1 = kind[key1-1]
kekka2 = "かつ"
kekka3 = sex[key2-1]
kekka4 = "の場合、\n適正体重は"
kekka5 = "です。"

if key1 == 1 and key2 == 1: #スコオス
	print(kekka1 + kekka2 + kekka3 + kekka4 + '3.0～6.0Kg' + kekka5)
elif key1 == 1 and key2 == 2: #スコメス
	print(kekka1 + kekka2 + kekka3 + kekka4 + '3.0～5.0Kg' + kekka5)
elif key1 == 2 and key2 == 1: #マンチオス
	print(kekka1 + kekka2 + kekka3 + kekka4 + '3.0～6.0Kg' + kekka5)
elif key1 == 2 and key2 == 2: #マンチメス
	print(kekka1 + kekka2 + kekka3 + kekka4 + '3.0～6.0Kg' + kekka5)
else:
	print("正しく選択しましたか？")
