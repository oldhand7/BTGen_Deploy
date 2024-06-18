import argparse
import os
import re
import shutil
import subprocess
import sys
from importlib.util import find_spec
from threading import Thread

from btgen_api_version import version
from btgenapi.repositories_versions import btgen_commit_hash

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

python = sys.executable
default_command_live = True
index_url = os.environ.get('INDEX_URL', "")
re_requirement = re.compile(r"\s*([-_a-zA-Z0-9]+)\s*(?:==\s*([-+_.a-zA-Z0-9]+))?\s*")

btgen_name = 'btgen'

btgen_github_repo = 'https://github.com/oldhand7/stable_diffusion_img_gen'

modules_path = os.path.dirname(os.path.realpath(__file__))
script_path = modules_path
dir_repos = "repositories"

if __name__ == "__main__":

    from btgenapi.file_serve_https import start_file_serve

    start_file_serve()
