import pyautogui, time
time.sleep(6)
for word in open("script.txt","r"):
	pyautogui.typewrite(word)
	pyautogui.press("enter")
# for word in open("script.txt","r"):
# 	print(word)STELLA: What'd you get?


