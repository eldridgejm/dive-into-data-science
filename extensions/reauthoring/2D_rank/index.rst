.. _2D-question:

************
2D Questions
************

This extension allows the inclusion of a ranking widget that uses a
two-dimensional plane to rank to questions simultaneously. For example, imagine
that you want to know how stimulating and useful the user perceived certain
page. You can ask these two questions together as follows:

.. xy-click:: two-question-widget-id
   :top: Very stimulating
   :bottom: Not at all stimulating
   :left: Useless
   :right: Very useful
   :size: 250px

The user then clicks anywhere in the 2D space and two numbers in the range
[-100,100] are computed for each dimension and sent as events.

The widget above is inserted by the following source code::

  .. xy-click:: two-question-widget-id
     :top: Very stimulating
     :bottom: Not at all stimulating
     :left: Useless
     :right: Very useful
     :size: 250px

All five configuration variables can also be defined in the configuration file
``conf.py`` so that they apply to all the 2D questions in a document. The
definitions in the text will take preference over those in the configuration
file. The names and default values of these variable are:

xy_click_top_label:
  Label to place at the top/center of the widget (default: TOP LABEL)

xy_click_bottom_label:
  Label to place at the bottom/center of the widget (default: BOTTOM LABEL)

xy_click_left_label:
  Label to place at the left/middle of the widget (default: LEFT LABEL)

xy_click_right_label:
  Label to place at the right/middle of the widget  (default: RIGHT LABEL)

xy_click_grid_size:
  Size of the grid image (default: 300px)


The options used in the example can be included in the configuration file as::

  xy_click_top_label = 'Very stimulating'
  xy_click_bottom_label = 'Not a all stimulating'
  xy_click_left = 'Useless'
  xy_click_right = 'Very useful'
  xy_click_size = '250px'
