from django.views.generic import TemplateView
import requests, xmltodict, json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse

@csrf_exempt
def call(request):

    button = request.POST.get('button')
    loc = request.POST.get('loc')
    acc = request.POST.get('acc')

    count = 0
    judge = []
    number = []
    name = []

    for j in range(1, 10):
        key = "lgNTbSDQ2pXNvQbnHSD7mKNcDJYkro%2BBMRgLeDL%2FPCA4hoCz5tYuqqB%2BGyS6QdbN9zd1TbIoMmJ50%2FTs08IgAQ%3D%3D"
        url = "http://apis.data.go.kr/B490001/sjPrecedentInfoService/getSjPrecedentNaeyongPstate?serviceKey={0}&kindB={1}&kindC=업무상사고&numOfRows=10&pageNo={2}".format(
            key, button, j)
        content = requests.get(url).content
        dicts = xmltodict.parse(content)

        jsonstring = json.dumps(dicts['response']['body'], ensure_ascii=False)

        jsonobject = json.loads(jsonstring)

        item = jsonobject['items']['item']

        for i in range(len(item)):
            if type(item[i]['noncontent']) == str and acc in item[i]['noncontent'] and loc in item[i]['noncontent']:
                count += 1

                number.append(item[i]['accnum'])
                name.append(item[i]['courtname'])
                judge.append(item[i]['noncontent'])


    data = {'count': count, "num": number, "name": name, "judge": judge,"button":button, 'loc':loc, 'acc':acc}

    return render(request,'judgement/judgement.html', {'data':data})