#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enchant sample code for Exercise 5.
"""

import enchant

d = enchant.Dict("en_US")
candidate_word = "cookie"
print(d.check(candidate_word)) # True
candidate_word = "lskvd"
print(d.check(candidate_word)) # False
