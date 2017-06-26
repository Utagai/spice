# A py module for basic stats (because no way in hell am I going to use NumPy
# to just compute averages and standard deviations).
#
# Oh, and a license thingy because otherwise it won't look cool and
# professional.
#
# MIT License
#
# Copyright (c) [2016] [Mehrab Hoque]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" A py module for basic stats.

WARN: This module is not meant to be used in any way besides in the internals of
the spice API source code, but because it is for general statistics, one can
extract this from the API and use it in their own projects.
"""

from __future__ import division
from decimal import Decimal
from collections import Counter
from math import sqrt


def sum(data):
    _data_check(data)
    total = 0
    for elem in data:
        total += elem

    return total


def square_sum(data):
    _data_check(data)
    total = 0
    for elem in data:
        total += elem ** 2

    return total


def sum_xy(datax, datay):
    _data_check(datax)
    _data_check(datay)
    total = 0
    for elemx, elemy in zip(datax, datay):
        total += elemx * elemy

    return total


def mean(data):
    _data_check(data)
    return sum(data)/len(data)


def median(data):
    _data_check(data)
    data_len = len(data)
    if data_len % 2 == 0:
        sorted_data = sorted(data)
        median_r = sorted_data[data_len//2]
        median_l = sorted_data[data_len//2 - 2]
        return (median_r + median_l)/2
    else:
        return Decimal(sorted(data)[data_len//2])


def mode(data):
    _data_check(data)
    mode_list = Counter(data)
    return mode_list.most_common(1)[0][0]


def extremes(data):
    _data_check(data)
    return (max(data), min(data))


def p_var(data):
    _data_check(data)
    second_sum = 0
    data_len = len(data)
    mean_val = mean(data)
    for elem in data:
        second_sum += (elem - mean_val) * (elem - mean_val)

    return second_sum/(data_len - 1)


def p_stddev(data):
    _data_check(data)
    return sqrt(p_var(data))


def karl_pearson(datax, datay):
    if len(datax) != len(datay):
        raise ValueError('Invalid sizes for data sets.')
    xy_sum = sum_xy(datax, datay)
    x_sum = sum(datax)
    y_sum = sum(datay)
    x_sum_square = x_sum ** 2
    y_sum_square = y_sum ** 2
    x_square_sum = square_sum(datax)
    y_square_sum = square_sum(datay)
    n = len(datax)

    numerator = (n * xy_sum) - (x_sum * y_sum)
    denominator_x_term = (n * x_square_sum) - x_sum_square
    denominator_y_term = (n * y_square_sum) - y_sum_square
    denominator_squared = denominator_x_term * denominator_y_term
    denominator = sqrt(denominator_squared)

    return numerator/denominator


def karl_pearson2(datax, datay):
    meanx = mean(datax)
    meany = mean(datay)

    product = 0
    sqmagx = 0
    sqmagy = 0
    mincount = 5

    for elemx, elemy in zip(datax, datay):
        product += (elemx - meanx)*(elemy - meany)
        sqmagx += (elemx - meanx)*(elemx - meanx)
        sqmagy += (elemy - meany)*(elemy - meany)

    similarity = product/sqrt(sqmagx*sqmagy)
    similarity = similarity*100
    if mincount >= len(datax):
        return -999
    return similarity


def data_check(data):
    if len(data) == 0:
        raise ValueError('Data must be non-empty.')
