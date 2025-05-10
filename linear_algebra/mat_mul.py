def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    m_a, n_a = get_dim(a)
    if m_a == 1:
        a = [a]
    m_b, n_b = get_dim(b)
    if m_b == 1:
        b = [b]

    ans = [[0] * n_b for _ in range(m_a)]
    for i in range(m_a):
        for j in range(n_b):
            for k in range(n_a):
                ans[i][j] += a[i][k] * b[k][j]
    return ans


def get_dim(a):
    if isinstance(a[0], int):
        m = 1
        n = len(a)
    else:
        m = len(a)
        n = len(a[0])
    return m, n


print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
