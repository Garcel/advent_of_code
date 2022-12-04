FROM rust:latest

ENV CARGO_HOME=/usr/.cargo

WORKDIR /usr/src/aoc_rust_2022

COPY . .

RUN chmod 777 .

# Add a new user non root user
RUN adduser docker_user --disabled-password --gecos ""

# Change to non-root privilege
USER docker_user

CMD cargo test && cargo bench
