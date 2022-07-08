__author__ = 'miserylab'


def data(relative_path):
    import demoqa_tests
    from pathlib import Path
    return (
        Path(demoqa_tests.__file__)
            .parent
            .parent
            .joinpath('data/')
            .joinpath(relative_path)
            .absolute()
            .__str__()
    )