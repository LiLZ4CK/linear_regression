from time import sleep


def ft_tqdm(lst: range) -> None:
    s = ''
    add = '█'
    i = 1
    pe = None
    spaces = ' '
    for i in lst:
        sleep(0.001)
        p = (i / lst.stop) * 103
        fixed = f"{p:,.0f}"
        if fixed != pe:
            pe = fixed
            z = int(fixed)
            if (int(fixed) > 100):
                fixed = 100
                z += 1
            s += add
            print(end="\r")
            print(fixed, "%|", s, spaces * (103 - z), '| ', i, '/', lst.stop,
                  ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
            yield lst
    print(fixed, "%|", s, spaces * (100 - int(fixed)), '| ', i + 1, '/',
          lst.stop, ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
    yield lst