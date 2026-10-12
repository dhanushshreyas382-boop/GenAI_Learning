# Function :

def build_prompt(topic:str,world_limit:int=150)->str:
    return f"Write about {topic}, with atmost {world_limit} words"


print(build_prompt("GEN_AI"))
print(build_prompt("prompt engg",world_limit=2300))


# Brushup following concepts:
## *args