
import os

import finddup


def test_folder_get_files():
    base_path = os.path.join('tests', 'data')

    folder = finddup.Folder(base_path)
    actual = folder.get_files()

    expect_abs_paths = [
        os.path.join(base_path, 'file1.txt'),
        os.path.join(base_path, 'file2.txt'),
        os.path.join(base_path, 'folder1', 'file11.txt'),
        os.path.join(base_path, 'folder1', 'folder11', 'file111.txt'),
        os.path.join(base_path, 'folder1', 'folder12', 'file121.txt'),
        os.path.join(base_path, 'folder1', 'folder13', 'file131.txt'),
        os.path.join(base_path, 'folder2', 'file21.txt'),
    ]
    actual_abs_paths = [i.abs_path for i in actual]
    assert actual_abs_paths == expect_abs_paths
