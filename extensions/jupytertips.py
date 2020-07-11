# adapted from https://www.sphinx-doc.org/en/master/development/tutorials/todo.html
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective


class jupytertip(nodes.Admonition, nodes.Element):
    pass


class jupytertiplist(nodes.General, nodes.Element):
    pass

class tiplist(nodes.General, nodes.Element):
    pass

def visit_jupytertip_node(self, node):
    self.visit_admonition(node)


def depart_jupytertip_node(self, node):
    self.depart_admonition(node)


class JupyterTiplistDirective(Directive):

    def run(self):
        return [jupytertiplist('')]

class TiplistDirective(Directive):

    def run(self):
        return [tiplist('')]


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

class TipDirective(directives.admonitions.Tip, SphinxDirective):
    """
    Extending the Tip directive so we can make a tip list.
    """

    # this enables content in the directive
    has_content = True

    def run(self):

        tip_node = super().run()[0]

        targetid = 'tip-%d' % self.env.new_serialno('tip')
        targetnode = nodes.target('', '', ids=[targetid])

        if not hasattr(self.env, 'tip_all_tips'):
            self.env.tip_all_tips = []

        self.env.tip_all_tips.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'tip': tip_node.deepcopy(),
            'target': targetnode,
        })

        return [targetnode, tip_node]


def purge_jupytertips(app, env, docname):
    if hasattr(env, 'jupytertip_all_jupytertips'):
        env.jupytertip_all_jupytertips = [jupytertip for jupytertip in env.jupytertip_all_jupytertips
                            if jupytertip['docname'] != docname]
    
    if hasattr(env, 'tip_all_tips'):
        env.tip_all_tips = [tip for tip in env.tip_all_tips
                            if tip['docname'] != docname]



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




    if not hasattr(env, 'tip_all_tips'):
        env.tip_all_tips = []

    for node in doctree.traverse(tiplist):
        content = []

        for tip_info in env.tip_all_tips:
            para = nodes.paragraph()
            filename = env.doc2path(tip_info['docname'], base=None)
            description = (
                _('(The original entry can be found ')
            )
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = tip_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, tip_info['docname'])
            newnode['refuri'] += '#' + tip_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the tiplist
            content.append(tip_info['tip'])
            content.append(para)

        node.replace_self(content)



def setup(app):
    app.add_node(jupytertiplist)
    app.add_node(tiplist)
    app.add_node(jupytertip,
                 html=(visit_jupytertip_node, depart_jupytertip_node),
                 latex=(visit_jupytertip_node, depart_jupytertip_node),
                 text=(visit_jupytertip_node, depart_jupytertip_node))

    app.add_directive('jupytertip', JupyterTipDirective)
    app.add_directive('tip', TipDirective)
    app.add_directive('jupytertiplist', JupyterTiplistDirective)
    app.add_directive('tiplist', TiplistDirective)
    app.connect('doctree-resolved', process_jupytertip_nodes)
    app.connect('env-purge-doc', purge_jupytertips)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
