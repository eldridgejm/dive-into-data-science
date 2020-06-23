**************************
Embedding Videos in a page
**************************

This extension is to simplify the inclusion of videos already existing in
either YouTube or Vimeo as part of your notes. The videos are included in the
way you usually see them in regular web pages. Here is an example of the markup
you would use in your source files::

  .. embedded-video:: SeoW3YNo3Zs

The string following the two colons is the identifier that YouTube attaches to
any video. You may find this identifier as part of the URL that appears in your
browser when watching it. Here is the result:

.. embedded-video:: SeoW3YNo3Zs

If the video is in Youtube (Vimeo does not offer this functionality), you can
also select just a segment of the video to be presented by optionally
specifying a start and end time (in seconds).  The player will start playing at
the given time, and will stop at the end time.  Here is an example of the
markup you would use to specify only the start of the video segment (at 120
seconds or 2 minutes)::

  .. embedded-video:: SeoW3YNo3Zs 120  
  
Here is an example that specifies both the start and the end of the segment::

  .. embedded-video:: SeoW3YNo3Zs 120 140
  
The result of this last directive is:

.. embedded-video:: SeoW3YNo3Zs 120 140

The directive allows four options:

- `element_id`: The name to assign the HTML element containing the video (`div`
  or `iframe`).

- `height`: height of the video window.

- `width`: width of the video window

- `format`: Either `youtube` or `vimeo` to include videos from either
  platform. The default value is `youtube`. You can also change the value for
  the whole document by setting the variable `embedded_video_format` in the
  `conf.py` file.

Here is an example of a video from Vimeo::

  .. embedded-video:: 130004497
     :format: vimeo

and the result:

.. embedded-video:: 130004497
   :format: vimeo

Multiple Videos in a page
=========================

The following document is an example of a file containing several videos.

.. toctree::

   sample_video

