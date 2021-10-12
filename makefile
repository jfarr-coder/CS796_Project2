PYTHON = python3

init:
	pip install -r requirements.txt
	
clean: 
	rm src/*
	rm bin/*
