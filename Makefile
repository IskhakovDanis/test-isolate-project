run: add_submodule update_submodule
add_submodule:
	git submodule add https://github.com/ToghrulMirzayev/store-app.git store-app-submod
update_submodule:
	git submodule update --init --recursive