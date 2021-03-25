def mendels_first_law(homo_dominant, hetero, homo_recessive):
    all_num = homo_dominant + hetero + homo_recessive
    c_result = 0
    if homo_recessive >= 2:
        ratio_hr_hr = homo_recessive / all_num * (homo_recessive-1) / (all_num-1)
        c_result += ratio_hr_hr
    if hetero >= 2:
        ratio_he_he = hetero / all_num * (hetero-1) / (all_num-1) * 0.25
        c_result += ratio_he_he
    if homo_recessive >= 1 and hetero >= 1:
        ratio_he_hr = homo_recessive / all_num * hetero / (all_num-1) * 0.5 * 2
        c_result += ratio_he_hr
    return 1 - c_result

if __name__ == '__main__':
    homo_dominant = 24
    hetero = 26
    homo_recessive = 21
    print('{:.5f}'.format(mendels_first_law(homo_dominant, hetero, homo_recessive)))