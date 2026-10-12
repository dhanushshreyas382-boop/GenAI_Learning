#type Hits 

model_name: str = "gemini-2.0-flash"
temperature: float = 0.7 # float
max_token: int = 103 #int 
is_streaming: bool = False #boolean
content_box: str|None = None #None
print(type(model_name))


# String: immutable | string formatting


# old version 
name = "LLM"
score = 97.0
print(" hello %s"%name)
print(" hello %.1f"%score)

# string formate(py 3.6 +)
print(f"name:{name}")
print(f"score:{score}")


# Expression  inside f-string
word_limit = 200
print(f"{'over' if word_limit > 150 else 'under'} limit")
word_limit = 100
print(f"{'over' if word_limit > 150 else 'under'} limit")




data = {"Name":"xyxy","topic":"RAG"}
print(f"Name:{data["Name"]}")
print(f"Topic:{data["topic"]}")


pi = 3.14159
print(f"pi:{pi:.2f}")


# Dedugging  = 

temp = 0.7
print(f"{temp=}")

# Multi line f-string formatting

user_input = "What is Langchain?"
content_text = "Langchain is a framework for building LLM apps"
system_prompt = f"""
you are helpful AI tutor.
context provided: {content_text}
student question:{user_input}
Instruction:
-Answer based only on the context above
-It the answer is not in the context, say "I don't know"
-Keep your answers under 3 sentences
""".strip()
print(system_prompt)


#lists: ordered, mutable,  heterogenous sequesces
chat_history: list [dict] = [
    {"role":"user","content":"what is an LLM"},
    {"role":"assistant","content":"An LLM is a large language model."
    "n/w trained om vast amount of text."},

] 
first_msg = chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])
chat_history.append({"role":"user","content":"what is RAG"})
print(chat_history)
chat_history.pop(0)
print(chat_history)
for msg in chat_history:
    print(msg["role"],":",msg["content"])
chunks:list[str]=[
    "RAG stands for Retrieval Augmented Generation."
    "its combines a retreval system with a generative model to provide more accurate and contextually relevant responses."

]   
valid_chunks = [c for c in chunks if len(c.split()) > 6]
print(valid_chunks)

