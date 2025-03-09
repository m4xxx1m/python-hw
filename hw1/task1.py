import click
import sys

@click.command
@click.argument('file', type=click.File('r'), default=sys.stdin)
def nl(file):
    for number, line in enumerate(file):
        print(f'{number+1:>6}\t{line}', end='')


if __name__ == '__main__':
    nl()
