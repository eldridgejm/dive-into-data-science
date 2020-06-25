# adapted from https://www.sphinx-doc.org/en/master/development/tutorials/todo.html
from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective


class jupytertip(nodes.Admonition, nodes.Element):
    pass


class jupytertiplist(nodes.General, nodes.Element):
    pass


def visit_jupytertip_node(self, node):
    self.visit_admonition(node)


def depart_jupytertip_node(self, node):
    self.depart_admonition(node)


class JupyterTiplistDirective(Directive):

    def run(self):
        return [jupytertiplist('')]


class JupyterTipDirective(SphinxDirective):

    # this enables content in the directive
    has_content = True

    def run(self):
        targetid = 'jupytertip-%d' % self.env.new_serialno('jupytertip')
        targetnode = nodes.target('', '', ids=[targetid])

        jupytertip_node = jupytertip('\n'.join(self.content))
        jupytertip_node += nodes.title(_('Jupyter Tip'), _('Jupyter Tip'))
        jupytertip_node.set_class('jupytertip')
        self.state.nested_parse(self.content, self.content_offset, jupytertip_node)

        if not hasattr(self.env, 'jupytertip_all_jupytertips'):
            self.env.jupytertip_all_jupytertips = []


        self.env.jupytertip_all_jupytertips.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'jupytertip': jupytertip_node.deepcopy(),
            'target': targetnode,
        })

        return [targetnode, jupytertip_node]


def purge_jupytertips(app, env, docname):
    if not hasattr(env, 'jupytertip_all_jupytertips'):
        return

    env.jupytertip_all_jupytertips = [jupytertip for jupytertip in env.jupytertip_all_jupytertips
                          if jupytertip['docname'] != docname]


def process_jupytertip_nodes(app, doctree, fromdocname):
    # Replace all jupytertiplist nodes with a list of the collected jupytertips.
    # Augment each jupytertip with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'jupytertip_all_jupytertips'):
        env.jupytertip_all_jupytertips = []

    for node in doctree.traverse(jupytertiplist):
        content = []

        for jupytertip_info in env.jupytertip_all_jupytertips:
            para = nodes.paragraph()
            filename = env.doc2path(jupytertip_info['docname'], base=None)
            description = (
                _('(The original entry can be found ')
            )
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = jupytertip_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, jupytertip_info['docname'])
            newnode['refuri'] += '#' + jupytertip_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the jupytertiplist
            content.append(jupytertip_info['jupytertip'])
            content.append(para)

        node.replace_self(content)


def setup(app):
    app.add_node(jupytertiplist)
    app.add_node(jupytertip,
                 html=(visit_jupytertip_node, depart_jupytertip_node),
                 latex=(visit_jupytertip_node, depart_jupytertip_node),
                 text=(visit_jupytertip_node, depart_jupytertip_node))

    app.add_directive('jupytertip', JupyterTipDirective)
    app.add_directive('jupytertiplist', JupyterTiplistDirective)
    app.connect('doctree-resolved', process_jupytertip_nodes)
    app.connect('env-purge-doc', purge_jupytertips)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
