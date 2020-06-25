"""Provides a directive which creates a link to open a notebook in JupyterHub
."""

import yaml
import pathlib

from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

config_path = pathlib.Path(__file__).parent / '../book/_config.yml'

with config_path.open() as fileobj:
    config = yaml.load(fileobj, Loader=yaml.Loader)


class jupyterhublink(nodes.General, nodes.Element):
    pass


def visit_jupyterhublink_node(self, node):
    pass


def depart_jupyterhublink_node(self, node):
    pass


def make_jupyterhub_launch_url(jupyterhub_url, repo_url, path_to_notebook):
    tree = repo_url.split('/')[-1]
    return f"{jupyterhub_url}/hub/user-redirect/git-pull?repo={repo_url}&urlpath=tree/{tree}/{path_to_notebook}"


class JupyterHubLinkDirective(SphinxDirective):

    has_content = False
    required_arguments = 1

    def run(self):
        node = jupyterhublink()

        url = make_jupyterhub_launch_url(
                config['launch_buttons']['jupyterhub_url'],
                config['repository']['url'],
                self.arguments[0]
                )

        link = f"<a href=\"{url}\" target=\"_blank\">Launch in JupyterHub</a>"

        self.content = [link]
        self.state.nested_parse(self.content, 0, node)

        return [node]


def setup(app):
    app.add_node(jupyterhublink,
                 html=(visit_jupyterhublink_node, depart_jupyterhublink_node),
                 latex=(visit_jupyterhublink_node, depart_jupyterhublink_node),
                 text=(visit_jupyterhublink_node, depart_jupyterhublink_node))

    app.add_directive('jupyterhublink', JupyterHubLinkDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

