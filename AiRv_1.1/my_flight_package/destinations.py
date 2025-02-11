def get_destinations():
    return [
        "New York", "London", "Tokyo", "Paris", "Berlin", "Madrid", "Rome", "Dubai", "Sydney", "Toronto",
        "Los Angeles", "Chicago", "San Francisco", "Miami", "Moscow", "Beijing", "Shanghai", "Hong Kong", "Bangkok", "Singapore",
        "Istanbul", "Seoul", "Mumbai", "Delhi", "Cape Town", "Johannesburg", "Rio de Janeiro", "São Paulo", "Buenos Aires", "Mexico City",
        "Barcelona", "Amsterdam", "Zurich", "Vienna", "Stockholm", "Helsinki", "Oslo", "Copenhagen", "Dublin", "Lisbon"
    ]

def get_price(destination, flight_class):
    prices = {
        "New York": {"Economy": 500, "Business": 1200},
        "London": {"Economy": 400, "Business": 1000},
        "Tokyo": {"Economy": 700, "Business": 1500},
        "Paris": {"Economy": 450, "Business": 1100},
        "Berlin": {"Economy": 420, "Business": 1050},
        "Madrid": {"Economy": 380, "Business": 950},
        "Rome": {"Economy": 410, "Business": 1020},
        "Dubai": {"Economy": 600, "Business": 1400},
        "Sydney": {"Economy": 750, "Business": 1600},
        "Toronto": {"Economy": 520, "Business": 1250},
        "Los Angeles": {"Economy": 530, "Business": 1270},
        "Chicago": {"Economy": 490, "Business": 1180},
        "San Francisco": {"Economy": 540, "Business": 1290},
        "Miami": {"Economy": 470, "Business": 1130},
        "Moscow": {"Economy": 580, "Business": 1350},
        "Beijing": {"Economy": 650, "Business": 1550},
        "Shanghai": {"Economy": 670, "Business": 1570},
        "Hong Kong": {"Economy": 690, "Business": 1590},
        "Bangkok": {"Economy": 500, "Business": 1250},
        "Singapore": {"Economy": 710, "Business": 1620},
        "Istanbul": {"Economy": 480, "Business": 1200},
        "Seoul": {"Economy": 690, "Business": 1590},
        "Mumbai": {"Economy": 550, "Business": 1320},
        "Delhi": {"Economy": 570, "Business": 1380},
        "Cape Town": {"Economy": 720, "Business": 1650},
        "Johannesburg": {"Economy": 710, "Business": 1620},
        "Rio de Janeiro": {"Economy": 680, "Business": 1580},
        "São Paulo": {"Economy": 660, "Business": 1550},
        "Buenos Aires": {"Economy": 640, "Business": 1500},
        "Mexico City": {"Economy": 520, "Business": 1260},
        "Barcelona": {"Economy": 390, "Business": 980},
        "Amsterdam": {"Economy": 450, "Business": 1120},
        "Zurich": {"Economy": 460, "Business": 1150},
        "Vienna": {"Economy": 430, "Business": 1080},
        "Stockholm": {"Economy": 470, "Business": 1180},
        "Helsinki": {"Economy": 480, "Business": 1200},
        "Oslo": {"Economy": 490, "Business": 1220},
        "Copenhagen": {"Economy": 460, "Business": 1160},
        "Dublin": {"Economy": 440, "Business": 1100},
        "Lisbon": {"Economy": 420, "Business": 1050}
    }
    return prices.get(destination, {}).get(flight_class, None)
