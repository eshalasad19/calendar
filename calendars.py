# Event Calendar
import calendar

# Step 1: Year & Month 
year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

print(f"\n📅 Calendar of {month}/{year}")
print(calendar.month(year, month))

# Step 2: User choose the date
date = int(input("Choose Date (day number): "))

# Step 3: Weekday 
weekday_index = calendar.weekday(year, month, date)     # 0=Mon ... 6=Sun
weekday_name = calendar.day_name[weekday_index]

print(f"\n👉 {date}/{month}/{year} falls on a {weekday_name}")

# Step 4: Optional -  Add Event
add_event = input("Do you want to add an event for this date? (yes/no): ").lower()
if add_event == "yes":
    event = input("Write your event: ")
    print(f"\n✅ Event Saved: {date}/{month}/{year} ({weekday_name}) → {event}")
else:
    print("\nNo event added.")

