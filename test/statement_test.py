from lib.index import StatementGenerator

input_folder = "input/"


def test_case_one():
    generator = StatementGenerator(input_folder + "test_1.txt")
    assert generator.run() == (
        'alice: $383.15\n'
        '  travel: $312.40\n'
        '  software: $45.00\n'
        '  meals: $25.75\n'
        '  top merchant: Delta\n'
        'company total: $383.15\n'
    )


def test_case_two():
    generator = StatementGenerator(input_folder + "test_2.txt")
    assert generator.run() == (
        'bob: $306.65\n'
        '  travel: $289.90\n'
        '  meals: $16.75\n'
        '  top merchant: Hilton\n'
        'company total: $306.65\n'
    )


def test_case_three():
    generator = StatementGenerator(input_folder + "test_3.txt")
    assert generator.run() == (
        'carol: $517.16\n'
        '  travel: $486.00\n'
        '  software: $20.00\n'
        '  meals: $11.16\n'
        '  top merchant: Lufthansa\n'
        'company total: $517.16\n'
    )


def test_case_four():
    generator = StatementGenerator(input_folder + "test_4.txt")
    assert generator.run() == (
        'dave: $335.50\n'
        '  travel: $300.00\n'
        '  meals: $35.50\n'
        '  top merchant: United\n'
        'company total: $335.50\n'
    )


def test_case_five():
    generator = StatementGenerator(input_folder + "test_5.txt")
    assert generator.run() == (
        'erin: $180.00\n'
        '  travel: $80.00\n'
        '  meals: $50.00\n'
        '  software: $50.00\n'
        '  top merchant: Amtrak\n'
        'company total: $180.00\n'
    )


def test_case_six():
    generator = StatementGenerator(input_folder + "test_6.txt")
    assert generator.run() == (
        'frank: $1,212.05\n'
        '  equipment: $1,204.00\n'
        '  meals: $8.05\n'
        '  top merchant: Apple\n'
        'company total: $1,212.05\n'
    )


def test_case_seven():
    generator = StatementGenerator(input_folder + "test_7.txt")
    assert generator.run() == (
        'gina: $175.12\n'
        '  travel: $97.19\n'
        '  meals: $65.94\n'
        '  software: $11.99\n'
        '  top merchant: Ryanair\n'
        'hugo: $1,590.00\n'
        '  software: $1,290.00\n'
        '  meals: $150.00\n'
        '  travel: $150.00\n'
        '  top merchant: AWS\n'
        'company total: $1,765.12\n'
    )
