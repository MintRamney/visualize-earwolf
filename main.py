import Earwolf
import pickle
from urllib.request import urlopen
from parse import parse_directory_page, find_hosted_shows, find_guested_shows

''''
guest_list = parse_directory_page(urlopen('http://www.earwolf.com/directory?role=guest&orderby=frequency'))

with open('temp.pickle','wb') as handle:
    pickle.dump(guest_list, handle, protocol=pickle.HIGHEST_PROTOCOL)


with open('temp.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)


handle = open('temp_fulll.pickle', 'wb')
print(unserialized_data)
i = 0

for guest in unserialized_data:
    find_hosted_shows(guest)
    find_guested_shows(guest)  
    print("\n", i , ". ", guest)
    print("Hosted:")
    guest.print_shows_hosted()
    print("Appeared in:")
    guest.print_guested_shows()
    pickle.dump(unserialized_data,handle,protocol=pickle.HIGHEST_PROTOCOL)
    i+=1
'''

with open('guest_data.pickle','rb') as handle:
    unserialized_data = pickle.load(handle)


