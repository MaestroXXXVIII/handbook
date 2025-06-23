# Show help message
help:
    just -l
# Install package with dependencies
install:
	uv sync
# Run pre-commit
lint:
	@pre-commit run --all-files
