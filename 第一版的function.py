def compare_recursive(k_group, j_group, s, Max=None, fit_dict=None, select_first=True):
    fit_list = []
    total = []
    if Max is None:
        Max = []
    if fit_dict is None:
        fit_dict = {k: {'fit': 0, 'count': 0} for k in k_group}

    if len(j_group) == 0:
        return Max

    for k in k_group:
        fit = 0
        j_list = []
        k_cover_j = []
        for j in j_group:
            if len(set(k) & set(j)) >= s:
                fit += 1
                j_list.append(j)
        k_cover_j.append(k)
        k_cover_j.append(j_list)
        total.append(k_cover_j)
        fit_list.append(fit)

        # 检查新的fit值是否与旧的fit值相同
        if fit == fit_dict[k]['fit']:
            # 如果相同，增加计数器
            fit_dict[k]['count'] += 1
        else:
            # 如果不同，更新fit值并重置计数器
            fit_dict[k]['fit'] = fit
            fit_dict[k]['count'] = 0

        # 检查计数器是否达到5
        if fit_dict[k]['count'] >= 10 and k in k_group:
            # 如果达到5，删除k
            k_group.remove(k)

    zero = [i for i, x in enumerate(fit_list) if x == 0]
    for z in zero:
        if total[z][0] in k_group:
            k_group.remove(total[z][0])
    print(fit_list)

    # 如果fit_list为空，返回Max和剩余的j_group
    if not fit_list:
        return Max

    # 根据select_first的值来选择第一个max或最后一个max
    if select_first:
        a = fit_list.index(max(fit_list))
    else:
        a = len(fit_list) - 1 - fit_list[::-1].index(max(fit_list))

    if total[a][0] in k_group:
        Max.append(total[a][0])
        k_group.remove(total[a][0])
    j_group = [j for j in j_group if j not in total[a][1]]

    # 在每次递归调用时切换select_first的值
    return compare_recursive(k_group, j_group, s, Max, fit_dict, not select_first)


def greedy_selection(k_group,j_group,s):
    #all k_group change to set
    k_group = set(map(frozenset,k_group))
    selected_k_group = []

    #all j_group change to set
    uncovered_j_group = set(map(frozenset,j_group))
    #choiced k_group

    #the j of each k cover,store in to a dict key:k
    #每个k能覆盖的j都已经存在了字典里
    covered_j_group = {k: {j for j in uncovered_j_group if len(set(k) & j) >= s} for k in k_group}

    while uncovered_j_group:
        #将每一个字典里面数据拿去和未配对的j作比较，能覆盖比较长的取出
        best_fit = max(covered_j_group,key=lambda i: len(covered_j_group[i] & uncovered_j_group),default=None)

        if best_fit and covered_j_group[best_fit]:

            selected_k_group.append(best_fit)
            uncovered_j_group -= covered_j_group[best_fit]

            # remove the sets that do not cover any uncovered elements
            #covered_j_group = {k: v for k, v in covered_j_group.items() if len(v & uncovered_j_group) > 0}
        else:
            break
    result = list(map(lambda a: list(a) ,selected_k_group))
    return result