# from test2 import test2_2
# from test1 import test1_1
#
# if __name__ == '__main__':
#     test2_2.t_2()
#     test1_1.t_1()

import random
import sys
import time


class MyInt(int):

    def __add__(self, other):
        __res = super().__add__(other)
        return f"{self.real} + {other.real} = {__res.real}"

    def __sub__(self, other):
        __res = abs(super().__sub__(other))
        return f"{self.real} - {other.real} = {__res.real}" if self >= other else f"{other.real} - {self.real} = {__res.real}"

    def __mul__(self, other):
        __res = super().__mul__(other)
        return f"{self.real} x {other.real} = {__res.real}"

    def __floordiv__(self, other):
        if other != 0:
            __res = super().__floordiv__(other)
            return f"{self.real} ÷ {other.real} = {__res.real}"
        else:
            return f"unlimited"


def gen_result(result: str):
    l = random.choice(range(3))
    res_list = result.split("=")
    __num_list = []
    if result.find("+") != -1:
        __num_list = res_list[0].split("+")
        __num_list.append(res_list[-1])
        __num_list[l] = "( )"
        return f"{__num_list[0]} + {__num_list[1]} = {__num_list[2]}"
    elif result.find("-") != -1:
        __num_list = res_list[0].split("-")
        __num_list.append(res_list[-1])
        __num_list[l] = "( )"
        return f"{__num_list[0]} - {__num_list[1]} = {__num_list[2]}"
    elif result.find("x") != -1:
        __num_list = res_list[0].split("x")
        __num_list.append(res_list[-1])
        __num_list[l] = "( )"
        return f"{__num_list[0]} x {__num_list[1]} = {__num_list[2]}"
    elif result.find("÷") != -1:
        __num_list = res_list[0].split("÷")
        __num_list.append(res_list[-1])
        __num_list[l] = "( )"
        return f"{__num_list[0]} ÷ {__num_list[1]} = {__num_list[2]}"
    else:
        return result


def gen_r():
    _res = (getattr(MyInt(random.randint(_s, _e)), random.choice(["__add__", "__sub__"]))(random.randint(_s, _e)) for _ in range(_range))
    __size = 0
    __data = set()
    for _each in _res:
        __r = gen_result(_each)
        __data.add(__r)
        if __size == 100:
            yield __data
            __size = 0
            __data = set()
        else:
            __size += 1
    if __data:
        yield __data


if __name__ == '__main__':
    try:
        start = time.time()
        _s, _e = 0, 100
        _range = 10000
        r = gen_r()
        for each in r:
            for each_re in each:
                print(each_re)
        print(f"use time: {time.time() - start}")
    except KeyboardInterrupt:
        sys.exit(0)

    # res = {getattr(MyInt(random.randint(a, b)), random.choice(["__add__", "__sub__"]))(
    #     random.randint(a, b)) for _ in
    #        range(_range)}
    # r = list(map(lambda x: gen_result(x), res))
    # for each in r:
    #     print(each)
    # print(len(r))
