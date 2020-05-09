import argparse
import os
import fs
from pcloud import PyCloud
import urllib.parse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('username', type=str)
    parser.add_argument('passwd', type=str)
    parser.add_argument('filepath', type=str)

    args = parser.parse_args()

    username = urllib.parse.quote_plus(args.username)
    password = urllib.parse.quote_plus(args.passwd)

    local_fs = fs.open_fs('./') # save to current directory
    remote_path = args.filepath
    local_path = os.path.split(args.filepath)[1]

    with fs.opener.open_fs('pcloud://{0}:{1}@/'.format(username, password)) as pcloud_fs:
        fs.copy.copy_file(pcloud_fs, remote_path, local_fs, local_path)
        # pcloud_fs.makedirs(path='/backup/second_level/third_level', recreate=True)
        # fs.copy.copy_dir(pcloud_fs, "", local_fs, "")
