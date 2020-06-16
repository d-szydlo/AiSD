#!/usr/bin/python3

import sys
from my_priority_queue import PriorityQueue

def main():
    commands = sys.stdin.readlines()
    commands = [cmd.split() for cmd in commands]
    if len(commands) - 1 == int(commands[0][0]):
        queue = PriorityQueue()
        commands.pop(0)
        for cmd in commands:
            if cmd[0] == 'insert':
                if len(cmd) == 3:
                    queue.insert(int(cmd[1]), int(cmd[2]))
                else:
                    print('Podano złą liczbę argumentów do procedury insert')
            elif cmd[0] == 'empty':
                print('empty {}'.format(queue.empty()))
            elif cmd[0] == 'top':
                print('top {}'.format(queue.top()))
            elif cmd[0] == 'pop':
                print('pop {}'.format(queue.pop()))
            elif cmd[0] == 'priority':
                if len(cmd) == 3:
                    queue.priority(int(cmd[1]), int(cmd[2]))
                else:
                    print('Podano złą liczbę argumentów do procedury priority')
            elif cmd[0] == 'print':
                queue.display()
            else:
                print('Program nie obsługuje komendy {}'.format(cmd))
    else:
        print('Podano nieprawidłowe argumenty')


if __name__ == '__main__':
    main()
