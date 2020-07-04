from docutils import nodes
from docutils.parsers.rst import roles

from sphinx import addnodes
# from sphinx.domains.std import Glossary, make_glossary_term
from sphinx.util.docutils import ReferenceRole
from sphinx.util.nodes import process_index_entry


class DtermRole(ReferenceRole):

    def run(self):

#         print(f"""
# *******************
# *** {self.target}
# *** {self.env.docname}
# *** {self.env.app.builder.get_relative_uri(self.env.docname, 'glossary')}
# *******************
#         """)
#         1/0

        term = self.target # This way we can still specify :term:`word <target>`
        
        page_title = self.inliner.document.next_node(nodes.title)[0].astext()

        target_id = 'index-%s' % self.env.new_serialno('index')
        indexnode = addnodes.index(entries=process_index_entry(
            f"single: {term}; {page_title}",
            target_id
        ))
        target = nodes.target('', '', ids=[target_id])

        rendered = nodes.Text(self.title)

        canon_term = nodes.make_id(term)
        base_uri = self.env.app.builder.get_relative_uri(self.env.docname, 'glossary')
        reference_uri = f"{base_uri}#term-{canon_term}"
        reference = nodes.reference('', rendered, refuri=reference_uri)
        text_node = nodes.strong('', '', reference)

        return [indexnode, target, text_node], []
        

def setup(app):

    roles.register_local_role("dterm", DtermRole())

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
