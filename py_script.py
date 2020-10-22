#%%
import requests

#%%
url = 'http://cubiq.mekagroupcol.com/externalapi/getMeasure'
#body = {"limit": "10"}
body= "{\"date\":{\"initial\":\"2020-05-01\",\"final\":\"2020-09-01\"},\"limit\":\"5000\"}"
response = requests.post(url, data = body, headers = {"auth": "CcKAtnb8hI5cSHr86SvXRXDF6cPyYrKf5PnGRi8x6Pg"})
mesarure_ocr= response.json()
display(len(mesarure_ocr['measures']),)

data= pd.DataFrame.from_dict(response.json()['measures'])

#%%
y_train = []
labels=dict()

categories = ['usps','amazon', 'dhl',"fedex", 'ups', 'china', 'singpost','royal', 'canada']


#recorrer todas los elementos en shipping code
def read_courier(input_courier):
    if (input_courier!=None):
        courier = str(input_courier[0]['courier'].lower()) #traer courier
        cont = 0
        for category in categories: #recorrer categories para comparar
            if category in courier:
                if category not in labels: #si se encuentra crear una lista con un zero al principio y el id del elemento
                    labels[category]=[0, list(input_courier[0]['id'])]                    
                else:
                    labels[category][1].append(input_courier[0]['id'])  #seguir incrementando el contador y añadiendo id 
                    labels[category][0]=len(labels[category][1])
    else:
        print('None!')                
            # labels.append(courier)
for count, i in enumerate(pdObj1.shipping_code):
    read_courier(i)
#%%
labels  #diccionario con elementos de la variable 'categories' como keys
        #y como values para cada key la lista de id que pertenecen a esa key.
        #el id se obtiene de del campo id del shipping_code
