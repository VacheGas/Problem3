def replace_file():
	file_path = input("input file path\n")
	replace_text = input("input replace text\n")
	replaced_text =  input("input replaced text\n")
	file = open(file_path, 'r+')
	line_file = file.readlines()
	file.seek(0)
	file.truncate()
	for line in line_file:
		new_str = line.replace(replace_text,replaced_text)
		file.write(new_str)
		print(new_str)
		print(line)
	file.close()

replace_file()