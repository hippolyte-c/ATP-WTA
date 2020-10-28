from selenium.webdriver.common.keys import Keys
from selenium import webdriver



def homme():
    driver = webdriver.Firefox()
    driver.get("https://www.lequipe.fr/Tennis/atp/epreuve-simple-messieurs/page-classement-individuel/general")

    driver.implicitly_wait(15)

    assert "ATP" in driver.title

    return driver


def femme():
    driver = webdriver.Firefox()
    driver.get("https://www.lequipe.fr/Tennis/wta/epreuve-simple-dames/page-classement-individuel/general")

    driver.implicitly_wait(15)

    assert "WTA" in driver.title

    return driver


def processus(driver):

    drapeaux = []
    pays = []

    elems = driver.find_elements_by_xpath("//img[@data-src]")

    for elem in elems:
        drapeaux.append(elem.get_attribute("data-src")[38:41])

    drapeaux = sorted(drapeaux, key=drapeaux.count,reverse=True)

    for drap in drapeaux:
        if(drap not in pays):
            pays.append(drap)

    for p in pays:
        print(p, ":", drapeaux.count(p))


def main():
    print("femmes ou hommes ? 1 ou 2")
    if(input() == 1):
        processus(femme())
    else:
        processus(homme())


if __name__ == '__main__':
    main()
