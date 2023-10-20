

EXE_OUTPUT = sierpinsky.exe
S_OUTPUT = test.s
FILES_TO_DELETE= dune-project _build/




all: do_nothing

do_nothing:
	@echo "Make need argument."
	@echo "  - dune_build\n    execute \"dune build\" command."
	@echo "  - save_in_file\n    save the execution of \"$(EXE_OUTPUT)\" in \"$(S_OUTPUT)\"."
	@echo ""
	@echo "  - clean\n    removes somes files/repo (with force)."
	@echo "  - cat\n    shows which files/repo will be removed with \"clean\"."

dune_build: temp_dune_build soft_clean
temp_dune_build:
	@dune build

save_in_file:
	./$(EXE_OUTPUT) > $(S_OUTPUT)
	@echo "Use \"spim -file $(S_OUTPUT)\" to test the program"



cat:
	@echo "FILES_TO_DELETE = $(FILES_TO_DELETE)"


soft_clean:
	@rm -rf $(FILES_TO_DELETE)
clean:
	rm -rf $(FILES_TO_DELETE) $(EXE_OUTPUT) $(S_OUTPUT)




