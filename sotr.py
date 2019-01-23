import random
import time

start_time = time.time()
SIZE_OF_HASH_TABLE = 100
Hash_table = [None]*SIZE_OF_HASH_TABLE

numbers_of_telephone = ['89084904936','89084906912','89371825591','89064683391','89012205467','89272279385','89176063696',
                        '89176399912','89032045512','89084412397','89032045512','89084412397','89032045512','89084412397',
                        '89032045512', '89074452367','89132045512','89049912397','89272092312','8923448897','89132034512']
names = ['Алексей Иванов', 'Петр Макеев','Александр Маковской','Владимир Красный','Илья Гончаров','Михаил Милонов',
         'Жак Рунн','Александра Полякова', 'Джеки Чоу Хината','Ильдар Владименко','Даниил Гаврилов','Леонид Сизов','Кристина Арефьева',
         'Алина Вольтер','Никита Чехов','Антон Дженикидзе','Ляйсан Михеева','Анастасия Владимирченко','Юрий Гавриленко',
         'Елена Препина','Ирина Моргенштерн','Люция Алексеева','Юлия Миланова','Анастасия Михеева','Владислава Хапойнова']
keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,22,24,25,26,27,28,29,30]

Works = ['Уборщик', 'Программист','Доктор','Слесарь','Директор','Дизайнер','Пожарный','Полицеский','Строитель','Электрик','Инженер',
        'Конструктор','Репетитор','Политик','Философ','Ботаник','Ученый','Генетик','Воспитатель']
class Sotrudnik:
    def __init__(self, Age= str(random.randint(0,99)), Work = Works[random.randint(0,len(Works))],
                 Height = str(random.randint(150,210)), Weight = str(random.randint(35,120))):
        self.Age = Age
        self.Work = Work
        self.Height = Height
        self.Weight = Weight
class Pair:
    def __init__(self, TKey, TValue, TNext= None, TPrevious = None):
        self.Key = TKey
        self.Value = TValue
        self.Next = TNext
        self.Previous = TPrevious
    def Get_index(self, size_of_mass=SIZE_OF_HASH_TABLE):
        element_now = self
        element_before = Hash_table[hash(self.Key)%size_of_mass]
        if(Hash_table[hash(self.Key)%size_of_mass] is None):
            return hash(self.Key) % size_of_mass
        else:
            while(element_before.Next is not None):
                element_before=element_before.Next
            element_before.Next = element_now
            element_now.Previous = element_before
            Hash_table[hash(self.Key) % size_of_mass] = element_before
            return hash(self.Key) % size_of_mass
    def hash(self):
        return ord(self[0])%7 + ord(self[-1])%13
def fill_element_of_Table():
    pair= Pair(names[random.randint(0,len(names)-1)], Sotrudnik(str(random.randint(0,99)),
                                                                Works[random.randint(0,len(Works)-1)],
                                                                str(random.randint(150,210)),
                                                                str(random.randint(35, 120))))
    return pair

def print_Hash_Table():
    for pair in Hash_table:
        if(pair is not None):
            output_file.write(pair.Key + " Возраст: " + pair.Value.Age + " Профессия: " + pair.Value.Work +
                  " Рост: " + pair.Value.Height + " Вес: " + pair.Value.Weight + "\n")
            while(pair.Previous is not None):
                output_file.write(pair.Previous.Key + " Возраст: " + pair.Previous.Value.Age + " Профессия: " +
                      pair.Previous.Value.Work + " Рост: " + pair.Previous.Value.Height + " Вес: " + pair.Previous.Value.Weight + "\n")
                pair = pair.Previous

output_file = open("output_file.txt", "w")
for i in range(len(Hash_table)):
    temp_pair = fill_element_of_Table()
    Hash_table[temp_pair.Get_index()] = temp_pair
print("Программа выполнена за %s секунд" % (time.time() - start_time))
print_Hash_Table()
