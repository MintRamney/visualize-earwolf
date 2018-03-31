import Earwolf
import pickle
from urllib.request import urlopen
from parse import parse_directory_page, find_hosted_shows, find_guested_shows

'''
Note I went fuckin crazy with the serialization because I didn't want to 
have to start over when I originally was pulling out 3500 guests
'''

'''
# get list of guests
guest_list = parse_directory_page(urlopen('http://www.earwolf.com/directory?role=guest&orderby=frequency'))

# serialize guest list 
with open('temp.pickle','wb') as handle:
    pickle.dump(guest_list, handle, protocol=pickle.HIGHEST_PROTOCOL)

# unserialize guest list
with open('temp.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

# now write to guest_data
handle = open('guest_data.pickle', 'wb')
print(unserialized_data)
i = 0

# construct host and guest lists for each guest
for guest in unserialized_data:
    find_hosted_shows(guest)
    find_guested_shows(guest)  
    print("\n", i , ". ", guest)
    print("Hosted:")
    guest.print_shows_hosted()
    print("Appeared in:")
    guest.print_guested_shows()

    # serialize 
    pickle.dump(unserialized_data,handle,protocol=pickle.HIGHEST_PROTOCOL)
    i+=1
'''

# unserialize completed data
with open('guest_data.pickle','rb') as handle:
    unserialized_data = pickle.load(handle)




