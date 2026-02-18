.PHONY: requirements

requirements:
	uv pip compile pyproject.toml -o requirements.txt
