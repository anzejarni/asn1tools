EXPECTED = {'ExtensibilityImplied': {'extensibility-implied': True,
                          'imports': {},
                          'object-classes': {},
                          'object-sets': {},
                          'types': {'Choice': {'members': [{'name': 'a',
                                                            'type': 'INTEGER'}],
                                               'type': 'CHOICE'},
                                    'Choice2': {'members': [{'name': 'a',
                                                             'type': 'INTEGER'},
                                                            '...'],
                                                'type': 'CHOICE'},
                                    'Enum': {'values': {1: 'one',
                                                   2: 'two',
                                                   3: '...'},
                                             'type': 'ENUMERATED'},
                                    'Nested': {'members': [{'members': [{'members': [{'name': 'a',
                                                                                      'type': 'INTEGER'}],
                                                                         'name': 'b',
                                                                         'type': 'CHOICE'}],
                                                            'name': 'a',
                                                            'type': 'SEQUENCE'}],
                                               'type': 'SET'},
                                    'Sequence': {'members': [],
                                                 'type': 'SEQUENCE'},
                                    'Sequence2': {'members': [{'default': 0,
                                                               'name': 'a',
                                                               'type': 'INTEGER'}],
                                                  'type': 'SEQUENCE'},
                                    'Sequence3': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...'],
                                                  'type': 'SEQUENCE'},
                                    'Sequence4': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'b',
                                                               'type': 'BOOLEAN'}],
                                                  'type': 'SEQUENCE'},
                                    'Sequence5': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'b',
                                                               'type': 'BOOLEAN'},
                                                              '...'],
                                                  'type': 'SEQUENCE'},
                                    'Sequence6': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'b',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'c',
                                                               'type': 'BOOLEAN'}],
                                                  'type': 'SEQUENCE'},
                                    'Sequence7': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'b',
                                                               'type': 'BOOLEAN'},
                                                              {'name': 'c',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              {'name': 'd',
                                                               'type': 'BOOLEAN'}],
                                                  'type': 'SEQUENCE'},
                                    'Sequence8': {'members': [{'name': 'a',
                                                               'type': 'BOOLEAN'},
                                                              '...',
                                                              '...'],
                                                  'type': 'SEQUENCE'},
                                    'Set': {'members': [], 'type': 'SET'},
                                    'Set2': {'members': [{'default': 1,
                                                          'name': 'a',
                                                          'type': 'INTEGER'}],
                                             'type': 'SET'}},
                          'values': {}}}