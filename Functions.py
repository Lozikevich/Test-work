from typing import Iterable
from Geoname import *
import io
from datetime import datetime
from zoneinfo import ZoneInfo
from pytils import translit


# Функция переводит строку из файла в класс Geoname
def make_geoname(line: str) -> Geoname:
    geoname_id, name, asciiname, alternatenames, latitude, longitude, feature_class, feature_code, country_code, cc2, \
    admin1_code, admin2_code, admin3_code, admin4_code, population, elevation, dem, timezone, modification_date = \
        line.split('\t')
    return Geoname(geoname_id, name, asciiname, alternatenames, latitude, longitude, feature_class, feature_code,
                   country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code, population, elevation, dem,
                   timezone, modification_date)


# Функция извлекает все строки из файла
def get_all() -> Iterable[Geoname]:
    with io.open("RU — копия.txt", "r", encoding='utf-8') as f:
        yield from (make_geoname(line.removesuffix('\n')) for line in f)


# Функция извлекает строку при совпадении geoname_id
async def get_one_by_geoname_id(geoname_id: str) -> Geoname | None:
    for geoname in get_all():
        if str(geoname.geoname_id) == geoname_id:
            return geoname
        else:
            return None


# Функция извлекает строки при совпадении с введенным на русской раскладке asciiname, сортирует по убыванию population
# и выдает первый элемент
async def get_by_asciiname(aname: str) -> Geoname:
    def comparison(geoname):
        if str(geoname.asciiname.lower()) == str(translit.translify(aname).lower()):
            return True
        else:
            return False

    lst = sorted(list(filter(comparison, get_all())), key=lambda geoname: geoname.population, reverse=True)
    if len(lst) > 0:
        return lst[0]
    else:
        return None


# Функция извлекает строки с параметром feature_class == 'P' (city, village,...)
async def get_only_cities() -> Iterable[Geoname]:
    def comparison(geoname):
        if str(geoname.feature_class) == 'P':
            return True
        else:
            return False

    lst = filter(comparison, get_all())
    return lst


# Функция извлекает строки в соответствии с заданным пользователем разбиением по страницам
async def page_maker(pn, n):
    if pn * n > len(list(await get_only_cities())):
        return None
    else:
        lst = []
        for i, geoname in enumerate(await get_only_cities()):
            if (pn - 1) * n <= i <= pn * n - 1:
                lst.append(geoname.to_json())
        return lst


# Функция вычисляет разницу временных зон
async def timezone_compare(geoname_1: Geoname, geoname_2: Geoname) -> str:
    dt1 = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo(str(geoname_1.timezone)))
    dt2 = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo(str(geoname_2.timezone)))
    return str(int((dt1 - dt2).total_seconds() / 3600))


# Функция вычисляет сравнивает широты
async def latitudde_compare(geoname_1: Geoname, geoname_2: Geoname) -> dict:
    dif = await timezone_compare(geoname_1, geoname_2)
    if geoname_1.latitude > geoname_2.latitude:
        return {str(geoname_1.asciiname): 'located to the north',
                'timezone': 'the same' if geoname_1.timezone == geoname_2.timezone else
                'different, the difference is: ' + dif + ' hours'}
    elif geoname_1.latitude < geoname_2.latitude:
        return {str(geoname_2.asciiname): 'located to the north',
                'timezone': 'the same' if geoname_1.timezone == geoname_2.timezone else
                'different, the difference is: ' + dif + ' hours'}
    else:
        return {(str(geoname_1.asciiname) + ' and ' + str(geoname_2.asciiname)): 'are at the same latitude',
                'timezone': 'the same' if geoname_1.timezone == geoname_2.timezone else
                'different, the difference is: ' + dif + ' hours'}


# Функция формирует список возможных названий городов
async def name_list(aname) -> list:

    def comparison(geoname):
        if str(translit.translify(aname)) in str(geoname.asciiname):
            return True
        else:
            return False

    name_list: list = []
    for geoname in filter(comparison, await get_only_cities()):
        if geoname.asciiname not in name_list:
            name_list.append(geoname.asciiname)
    if len(name_list) > 0:
        return name_list
    else:
        return None
