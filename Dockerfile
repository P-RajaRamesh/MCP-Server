# Use Python 3.12 slim as the base image
FROM python:3.12-slim-bookworm

# Install UV from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Create and activate a virtual environment
RUN uv venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install fastmcp httpx

# Expose any necessary ports (adjust if needed)
EXPOSE 8000

# Run the server
CMD ["uv", "run", "server.py"]