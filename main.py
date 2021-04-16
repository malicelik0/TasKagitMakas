import random
import PySimpleGUI as sg
secenek=["Taş","Kağıt","Makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
bilpuan=0
oypuan=0
print("Taş,Kağıt, Makas oyununa hoş geldinizn Oyunu bitirmek için q tuşuna basın")

sg.theme('dark amber')
while True:
    layout = [[sg.Button('Taş', size=(10,1)), sg.Button('Kağıt', size=(10,1)), sg.Button('Makas', size=(10,1)),],
            [sg.Text(bilpuan, size=(15,1)), sg.Text(oypuan, size=(15,1))],[[sg.Button('Exit',size=(30,1))]]]
    window = sg.Window('Taş Kağıt Makas Oyunu', layout,size=(300, 250))
    event, values = window.read()

    bil_secim = random.choice(secenek)
    if event =='Taş':
        if bil_secim=='Taş':
            print("Bilgisayarın seçimi: Taş Sonuç: Berabere")

        elif bil_secim=='Kağıt':
            print("Bilgisayarın seçimi: Kağıt Kaybettiniz")
            bilpuan += 1
        else:
            print("Bilgisayarın seçimi: makas Sonuç:Kazandınız")
            oypuan += 1

    if event == 'Kağıt':
        if bil_secim=='Taş':
            print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
            oypuan += 1
        elif bil_secim=='Kağıt':
            print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: makas Sonuç:Kaybettiniz")
            bilpuan += 1
    if event == 'Makas':
        if bil_secim=='Taş':
            print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
            bilpuan += 1
        elif bil_secim=='Kağıt':
            print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
            oypuan += 1
        else:
            print("Bilgisayarın seçimi: makas Sonuç:Berabere")
    if event == sg.WIN_CLOSED or event == 'Exit':
        print("Çıkılıyor...")
        break
