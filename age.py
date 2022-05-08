#年齡判斷程式
smoking = input("你有沒有抽過菸?")
if smoking != "有" and smoking != "沒有" :
	print("只能輸入 有 或 沒有 ")
	raise SystemExit

age = input("那麼您目前幾歲?")
age = int(age)
if smoking == "有":
	if age >= 18 :
		print("法律允許您抽菸，但還是別抽，身體比較健康")
	else:
		print("未成年請勿吸菸!")
elif smoking == "沒有":
	if age >= 18 :
		print("很好，您很健康")
	else:
		print("您是乖寶寶")