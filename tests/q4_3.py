test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You have not set the fixed_products variable.
          >>> 'fixed_products' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You have not set the fixed_products variable.
          >>> fixed_products is ...
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # fixed_products should be an array.
          >>> isinstance(fixed_products, np.ndarray)
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
