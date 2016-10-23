
import os

import finddup


_BASE_DIR = os.path.dirname(__file__)


def test_create_profile():
    profile_file_path = os.path.join(_BASE_DIR, '..', 'Pictures.properties')
    root_dir = 'tests/data/root_dir'

    if os.path.exists(profile_file_path):
        os.unlink(profile_file_path)

    assert not os.path.exists(profile_file_path)

    finddup.Profile('Pictures', root_dir)

    assert os.path.exists(profile_file_path)
    lines = []
    with open(profile_file_path, 'rb') as f:
        for line in f:
            lines.append(line)

    assert len(lines) == 1
    assert lines[0] == '/rootdir={}{}'.format(root_dir, os.linesep)

    os.unlink(profile_file_path)


def test_load_profile():
    profile_file_path = os.path.join(_BASE_DIR, '..', 'Pictures.properties')
    root_dir = 'tests/data/root_dir'

    if os.path.exists(profile_file_path):
        os.unlink(profile_file_path)

    with open(profile_file_path, 'wb') as f:
        line = '/rootdir={}'.format(root_dir)
        f.write(line+os.linesep)

    assert os.path.exists(profile_file_path)

    profile = finddup.Profile('Pictures')

    assert profile.root_dir == root_dir

    os.unlink(profile_file_path)
