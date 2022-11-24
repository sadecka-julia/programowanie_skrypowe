from collections import Counter as count; import sys; print(dict(count(map(len, sys.stdin.read().split()))))
