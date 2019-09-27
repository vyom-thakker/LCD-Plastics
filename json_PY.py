import json

with open('LC_DOC.json') as json_file:
    data = json.load(json_file)
 #   for n in data['nodes']:
 #      print('Name: ' + n['name'])
 #      print('')
i=1
for l in data['links']:
       print(str(i)+'. Flow from '+data['nodes'][l['source']]['name']+' to '+data['nodes'][l['target']]['name']+': ' + str(l['value']))
       print('')
       i=i+1
