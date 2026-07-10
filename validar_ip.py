def es_ip_valida(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte:
            return False
        if not parte.isdigit():
            return False
        if len(parte) > 1 and parte.startswith('0'):
            return False
        val = int(parte)
        if val < 0 or val > 255:
            return False
    return True