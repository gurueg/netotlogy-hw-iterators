import hashlib

def create_generator(file_path):
    for line in open(file_path, 'r', encoding='utf-8'):
        yield hashlib.md5(bytes(line, encoding='utf-8'))