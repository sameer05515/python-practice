import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url = "https://api.github.com/users/sameer05515/repos?per_page=100&page="

my_list = [1, 2, 3]
count = 1
respList = []
for i in my_list:
    response = requests.get(api_url + str(i))
    json = response.json()
    for x in json:
        resp = {'id': x['id'], 'name': x['name'], 'description': x['description'], 'language': x['language'],
                'html_url': x['html_url']}
        respList.append(resp)
        count = count + 1

print(respList)

# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
