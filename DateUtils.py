def get_date(year: int, month: str, start: bool):
    month_switcher = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'

    }

    day_switcher = {
        'January': '31',
        'February': '28',
        'March': '31',
        'April': '30',
        'May': '31',
        'June': '30',
        'July': '31',
        'August': '31',
        'September': '30',
        'October': '31',
        'November': '30',
        'December': '31'
    }

    if start:
        return str(year) + '-' + month_switcher[month] + '-01'
    else:
        return str(year) + '-' + month_switcher[month] + '-' + day_switcher[month]


def get_full_month_dates(year: int, month: str):
    return [get_date(year, month, True), get_date(year, month, False)]
