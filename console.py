#from tradePlan import TradePlan
from cmd import Cmd
import datetime
import agent


class MyPrompt(Cmd):

    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M"))
    # capital = input("Capital to deploy: ")
    # capital = float(capital)

    def do_market(self, args):
        """
        Changes context currency
        :param args: str for market currency
        """
        market = args
        agent.market(args)


    def do_capital(self, args):
        agent.capital(float(args))

    def do_entry(self, args):
        agent.entry(float(args))

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')