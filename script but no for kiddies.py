import requests

base_url = "https://prnt.sc/"

# Open a text file for writing the successful links
output_file = open("successful_links.txt", "w")

# Loop through all possible 6-character combinations
for i in range(62 ** 6):
    # Convert the loop counter to a 6-character string using base-62 encoding
    short_url = ""
    for j in range(6):
        short_url += chr(i % 62 + (48 if i % 62 < 10 else 55))
        i //= 62
    full_url = base_url + short_url

    # Try to download the URL
    response = requests.get(full_url)

    # Check if the URL exists
    if response.status_code == 200:
        print(full_url)
        output_file.write(full_url + "\n")

    # Print the value of each try
    print(full_url, response.status_code)

# Close the output file
output_file.close()
