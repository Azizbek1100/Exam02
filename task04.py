def rearrange_fish(fish):
    parts = fish.split(" ")
    surname = parts[0]
    name_and_patronym = " ".join(parts[1:])
    return f"{name_and_patronym}, {surname}"

print(rearrange_fish("Aliyev Vali G'aniyevich"))