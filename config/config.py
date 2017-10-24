import json
import os
from typing import List, NamedTuple


class Config(NamedTuple):
    api_base_url: str
    path_html5_comment_generator: str
    execute_command: List[str]
    highlight: List[str]

    @property
    def path_xml_html5_comment_generator(self):
        return os.path.join(self.path_html5_comment_generator, 'comment.xml')


def generate_from_file(path):
    info = json.load(open(path, encoding='utf-8'))
    return Config(
        api_base_url=info['api_base_url'],
        path_html5_comment_generator=info['path_html5_comment_generator'],
        execute_command=info['execute_command'],
        highlight=info['highlight'],
    )
