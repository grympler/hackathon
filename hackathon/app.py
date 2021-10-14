#!/usr/bin/env python
"""
Usage:
    hackathon [options]
    hackathon -h | --help

Options:
    --ipdb              Enable ipdb on exceptions.
    --log-level=L       Log level to set [default: info]
    --log-formatter=F   Log formatter (json or standard), by default set to standard
    --time              Enable excecution time measurement.
    -h, --help          Show help.
"""
import logging

import docopt

from hackathon.init_logging import init_logging
from hackathon.utils.wrappers import ipdb_on_exception, timer
from hackathon.player import test


LOGGER = logging.getLogger(__file__)


@ipdb_on_exception
@timer
def run(*args, **kwargs):
    pass


def main():
    """Main function of project hackathon."""
    args = docopt.docopt(__doc__)
    init_logging(args['--log-level'], args['--log-formatter'])
    run(args)


def play_game():
    ongoing = True
    players_amount = int(input('How many players?'))

    first_card, card_decks = create_decks(players_amount)

    players = [ManualPlayer(card_decks[0])] + [BotPlayer(i)for card_decks[1:]]

    tas = [first_card]

    while ongoing:
        # async call for each player
        display(tas)
        for each player -> player.play(tas, who_is_playing)

        if (looser:= Player.who_is_cardless(players)):
            shame_looser(looser)
            ongoing = False


if __name__ == "__main__":
    main()
