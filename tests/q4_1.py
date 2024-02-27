test = {
  'name': 'Question 4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You have not set the first_product variable.
          >>> 'first_product' in vars()
          True
          >>> # You have not set the second_product variable.
          >>> 'second_product' in vars()
          True
          >>> # You have not set the third_product variable.
          >>> 'third_product' in vars()
          True
          >>> # You have not set the fourth_product variable.
          >>> 'fourth_product' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have not set the fourth_product variable.
          >>> fourth_product is ...
          False
          """,
          'hidden': False,
          'locked': False
        },

      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
