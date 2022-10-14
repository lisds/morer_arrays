test = {
  'name': 'Question 5_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The decrease should be a positive number.
          >>> biggest_decrease > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: biggest decrease is above 30, but not 47.
          >>> 30 <= biggest_decrease < 47
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(biggest_decrease,
          ...            np.abs(np.min(np.diff(waiting_times))))
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
