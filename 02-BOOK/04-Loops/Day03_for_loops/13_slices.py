# Using one of the programs you wrote in this chapter, add several lines to the 
# end of the program that do the following:

# Print the message "The first three items in the list are:" 
# Then use a slice to print the first three items from that program’s list.
# Print the message "Three items from the middle of the list are:" 
# Then use a slice to print three items from the middle of the list.
# Print the message "The last three items in the list are:"
# Then use a slice to print the last three items in the list.

# Creo la playlist
playlist = [
    'Eight Days A Week', 
    'Let It Be', 
    'In My Life', 
    'Hey Jude', 
    'While My Guitar Gently Weeps',
    'Strawberry Fields Forever',
    'Across The Universe',
]

print(f"The first three items in the list are: {playlist[:3]}")
print(f"Three items in the middle are: {playlist[2:5]}")
print(f"The last three items in the list are: {playlist[-3:]}")