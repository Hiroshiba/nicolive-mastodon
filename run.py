import datetime
import subprocess
from typing import NamedTuple
from mastodon import Mastodon, StreamListener
import xml.etree.ElementTree as ET

from config import generate_from_file
from utility import strip_html_tags


class Comment(NamedTuple):
    user: str
    html_text: str
    unix_time: int
    icon_url: str

    @property
    def text(self) -> str:
        return strip_html_tags(self.html_text)


def construct_execute_command(execute_command_format: str, comment: Comment):
    return execute_command_format.format(
        user=comment.user,
        text=comment.text,
        unix_time=comment.unix_time,
    )


class Runner(StreamListener):
    def __init__(self, config):
        self.config = config
        self.highlight_list = self.config.highlight
        self.path_xml = self.config.path_xml_html5_comment_generator

        self.mastodon = Mastodon(
            client_id='hiho_bot_app.secret',
            access_token='hiho_karuta.secret',
            api_base_url='https://friends.nico',
        )

    def make_comment(self, toot):
        user = toot['account']['display_name']
        icon_url = toot['account']['avatar']
        text = toot['content']

        ok = False
        if self.highlight_list is None or len(self.highlight_list) == 0:
            ok = True
        for highlight in self.highlight_list:
            if highlight in text:
                ok = True

        if not ok:
            return None

        unix_time = int(datetime.datetime.now().timestamp())
        return Comment(user, text, unix_time, icon_url)

    def make_xml_element(self, root_xml, comment: Comment):
        last_no = int(list(root_xml)[-1].attrib['no'])
        attr = dict(
            no=str(last_no + 1),
            time=str(comment.unix_time + 3),
            handle=comment.user,
        )
        element = ET.Element('comment', attrib=attr)
        element.text = "<img src='{}'>".format(comment.icon_url) + comment.text
        return element

    def on_update(self, toot):
        comment = self.make_comment(toot)
        if comment is None:
            return

        # execute command
        for f in self.config.execute_command:
            subprocess.run(construct_execute_command(f, comment).split(' '))

        # get last number of xml
        tree = ET.parse(self.path_xml)
        root_xml = tree.getroot()
        element = self.make_xml_element(root_xml, comment)

        # add xml
        root_xml.append(element)
        tree.write(self.path_xml, encoding='utf-8')

    def run(self):
        self.mastodon.local_stream(self)


path_config = "./config.json"
config = generate_from_file(path_config)

runner = Runner(
    config=config,
)
runner.run()
