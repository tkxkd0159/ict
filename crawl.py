import pickle
# from selenium import webdriver

ACT = "READ"

if ACT == "WRITE":

    URL = 'https://www.ethernodes.org/countries?synced=0'

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    print(driver.title)

    node_set = dict() # country : node_counts

    total_node_element = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li')
    for item in total_node_element:
        try:
            country_name = item.find_element_by_tag_name("a").text
            temp = item.find_element_by_xpath("span[2]").text
            node_count = temp.split()[0]

            if country_name is not None:
                node_set[country_name] = node_count
        except:
            continue

    with open("eth_node.pickle", 'wb') as f:
        pickle.dump(node_set, f)


if ACT == "READ":
    with open('eth_node.pickle', 'rb') as f:
        data = pickle.load(f)

        from math import log, sqrt

        cNum = 195
        cList = [0] * cNum
        # BTC
        mu = 9754 / cNum
        cList[0] = 9754
        sigma = 0
        for i in cList:
            sigma += (i - mu) ** 2 / cNum
        sigma = sqrt(sigma)
        print(sigma)

        # ETH
        mu = 11034 / cNum
        cList[0] = 11034
        sigma = 0
        for i in cList:
            sigma += (i - mu) ** 2 / cNum
        sigma = sqrt(sigma)
        print(sigma)



