
import os

import finddup


def test_generate_hash_code():
    abs_path = os.path.join('tests', 'data', 'file1.txt')
    f = finddup.File(abs_path)
    assert f.hash_code is None
    f.generate_hash_code()
    expected = '88cd4913928bef2a5d9b8def93579322cf3459a4'
    assert f.hash_code is not None
    assert f.hash_code == expected
