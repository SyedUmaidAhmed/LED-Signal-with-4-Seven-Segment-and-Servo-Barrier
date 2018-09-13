import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED

red = LED(23)
yello = LED(24)
gree = LED(25)


def green():
    t=5
    gree.on()
    pwm.ChangeDutyCycle(10.5)
    sleep(1)
    pwmt.ChangeDutyCycle(12)
    for u in range(0,6):
        for r in range(0,1):
            for y in range(0,7):
                GPIO.output(gpin[y],num[9][y]), GPIO.output(gpino[y],num[t][y])
            sleep(1)

        for a in range(0,1):
            for b in range(0,7):
                GPIO.output(gpin[b],num[8][b])
            sleep(1)

        for c in range(0,1):
            for d in range(0,7):
                GPIO.output(gpin[d],num[7][d])
            sleep(1)

        for e in range(0,1):
            for f in range(0,7):
                GPIO.output(gpin[f],num[6][f])
            sleep(1)

        for f in range(0,1):
            for g in range(0,7):
                GPIO.output(gpin[g],num[5][g])
            sleep(1)

        for g in range(0,1):
            for h in range(0,7):
                GPIO.output(gpin[h],num[4][h])
            sleep(1)

        for j in range(0,1):
            for k in range(0,7):
                GPIO.output(gpin[k],num[3][k])
            sleep(1)

        for l in range(0,1):
            for m in range(0,7):
                GPIO.output(gpin[m],num[2][m])
            sleep(1)

        for n in range(0,1):
            for o in range(0,7):
                GPIO.output(gpin[o],num[1][o])        
            sleep(1)


        for p in range(0,1):
            for q in range(0,7):
                GPIO.output(gpin[q],num[0][q])
            sleep(1)

        t-=1
        if (t==-1):
            t=5
























    
def yellow():
    yello.on()
    sleep(2)
    yello.off()


a1=4
b1=17
c1=18
d1=15
e1=14
f1=27
g1=2
dot1=21


# Now set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

gpin=[19,26,20,16,12,13,6]
gpino=[15,14,27,4,17,18,2]

GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)








num = {

0: (0,0,0,0,0,0,1),
1: (1,1,1,1,0,0,1),
2: (0,0,1,0,0,1,0),
3: (0,1,1,0,0,0,0),
4: (1,1,0,1,0,0,0),
5: (0,1,0,0,1,0,0),
6: (0,0,0,0,1,0,0),
7: (1,1,1,0,0,0,1),
8: (0,0,0,0,0,0,0),
9: (0,1,0,0,0,0,0)
}
 
v=5

GPIO.setwarnings(False)
GPIO.setup(9,GPIO.OUT)
pwm = GPIO.PWM(9,50)   # 3 band...6.5 beech...10.5 khul
GPIO.setup(10,GPIO.OUT)
    
pwmt = GPIO.PWM(10,50)   # 3 band...6.5 beech...10.5 khul

def off_the_signal():
    pwm.start(3)
    sleep(1)
    pwmt.start(6)





while True:
    off_the_signal()
    red.on()
    for r in range(0,1):
        for y in range(0,7):
            GPIO.output(gpin[y],num[9][y]), GPIO.output(gpino[y],num[v][y])
        sleep(1)

    for a in range(0,1):
        for b in range(0,7):
            GPIO.output(gpin[b],num[8][b])
        sleep(1)

    for c in range(0,1):
        for d in range(0,7):
            GPIO.output(gpin[d],num[7][d])
        sleep(1)

    for e in range(0,1):
        for f in range(0,7):
            GPIO.output(gpin[f],num[6][f])
        sleep(1)

    for f in range(0,1):
        for g in range(0,7):
            GPIO.output(gpin[g],num[5][g])
        sleep(1)

    for g in range(0,1):
        for h in range(0,7):
            GPIO.output(gpin[h],num[4][h])
        sleep(1)

    for j in range(0,1):
        for k in range(0,7):
            GPIO.output(gpin[k],num[3][k])
        sleep(1)

    for l in range(0,1):
        for m in range(0,7):
            GPIO.output(gpin[m],num[2][m])
        sleep(1)

    for n in range(0,1):
        for o in range(0,7):
            GPIO.output(gpin[o],num[1][o])        
        sleep(1)


    for p in range(0,1):
        for q in range(0,7):
            GPIO.output(gpin[q],num[0][q])
        sleep(1)

    
    v-=1
    if (v==-1):
        red.off()
        yellow()
        green()
        gree.off()
        v=5
