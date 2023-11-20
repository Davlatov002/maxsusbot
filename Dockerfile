# Stage 1: Build dependencies
FROM --platform=linux/amd64 python:3.11.3 as builder

WORKDIR /app

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Stage 2: Final image
FROM --platform=linux/amd64 python:3.11.3

WORKDIR /app

# Copy virtual environment from the builder stage
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /opt/venv /opt/venv

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 10000

# Run the Python application
CMD ["python", "bot.py"]

