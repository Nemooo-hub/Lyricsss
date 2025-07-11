import sys
import time
from time import sleep

def print_lyrics():
    lyrics = [
        ("Do you think I have forgotten?", 0.08),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.1),
        ("about you?", 0.2),
        ("There was something bout you that now I cant remember", 0.08),
        ("Its the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about youuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]
    delays = [1.5, 1.5, 2.5, 3.8, 0.2, 0.2, 0.2, 0.2, 0.2]
    
    for i, (line, char_delay) in enumerate(lyrics):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        print('')
        time.sleep(delays[i])

print_lyrics()
