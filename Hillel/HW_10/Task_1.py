with open("text.txt", "r") as f_in:
  data = f_in.read()
with open("text_copy.txt", "w") as f_out:
  f_out.write(data)