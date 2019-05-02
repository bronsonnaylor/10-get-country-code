def get_country_codes(prices):
    list = prices.split()
    code_list = []
    for i in list:
        country_code = str(i).split("$")[0]
        code_list.append(country_code)
    return ", ".join(code_list)
