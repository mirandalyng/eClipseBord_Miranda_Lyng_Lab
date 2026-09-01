# official image 
#slim version of python (to keep the size small)
FROM python:3.13-slim

#copies the folder backend into a folder we create (app)
#everython in backend folder goes into /app folder 
COPY frontend/ /app/

# Install uv 
#but adds no cache to be able to save space 
RUN pip install --no-cache-dir uv

#changes working directory to /app 
WORKDIR /app

# installs all dependencies specified in pyproject.toml without dev packages 
RUN uv sync --no-dev

# change working directory to where we have api.py 
WORKDIR /app/src/backend

# 0.0.0.0 -> accept connections from local machine and external 
CMD [ "uv" , "run", "streamlit", "run", "dashboard.py", "--server.address", "0.0.0.0"]
