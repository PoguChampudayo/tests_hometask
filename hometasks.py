from hometask_data import IDs, GEO_LOGS, QUERIES

#---------Hometask #1--------------
def find_visits_to_country(country, geo_logs):
    result = []
    for log in geo_logs:
        a = list(*log.values())
        if country in list(*log.values()):
            result.append(log)
    return result
#----------------------------------
#---------Hometask #2--------------
def dict_values_to_list(id_info):
    result = []
    for user in list(id_info.values()):
        result.extend(user)
    return result
    
def delete_nonunique(values:list):
    return sorted(list(set(values)), reverse = True)
#----------------------------------
#---------Hometask #3--------------
def get_percentage_of_query_by_words(words_count, queries:list):
    queries_words_count = {}
    for elem in queries:
        queries_words_count[len(elem.split())] = queries_words_count.get(len(elem.split()), 0) + 1
    return queries_words_count[words_count]
#----------------------------------
