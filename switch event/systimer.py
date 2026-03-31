from machine import Timer

#-------------------------------------------------------------
#main loop内で10msecのタイミングを提供します
#動作確認用にRUN LEDの点灯パターンも提供します
#-------------------------------------------------------------
class systimer:
    def __timerCallback(self, timer):
        self.__interruptCt += 1
        
        self.__ledInterval += 1
        self.__ledInterval %= 8
        
        if self.__ledInterval == 0:#80msecで点滅処理
            self.__ledStep += 1
            self.__ledStep %= len(self.__LED_PTN)
    
    def __init__(self):
        self.__tm = Timer()
        self.__tm.init(period=10, mode=Timer.PERIODIC, callback=self.__timerCallback)
        self.__interruptCt = 0
        self.__ledInterval = 0
        self.__ledStep = 0
#        self.__LED_PTN = [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__LED_PTN = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        
    #--------------------------------------------------------------
    #無限ループ内で常時読みます
    #戻り値が0でなければタイマー割り込みが発生したということです
    #
    #例
    #if systimer.interruptCt() != 0:
    #   print('hello') #10msecごとに表示される
    #
    #--------------------------------------------------------------
    def interruptCt(self):
        # if self.__interruptCt == 0:
        #     return 0
        # else:
        #     result = self.__interruptCt
        #     self.__interruptCt = 0
        #     return result
        result = self.__interruptCt
        self.__interruptCt = 0
        return result
        
    #--------------------------------------------------------------
    #RUN LEDの点滅制御をします
    #LED用ピンオブオブジェクトに戻り値を入れるとハートビート点滅します
    #
    #メインループのどこでコールしても動きますが、頻繁に実行する必要もないので、
    #10msecのタイミングでコールするのがおすすめです
    #
    #例
    #led.value(systimer.runLedState())
    #--------------------------------------------------------------
    def runLedState(self):
        return self.__LED_PTN[self.__ledStep]