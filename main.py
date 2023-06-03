from upgraded_cmd import *

PROMPTS = (
    '\n'.join((
        red('┌─ '),
        red('   ') + ' > {{ {} }}',
        red('   ')
    )), '\n'.join((
        red(' ─┐'),
        red('   ') + ' > {{ {} }}',
        red('   ')
    )), '\n'.join((
        red('  ┐'),
        red('  │') + ' > {{ {} }}',
        red('   ')
    )), '\n'.join((
        red('   '),
        red('  │') + ' > {{ {} }}',
        red('  ┘')
    )), '\n'.join((
        red('   '),
        red('   ') + ' > {{ {} }}',
        red(' ─┘')
    )), '\n'.join((
        red('   '),
        red('   ') + ' > {{ {} }}',
        red('└─ ')
    )), '\n'.join((
        red('   '),
        red('│  ') + ' > {{ {} }}',
        red('└  ')
    )), '\n'.join((
        red('┌  '),
        red('│  ') + ' > {{ {} }}',
        red('   ')
    ))
)

OLD_P = '\n'.join((
        red('┌─┐'),
        red('│ │') + ' > {{ {} }}',
        red('└─┘')
    ))


@new_command('wait')
def _(self: CMD, *args):
    """wait\nWastes all your time"""
    try:
        while True:
            continue
    except KeyboardInterrupt:
        return


class cmd(CMD):
    pass


P = AnimatedPrompt(PROMPTS, OLD_P)
cmd(P).run()
