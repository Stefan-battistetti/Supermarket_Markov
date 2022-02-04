from PIL import Image
import numpy as np

im = Image.open('supermarket.png')
ti = Image.open('tiles.png')
market = np.array(im)
tiles = np.array(ti)

#choose certain icons from 
ax = 4 * 32   # 5th column starting from 0
ay = 1 * 32   # 2nd row
apple = tiles[ay:ay+32, ax:ax+32]

ax = 6 * 32   # 5th column starting from 0
ay = 2 * 32   # 2nd row
dairy = tiles[ay:ay+32, ax:ax+32]

x = 1 * 32   # 5th column starting from 0
y = 4 * 32   # 2nd row
smiley = tiles[y:y+32, x:x+32]



#print(market.shape, market.dtype)
#print(smiley)

#position the icons on the market

#fruits section
tx = 13 * 32
ty = 2 * 32

#dairy section

dx = 4 * 32
dy = 2 * 32

#customer
sx = 14 * 32
sy = 10 * 32
market[ty:ty+32, tx:tx+32] = apple
market[sy:sy+32, sx:sx+32] = smiley
market[dy:dy+32, dx:dx+32] = dairy

im2 = Image.fromarray(market)
im2.save('supermarket_filled.png')



##################
# """
# Start with this to implement the supermarket simulator.
# """

# https://spiced.space/euclidean-eukalyptus/ds-course/_images/class_diagram.png

# import numpy as np
# import pandas as pd


# class Supermarket:
#     """manages multiple Customer instances that are currently in the market.
#     """
#     total_customers = 0 #keep track of the number of customers

#     def __init__(self, name, customers, minutes=960):
#         """to initializes a supermarket, the following arguments are needed; which is 16h/960min open, with a certain number of customers per day -> list of customers
#         """
#         self._name = name #we define our attribute with an underscore that makes it inaccessible as .name        
#         # a list of Customer objects
#         self.customers = []
#         self.minutes = minutes
#         #self.last_id = []   #what is the last_id about?

#     def __repr__(self):
#          """ Representation of the instance Supermarket itself
#         """
#         return f'Supermarket is now open for {self.minutes}'

#     def get_time(self):
#         """current time in HH:MM:SS format, 
#         which customers are right now in the supermarket in which aisle
#         """
#         start_time = '07:00:00'
#         given_time = datetime.strptime(start_time, "%H:%M:%S")
#         return f'The time is {given_time}'

#     def print_customers(self):
#         """print all customers with the current time and id in CSV format.
#         """
#         return None

#     def next_minute(self):
#         """propagates all customers to the next state.
#         move_all_customers_to_next_state
        
#         """
#         time = get_time
#         if not customers in self.customers:
#             self.customers.append(customers)
#             print(f'{customer.id} is at the entrance of the supermarket')
#         # else:
#         #     print(f'{self.name} already owns {pokemon.name}')
#         return None
    

#     def add_new_customers(self):
#         """randomly creates new customers.
#         """
#         return None


#     def remove_exitsting_customers(self):
#         """removes every customer that is not active any more.
#         """
#         return None




# class Customer():
#     """in composition with the Supermarket class the instances of the Customer class are working
#     """
#     def __init__(self, name):
#         """to initializes newly customers with uniwue ids
#         """
#         self.id = RandomInt
#         self.state=

#     def __repr__(self):
#         return f'<Customer {self.name} in {self.state}>'

#     def next_state(self):
#         '''
#         Propagates the customer to the next state.
#         Returns nothing.
#         '''
#         #self.state = random.choice(['spices', 'drinks', 'fruit'])
#         self.state = random.choices(states, weights=self.transition_probs[self.state])[0]
#         return self.state

#     def is_active(self):
#         """Returns True if the customer has not reached the checkout yet."""
#         return self.state != 'checkout'