# Author: Pari Malam
# -*- coding:utf-8 -*-

import os
import random
import re
import colorama
import requests
import urllib3

FRom multiprocessing.dummy import Pool
FRom sys import stdout
FRom colorama import Fore, init

init(autoreset=True)
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


FR  =   Fore.RED
FC  =   Fore.YELLOW
FW  =   Fore.WHITE
FG  =   Fore.GREEN


MEOW = 'Results'

if not os.path.exists(MEOW):
    os.mkdir(MEOW)


def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
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



filename = raw_input("\n" + Fore.RED + "[+] " + Fore.YELLOW + "IP/DOMAIN LIST: " + Fore.WHITE)
try:
    target = [i.strip() for i in open(filename, mode='r').readlines()]
except FileNotFoundError:
    exit('[!] File not found: ' + filename)










with open('Wordlist/Shell-Strings.txt', 'r') as f1, open('Wordlist/Shell-Strings.txt', 'r') as f2, open('Wordlist/Other-Strings.txt', 'r') as f3, open('Wordlist/Traversals.txt', 'r') as f4, open('Wordlist/Trusted-Files.txt', 'r') as f5, open('Wordlist/User-Agents.txt', 'r') as f:
    Signs = f1.read().splitlines()
    Strings_Shells = f2.read().splitlines()
    Strings_Uploads = f3.read().splitlines()
    Locations = f4.read().splitlines()
    TrustedFiles = f5.read().splitlines()
    user_agents = [line.strip() for line in f.readlines()]

headers = {
    'User-Agent': random.choice(user_agents),
    'Content-type': '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive'
}


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

        Check_Content = requests.get(url + Path, headers=headers, verify=False, timeout=15)
        if(len(Check_Content.content) == 0):
            Content= requests.get(url + Path, headers=headers, verify=False, timeout=15)
            return Content
        else:
            Content = requests.get(url + Path, headers=headers, verify=False, timeout=15)
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



def Exploiter(site,Dirctorys):
    try:
        url = "http://" + URLdomain(site)

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
                                    print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_FirstFilePhP)
                                    open('Results/Shells.txt','a').write(url + _FirstFilePhP + "\n")
                                    exit()
                                elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                    print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_FirstFilePhP)
                                    open('Results/Uploaders.txt','a').write(url + _FirstFilePhP + "\n")
                                    exit()
                                
                                else:
                                    print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_FirstFilePhP)
                                    open('Results/Success.txt','a').write(url + _FirstFilePhP + "\n")
                                    exit()

                            else:
                                print("[Shell-Scanner] - {} {} [Not Found!]").format(url,FR,_FirstFilePhP)
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
                                                print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_NextFilePhP)
                                                open('Results/Shells.txt','a').write(url + _NextFilePhP + "\n")
                                                exit()
                                            elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                                print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_NextFilePhP)
                                                open('Results/Uploaders.txt','a').write(url + _NextFilePhP + "\n")
                                                exit()
                                            
                                            else:
                                                print("[Shell-Scanner] - {} {} [W00T!]").format(url,FG,_NextFilePhP)
                                                open('Results/Success.txt','a').write(url + _NextFilePhP + "\n")
                                                exit()
                                                
                                        else:
                                            print("[Shell-Scanner] - {} {} [Not Found!]").format(url,FR,_NextFilePhP)
                                            
                                            
            else:
                print("[Shell-Scanner] - {} {} [Not Found!]").format(url,FR,Path)
                
    except :
        pass



def CmsCheckers(site):
    try:
        
        
        
        
        Exploiter(site,Locations)
    

        
        
        
    except:
        pass


mp = Pool(70)
mp.map(CmsCheckers, target)
mp.close()
mp.join()
