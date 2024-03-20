import re
import subprocess
import sys


def main():
    commit_msg_file = sys.argv[1]
    current_branch = get_branch_name()

    m = re.match(r"^([A-Z]{3,}-\d+)-.+$", current_branch)
    if not m:
        exit()

    jira_issue_prefix = m.group(1) + ": "

    with open(commit_msg_file, "r") as f:
        contents = f.read()

    subject = contents.split("\n")[0]

    if subject.startswith(jira_issue_prefix):
        exit()

    with open(commit_msg_file, "w") as f:
        f.write(jira_issue_prefix)
        f.write(contents)

    exit()


def get_branch_name() -> str:
    output = subprocess.check_output(["git", "branch", "--show-current"])
    return output.decode("utf-8").strip()


if __name__ == "__main__":
    main()
