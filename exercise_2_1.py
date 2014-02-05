__author__ = 'ericrgon'

"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: bowl used
        """
        hypo.nom_nom(data)

        return hypo.percentage(data)

class Bowl():
    cookies = {}

    def __init__(self, cookies):
        self.cookies = cookies

    def nom_nom(self, type):
        self.cookies[type] -= 1

    def percentage(self, cookie):
        total = 0

        for count in self.cookies.values():
            total += count

        return float(self.cookies[cookie]) / total

    def __str__(self):
        return str(self.cookies)



def main():
    bowl_1 = Bowl({"vanilla": 75, "chocolate": 25})
    bowl_2 = Bowl({"vanilla": 50, "chocolate": 50})

    hypos = [bowl_1, bowl_2]

    pmf = Cookie(hypos)

    pmf.Update('vanilla')
    pmf.Update('chocolate')

    for hypo, prob in pmf.Items():
        print hypo, prob


if __name__ == '__main__':
    main()
