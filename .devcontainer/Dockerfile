FROM mcr.microsoft.com/devcontainers/python:3.11

# Install build tools and ODBC support
RUN apt-get update && \
    apt-get install -y build-essential curl apt-transport-https lsb-release ca-certificates gnupg unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Azure Developer CLI (azd)
RUN curl -fsSL https://aka.ms/install-azd.sh | bash

# Install Dapr CLI
RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
