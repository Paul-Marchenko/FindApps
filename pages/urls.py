MAIN_URL = 'https://dou.ua/'
JOBS_URN = 'https://jobs.dou.ua/'
POSITION_URN = 'https://jobs.dou.ua/vacancies/?category=QA'


def main_url(path=None):
    if path is not None:
        return f'https://dou.ua/{path}'
    return 'https://dou.ua/'

