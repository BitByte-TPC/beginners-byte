# Contributing

## Getting Started

1. Feel free to open an issue if you wish to propose something new.
2. Fork the repository on GitHub.
3. Clone the fork

## Making Changes

* Create a branch : `git checkout -b branch-name`. Please avoid working directly on the `master` branch.
* Make commits of logical units.
* Make changes in `repositories.json` file only.
* Put this `json object` anywhere in between the other repositories listed in the file **but please do not add it at the start or end of the list.**


```json
{
    "name": "repo-name",
    "link": "repo-link",
    "labels": ["issue-label1", "issue-label2"]
},
```
* Make sure your commit messages are in the proper format.

## Submitting Changes

* Push your changes to the branch in your fork of the repository.
* Submit a pull request to the repository.
* The contributors look at Pull Requests and review them on a regular basis.
* Upon merging of your pull request, `Readme.md` will be automatically updated listing the beginners-friendly repository added by you.