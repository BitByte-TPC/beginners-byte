import json

json_file = open("repositories.json", "r")

repo_json = json.load(json_file)

json_file.close()

print(repo_json)

# Create a readme file

template_file = open("template.md", "r")
readme_file = open("README.md", "w")

readme_output = template_file.read()
readme_output += '\n'

repos = repo_json['repositories']

# Sort repos
repos = sorted(repos, key=lambda repo: repo['name'].lower())

for repo in repos:
    readme_output += f"| [{repo['name']}]({repo['link']}) | \
        [![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}?color=pink&logo=github)]({repo['link']}/issues) "
    for label in repo['labels']:
        shields_label = label.replace(' ', '%20')
        url_label = label.replace(' ', '+')
        readme_output += f"[![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}/{shields_label}?color=pink&logo=github)]({repo['link']}/issues?q=is%3Aissue+is%3Aopen+label%3A%22{url_label}%22) "
    readme_output += '|\n'
    readme_output = readme_output.replace('    ', '')

print(readme_output)

readme_file.write(readme_output)