import requests

TOKEN = '10db12470ec8512d81f372c0750b889ac7bd97fa'

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'VERIFIER']
GROUPS = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Fixed']


def prepare_headers():
    return{
      'Authorization': 'token{}'.format(TOKEN),
      'Accept': "application/vnd.github.v3+json"
        }


def get_lines_from_file():
    f = open('links.txt')
    file = f.readlines()
    f.close()
    return file


def check_message(pull):
    title = pull['title'].split()
    prefix = title[0].split('-')
    pref = prefix[0]
    group = prefix[1]
    if len(prefix) != 2:
        return False
    if pref not in PREFIXES and group not in GROUPS and (len(title) < 2 or title[1] not in ACTION):
        return False
    else:
        return True


def print_pull(file):
    for lines in file:
        line = lines[-1]
        username = line[23:-15]
        print(username)
        all_pulls = requests.get(line)
        print(all_pulls)
        print("* Pull Request title must start with right prefix in {}".format(PREFIXES))
        for pull in all_pulls.json():
            if check_message(pull) is False:
                print(pull['title'])


def verif(file):
    for lines in file:
        line = lines[:-1]
        username = line[23:-15]
        print(username)
        all_pulls = requests.get(line)
        print(all_pulls)
        for param in all_pulls.json():
            print(param['commits_url'])
            commit = requests.get(param['commits_url'])
            for message in commit.json():
                print(message['commit']['message'])


if __name__ == '__main__':
    file = get_lines_from_file()
    verif(file)