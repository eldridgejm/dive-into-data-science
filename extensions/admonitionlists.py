# General Logic
# -------------
# 
# For each supported Admonition directive class, we:
# 1. Create and register the class for the list node
# 2. Extend and re-register the Admonition
#    - The run function is rewritten to call the super in order to create the
#      content node, and then additionally create the target node and add itself
#      to a variable in the Builder environment.
# 3. Create and register the class for the list directive
# 
# Then we connect Process and Purge functions to the app, just like in the
# Sphinx TodoList tutorial.
# https://www.sphinx-doc.org/en/master/development/tutorials/todo.html
# 

# Explanation Of Generalized Admonition Lists
# -------------------------------------------
# 
# In `setup`, define a list of Admonition directive classes that we want to
# support listing.
# 
# If supported, a new directive should be added with the name "<admnname>list"
# which will function equivalently to the Todolist example seen in the Sphinx
# docs.
# 
# This means each inputted admonition directive needs to be extended with the
# functionality of the Todo directive, and then re-registered.
# 
# Additionally, the admonitionlist directives need to be created and registered
# for each supported admonition.
# 
# In order to create the run functions, node classes, and directive classes
# unique to each supported admonition, we need to use closures heavily.
# Additionally, we can use an awesome feature of the `type()` function which I
# had no clue about until now:
# 
# We can use type to create new classes -- see the following snippet
# ```
# class Generic():
#   pass
# 
# extended = type(
#   'ExtendedClass',
#   (Generic, othersuperclasses),
#   {
#       'additionalattributes': values
#   }
# )
# ```
# resulting in
# ```
# >>> extended
# <class '__main__.ExtendedClass'>
# ```
# 

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

from jupytertips import JupyterTip

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

from sphinx.util import logging
logger = logging.getLogger(__name__)



class generic_list_node(nodes.General, nodes.Element):
    pass

def create_list_node(Admonition):
    """
    Returns a new generic class for the list node for this Admonition.
    """

    list_node = type(
        Admonition.__name__.lower()+'list_node',
        (generic_list_node, nodes.General, nodes.Element),
        {}
    )
    return list_node



class generic_extended_directive(SphinxDirective):
    has_content = True

def generic_extended_run(Admonition):
    """
    A closure so that the extended_run can reference this Admonition.
    """

    def extended_run(self):
        admn_name = Admonition.__name__.lower()
        admnlist_name = admn_name + 'list'

        admonition_node = Admonition.run(self)[0]

        target_id = f"{admn_name}-%d" % self.env.new_serialno(admn_name)
        target_node = nodes.target('', '', ids=[target_id])

        if not hasattr(self.env, admnlist_name):
            setattr(self.env, admnlist_name, [])

        getattr(self.env, admnlist_name).append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'node': admonition_node.deepcopy(),
            'target': target_node,
        })

        return [target_node, admonition_node]

    return extended_run

def create_extended_directive(Admonition):
    """
    Extends the run function for this Admonition with tracking of occurrences.
    """

    extended_directive = type(
        Admonition.__name__,
        (Admonition, generic_extended_directive),
        {
            'run': generic_extended_run(Admonition)
        }
    )
    return extended_directive



class generic_list_directive(Directive):
    pass

def generic_list_run(list_node):
    def list_run(self):
        return [list_node('')]

    return list_run

def create_list_directive(Admonition, list_node):
    """
    Returns a new class named admonitionlist whose run function calls the
    admonitionlist_node class.
    """

    list_directive = type(
        Admonition.__name__.lower()+'list',
        (generic_list_directive,),
        {
            'run': generic_list_run(list_node)
        }
    )
    return list_directive



def generic_process_admonition_list_nodes(admonitions, list_nodes):
    """
    A closure so that the process_admonition_list_nodes can handle all supported
    Admonition classes.
    """

    def process_admonition_list_nodes(app, doctree, fromdocname):
        """
        Finds all admonitionlist nodes and replaces them with a collection of
        all the admonitions of that type, for all supported Admonition classes.
        """
        
        env = app.builder.env

        # print(f"""
        # ********
        # Processing admonition list nodes
        # ********
        # """)

        for Admonition, list_node in zip(admonitions, list_nodes):

            # print(f"""
            # ********
            # {Admonition}
            # {list_node}
            # ********
            # """)

            admn_name = Admonition.__name__.lower()
            admnlist_name = admn_name + 'list'

            if not hasattr(env, admnlist_name):
                setattr(env, admnlist_name, [])

            for node in doctree.traverse(list_node):
                content = []

                for admn_info in getattr(env, admnlist_name):
                    para = nodes.paragraph()
                    filename = env.doc2path(admn_info['docname'], base=None)
                    description = (
                        _('(The original entry can be found ')
                    )
                    para += nodes.Text(description, description)

                    # Create a reference
                    newnode = nodes.reference('', '')
                    innernode = nodes.emphasis(_('here'), _('here'))
                    newnode['refdocname'] = admn_info['docname']
                    newnode['refuri'] = app.builder.get_relative_uri(
                        fromdocname, admn_info['docname'])
                    newnode['refuri'] += '#' + admn_info['target']['refid']
                    newnode.append(innernode)
                    para += newnode
                    para += nodes.Text('.)', '.)')

                    # Insert the copied node onto the page
                    content.append(admn_info['node'])
                    content.append(para)

                node.replace_self(content)

    return process_admonition_list_nodes

def generic_purge_admonition_lists(admonitions):
    """
    A closure so that the purge_admonition_list_nodes can handle all supported
    Admonition classes.
    """

    def purge_admonition_lists(app, env, docname):

        for Admonition in admonitions:

            admnlist_name = Admonition.__name__.lower() + 'list'

            if hasattr(env, admnlist_name):
                setattr(env, admnlist_name, [
                    admonition for admonition in getattr(env, admnlist_name)
                    if admonition['docname'] != docname
                ])

    return purge_admonition_lists



def setup(app):

    SUPPORTED_ADMONITIONS = [
        JupyterTip,
        directives.admonitions.Tip
    ]


    list_nodes = []
    for Admonition in SUPPORTED_ADMONITIONS:

        list_node = create_list_node(Admonition)
        list_nodes.append(list_node)
        globals()[Admonition.__name__.lower()+'list_node'] = list_node
        app.add_node(list_node)
        # print(f"""
        # ***********
        # {list_node}
        # ***********
        # """)

        extended_directive = create_extended_directive(Admonition)
        app.add_directive(Admonition.__name__.lower(), extended_directive)

        list_directive = create_list_directive(Admonition, list_node)
        app.add_directive(Admonition.__name__.lower()+'list', list_directive)


    app.connect(
        'doctree-resolved',
        generic_process_admonition_list_nodes(SUPPORTED_ADMONITIONS, list_nodes)
    )
    app.connect(
        'env-purge-doc',
        generic_purge_admonition_lists(SUPPORTED_ADMONITIONS)
    )


    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
