#!/usr/bin/env python3

import random

tasks = ["Work on LinkedIn/Portfolio/Website.",
         "Watch online courses.",
         "Contribute to Cedille.",
         "Look for emacs plugins to improve 'workflow'.",
         "Explore with bash/linux/low level stuff.",
         "Explore with Cloud stuff.",
         "Read articles on HackerNews."
         "Close computer, go read a book you nerd."
]

print(tasks[random.randint(1,len(tasks))])
