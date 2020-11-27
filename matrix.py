import typing
import re
import math


def parse_matrix(raw) -> typing.List[int]:
    return [int(num) for num in re.findall(r'\d+', raw)]


def _get_circle(
        depth: int, matrix: typing.List[int], n: int) -> typing.List[int]:
    """Return flattened circle of matrix at level 'depth'.
    params:
        depth: circle level
        matrix: flat square matrix
        n: matrix side
    """
    i0, j0 = depth, depth
    circle_len = n-2*depth
    res = [matrix[n*i0 + j0]]
    # down
    for i in range(i0 + 1, i0 + circle_len):
        res.append(matrix[i*n + j0])

    # right
    i0 = i0 + circle_len - 1
    for j in range(j0 + 1, j0 + circle_len):
        res.append(matrix[i0*n + j])

    # up
    j0 = j0 + circle_len - 1
    for i in range(i0 - 1, i0 - circle_len, -1):
        res.append(matrix[i*n + j0])

    # left
    i0 = i0 - circle_len + 1
    for j in range(j0 - 1, j0 - circle_len + 1, -1):
        res.append(matrix[i0*n + j])

    return res


def traverse(matrix: typing.List[int]) -> typing.List[int]:
    res = []
    n = int(math.sqrt(len(matrix)))
    for i in range(n // 2):
        res.extend(_get_circle(i, matrix, n))
    if n % 2 == 1:
        i = n // 2
        res.append(matrix[i*n + i])
    return res
