import urllib
import urllib.request
import http.cookiejar

cook = {"Cookie":'_umdata=E4573FB5B43479059BBA34B3164BDA494189BED61A02DD4D91B2DCAD680DCFEE0F4E40E9C439A748A6FA9B961EB589684825F32405B6F2207D85D247FF40A908555F6ECE482AE04CFD007E5A9130E7EE009C9F98AA9B0C770A8948FF8DD4D7CC7B37131448EB2C04; cna=9UwZDtf4YzoCAdoWFQ7dBl/s; thw=cn; _uab_collina=145680766319846663200855; _tb_token_=MhI61JkZ3w5YG9; lid=%E9%BD%90%E7%90%AA%E6%98%AF%E4%B8%AA%E5%A5%BD%E4%BA%BA; uss=BvWyeGAPBBP5BIiokEBPKFvg5V2lNoJCTmJwPWt9RnlS12KWrFd%2FuKlJmg%3D%3D; _cc_=VT5L2FSpdA%3D%3D; tg=0; lc=Vy1Hb8rnlKZ%2FcVKyzB6ALg%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261457011580274; uc3=sg2=AQd8joq9WXd3lYwAq08cDvMFZVyfq0nsJ5qnYrLeV9A%3D&nk2=&id2=&lg2=; tracknick=; mt=ci=0_0&cyk=0_0; v=0; cookie2=1566cb92ab640fec07682df38ca04dfa; t=1b6e49dc657eae175612eec0d009b93c; _umdata=E4573FB5B43479059BBA34B3164BDA494189BED61A02DD4D91B2DCAD680DCFEE0F4E40E9C439A748A6FA9B961EB589684825F32405B6F2207D85D247FF40A908555F6ECE482AE04CFD007E5A9130E7EE009C9F98AA9B0C770A8948FF8DD4D7CC7B37131448EB2C04; l=Aq2tezc-4g7Sg3/eGkKPLBjxPUMm5uHc'}
req =urllib.request.Request("http://www.taobao.com")
opener = urllib.request.build_opener(cook)
response = opener.open(req)
print (response.read())