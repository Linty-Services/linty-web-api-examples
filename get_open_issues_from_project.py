import argparse
import json

from src.linty import LintyApi

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Get all issues on project")
    arg_parser.add_argument("--url", help="Linty platform URL", default="http://localhost:9000")
    arg_parser.add_argument("--token", help="Token of Linty user with Browse permission on project", required=True)
    arg_parser.add_argument("--key", help="Linty project key to retrieve issues from", required=True)
    args = arg_parser.parse_args()

    linty_api = LintyApi(args.url, args.token)

    issues_as_list = linty_api.get_open_issues_from_project(args.key)
    issues_as_json = json.dumps(issues_as_list)

    with open('output.json', 'w') as f:
        f.write(issues_as_json)

    # See https://demo.linty-services.com/web_api/api/issues/search
    csv = 'rule|message|component\n'
    for issue in issues_as_list:
        csv += f"{issue['rule']}|{issue['message']}|{issue['component']}\n"

    with open('output.csv', 'w') as f:
        f.write(csv)
