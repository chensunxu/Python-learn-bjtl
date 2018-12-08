from urllib import request

if __name__ == '__main__':

    url = 'http://www.renren.com/965187997/profile'

    headers = {
        "Cookie":"anonymid=jeczei1q-81jxm5; Hm_lvt_1e59e639119e3bf348b864db2b258c57=1523104771; Hm_lvt_4397070d9365caef87e72dc468269464=1523104771; depovince=GW; _r01_=1; JSESSIONID=abc2rgl-x1GMj7jQHInEw; ick_login=4ec27d4d-b071-4504-a5bb-cbfed73225cf; t=a0549a147c04da581263f316e24d339b3; societyguester=a0549a147c04da581263f316e24d339b3; id=969053443; xnsid=726ba594; jebecookies=60becb77-bb9b-4794-8c26-2ee8816f6f64|||||; ch_id=10016; jebe_key=53dc40e5-0a98-4dfb-9b85-f2227de80670%7Cb9cc955b1e3a0fc3d2e0139f54548bf9%7C1544268571890%7C1%7C1544268572562; wp_fold=0"
    }

    req = request.Request(url,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding="utf-8") as f:
        f.write(html)
