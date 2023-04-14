echo "# nytimes_search" >> README.md

# Create a virtual environment for project
 sudo apt install python3-venv
 python3 -m venv venv
 source  venv/bin/activate

# Obtain NYTimes RSS Feed
    # Fetch the given url using requests
        # pip3 install requests

    # Parse the XML with BeautifulSoup
        # pip3 install beautifulsoup4
        # pip3 install lxml


# Retrieve all titles mentioning China


# Store these titles in an Amazon RDS database
    # Use Terraform to create an RDS database
    (Example) https://adamtheautomator.com/terraform-and-aws-rds/

# Return a list of these titles via an API endpoint (ie https://.../china)
