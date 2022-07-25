from bs4 import BeautifulSoup

with open("page_source.html") as page:
    soup = BeautifulSoup(page.read(), "html.parser")

def marathonOpportunity(tag):
    if tag.name != "section":
        return False
    
    if tag.get("class") is None:
        return False

    if "role_listing" not in tag.get("class"):
        return False
    
    if tag.find("div", class_="medical_icon") is not None:
        return False

    if tag.find("div", class_="tag--no") is not None:
        return False

    return True

opportunities = soup.find_all(marathonOpportunity)

for opp in opportunities:
    print(opp.text, end="\n\n\n")