#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import io

# Read txt file
with open('tasks.txt', 'r') as myfile:
    tasks=myfile.read().split('\n')
    del tasks[-1] # Removes trailing return line

chosen = tasks[random.randint(0, len(tasks) - 1)]

print(chosen)
