#!/usr/bin/python3

import sys


LEETCODE_END_MD_LINKS = '<!---end_templates--->'


class LeetCodeSolution:
    def __init__(self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link = link.rstrip('\n')
        self.code = code

def __str__(self):
    return 'title = {}, link = {}, code = {}'.format(self.title, self.link, self.code)

def get_md_formatted_solution(self):
    return '```python\n{}```'.format('\n'.join(map(lambda x: x.rstrip('\n')[4:], self.code)))

def get_md_title(self):
    return '## {}'.format(self.title)

def get_md_solution_link(self):
    return '+ [{}](#{})'.format(self.title, self.link[9:-1])

def get_md_formatted_code(self):
    return (self.get_md_solution_link(),
'{}\n\n{}\n\n{}'.format(self.get_md_title(), self.link, self.get_md_formatted_code()))


def read_all_lines_from_file(file_name):
    file = open(file_name)
    result = file.readlines()
    file.close()
    return result


def write_to_md(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def read_all_file(file_name):
    file = open(file_name)
    result = file.read()
    file.close()
    return result


def merge_solutions(old_solution, new_solution):
    old_splitted = old_solution.split(LEETCODE_END_MD_LINKS)
    if len(old_splitted == 1):
        return new_solution
    return '{}{}{}'.format(old_splitted[0], new_solution, old_splitted[1])


def main(src, dst):
    in_text = read_all_lines_from_file(src)
    solution = LeetCodeSolution(in_text[0], in_text[1], in_text[3:])
    new_solution = solution.get_md_formatted_solution()
    old_solution = read_all_file(dst)
    result = merge_solutions(old_solution, new_solution)
    write_to_md(dst, result)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
