from shell.constants import *
from shell import *

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

P = AnimatedPrompt(PROMPTS, OLD_P)
CMD(P).run()
