#!/usr/bin/python

import hashlib
import os

_BASE_DIR = os.path.dirname(__file__)


class File(object):

    def __init__(self, abs_path):
        self.abs_path = abs_path
        self.hash_code = None

    def generate_hash_code(self):
        with open(self.abs_path, 'rb') as f:
            self.hash_code = hashlib.sha1(f.read()).hexdigest()


class Folder(object):

    def __init__(self, abs_path):
        self.__abs_path = abs_path

    def get_files(self):
        folder_files = []
        for root, dirs, files in os.walk(self.__abs_path):
            for i in files:
                abs_path = os.path.join(root, i)
                f = File(abs_path)
                folder_files.append(f)

        def cmp_key(i):
            return i.abs_path

        return sorted(folder_files, key=cmp_key)


class Profile(object):

    _ROOT_DIR = '/rootdir'

    def __init__(self, name, root_dir=None):
        self.__name = name
        self.root_dir = root_dir
        self.__profile_file_name = '{}.properties'.format(self.__name)

        profile_file_path = os.path.join(_BASE_DIR, self.__profile_file_name)
        if os.path.exists(profile_file_path):
            line_no = 0
            with open(profile_file_path, 'rb') as f:
                for line in f:
                    line_no += 1
                    if line_no == 1:
                        parts = line.strip().split('=')
                        if parts[0] == Profile._ROOT_DIR:
                            self.root_dir = parts[1]
                            break
        else:
            with open(profile_file_path, 'wb') as f:
                line = '{}={}'.format(Profile._ROOT_DIR, self.root_dir)
                f.write(line+os.linesep)
