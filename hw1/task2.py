import click
import sys


def tail_impl(file, num_lines):
    lines = file.readlines()
    for line in lines[-num_lines:]:
        print(line, end='')


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def tail(files):
    if not files:
        tail_impl(sys.stdin, 17)
    elif len(files) == 1:
        tail_impl(files[0], 10)
    else:
        for i, file in enumerate(files):
            if i > 0:
                print()
            print(f'==> {file.name} <==')
            tail_impl(file, 10)


if __name__ == '__main__':
    tail()
