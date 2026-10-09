import sys

if __name__ == '__main__':
    print('=== Command Quest ===')
    argv = sys.argv
    print('Program name:', argv[0])
    count = len(argv)
    if count == 1:
        print('No arguments provided!')
    else:
        print('Arguments received:', count - 1)
        for i in range(1, count):
            print(f'Argument {i}:', argv[i])
    print('Total arguments:', count)
