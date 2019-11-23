import json
from urllib.request import urlopen

from UrlUtils import get_url_of_month

token = '7afe3026164cc3dc078870a0522395d647163b9d6286982bcaba2e597eda450d'


def get_expa_data(year: int, month: str, lc: str):
    expa_url = get_url_of_month(token, year, month, lc)

    with urlopen(expa_url) as url:
        data = json.loads(url.read().decode())

    fin_sum = sum([data['i_finished_gv']['doc_count'],
                   data['i_finished_ge']['doc_count'],
                   data['o_finished_gv']['doc_count'],
                   data['o_finished_gt']['doc_count'],
                   data['o_finished_ge']['doc_count']])

    co_sum = sum([data['i_completed_gv']['doc_count'],
                  data['i_completed_ge']['doc_count'],
                  data['o_completed_gv']['doc_count'],
                  data['o_completed_gt']['doc_count'],
                  data['o_completed_ge']['doc_count']])

    results = [[fin_sum,
                data['i_finished_gv']['doc_count'],
                data['i_finished_ge']['doc_count'],
                data['o_finished_gv']['doc_count'],
                data['o_finished_gt']['doc_count'],
                data['o_finished_ge']['doc_count']],
               [co_sum,
                data['i_completed_gv']['doc_count'],
                data['i_completed_ge']['doc_count'],
                data['o_completed_gv']['doc_count'],
                data['o_completed_gt']['doc_count'],
                data['o_completed_ge']['doc_count']]]

    return results
