from hometask_data import IDS, GEO_LOGS, QUERIES

#---------Hometask #1--------------
#Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.
def find_visits_to_country(country:str, geo_logs:dict) -> dict:
    '''Returns a list of dictionaries with destination == country'''
    result = []
    for log in geo_logs:
        a = list(*log.values())
        if country in list(*log.values()):
            result.append(log)
    return result
#----------------------------------

#---------Hometask #2--------------
# Выведите на экран все уникальные гео-ID из значений словаря ids. Т.е. список вида [213, 15, 54, 119, 98, 35]
def dict_values_to_list(id_info:dict) -> list:
    '''Appends all values from dict into one list (values must be lists)'''
    result = []
    for user in list(id_info.values()):
        result.extend(user)
    return result
    
def delete_nonunique(values:list) -> list:
    '''Gets sorted list of unique values from input list'''
    return sorted(list(set(values)), reverse = True)
#----------------------------------

#---------Hometask #3--------------
# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
def get_percentage_of_query_by_words(words_count:int, queries:list) -> int:
    '''Shows percentage of queries with secified length of all queries'''
    queries_words_count = {}
    for elem in queries:
        queries_words_count[len(elem.split())] = queries_words_count.get(len(elem.split()), 0) + 1
    try:
        return round(queries_words_count[words_count] / len(queries) * 100)
    except KeyError:
        return 0
#----------------------------------

