test = {
  'name': 'Question 4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You have not set the products variable.
          >>> 'products' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have not set the products variable.
          >>> products is ...
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Products should be an array.
          >>> isinstance(products, np.ndarray)
          True
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
