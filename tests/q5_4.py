test = {
  'name': 'Question 5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 15 <= average_error <= 25
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_error = np.abs(np.diff(waiting_times))
          >>> np.isclose(average_error, np.mean(my_error))
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
