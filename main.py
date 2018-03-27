def get_BMBC(pattern):
    # 预生成坏字符表
    BMBC = dict()
    for i in range(len(pattern) - 1):
        char = pattern[i]
        # 记录坏字符最右位置（不包括模式串最右侧字符）
        BMBC[char] = i + 1
    return BMBC


def get_BMGS(pattern):
    # 预生成好后缀表
    BMGS = dict()

    # 无后缀仅根据坏字移位符规则
    BMGS[''] = 0

    for i in range(len(pattern)):

        # 好后缀
        GS = pattern[len(pattern) - i - 1:]

        for j in range(len(pattern) - i - 1):

            # 匹配部分
            NGS = pattern[j:j + i + 1]

            # 记录模式串中好后缀最靠右位置（除结尾处）
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS


def BM(string, pattern, BMBC, BMGS):
    # 匹配过程
    i = 0
    j = len(pattern)

    while i < len(string):
        while (j > 0):

            # 主串判断匹配部分
            a = string[i + j - 1:i + len(pattern)]

            # 模式串判断匹配部分
            b = pattern[j - 1:]

            # 当前位匹配成功则继续匹配
            if a == b:
                j = j - 1

            # 当前位匹配失败根据规则移位
            else:
                i = i + max(BMGS.setdefault(b[1:], len(pattern)), j - BMBC.setdefault(string[i + j - 1], 0))
                j = len(pattern)

            # 匹配成功返回匹配位置
            if j == 0:
                return i

    # 匹配失败返回 None
    return None


if __name__ == '__main__':
    string = 'abddacbcbcabc'
    pattern = 'bcabc'

    BMBC = get_BMBC(pattern=pattern)  # 坏字符表
    BMGS = get_BMGS(pattern=pattern)  # 好后缀表

    x = BM(string=string, pattern=pattern, BMBC=BMBC, BMGS=BMGS)

    print(string[x:])
