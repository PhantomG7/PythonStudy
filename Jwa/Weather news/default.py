import requests

resRegion = requests.api.get('http://ip-api.com/csv')
region = str(resRegion.text).split(',')[5]
res = requests.api.get('https://develope.dev/api/weather?api='+key+'&where='+region)
indexRes = str(res.text).index('<span class="vk_gy vk_sh" id="wob_dc">')+38
strRes = str(res.text)[indexRes:-6]
print(strRes)

