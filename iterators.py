import json


class wikiChecker():
    def __init__(self):
        with open('countries.json', encoding='utf-8') as c:
            self.countries = json.load(c)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == len(self.countries):
            raise StopIteration
        self.current += 1
        return self.countries[self.current - 1]['translations']['rus']['common']

    def create_html_file(self, file_name):
        with open(file_name + '.html', 'w', encoding='utf-8') as f:
            for country_name in self:
                f.write(f'<p><a href=\'http://ru.wikipedia.org/wiki/{country_name}\'>{country_name}</a></p>\n')
        pass

    def create_txt_file(self, file_name):
        with open(file_name + '.txt', 'w', encoding='utf-8') as f:
            for country_name in self:
                f.write(f'{country_name}: \'http://ru.wikipedia.org/wiki/{country_name}\'\n')
        pass


if __name__ == '__main__':
    txt_checker = wikiChecker()
    txt_checker.create_txt_file('txt')