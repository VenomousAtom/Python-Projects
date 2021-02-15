dimensions_input = input("Enter the Dimensions (LxB): ")
dim_calc_list = dimensions_input.split(' ')
listing_input = []
i = 1
while i <= int(dim_calc_list[1]):
    j = int(dim_calc_list[0])
    while j >= i:
        listing_input.append(j)
        j-=1
    listing_input.append(' ')
    i+=1
print(listing_input)
listing_split = [str(x) for x in listing_input]
print(listing_split)
listing_pop = listing_split#.remove()
print(listing_pop)
listing_joining = ''.join(listing_pop)
print(listing_joining)
listing_strip = listing_joining.rstrip()
listing_final = listing_strip.split(' ')
print(listing_final)

