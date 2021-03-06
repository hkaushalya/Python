"""This file contains code used in "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import csv
import math
import numpy
import sys

import matplotlib

import thinkbayes
import myplot


def ReadScale(filename='sat_scale.csv', col=2):
    """Reads a CSV file of SAT scales (maps from raw score to standard score).

    Args:
      filename: string filename
      col: which column to start with (0=Reading, 2=Math, 4=Writing)

    Returns: thinkbayes.Interpolator object
    """
    def ParseRange(s):
        t = [int(x) for x in s.split('-')]
        return 1.0 * sum(t) / len(t)

    fp = open(filename)
    reader = csv.reader(fp)
    raws = []
    scores = []

    for t in reader:
        try:
            raw = int(t[col])
            raws.append(raw)
            score = ParseRange(t[col+1])
            scores.append(score)
        except:
            pass

    raws.sort()
    scores.sort()
    return thinkbayes.Interpolator(raws, scores)


def ReadRanks(filename='sat_ranks.csv'):
    """Reads a CSV file of SAT scores.

    Args:
      filename: string filename

    Returns:
      list of (score, freq) pairs
    """
    fp = open(filename)
    reader = csv.reader(fp)
    res = []

    for t in reader:
        try:
            score = int(t[0])
            freq = int(t[1])
            res.append((score, freq))
        except ValueError:
            pass

    return res


def DivideValues(pmf, denom):
    """Divides the values in a Pmf by denom.

    Returns a new Pmf.
    """
    new = thinkbayes.Pmf()
    denom = float(denom)
    for val, prob in pmf.Items():
        x = val / denom
        new.Set(x, prob)
    return new


class Exam(object):
    """Encapsulates information about an exam.

    Contains the distribution of scaled scores and an
    Interpolator that maps between scaled and raw scores.
    """
    def __init__(self):
        self.scale = ReadScale()

        scores = ReadRanks()
        score_pmf = thinkbayes.MakePmfFromDict(dict(scores))

        self.raw = self.ReverseScale(score_pmf)
        self.max_score = max(self.raw.Values())
        self.prior = DivideValues(self.raw, denom=self.max_score)

    def Lookup(self, raw):
        """Looks up a raw score and returns a scaled score."""
        return self.scale.Lookup(raw)
        
    def Reverse(self, score):
        """Looks up a scaled score and returns a raw score.

        Since we ignore the penalty, negative scores round up to zero.
        """
        raw = self.scale.Reverse(score)
        return raw if raw > 0 else 0
        
    def ReverseScale(self, pmf):
        """Applies the reverse scale to the values of a PMF.

        Args:
            pmf: Pmf object
            scale: Interpolator object

        Returns:
            new Pmf
        """
        new = thinkbayes.Pmf()
        for val, prob in pmf.Items():
            raw = self.Reverse(val)
            new.Incr(raw, prob)
        return new


class Sat(thinkbayes.Suite):
    """Represents the distribution of efficacy for a test-taker."""

    def __init__(self, exam):
        thinkbayes.Suite.__init__(self)

        self.exam = exam

        # start with the prior distribution
        for p, prob in exam.prior.Items():
            self.Set(p, prob)

    def Likelihood(self, hypo, data):
        """Computes the likelihood of a test score, given efficacy."""
        p = hypo
        score = data
        raw = self.exam.Reverse(score)

        yes, no = raw, self.exam.max_score - raw
        like = p**yes * (1-p)**no
        return like


def PmfProbGreater(pmf1, pmf2):
    """Probability that a value from pmf1 is less than a value from pmf2.

    Args:
        pmf1: Pmf object
        pmf2: Pmf object

    Returns:
        float probability
    """
    total = 0.0
    for v1, p1 in pmf1.Items():
        for v2, p2 in pmf2.Items():
            # fill this in
            pass

    return total


def MakeFigures(exam, alice, bob):
    formats=['png']

    myplot.Pmf(exam.prior, label='prior')
    myplot.Save(root='sat_prior',
                formats=formats,
                xlabel='p',
                ylabel='PMF')


    myplot.Clf()
    myplot.Pmfs([alice, bob])
    myplot.Save(root='sat_posterior',
                formats=formats,
                xlabel='p',
                ylabel='PMF')


def main(script):

    exam = Exam()

    alice = Sat(exam)
    alice.name = 'alice'
    alice.Update(780)

    bob = Sat(exam)
    bob.name = 'bob'
    bob.Update(760)

    print 'Prob Alice is "smarter":', PmfProbGreater(alice, bob)


if __name__ == '__main__':
    main(*sys.argv)
