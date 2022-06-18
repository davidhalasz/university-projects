#!/usr/bin/env python3






def donuts(count):
    if count < 10:
        return 'Fánkok száma: ' + str(count)
    return 'Fánkok száma: sok'



def both_ends(s):
    if len(s) < 2:
        return ''
    return s[0:2] + s[-2:]


def fix_start(s):
    fs = s[0:1]
    s2 = s[1:]
    if s2.find(fs) > -1:
        return fs + s2.replace(fs, '*')
    return s


def mix_up(a, b):
    ftChar1 = a[0:2]
    ftChar2 = b[0:2]
    return ftChar2 + a[2:] + " " + ftChar1 + b[2:]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('donuts')
    test(donuts(4), 'Fánkok száma: 4')
    test(donuts(9), 'Fánkok száma: 9')
    test(donuts(10), 'Fánkok száma: sok')
    test(donuts(99), 'Fánkok száma: sok')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
    main()