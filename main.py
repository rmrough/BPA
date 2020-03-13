import torch
import test

from test import my_function


def main():
    x = torch.tensor([[1,2,3,4], [5,6,7,8]])

    my_function(x)
    print("this is some really not advanced software")


if __name__ == '__main__':
    main()

