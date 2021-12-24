import time
import pyautogui
import cv2 as cv

pyautogui.PAUSE = 0.02

def region():
    r = None
    while r is None:
        print('Procurando Regiao')
        r = pyautogui.locateOnScreen('regiao.png', confidence=0.9)
    else:
        time.sleep(2)
        pyautogui.click(r)
        print('Regiao selecionada')
        pyautogui.hotkey('f5')
        time.sleep(1)
        login()


def login():
    attemp = 0
    a = None
    while a is None:
        print('Conectando wallet')
        a = pyautogui.locateCenterOnScreen('1.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        time.sleep(1)
        pyautogui.click(a)
        print('Conectado')
        login2() 

def login2():
    attemp = 0
    b = None
    while b is None:
        print('Assinando')
        b = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        time.sleep(1)
        pyautogui.click(b)
        print('Assinado')
        hero()

def mapa():
    attemp = 0
    c = None
    while c is None:
        print('conectando meta')
        c = pyautogui.locateCenterOnScreen('3.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 35:
            erros()
    else:
        time.sleep(0.5)
        pyautogui.click(c)
        pyautogui.click(c)
        print('Entrando no Mapa')

def hero():
    attemp = 0
    d = None
    while d is None:
        print('Selecionando Heroi 0')
        d = pyautogui.locateCenterOnScreen('4.png', confidence=0.8)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        pyautogui.moveTo(d)
        time.sleep(5)
        pyautogui.click(d)
        print('Lista de Herois')
        time.sleep(5)
        pyautogui.click(d)
        scroll()

def scroll():
    attemp = 0
    e = None
    while e is None:
        print('Selecionando Heroi 1')
        e = pyautogui.locateCenterOnScreen('5.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        time.sleep(1)
        pyautogui.moveTo(e)
        print('Scrollando')
        time.sleep(1)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        pyautogui.scroll(-10)
        selecthero()

def selecthero():
    attemp = 0
    f = None
    while f is None:
        print('Selecionando Heroi 2')
        f = pyautogui.locateCenterOnScreen('6.png', confidence=0.9)
        g = pyautogui.locateCenterOnScreen('7.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(f)
        time.sleep(1)
        pyautogui.click(g)
        time.sleep(1)
        pyautogui.click(g)
        time.sleep(1)
        pyautogui.click(g)
        mapa()

def erros():
    relogio = 0
    region()
    okk = None
    newmap = None
    while True:
        okk = pyautogui.locateCenterOnScreen('ok.png', confidence=0.8)
        newmap = pyautogui.locateCenterOnScreen('new.png', confidence=0.8)
        print('Procurando')
        time.sleep(34)
        relogio += 1
        print(relogio)
        if okk is not None:
            print('Achou erro')
            pyautogui.click(okk)
            return erros()
        if newmap is not None:
            print('Achou novo mapa')
            pyautogui.click(newmap)
            return erros()
        if relogio > 55:
            return  erros()

erros()
