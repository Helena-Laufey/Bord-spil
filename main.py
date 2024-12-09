from machine import Pin, PWM, ADC
from random import randint
from time import sleep_ms
from machine import SoftI2C
from I2C_LCD import I2cLcd
import time
from machine import I2C
from time import ticks_ms, ticks_diff
import random

takkiA=Pin(12, Pin.IN, Pin.PULL_UP)
takkiB=Pin(11, Pin.IN, Pin.PULL_UP)
takkiC=Pin(10, Pin.IN, Pin.PULL_UP)
takkiD=Pin(21, Pin.IN, Pin.PULL_UP)
takkiE=Pin(5, Pin.IN, Pin.PULL_UP)
takkiH=Pin(4, Pin.IN, Pin.PULL_UP)

bla=Pin(18, Pin.OUT)
raud=Pin(17, Pin.OUT)
gul1=Pin(16, Pin.OUT)
gren=Pin(15, Pin.OUT)
gull=Pin(8, Pin.OUT)

hatalaripassive = PWM(Pin(7), freq=20000)

ON=False

timi=False

hard=False

score = 0

perur = [gul1, gren, raud, bla, gull]

milli = 1700

i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)

lcd = I2cLcd(i2c, 38, 2, 16)  
lcd2 = I2cLcd(i2c, 39, 2, 16)
    
print(i2c.scan())

TIMER_DURATION = 60 * 1000  # 60000 ms


start_timi = ticks_ms()




def tonbrjalad():
    hatalaripassive.duty(512)
    hatalaripassive.freq(988)
    sleep_ms(50)
    hatalaripassive.freq(1174)
    sleep_ms(50)
    hatalaripassive.freq(1568)
    sleep_ms(50)
    hatalaripassive.duty(0)
    sleep_ms(50)



        
        
    

def tonlist():
    hatalaripassive.duty(512)
    hatalaripassive.freq(311)
    sleep_ms(500)
    hatalaripassive.freq(623)
    sleep_ms(500)
    hatalaripassive.freq(784)
    sleep_ms(500)
    hatalaripassive.freq(623)
    hatalaripassive.duty(0)
    sleep_ms(500)

def tonlitid():
    hatalaripassive.duty(512)
    hatalaripassive.freq(659)
    sleep_ms(200)
    hatalaripassive.freq(1318)
    hatalaripassive.duty(0)
    

def display_score():
    lcd2.clear()
    lcd2.putstr("Score Kerfi")
    lcd2.move_to(0, 1)
    lcd2.putstr(f"Score: {score}")

def blick():
    gul1.value(1)
    sleep_ms(50)
    gul1.value(0)
    gren.value(1)
    sleep_ms(50)
    gren.value(0)
    raud.value(1)
    sleep_ms(50)
    raud.value(0)
    bla.value(1)
    sleep_ms(50)
    bla.value(0)
    gull.value(1)
    sleep_ms(50)
    gull.value(0)






for pera in perur:
    pera.value(0)
pot = randint(0,4) 

while ON == False:
    if takkiA.value() == 0:
        gul1.value(1)
        sleep_ms(50)
        gul1.value(0)
        sleep_ms(50)
        gul1.value(1)
        sleep_ms(50)
        gul1.value(0)
        sleep_ms(50)
        gul1.value(1)
        sleep_ms(50)
        gul1.value(0)
        tonlist()
        sleep_ms(2000)
        ON = True
        timi = True
    if takkiH.value() == 0:
        for i in range(5):
            blick()
            tonbrjalad()
        sleep_ms(1000)
        hard=True
        ON=True

    

