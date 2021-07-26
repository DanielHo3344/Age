driving = input ('請問您有沒有開過車')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
age = input ('請問您的年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('再過幾年你可以考駕照')



