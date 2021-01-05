import pyautogui
import time
pesan = "cuy"
jumlah = 10
waktu = 10

for i in range(waktu):
    print("akan mengirim dalam waktu {}".format((waktu-1)-i))
    time.sleep(1)

for i in range(jumlah):
    pyautogui.typewrite(pesan + "\n")

print("spam sukses")