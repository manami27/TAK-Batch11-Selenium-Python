import configparser

def read_config(section, key):
    config = configparser.ConfigParser() # untuk memanggil config parser class
    config.read("./Config/config.cfg")  # Pastikan path ini sesuai
    return config.get(section, key)

def get_locator(section, key):
    config = configparser.ConfigParser() # untuk memanggil config parser class
    config.read("./Config/element.cfg")  # Pastikan path ini sesuai
    return config.get(section, key)

# Untuk logging, hanya mengecek apakah config filenya berhasil
print (read_config("Details","app_url"))
print (read_config("Details","browser"))
print (get_locator("Login","username"))