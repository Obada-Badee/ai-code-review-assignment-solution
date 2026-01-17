# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if isinstance(email, str) and "@" in email and email.count("@") == 1:
            parts = email.split("@")
            local, domain = parts[0], parts[1]
            # Check: local and domain exist, domain has a dot, no spaces
            if local and domain and "." in domain and " " not in email:
                count += 1

    return count
