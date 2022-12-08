kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{str(kata[0]).rjust(2, '0')}, ", end='')
print(f"ex_{str(kata[1]).rjust(2, '0')} : ", end='')
print(f"{kata[2]:.2f}, ", end='')
print(f"{kata[3]:.2e}, ", end='')
print(f"{kata[4]:.2e}", end='')
