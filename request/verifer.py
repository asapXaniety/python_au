import requests
import json
import datetime


TOKEN = ''

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'VERIFIER']
GROUPS = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Fixed']


def prepare_headers():
    return{
      'Authorization': TOKEN,
      'Accept': "application/vnd.github.v3+json"
        }


def prepare_body(pull, comment):
    return {
        'body': f"{comment}",
        'path': requests.get(pull['url'], headers=prepare_headers()).json(),
        'position': 1,
        'commit_id': pull['head']['sha']
    }


def check_prefix(pull):
    errors = []
    title = pull['title'].split()
    prefix = title[0].split('-')
    pref = prefix[0]
    group = prefix[1]
    if len(prefix) != 2:
        return False
    if pref not in PREFIXES:
        errors.append("* Pull Request title must start with prefix in {}".format(PREFIXES))
    if group not in GROUPS:
        errors.append("* Pull Request title must include group number in {}".format(GROUPS))
    if len(title) < 2 or title[1] not in ACTION:
        errors.append("* Pull Request action must start with {}".format(ACTION))
    return '\n'.join(errors)


def get_users_pulls(username, repos_name, state):
    url = f'https://api.github.com/repos/{username}/{repos_name}/pulls'
    pulls = requests.get(url, headers=prepare_headers())
    #print(pulls.status_code)
    return pulls.json()


def get_all_commits(pull):
    all_commits = requests.get(pull['commits_url'], headers=prepare_headers())
    return all_commits


def verify(pull):
    commits = []
    all_commits = get_all_commits(pull)
    #print(all_commits)
    for param in all_commits.json():
        comment = check_prefix(param['commit'], ['message'])
        if len(comment) > 0:
            commits.append(comment)
            #print(commit)
        if len(commits) != 0:
            commits.insert(0, f"# Incorrect Pull Commit")
            print(send_pull_comment(usernames[0], pull, '\n'.join(commits)))


def send_pull_comment(pull, comment):
    url = pull['url'] + '/comments'
    post = requests.post(url, headers=prepare_headers(), data=json.dumps(prepare_body(pull, comment)))
    return pull['html_url']


def convert_string_to_date(date):
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    return datetime.strptime(date, date_format)


def get_date_of_comment(pull, author):
    r = requests.get(pull['review_comments_url'], headers=prepare_headers()).json()
    if len(r) > 0:
        if r[-1]['user']['login'] == author:
            return convert_string_to_date([-1]['created_at'])
    return None


def get_date_of_commit(pull):
    return convert_string_to_date(pull['commit']['author']['date'])


def compare_commits(pull, date):
    comments = list()
    all_commits = get_all_commits(pull)
    for commit in all_commits:
        if get_date_of_comment(commit) > date:
            comment = check_prefix(commit['commit']['message'])
            if len(comment) > 0:
                comments.append(comment)
    if len(comments) != 0:
        comments.insert(0, f"Incorrect comment")
        send_pull_comment(pull, '\n\n'.join(comments))


if __name__ == '__main__':
    repos_name = 'python_au'
    usernames = ['asapxaniety', 'alexarlord-boop', 'Vasis3038']
    state = 'open'
    #for user in usernames:
        #pulls = get_users_pulls(user, repos_name, state)
        #for param in pulls:
            #verify(param)
    name = 'asapxaniety'
    date_of_comment = get_date_of_comment(name)
    if date_of_comment is not None:
        compare_commits(name, date_of_comment)
    else:
        verify(name)