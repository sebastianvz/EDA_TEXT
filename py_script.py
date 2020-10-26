#%%
import requests
import pandas as pd
import nltk
import unidecode

nltk.download('punkt')
#%%
url = 'http://cubiq.mekagroupcol.com/externalapi/getMeasure'
#body = {"limit": "10"}
body= "{\"date\":{\"initial\":\"2020-05-01\",\"final\":\"2020-09-01\"},\"limit\":\"5000\"}"
response = requests.post(url, data = body, headers = {"auth": "CcKAtnb8hI5cSHr86SvXRXDF6cPyYrKf5PnGRi8x6Pg"})
mesarure_ocr= response.json()
display(len(mesarure_ocr['measures']),)
data= pd.DataFrame.from_dict(response.json()['measures'])
#%%
import re
re_list = '|'.join([r'[0-9]+',r'[^\w]'])
label = {}
label_num = []
label['unk']=0
categories = ['usps','amazon', 'dhl',"fedex", 'ups']
unknown_categories = []
def read_ocr(input_ocr, num):
    if (input_ocr!=None and len(input_ocr)!=0):
        ocr_txt = unidecode.unidecode(input_ocr.lower().replace('\n', ' '))
        ocr_txt = ' '.join(re.sub(re_list, ' ', ocr_txt).split())
        ocr = nltk.word_tokenize(ocr_txt)
        cont = 0
        for category in categories: 
            cont+=1
            if category in ocr:
                if category not in label:
                    label[category]=0
                    label_num.append(categories.index(category))
                    break   
                else:
                    label[category]+=1
                    label_num.append(categories.index(category))
                    break
            if cont==5:
                label['unk']+=1
                unknown_categories.append(num)
                label_num.append(5)
    else:
         label['unk']+=1
         label_num.append(5)
for count, i in enumerate(data.ocr):
    read_ocr(i, count)
label.pop('unk',None)
#%%
data['label'] = label_num