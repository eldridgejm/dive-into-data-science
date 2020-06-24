"""Create a question along with a hidden answer.

Use
---

```{hiddenanswer}
---
question: This is the question.
answer: This is the answer.
```

"""
from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective


class hiddenanswer(nodes.General, nodes.Element):
    pass


def visit_hiddenanswer_node(self, node):
    pass


def depart_hiddenanswer_node(self, node):
    pass


class HiddenAnswerDirective(SphinxDirective):

    has_content = True
    optional_arguments = 0

    option_spec = {
        'question': str,
        'answer': str
    }

    def run(self):
        node = hiddenanswer()

        print(self.options)

        s = f"""
```````{{tabs}}
``````{{tab}} Question

{self.options['question']}
``````
``````{{tab}} Answer

{self.options['answer']}
``````

```````
        """

        self.content = [s]
        self.state.nested_parse(self.content, 0, node)

        return [node]


def setup(app):
    app.add_node(hiddenanswer,
                 html=(visit_hiddenanswer_node, depart_hiddenanswer_node),
                 latex=(visit_hiddenanswer_node, depart_hiddenanswer_node),
                 text=(visit_hiddenanswer_node, depart_hiddenanswer_node))

    app.add_directive('hiddenanswer', HiddenAnswerDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

