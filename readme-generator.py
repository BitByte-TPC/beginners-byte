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
        [![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}?color=pink&logo=github)]({repo['link']}/issues) \
        [![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}/first-timers-only?color=pink&logo=github)]({repo['link']}/issues?q=is%3Aissue+is%3Aopen+label%3Afirst-timers-only) \
        [![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}/good%20first%20issue?color=pink&logo=github)]({repo['link']}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) \
        [![GitHub issues](https://img.shields.io/github/issues/{repo['link'][19:]}/help%20wanted?color=pink&logo=github)]({repo['link']}/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) |\n".replace('    ', '')

print(readme_output)

readme_file.write(readme_output)