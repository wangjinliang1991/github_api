import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()
print("Total respositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about first repository:")
for repo_dict in repo_dicts[:10]:
    print("Name:", repo_dict['name'])
    # 先用键owner访问表示所有者的字典，再用key获取所有者的登录名
    print("Owner:", repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description', repo_dict['description'])
