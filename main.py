import Earwolf
import pickle
from parse import find_people, find_hosted_shows, find_guested_shows
'''
guest_list = find_people()

with open('guests.pickle','wb') as handle:
    pickle.dump(guest_list, handle, protocol=pickle.HIGHEST_PROTOCOL)


with open('guests.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)



handle = open('full_guests.pickle', 'wb')


print(unserialized_data)
i = 0

for guest in unserialized_data[42:]:
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

find_people()