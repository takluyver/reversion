import itertools
import re

part_pat = re.compile('(\d+|\.|[^\d.]+)')

class BadDelta(ValueError): pass

def add(current, increment):
    # Normalise the increment - insert zeros between consecutive .s
    increment = increment.replace('..', '.0.')
    if increment.startswith('.'):
        increment = '0' + increment

    current_parsed = part_pat.findall(current)
    increment_parsed = part_pat.findall(increment)
    new_parts = []

    if len(increment_parsed) > len(current_parsed):
        raise BadDelta("Increment {!r} has more parts than version {!r}"
                         .format(increment, current))

    for cp, ip in zip(current_parsed, increment_parsed):
        if ip.isdigit():
            if not cp.isdigit():
                raise BadDelta("Increment {!r} does not match version {!r}"
                                 .format(increment, current))
            res = int(cp) + int(ip)
            new_parts.append(str(res))

        elif cp != ip:
            raise BadDelta("Increment {!r} does not match version {!r}"
                             .format(increment, current))
        else:
            new_parts.append(cp)

    new_parts.extend(current_parsed[len(increment_parsed):])

    return ''.join(new_parts)

def final(current):
    current_parsed = part_pat.findall(current)
    def number_or_dot(p):
        return p.isdigit() or p == '.'
    res = ''.join(itertools.takewhile(number_or_dot, current_parsed))
    return res.rstrip('.')

def apply(current, delta):
    if delta[0].isdigit():
        return delta

    if delta[0] == '~':
        return current + delta[1:]

    if delta[0] == '+':
        return add(current, delta[1:])

    if delta == 'final':
        return final(current)

    raise BadDelta(("Unrecognised change: {!r}. Changes should start with "
                 "a number, + or ~, or be the word 'final'.").format(delta))