#rod.value(pot)
#grenn.value(pot)
display_score()

    
while ON == True and timi == True:
    current_timi = ticks_ms()
    elapsed_timi = ticks_diff(current_timi, start_timi)
    
    remaining_timi = max(0, 60 - elapsed_timi // 1000)
    
    lcd.clear()
    lcd.putstr(f"Timi eftir:\n{remaining_timi} s")
    
    if elapsed_timi >= TIMER_DURATION:
        lcd.clear()
        lcd.putstr("Timi buinn!")
        timi = False
    for i in range(1):
        perur[pot].value(1)
    if gul1.value() == 1:
        if takkiA.value() == 0:
            score += 10
            milli -= 100
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gul1.value(1)
            sleep_ms(50)
            gul1.value(0)
            sleep_ms(50)
            gul1.value(1)
            gul1.value(0)
            tonlitid()
            sleep_ms(milli)
            print(score)
    if gren.value() == 1:
        if takkiB.value() == 0:
            score += 10
            milli -= 100
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gren.value(1)
            sleep_ms(50)
            gren.value(0)
            sleep_ms(50)
            gren.value(1)
            gren.value(0)
            tonlitid()
            sleep_ms(milli)
            print(score)
    if raud.value() == 1:
        if takkiC.value() == 0:
            score += 10
            milli -= 100
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            raud.value(1)
            sleep_ms(50)
            raud.value(0)
            sleep_ms(50)
            raud.value(1)
            raud.value(0)
            tonlitid()
            sleep_ms(milli)
            print(score)
    if bla.value() == 1:
        if takkiD.value() == 0:
            score += 10
            milli -= 100
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            bla.value(1)
            sleep_ms(50)
            bla.value(0)
            sleep_ms(50)
            bla.value(1)
            bla.value(0)
            tonlitid()
            sleep_ms(milli)
            print(score)
    if gull.value() == 1:
        if takkiE.value() == 0:
            score += 10
            milli -= 100
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gull.value(1)
            sleep_ms(50)
            gull.value(0)
            sleep_ms(50)
            gull.value(1)
            gull.value(0)
            tonlitid()
            sleep_ms(milli)
            print(score)

while hard == True:
    current_timi = ticks_ms()
    elapsed_timi = ticks_diff(current_timi, start_timi)
    
    remaining_timi = max(0, 60 - elapsed_timi // 1000)
    
    lcd.clear()
    lcd.putstr(f"Timi eftir:\n{remaining_timi} s")
    
    if elapsed_timi >= TIMER_DURATION:
        lcd.clear()
        lcd.putstr("Timi buinn!")
        hard=False
    for pera in perur:
        pera.value(random.choice([0, 1]))
        
        time.sleep(random.uniform(0.05, 0.2))

        if random.random() < 0.1:
            for pera in perur:
                pera.value(0)
            time.sleep(0.1)
    if gul1.value() == 1:
        if takkiA.value() == 0:
            score += 10
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gul1.value(1)
            sleep_ms(50)
            gul1.value(0)
            sleep_ms(50)
            gul1.value(1)
            gul1.value(0)
            tonlitid()
            print(score)
    if gren.value() == 1:
        if takkiB.value() == 0:
            score += 10
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gren.value(1)
            sleep_ms(50)
            gren.value(0)
            sleep_ms(50)
            gren.value(1)
            gren.value(0)
            tonlitid()
            print(score)
    if raud.value() == 1:
        if takkiC.value() == 0:
            score += 10
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            raud.value(1)
            sleep_ms(50)
            raud.value(0)
            sleep_ms(50)
            raud.value(1)
            raud.value(0)
            tonlitid()
            print(score)
    if bla.value() == 1:
        if takkiD.value() == 0:
            score += 10
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            bla.value(1)
            sleep_ms(50)
            bla.value(0)
            sleep_ms(50)
            bla.value(1)
            bla.value(0)
            tonlitid()
            print(score)
    if gull.value() == 1:
        if takkiE.value() == 0:
            score += 10
            display_score()
            time.sleep(0.3)
            pot = randint(0,4)
            gull.value(1)
            sleep_ms(50)
            gull.value(0)
            sleep_ms(50)
            gull.value(1)
            gull.value(0)
            tonlitid()
            print(score)

