from argparse import  ArgumentParser, ArgumentDefaultsHelpFormatter
test = "coucou"
print(test)

def adition(a, b):
    if b > 10:
        # import pdb; pdb.set_trace()
        return b * a
    return a + b

def main():
    parser = ArgumentParser(
        description="Démo script.",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'val', type=int,
        help="Interger to add to the other"
    )
    parser.add_argument(
        '--val2', type=int, default=5,
        help="Interger to add to the firstone"
    )
    arguments = parser.parse_args()
    print(adition(arguments.val, arguments.val2))
    input("Connard!")