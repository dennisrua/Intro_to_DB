import datetime

# --- Creating datetime objects ---

# Current local date and time
now = datetime.datetime.now()

# Current UTC date and time
utcnow = datetime.datetime.utcnow()

# Specific date
d = datetime.date(2025, 10, 26)

# Specific time
t = datetime.time(10, 30, 0, 123456) # hour, minute, second, microsecond

# Specific datetime
dt = datetime.datetime(2025, 10, 26, 10, 30, 0, 123456)

# From ISO format string
date_from_iso = datetime.date.fromisoformat("2025-10-26")
datetime_from_iso = datetime.datetime.fromisoformat("2025-10-26T10:30:00")

# --- Accessing components ---

print(f"Year: {dt.year}")
print(f"Month: {dt.month}")
print(f"Day: {dt.day}")
print(f"Hour: {dt.hour}")
print(f"Minute: {dt.minute}")
print(f"Second: {dt.second}")
print(f"Microsecond: {dt.microsecond}")
print(f"Weekday (0=Monday): {dt.weekday()}")
print(f"ISO Weekday (1=Monday): {dt.isoweekday()}")
print(f"ISO Calendar: {dt.isocalendar()}") # (ISO year, ISO week number, ISO weekday)

# --- Formatting and Parsing ---

# Format datetime to string (strftime)
formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S") # e.g., 2025-10-26 10:30:00

# Parse string to datetime (strptime)
parsed_datetime = datetime.datetime.strptime("2025-10-26 10:30:00", "%Y-%m-%d %H:%M:%S")

# Common format codes:
# %Y: Year with century (e.g., 2025)
# %m: Month as a zero-padded decimal number (01-12)
# %d: Day of the month as a zero-padded decimal number (01-31)
# %H: Hour (24-hour clock) as a zero-padded decimal number (00-23)
# %M: Minute as a zero-padded decimal number (00-59)
# %S: Second as a zero-padded decimal number (00-59)
# %f: Microsecond as a decimal number, zero-padded to 6 digits
# %A: Weekday's full name (e.g., Sunday)
# %a: Weekday's abbreviated name (e.g., Sun)
# %B: Month's full name (e.g., October)
# %b: Month's abbreviated name (e.g., Oct)

# --- Time Differences (timedelta) ---

# Create a timedelta object
one_day = datetime.timedelta(days=1)
five_hours = datetime.timedelta(hours=5)

# Add/subtract timedeltas
tomorrow = d + one_day
yesterday = d - one_day
future_time = dt + five_hours

# Calculate difference between two datetimes
time_difference = now - dt
print(f"Time difference in seconds: {time_difference.total_seconds()}")

# --- Replacing components ---
modified_dt = dt.replace(year=2026, hour=15)