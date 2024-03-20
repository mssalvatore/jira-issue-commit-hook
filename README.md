# JIRA Issue Commit Hook

## Description
This is a pre-commit hook that automatically prefixes the commit-message's
summary line with a JIRA issue if the branch name begins with a JIRA issue ID.

Example:
```sh
$ git branch --show-current
JIRAPROJ-101-fix-a-bug
$ git commit
```

Running `git commit` results in a commit message that looks like

```
JIRAPROJ-101: 

...
```


## Installation

Add the following to your `.pre-commit.yaml`:
```yaml
  - repo: https://github.com/mssalvatore/jira-issue-commit-hook
    rev: v1.0.0
    hooks:
      - id: jira-issue
```

Then run `pre-commit install -t prepare-commit-msg`.
