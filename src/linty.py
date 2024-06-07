import logging
import requests


class LintyApi:

    def __init__(self, base_url, token):
        self._token = token
        self._base_url = base_url
        self._session = requests.Session()
        self._session.auth = token, ''

    # See https://demo.linty-services.com/web_api/api/issues/search
    def get_open_issues_from_project(self, project_key):
        all_issues = []
        i = 1
        while True:
            r = self.request(
                "issues/search",
                {"componentKeys": project_key, "issueStatuses": "OPEN", "ps": "500", "p": i},
                200,
                f'Cannot retrieve the list of issues on "{project_key}" project'
            )

            issues = r.json()["issues"]
            if not issues:
                break

            for issue in issues:
                all_issues.append(issue)

            i += 1

        return all_issues

    def request(self, api, params, expected_response_status_code, error_message, verb="get"):
        response = getattr(self._session, verb)(self._base_url + "/api/" + api, params=params)

        if response.status_code != expected_response_status_code:
            logging.error(response)
            logging.error(response.text)
            raise ConnectionError(error_message)

        return response
