.. _Embedded-MCQ:

***************************
Questions Embedded in Notes
***************************

These extensions insert several question types in the middle of the text with
their automatic assessment. Students can check the answer immediately. The kit
supports the following type of questions:

- Multiple choice with one correct answer.
- Fill in the blank (fixed answer)

Multiple Choice with One Correct Answer
=======================================

The directive to insert a multiple choice question with a single correct answer
is::

  .. eqt:: COD-integerencoding-videoeqt-eqt_11

     **Question 1** What is the representation of the number -127 in 2s
     complement with 8 bits?

     A) :eqt:`I` `1000 0000`
        :expl:`Explanation of why this one is incorrect`

     #) :eqt:`I` `1111 1111`

     #) :eqt:`C` `1000 0001`
        :expl:`Explanation of why this is correct this time`

     #) :eqt:`I` None of the above
        :expl:`Well no! Try again...`

     .. eqt-solution:: This is the solution.

        It can span on several lines, and contain other nodes, like:

        - Bullet lists
        - Images
        - etc.

Make sure the string that follows the `.. eqt::` directive is unique throughout
your documents. Can you spot which answer is marked as the correct one? After
processing, the result is:

.. eqt:: COD-integerencoding-videoeqt-eqt_11

   **Question 1** What is the representation of the number -127 in 2s
   complement with 8 bits?

   A) :eqt:`I` `1000 0000`
      :expl:`Explanation of why this one is incorrect`

   #) :eqt:`I` `1111 1111` (has no explanation)

   #) :eqt:`C` `1000 0001`
      :expl:`Explanation of why this is correct this time`

   #) :eqt:`I` None of the above
      :expl:`Well no! Try again...`

   .. eqt-solution:: This is the solution.

      It can span on several lines, and contain other nodes, like:

      - Bullet lists
      - Images
      - etc.

Go ahead, answer it! The question is translated to the proper HTML, the right
scripts inserted, and everything handled properly as specified by the
markup.

Check the following document for an example of a file containing **only**
questions of this type.

.. toctree::

   sample_eqt

Multiple Choice with Multiple Answers Correct
=============================================

The directive to insert a multiple choice question with multiple correct
answers is::

  .. eqt-mc:: COD-hexanane-11

     **Question 1** How is the base with 16 symbols called?

     A) :eqt:`I` Strange

     #) :eqt:`C` Hexadecimal

     #) :eqt:`I` Hexagonal

     #) :eqt:`C` Base 16

Remember that the string that follows the `.. eqt-mc::` directive must be
unique throughout your documents. The correct choices are marked as in the
previous case. The result is:

.. eqt-mc:: COD-hexanane-11

   **Question 1** How is the base with 16 symbols called?

   A) :eqt:`I` Strange
      :expl:`Well, obviously not`

   #) :eqt:`C` Hexadecimal
      :expl:`Great! Another one is true ;)`

   #) :eqt:`I` Hexagonal
      :expl:`This is not a geometry class!`

   #) :eqt:`C` Base 16

   .. eqt-solution:: This is the solution.

Fill in the Blank
=================

The directive to insert these questions is almost identical to the previous one
with a slight difference in the first line and the way you specify the answer::

  .. eqt-fib:: COD-integerencoding-sequence-11

     **Question 1** What is the representation of the number -127 in 2s
     complement with 8 bits?

     :eqt:`10000001`

The rendering of the directive is:

.. eqt-fib:: COD-integerencoding-sequence-11

   **Question 1** What is the representation of the number -127 in 2s
   complement with 8 bits?

   :eqt:`10000001`

   .. eqt-solution:: This is the solution.

The answer is case sensitive. Thus, if you use it for a string, make sure the
answer is the obvious one with respect to case.

