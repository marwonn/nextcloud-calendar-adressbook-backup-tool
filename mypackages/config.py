class Config:
# user nextcloud credentials
    username = "add username"
    password = "add password"

# url of the Nextcloud account
    nextcloud_url = "https://www.your-domain.com/directory-of-nextcloud/" # Subdomains work as well

# name of the different calendar; if only one calendar is in use, remove the other entries
    name_of_calendar_1 = "name-of-calendar"
    name_of_calendar_2 = "name-of-calendar"
    name_of_calendar_3 = "name-of-calendar"
    name_of_calendar_4 = "name-of-calendar"

# Wifi SSID settings; if only one wifi shall be used, remove the other entry
    wifi_ssid_1 = "name-of-wifi"
    wifi_ssid_2 = "name-of-wifi"

# do not change - start
    url_calendar_1 = f"calendars/{username}/{name_of_calendar_1}/?export"
    url_calendar_2 = f"calendars/{username}/{name_of_calendar_2}/?export"
    url_calendar_3 = f"calendars/{username}/{name_of_calendar_3}/?export"
    url_calendar_4 = f"calendars/{username}/{name_of_calendar_4}/?export"

    url_adressbook = f"addressbooks/users/{username}/contacts/?export"

# do not change - end
