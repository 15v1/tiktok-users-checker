import requests
import threading
def checkbo():
    headres={
    'authority': 'www.tiktok.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    'cookie': 'tt_webid_v2=6949430705537549826; tt_webid=6949430705537549826; MONITOR_WEB_ID=6949430705537549826; ttwid=1%7CGHCZdyEnJ2n_xH4evNKnq_-yDMfIJo6Nmg6AmTdDS_c%7C1618040432%7C6a94598ef1b3cccc0c45f8dd773831588b06f797ca0fc102f22726ffb09ecf00; tt_csrf_token=oVzjmIGuYbu6puI6husp72PN; ak_bmsc=56000488FFAFA8BC0C39D5ED9711271551DA1F95F37F0000AFC38360DFD79C26~pln40zZmUR9HCKX0LPKv2GgpLZyRUHEEwwrC+18+iD9dtuGG0G0jdCrl/+iQ6jawzgthD6gMPyB0zatOWEU8fydCpHGOxR0ZljC6WUnX8sZ3C7JhEH6P+87/ZRIkAIiMYv6zUbkpB5N9F7yx6DN3qouZcFJNv3ePyb+u9TxSv+d0+wH/ynpoS+hxCXNk88So6kgbylorfD6farPIVYp3VjNyyyN+esaMvVmMdzGC1D+ag=; bm_sz=661CA00037C0C0957FDD4579FBC35DDB~YAAQlR/aUQpddPZ4AQAArWS0AgvG+WtkY8K6DM2K64WhMTRRZ0NY5RJDSxUoVfjHa+PUODcmICelsXAx1ysug7gDddF/tQGYAEFiZUyO3bCuXnc7P/OH4rrJY6T+005yWPX45F2/InsgaPOMtrpnlmurSW0qnEaRD9jEKba1n4iHNw31kNlwejOHaH6ifYmD; _abck=5110DF18ABD1EAD641093763CE3810E7~-1~YAAQlR/aUQtddPZ4AQAArWS0AgXXyslHAFEqlThFhIzigh1On9AXBelpNL9Xlkd/9vuw3DAdOHo4YpEfI3Lqys+W1ykfc8qmh2IQ01hoAdMpsJx2FWa8EoWjMrZkgVIKjGJukaGuBxzxSS4pz9O31j3dOV3KkUfBydSWSx/NdZSDhOWAPfETL8nD67aWUYArPGgvqlxPWYnWEjhmcLXKM+VYpwbDpX4a/GI926r4u1HJwLo2ac/wNqvNA+vryZggdJ9Kuvgq9ogZKEKYe5cJ11yiFRaHbLwa1Jw9Ll7q8VQqgyJubIWvoNhYvZcUOTuuByW6RjBIE/r63lNfZKTVWz/eX6dlPVBqBvncPtPKh/IxIiHlOYBsssZXBFhm9QK6/r6XhWbkoDhRLg==~-1~-1~-1; csrf_session_id=b001be0de9f74cbca51d3fffac44ddab; R6kq3TV7=ANxutAJ5AQAAuXent2-hdn_INFgRH5LPCzfUBF-t1oaQgQVcDVl0E3VbOM9o|1|0|9812fa4e4b28ba7010c0ee96887b41a4cacd86a8; s_v_web_id=verify_knvehdj4_vUdq6dTA_YkIK_4sAT_AIvE_BH3qE9YwkU79; bm_mi=3F517A21D252E06623CF0BB8888B5078~wV9hQezGVz7j5SBtW2L/aJhtTo4sePOeszJWlsFBM36clhjXHfIipAnYVvCYC6+CJV+Bv1AuKjvjHFl3pPJ5vvOk+QXiHdYWBaZpNgVpwIv3XK67xuWevbxn9JJy7RlqpmoeI+/NVThOce5aXWJrNR/Z9DCiwaTmWFqgwRX8F6sU8zznqvRnnYtpqQerW/zP9lGUwkbW+RUf7eH5OkC0jc5uaSbLLBC1+YDiEUQ1HvQ=; bm_sv=F759FC6C8C966292A4EA88BE7C457091~qD3ytW92zYmnCLHj9wPbNnjdI1zafvmQrMjGkDS9s2cgl/fTonGgXEIMKkAkv/c6cP5oiFmsRGqTu9HwZxzMAHEezehDfDuIFmRZ7ghXHjUt18L8K4qZ3EelDplF33Dxw03S7TBr5bAKCRseYj1tTRNEuRTUH+mS1xSBsDyDobk=',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    }
    ff=open("404.txt","a")
    fuse=open("list.txt","r").read().splitlines()
    for us in fuse:
        url1=(f'https://www.tiktok.com/@{us}?')
        kk=requests.get(url1,headres)
        print(kk.status_code , f'{us}')
        if kk.status_code ==404:
            ff.write(f'{us}\n')    
t1=threading.Thread(target=checkbo)
t1.start()
