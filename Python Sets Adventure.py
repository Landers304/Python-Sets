#Task 1:


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

#Destinations unique to your airline
unique_destinations_ours = our_routes.difference(competitor_routes)

#Destinations unique to the competitor airline
unique_destinations_competitor = competitor_routes.difference(our_routes)

#Destinations that neither airline shares
destinations_neither = our_routes.symmetric_difference(competitor_routes)

#Results
print("Destinations that both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_destinations_ours)
print("Destinations unique to the competitor airline:", unique_destinations_competitor)
print("Destinations that neither airline shares:", destinations_neither)
