def correct_ap(a_p):
    # First i have find the difference b/w the element
    diff_list = [a_p[_+1]-a_p[_] for _ in range(0, len(a_p)-1)]
    diff_count_dict = {_:diff_list.count(_) for _ in diff_list}
    difference_value = max(zip(diff_count_dict.values(), diff_count_dict.keys()))[1]

    #separating the element
    a_p_element = []
    for i in range(0, len(a_p)-1):
        if (a_p[i+1] - a_p[i]) == difference_value:
            a_p_element.append(a_p[i+1]), a_p_element.append(a_p[i])
        else:
            a_p_element.append(a_p[i])
            break

    # Replacing the Wrong Element with Correct Element
    max_num_index = a_p.index(max(a_p_element))
    if len(set(a_p_element)) != len(a_p):
        a_p[max_num_index+1] = a_p[max_num_index]+difference_value
    return a_p

def correct_gp(g_p):
    # First i have to find the difference b/w the element
    diff_list = [g_p[_+1]/g_p[_] for _ in range(0, len(g_p)-1)]
    diff_count_dict = {_:diff_list.count(_) for _ in diff_list}
    difference_value = max(zip(diff_count_dict.values(), diff_count_dict.keys()))[1]

    #separating the element
    g_p_element = []
    for i in range(0, len(g_p)-1):
        if (g_p[i+1]/g_p[i]) == difference_value:
            g_p_element.append(g_p[i+1]), g_p_element.append(g_p[i])
        else:
            g_p_element.append(g_p[i])
            break

    # Replacing the Wrong Element with Correct Element
    max_num_index = g_p.index(max(g_p_element))
    if len(set(g_p_element)) != len(g_p):
        g_p[max_num_index+1] = round(g_p[max_num_index]*difference_value)
    return g_p


if __name__ == "__main__":
    a_p = [2, 5, 8, 11, 14, 17]
    g_p = [3, 9, 27, 81,243, 729]
    print(correct_gp(g_p))
    print(correct_ap(a_p))
