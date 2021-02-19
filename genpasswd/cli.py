from optparse import OptionParser
from genpasswd import generate

__version__ = '2.0.2'


def main():
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option('-c', '--count', dest='length', default=3, action='store', type='int', metavar="SETS",
                      help='the count of the strings between separators')
    parser.add_option('-l', '--str-length', dest='set_length', default=6, action='store', type='int', metavar="LENGTH",
                      help='the length of characters between separators')
    parser.add_option('-d', '--digits', dest='numbers', default=1, action='store', type='int', metavar="NUMS",
                      help='the amount of digits in the password')
    parser.add_option('-u', '--uppercase', dest='uppercase', default=1, action='store', type='int', metavar="CAPS",
                      help='the amount of uppercase letters in the password')
    parser.add_option('-s', '--separator', dest='separator', default='-', action='store', metavar="CHAR",
                      help='the separator character')
    parser.add_option('-n', '--number', dest='iterations', default=1, action='store', type='int', metavar="ITER",
                      help='executes the command N times')
    parser.add_option('-v', '--version', default=False,
                      dest='version', action='store_true',
                      help='print the version number and quit')

    (options, args) = parser.parse_args()

    # print out errors beforehand
    if options.numbers + options.uppercase > options.set_length * options.length:
        print('Error:\n  The amount of numbers plus the count of uppercase letters\n  must be less than or equal to the total amount of characters')
        print('\n  numbers + uppercase <= str-length * count\n')
        exit(1)

    if options.version:
        print(f'genpasswd {__version__}')
        exit(0)

    for i in range(options.iterations):
        print(generate.superset(
            length=options.length,
            set_length=options.set_length,
            numbers=options.numbers,
            uppercase=options.uppercase,
            separator=options.separator
        ))


if __name__ == '__main__':
    main()
