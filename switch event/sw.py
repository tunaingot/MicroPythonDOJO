from machine import Pin
from utime import sleep

switch = Pin(14, Pin.IN, Pin.PULL_UP) #スイッチがつながっているピンを入力に設定、PULL_UPでプルアップ抵抗を有効にする

while True:
    if switch.value() == 1:  # スイッチが押されていない時
        print("Switch is ON")
    else:
        print("Switch is OFF")

    sleep(1)  # 1秒眠る
    