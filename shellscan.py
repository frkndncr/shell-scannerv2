import requests, argparse, sys, time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Back, Style, init
import os


ap = argparse.ArgumentParser(description="Shell Scanner")
ap.add_argument("-u", required=True)
ap.add_argument("-w", required=True)
ap.add_argument("-t", required=True)
args = vars(ap.parse_args())

def local_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
    
def exploit(u, list_password):
    host = "http://"+u+"/"+list_password
    
    req = requests.get(host).status_code
    if req == 200:
        print("\33[92m[+] \33[0m{:<55} status: \33[92m{:<20}".format(host, req))
    else:
        print("\33[91m[-] \33[0m{:<55} status: \33[91m{:<20}".format(host, req))

def brute(u):
   try:
       password = args["w"]
       with ThreadPoolExecutor(max_workers=int(args["t"])) as executor:
           with open(password, "r") as password_list:
               for list_password in password_list:
                   list_password = list_password.replace("\n", "")
                   executor.submit(exploit, u, list_password)
                   
   except requests.exceptions.ConnectionError as e:
       print("\33[91m[!] \33[0m Ups, Connection Error")
   except Exception as e:
       print("\33[91m[!] \33[0m Something Wrong")

def main():
    try:
        if len(sys.argv) < 2:
            print(parser.usage())
        else:
            os.system("clear")
            os.system("cls")
            print("\33[96m[#] \33[94m Tarama Başlatıldı {}".format(local_time()))
            time.sleep(1)
            print("\33[96m[#] \33[94m Sadece birkaç dakika bekleyin\n")
            u = args["u"]
            brute(u)
            print("\n\33[96m[#] \33[94m  Tarama Yapıldı. {}".format(local_time()))
            time.sleep(1)
            os.system("clear")
            os.system("cls")
            print("")
            print("\33[96m[#] \33[94m İyi Günler...")
            print(Style.RESET_ALL)
    except KeyboardInterrupt as e:
        print("\33[91m[!] \33[0m Programdan Çıkıldı")
        
if __name__ == '__main__':
   main()
