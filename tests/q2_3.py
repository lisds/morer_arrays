test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You have not set the with_commas variable.
          >>> 'with_commas' in vars()
          True
          >>> # You have not set the without_commas variable.
          >>> 'without_commas' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have not set the with_commas variable.
          >>> with_commas is ...
          False
          >>> # You have not set the without_commas variable.
          >>> without_commas is ...
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
