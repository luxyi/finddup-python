#!/usr/bin/python

import os


class File(object):

    def __init__(self, abs_path):
        self.abs_path = abs_path


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