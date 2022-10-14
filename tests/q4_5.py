test = {
  'name': 'Question 4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(celsius_temperature_ranges)
          65000
          >>> celsius_temperature_ranges.item(1) == 10
          True
          >>> round(sum(celsius_temperature_ranges)) == 768351
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> min_temperatures = np.array(pd.read_csv("temperatures.csv")["Daily Min Temperature"])
          >>> np.all(celsius_temperature_ranges ==
          ...        celsius_max_temperatures -
          ...        np.round((min_temperatures - 32) * 5 / 9))
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
