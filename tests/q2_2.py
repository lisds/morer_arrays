test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You have not set the weird_numbers variable.
          >>> 'weird_numbers' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have not set the weird_numbers variable.
          >>> weird_numbers is ...
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> # It looks like you didn't make an array.
          >>> type(book_title_words) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you included commas in the text.
          >>> # The three pieces of text in the array should be:
          >>> #   "Eats"
          >>> #   "Shoots"
          >>> #   "and Leaves"
          >>> not any([',' in text for text in book_title_words])
          True
          >>> # It looks like you didn't include both words in the
          >>> # last piece of text.  It should be the actual string:
          >>> #   "and Leaves"
          >>> 'and ' in book_title_words.item(2)
          True
          >>> np.all(book_title_words == ['Eats', 'Shoots', 'and Leaves'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
