test:
	semgrep --validate --config=$$PWD/rules $$PWD
	semgrep --test --strict --test-ignore-todo $$PWD
