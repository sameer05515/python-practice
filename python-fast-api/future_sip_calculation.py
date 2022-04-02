
def cal_future_sip_amount(amount: float, interest_rate: float, year: int):
    return_obj = {"amount": amount, "interest_rate": interest_rate, "years": year, "year_wise_detail": []};
    future_amount: float = 0
    fut = []
    for x in range(1, year + 1):
        tot_principle = (future_amount + amount)
        future_amount = (future_amount + amount) * (1 + interest_rate)
        interest_credited = future_amount - tot_principle
        year_wise_detail = {
            "total_principle": tot_principle,
            "interest_credited": interest_credited,
            "year": x,
            "total_accumulated_amount": future_amount
        }
        add_value(year_wise_detail, return_obj)
        print(future_amount)
    return_obj["future_amt"] = future_amount
    return return_obj


def add_value(val, dict_obj):
    dict_obj["year_wise_detail"].append(val)