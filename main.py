from iterators import wikiChecker
from generators import create_generator

if __name__ == '__main__':
    my_wiki = wikiChecker()
    my_wiki.create_html_file('result')

    my_gen = create_generator('test.txt')
    for val in my_gen:
        print(val.hexdigest)