def planetary_age(seconds):

    Earth_orbital=31557600

    earth_age=seconds/Earth_orbital
    mercury_age=seconds/(Earth_orbital*0.2408467)
    venus_age=seconds/(Earth_orbital*0.61519726)
    mars_age=seconds/(Earth_orbital*1.8808158)
    jupiter_age=seconds/(Earth_orbital*11.862615)
    saturn_age=seconds/(Earth_orbital*29.447498)
    uranus_age=seconds/(Earth_orbital*84.016846)
    neptune_age=seconds/(Earth_orbital*164.79132)

    print(f"{earth_age} Earth- years old")
    print(f"{mercury_age} Mercury- years old")
    print(f"{venus_age} Venus- years old")
    print(f"{mars_age} Mars- years old")
    print(f"{jupiter_age} Jupiter- years old")
    print(f"{saturn_age} Saturn- years old")
    print(f"{uranus_age} Uranus- years old")
    print(f"{neptune_age} Neptune- years old")

planetary_age(1000000000)