from github import Github

API_TOKEN = "Api_keyiz"

g = Github(API_TOKEN)

owner = "github_KullaniciAdiniz"
repo = "repo_adiniz"

contributors = g.get_repo(f"{owner}/{repo}").get_contributors()

usernames = []
avatar_urls = []

for contributor in contributors:
    usernames.append(contributor.login)
    avatar_urls.append(contributor.avatar_url)

contributors_data = zip(avatar_urls, usernames)

markdown_content = "## Katkıda Bulunanlar\n\n"
markdown_content += '<div style="display: flex; flex-wrap: wrap;">\n'
for avatar_url, username in contributors_data:
    markdown_content += f'  <div style="display: flex; flex-direction: column; align-items: center; margin: 10px;">\n'
    markdown_content += f'    <img src="{avatar_url}" width="70" height="70">\n'
    markdown_content += f'    <span style="text-align: center;">{username}</span>\n'
    markdown_content += f'  </div>\n'
markdown_content += '</div>'

with open("README.md", "w",encoding="utf-8") as readme:
    readme.write(markdown_content)
