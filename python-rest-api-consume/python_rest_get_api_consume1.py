import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url = "https://api.github.com/users/sameer05515/repos?per_page=100&page="

list =[1,2,3]
count=1
respList=[]
for i in list:
    response = requests.get(api_url+str(i))
    json=response.json()    
    for x in json: 
        resp={}
        resp['id']= x['id']
        resp['name']= x['name']
        resp['description']= x['description']
        resp['language']= x['language']
        resp['html_url']= x['html_url']
        respList.append(resp)
        # print(str(count) ," : ", x['name'] , " : ", x['language'])
        count=count+1


print(respList)


  
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}