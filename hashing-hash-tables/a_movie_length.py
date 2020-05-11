# Write a function that takes an integer flight_length (in minutes)
# and a list of integers movie_lengths (in minutes)
# and returns a boolean indicating whether there are two numbers
# in movie_lengths whose sum equals flight_length.

#When building your function:

#Assume your users will watch exactly two movies
#Don’t make your users watch the same movie twice
#Optimize for runtime over memory

def movies_fit_flight(flight_length, movie_lengths):
    fitting_movie_lengths = set()
    
    for movie_len in movie_lengths:
        if movie_len in fitting_movie_lengths:
            return True            
        fitting_movie_lengths.add(flight_length - movie_len)
    return False
    


print(movies_fit_flight(91, [85, 93, 116, 189]) == False)
print(movies_fit_flight(180, [90]) == False)
print(movies_fit_flight(182, [85, 93, 116, 189, 97, 75]) == True)
print(movies_fit_flight(96, [85, 93, 116, 189, 96, 75]) == False)
print(movies_fit_flight(302, [85, 93, 116, 189, 97, 75, 111]) == False)
print(movies_fit_flight(167, [85, 93, 116, 189, 68, 56, 99]) == True)