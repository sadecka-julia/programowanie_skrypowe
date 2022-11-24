

# import sys; print(len(list(filter(lambda num: num % 2 == 0, [int(number) for file in sys.argv[1:] for line in open(file, 'r').readlines() for number in line.rstrip().split()]))))
import sys; print(len(list(filter(lambda num: int(num) % 2 == 0, sum(list(map(lambda file: open(file, 'r').read().split(), sys.argv[1:])), [])))))
