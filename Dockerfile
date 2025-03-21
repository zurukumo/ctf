FROM --platform=linux/amd64 kalilinux/kali-rolling

RUN apt update && \
    apt upgrade -y && \
    apt install -y kali-linux-headless && \
    apt autoremove && \
    apt autoclean

RUN useradd -m -s /bin/bash kali && \
    echo "kali:kali" | chpasswd && \
    usermod -aG sudo kali

USER kali

WORKDIR /home/kali
