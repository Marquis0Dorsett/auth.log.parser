import re  # [RED] This line loads the regular expression module, which helps us search for patterns in text.
from collections import defaultdict  # [RED] This line loads a special dictionary that automatically creates empty lists for new keys.

# [RED] This dictionary will store failed login attempts, grouped by IP address.
failed_logins = defaultdict(list)

# [RED] This pattern looks for lines that mention either "AUTH ERROR" or "FAILED", followed by a username and an IP address.
pattern = r"(AUTH ERROR|FAILED).*user (\w+).*from (\d+\.\d+\.\d+\.\d+)"

# [RED] This line opens the log file named "auth.log" so we can read each line one at a time.
with open ("auth.log.txt") as f:
    for line in f:  # [RED] This loop goes through each line in the log file.
        match = re.search(pattern, line)  # [RED] This checks if the current line matches the pattern we defined.
        if match:  # [RED] If the line matches, we continue with extracting the details.
            reason, user, ip = match.groups()  # [RED] This pulls out the failure type, username, and IP address from the matched line.
            timestamp = line[:15]  # [RED] This grabs the first 15 characters of the line, which represent the timestamp.
            failed_logins[ip].append((user, timestamp))  # [RED] This adds the username and timestamp to the list for that IP address.

# [RED] After reading all lines, this loop goes through each IP address that had failed login attempts.
for ip, attempts in failed_logins.items():
    # [RED] This counts how many failed attempts came from this IP address.
    attempt_count = len(attempts)
    # [RED] This creates a list of usernames involved in the failed attempts.
    users = [user for user, _ in attempts]
    # [RED] This creates a list of timestamps for when the failed attempts happened.
    times = [time for _, time in attempts]
    # [RED] This prints a summary showing the IP address, number of attempts, usernames, and timestamps.
    print(f"IP: {ip}, Attempts: {attempt_count}, Users: {users}, Timestamps: {times}")
