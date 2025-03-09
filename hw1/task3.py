import click
import sys


def calc_file_data(file):
    lines = words = bytes = 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes += len(line.encode('utf-8'))
    return lines, words, bytes


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def wc(files):
    if not files:
        files = [sys.stdin]
    
    total_lines = total_words = total_bytes = 0
    for file in files:
        lines, words, bytes = calc_file_data(file)
        total_lines += lines
        total_words += words
        total_bytes += bytes
        if file == sys.stdin:
            print(f'{lines}\t{words}\t{bytes}')
        else:
            print(f'{lines}\t{words}\t{bytes}\t{file.name}')

    if len(files) > 1:
        print(f'{total_lines}\t{total_words}\t{total_bytes}\ttotal')


if __name__ == '__main__':
    wc()
