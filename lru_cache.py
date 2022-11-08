import hashlib,datetime
from operator import itemgetter

class lru_cache:
    def __init__ (self):
        self.__cache_n_value=3 # размер кэша (сколько значений хранить)
        self.__cache_map=[]  # массив типа словарь для кэша

    def calc_hash(self,text):
        res=None
        n=-1

        for i in range(len(self.__cache_map)):
            if(str(text) in self.__cache_map[i]):
                n=i
                break

        if(n==-1):
            if(len(self.__cache_map)==self.__cache_n_value):
                self.__cache_map=sorted(self.__cache_map,key=itemgetter("date_time"),reverse=False)
                print("[D] delete from cache: ",self.__cache_map[0])
                del self.__cache_map[0]

            hash_str=hashlib.sha512(text.encode()).hexdigest()
            self.__cache_map.append({text:hash_str,"date_time":datetime.datetime.now()})
            print("[S] set hash of string: ",text,"to cache")
            res=hash_str
        else:
            res=self.__cache_map[n][text]
            self.__cache_map[n]["date_time"]=datetime.datetime.now()
            print("[G] get hash of string: ",text,"from cache")
        return res

def main():
    test_lru = lru_cache()

    test_lru.calc_hash("123")
    test_lru.calc_hash("123")

    test_lru.calc_hash("1234")
    test_lru.calc_hash("1234")

    test_lru.calc_hash("12345")
    test_lru.calc_hash("12345")

    test_lru.calc_hash("123456")
    test_lru.calc_hash("12346")

    test_lru.calc_hash("123")
    test_lru.calc_hash("123")

if __name__ == '__main__':
 	main()