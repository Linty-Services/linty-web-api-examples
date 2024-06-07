# Linty Web API Examples

## Requirements

* Install Python 3 and pip
* Run `pip install -r requirements.txt`

## Usage

### Get all open issues from a given project

```shell
python3 get_open_issues_from_project.py \
  --url "<url_of_your_Linty_platform>" \
  --token "<token_of_a_Linty_user_with_browse_permission_on_the_project>" \
  --key "<linty_project_key>"
   
# For instance:
python3 get_open_issues_from_project.py \
  --url "http://localhost:9000" \
  --token "squ_xxx" \
  --key "my_project_key"
```

It outputs two files:

* JSON format: `output.json`
* CSV format: `output.csv`
