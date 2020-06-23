**********
Activities
**********

The use of reStructuredText in combination with Sphinx allows for a very simple
use of *templates* for certain learning resources. A template is simply a
skeleton with a tentative structure that needs to be expanded or completed by
the final user.

The term activity is here applied in the context of learning, and refers to a
set of steps or procedure that is required from the students that may require
between a few minutes to up to two hours. In other words, students may need to
work on several activities to prepare a session, and a reasonably high amount
of activities would be included in a full course (whatever this means to you).

The document pointed by the following link is the rendering of the
:download:`activity template <activity_template.rst>`. Things to take into
account with the template:

- The directive `.. rst-class::activity` is used to detect its structure.

- The directive `.. iguide::` is used to do conditional processing. Some parts
  of the document will be included/excluded depending on some configuration
  options. This is not used in this example.

- The labels `.. rst-class::` followed by a name are to identify specific
  sections and render them with special icons in the HTML page. You can try to
  remove/insert these lines and see the effect in the final page.

- The directive `.. activity-duration::` is followed by the number of minutes
  that the author assumes it should be needed. This is rendered in HTML as a
  pull down menu with 7 options (automatically calculated). With a more
  sophisticated configuration the data can be captured by another application
  for further study.

.. toctree::
   
   activity_template


