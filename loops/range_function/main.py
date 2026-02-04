# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Write your code here
for day in range(len(weekdays)):
   wd = weekdays[day].lower()
   promo = daily_promotions[day].lower()
   print(f"{wd}: promotion on {promo}")