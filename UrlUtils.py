from DateUtils import get_full_month_dates
from LcUtils import lc_ids


def get_url(token: str, start_date: str, end_date: str, lc: str):
    return 'https://api.aiesec.org/v2/applications/analyze.json?access_token=' + token + '&start_date=' + start_date + \
           '&end_date=' + end_date + '&performance_v3[office_id]=' + str(lc_ids[lc])


def get_url_of_month(token: str, year: int, month: str, lc: str):
    return get_url(token, get_full_month_dates(year, month)[0], get_full_month_dates(year, month)[1], lc)
