#Jangan ganti author , hargai creator cape loh buat nya

import requests,os,re,time

b="\033[1;94m"
g="\033[1;92m"
w="\033[1;97m"
r="\033[1;91m"
y="\033[1;93m"
cyan = "\033[1;96m"
lgray = "\033[0;30m"
dgray = "\033[1;90m"
ir = "\033[0;101m"
reset = "\033[0m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def italy():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/IT/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    print ("")
    time.sleep(1)
    print(" \033[1;92m +$$$$$$$$$$$$$$$$$$$$$$$$$$\033[1;91m*\033[1;92m$$$$$$$$$$$$$$$$$$$$$$+")
    print("\033[1;92m  # \033[1;90mAuthor   \033[1;90m -->>> \033[1;95m*\033[1;97mERR0R\033[1;95m*\033[1;92m                         #")
    print("\033[1;92m  # \033[1;93mGithub   \033[1;90m -->>> \033[1;90mhttps://github.com/Err0r-ICA \033[1;92m   #")
    print("\033[1;92m  # \033[1;95mTeam     \033[1;90m -->>> \033[1;92mITALIA \033[1;97mCYBER \033[1;91mARMY \033[1;92m              #")
    print("\033[1;92m  # \033[1;91mInstagram\033[1;90m -->>> \033[1;97m@termux_hacking          \033[1;92m       #")
    print("\033[1;92m  # \033[1;96mTelegram \033[1;90m -->>> \033[1;94mhttps://t.me/termuxxhacking   \033[1;92m  #")
    print("\033[1;92m  # \033[1;97mVersion  \033[1;90m -->>> \033[1;91m2.0                     \033[1;92m        #")
    print("\033[1;92m  +$$$$$$$$$$$$$$$$$$$$$$$$$$\033[1;91m*\033[1;92m$$$$$$$$$$$$$$$$$$$$$$+")
    print("")
    print("      \033[1;93m [\033[1;92m List page :\033[1;93m ]\033[1;92m")
    print("")
    run()
    
def run():
    try:
        page = input("\033[1;93m       [ \033[1;92mPage \033[1;93m]\033[1;37m-->>> ")
        url = ("https://www.insecam.org/en/bycountry/IT/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}[ {}{} {}]").format(r,w,hasil,r)
             count += 1
    except:
        print ""
        print r+"Thanks for using our tools"+w
