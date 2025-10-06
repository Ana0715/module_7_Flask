import requests

# 1

git_url = 'https://api.github.com/users/{username}/repos'

def main():
    username = input('Введите имя пользователя GitHub: ')
    if not username:
        return 'Ошибка: имя пользователя не указано'
    
    repos = get_repos(username)

    if isinstance(repos, list):
        info = analyze_repos(repos=repos, username=username)
        return info
    elif isinstance(repos, str) and '403' in repos:
        return f'Ошибка: превышен лимит запросов к API. Попробуйте позже.'
    else:
        return f'Ошибка при получении данных: {repos}'


def get_repos(username):
    try:
        formatted_url = git_url.format(username=username)
        response = requests.get(formatted_url)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return 'Ошибка: пользователь не найден'
        elif response.status_code == 403:
            return 'Ошибка 403: превышен лимит запросов'
        else:
            return f'Ошибка {response.status_code}: {response.reason}'
        
    except requests.exceptions.RequestException as e:
        return f'Ошибка: {str(e)}'


def analyze_repos(repos, username):
    repos_length = len(repos)
    count_stars = 0
    max_stars = 0
    most_starred_repo = ''
    language_count = {}

    for repo in repos:
        count_stars += repo['stargazers_count']

        if repo['stargazers_count'] > max_stars:
            max_stars = repo['stargazers_count']
            most_starred_repo = repo['name']

        language = repo.get('language', 'Unknown')
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1


    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    top_languages = '\n'.join([f'- {lang}: {count} repos' for lang, count in sorted_languages[:3]])

    return f'''
Аналитика профиля GitHub: {username}
{'-'*40}
Количество публичных репозиториев: {repos_length}
Общее количество звёзд: {count_stars}
Самый популярный репозиторий: {most_starred_repo} (⭐ {max_stars} звёзд)
Топ языков программирования: 
{top_languages}
'''

print(main())





# 2

harry_potter_url = 'https://potterapi-fedeperin.vercel.app/en/{value}'

def hp_main():
    value = (input('О чем вы хотите узнать? (Введите: books, characters или spells):')).lower()

    if not value.strip():
        return 'Ошибка: ввод не может быть пуст.'
    
    if value not in ['books', 'characters', 'spells']:
        return 'Ошибка: неверное значение. Допустимые значения: books, characters, spells'

    try: 
        data = get_hp_data(value)
        if isinstance(data, dict) or isinstance(data, list):
            result = formatted_data(data, value)
            return '\n'.join(result)
        else:
            return f'Ошибка при получении данных: {data}'
    except Exception as e:
        return f'Ошибка: {str(e)}'
    

def get_hp_data(value):
    try:
        formatted_url = harry_potter_url.format(value=value)
        response = requests.get(formatted_url)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            return 'Ошибка 403: превышен лимит запросов'
        elif response.status_code == 404:
            return 'Ошибка 404: ресурс не найден'
        else:
            return f'Ошибка {response.status_code}: {response.reason}'
        
    except requests.exceptions.RequestException as e:
        return f'Ошибка: {str(e)}'


def formatted_data(data, category):
    data_list = []
    if category == 'books':
        for book in data:
            data_list.append(f'''
            {'-'*40}
            Номер книги: {book.get('number', 'N/A')}, 
            Название: {book.get('originalTitle', 'N/A')},
            Дата публикации: {book.get('releaseDate', 'N/A')},
            Количество страниц: {book.get('pages', 'N/A')}
            ''')
           
    elif category == 'characters':
        for char in data:
            data_list.append(f'''
            {'-'*40}
            Полное имя персонажа: {char.get('fullName', 'N/A')}, 
            Имя актёра: {char.get('interpretedBy', 'N/A')}
            ''')

            
    elif category == 'spells':
        for spell in data:
            data_list.append(f'''
            {'-'*40}
            Название заклинания: {spell.get('spell', 'N/A')}, 
            Описание заклинания: {spell.get('use', 'N/A')}
            ''')

    return data_list

print(hp_main())

