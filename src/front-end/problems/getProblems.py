problems_data = [
    {
        'id': 1,
        'title': 'Problem 1',
        'description': 'Realizar un ciclo for bien fachero',
        'test_cases': [
            {'input': 'test_input_1', 'output': 'expected_output_1'},
            {'input': 'test_input_2', 'output': 'expected_output_2'},
        ]
    },
    {
        'id': 2,
        'title': 'Problem 2',
        'description': 'Realizar un while infinito',
        'test_cases': [
            {'input': 'test_input_1', 'output': 'expected_output_1'},
            {'input': 'test_input_2', 'output': 'expected_output_2'},
        ]
    },
]

def getProblems():
    return problems_data