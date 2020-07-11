from docutils import nodes

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

def generic_visit_admonition(self, node):
    self.visit_admonition(node)
def generic_depart_admonition(self, node):
    self.depart_admonition(node)

class jupytertip(nodes.Admonition, nodes.Element):
    pass

class JupyterTip(SphinxDirective):

    has_content = True

    def run(self):
        jupytertip_node = jupytertip('\n'.join(self.content))
        jupytertip_node += nodes.title(_('Jupyter Tip'), _('Jupyter Tip'))
        jupytertip_node.set_class('jupytertip')
        self.state.nested_parse(self.content, self.content_offset, jupytertip_node)

        return [jupytertip_node]

def setup(app):

    app.add_node(
        jupytertip,
        html=(generic_visit_admonition, generic_depart_admonition),
        latex=(generic_visit_admonition, generic_depart_admonition),
        text=(generic_visit_admonition, generic_depart_admonition)
    )
    app.add_directive('jupytertip', JupyterTip)


    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }