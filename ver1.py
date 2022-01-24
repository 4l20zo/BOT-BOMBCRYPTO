import time
import pyautogui
import cv2 as cv

pyautogui.PAUSE = 0.055

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
        if attemp > 25:
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
        if attemp > 100:
            erros()
    else:
        pyautogui.moveTo(d)
        time.sleep(2.5)
        pyautogui.click(d)
        print('Lista de Herois')
        time.sleep(2.5)
        pyautogui.click(d)
        scroll()

def scroll():
    attemp = 0
    e = None
    while e is None:
        mm = pyautogui.locateCenterOnScreen('7.png', confidence=0.9)
        print('Selecionando Heroi 1')
        e = pyautogui.locateCenterOnScreen('all.png', confidence=0.9)
        attemp += 1
        time.sleep(0.5)
        if attemp > 15:
            erros()
    else:
        print('all')
        pyautogui.click(e)
        time.sleep(0.5)
        pyautogui.click(e)
        time.sleep(0.5)
        pyautogui.click(mm)
        time.sleep(0.5)
        pyautogui.click(mm)
        mapa()

def erros():
    relogio = 0
    vv = 0
    okk = None
    newmap = None
    region()
    while True:
        okk = pyautogui.locateCenterOnScreen('ok.png', confidence=0.7)
        voltar = pyautogui.locateCenterOnScreen('voltar.png', confidence=0.8)
        print('Procurando')
        time.sleep(34)
        relogio += 1
        vv += 1
        print(relogio)
        print(vv)
        if okk is not None:
            vv = 0
            print('Achou erro')
            erros()
        if vv > 6:
            voltar = None
            vv = 0
            while voltar is None:
                voltar = pyautogui.locateCenterOnScreen('voltar.png', confidence=0.8)
            else:
                vv = 0
                pyautogui.doubleClick(voltar)
                time.sleep(0.6)
                pyautogui.doubleClick(voltar)
                voltarmap = None
            while voltarmap is None:
                voltarmap = pyautogui.locateCenterOnScreen('3.png', confidence=0.8)
            else:
                pyautogui.doubleClick(voltarmap)
                time.sleep(0.6)
                pyautogui.doubleClick(voltarmap)
                vv = 0
        if relogio > 36:
            erros()

erros()
