build-mac: clean
	pyinstaller -F -w -n Acronyms -i resources/acronyms.icns cli.py && cd dist/ && zip -r9 acronyms acronyms.app/
.PHONY: build

clean:
	rm -rf acronyms.spec dist build __pycache__ 
.PHONY: clean
