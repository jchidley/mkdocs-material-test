---
date: "2025-02-23"
title: "Database_GraphQL"
tags:
  - database
  - postgresql
  - graphql
  - rust
  - docker
---
<!-- markdownlint-disable MD025 -->
# Template
<!-- markdownlint-enable MD025 -->

## Introduction

Open source choices seem to be between MySQL, PostgresQL and SQLite. I am leaning twoards both SQLite and PostgresQL because they have vector extensions (useful for storing and searching LLM type data).

There are plenty of database offerings for rust with sqlx and libsql / Turso being my currently preferred. Whist libsql / Turso support vector stuff that variant isn't supported by SQLx at the moment.

For getting data from websites, it seems as if we have REST, GraphQL and gRPC, with REST and GraphQL being the most well used.

# Database

- [PostgreSQL SELECT](https://neon.tech/postgresql/postgresql-tutorial/postgresql-select)
- [PostgreSQL Primer for Busy People · Zaiste Programming](https://zaiste.net/posts/postgresql-primer-for-busy-people/)
- [launchbadge/sqlx: 🧰 The Rust SQL Toolkit. An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.](https://github.com/launchbadge/sqlx/tree/main)
- [Introduction - Turso](https://docs.turso.tech/sdk/introduction)
- [libSQL | 🦜️🔗 Langchain](https://js.langchain.com/docs/integrations/vectorstores/libsql/)
- [Getting unknown database public error while trying to convert PostgreSQL database backup to sqlite · Issue #8 · caiiiycuk/postgresql-to-sqlite](https://github.com/caiiiycuk/postgresql-to-sqlite/issues/8)
- [Rust SQLx basics with SQLite: super easy how to - TMS DEV](https://tms-dev-blog.com/rust-sqlx-basics-with-sqlite/#:~:text=In%20this%20tutorial%2C%20we%20will%20learn%20the%20basics,and%20do%20SQL%20operations%20on%20it%20with%20SQLx.)

# GraphQL

- [octocrab - Rust](https://docs.rs/octocrab/latest/octocrab/index.html)
- [octocrab/examples/graphql_issues.rs at main · XAMPPRocky/octocrab](https://github.com/XAMPPRocky/octocrab/blob/main/examples/graphql_issues.rs)
- [Forming calls with GraphQL - GitHub Docs](https://docs.github.com/en/graphql/guides/forming-calls-with-graphql)
- [graphql - Search](https://www.bing.com/search?pglt=163&q=graphql&cvid=9220428e9c88482f8147ab316eff528d&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAuGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEEUYPDIGCAcQRRg9MgYICBBFGDzSAQgyMDI4ajBqMagCALACAA&FORM=ANNTA1&PC=U531)
- [Thinking in Graphs | GraphQL](https://graphql.org/learn/thinking-in-graphs/)
- [graphql and rust - Search](https://www.bing.com/search?pglt=163&q=graphql+and+rust&cvid=4033d1c1c0aa4bf898f20d985a852132&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBBFGDzSAQgzMjgxajBqMagCALACAA&FORM=ANNTA1&PC=U531)
- [Quickstart - Juniper Book](https://graphql-rust.github.io/juniper/quickstart.html)
- [How to create a GraphQL server in Rust - LogRocket Blog](https://blog.logrocket.com/how-to-create-a-graphql-server-in-rust/)
- [How To Build Powerful GraphQL Servers With Rust - ExpertBeacon](https://expertbeacon.com/how-to-build-powerful-graphql-servers-with-rust/)
- [How to Build a Powerful GraphQL API with Rust](https://oliverjumpertz.com/blog/how-to-build-a-powerful-graphql-api-with-rust/)

# PostgresQL and Docker

4. **Persist data using volumes (optional)**:

   If you want to persist data beyond the lifecycle of the container, you can mount a volume to the container. Here's how you can run a PostgreSQL container with a volume:

   ```shell
   docker run --name my-postgres -e POSTGRES_PASSWORD=pass -p 5432:5432 -d -v my_pgdata:/var/lib/postgresql/data postgres:alpine 
   ```

   In this command:
   - `-v my_pgdata:/var/lib/postgresql/data`: Mounts a volume named `my_pgdata` to the PG data directory, preventing data loss when the container stops.
   - `--name my-postgres`: Names the container "my-postgres" for easy reference.
   - `-e POSTGRES_PASSWORD=pass`: Sets an environment variable to define the password for the default `postgres` user.
   - `-d`: Runs the container in detached mode, meaning it runs in the background.
   - `postgres:alpine`: Specifies the image to use.
   This maps port 5432 of your host to port 5432 of the container, allowing you to connect using a PostgreSQL client.

   If you haven't already specified a host port, find the container ID or name and inspect it:
   ```sh
   docker inspect <container_id_or_name> | grep "IPAddress"
   ```

   If you've mapped the container port to a host port, you can see the mapping with:
   ```sh
   docker port <container_id_or_name>
   ```
  
6. **Example**:

   Suppose your PostgreSQL container name is `my_postgres_container`, running on default port `5432`, with a database named `mydatabase` and a user `myuser`. Also, assume you've mapped your container's port `5432` to host port `5432`, and the password for `myuser` is `mypassword`. The command would look like:

   ```sh
   psql -h localhost -p 5432 -U myuser -d mydatabase
   ```

   ```sh
   export PGPASSWORD=pass
   ```
  
   You would be prompted for `mypassword` unless you've set it with `PGPASSWORD`.
   Alternatively, you can include the password in a `.pgpass` file for more convenience.

- [PostgreSQL with Docker Setup](https://www.baeldung.com/ops/postgresql-docker-setup)
- [Quick reference from the Docker Postgres Community for the official image](https://github.com/docker-library/docs/blob/master/postgres/README.md)
- [PostgreSQL Tutorial](https://neon.tech/postgresql/tutorial)

```sh
apk add postgresql17-client
apk add lazydocker
wget https://neon.tech/postgresqltutorial/dvdrental.zip
unzip ./dvdrental.zip 
cat << EOF > Dockerfile
FROM postgres:alpine
COPY ./dvdrental.tar /
COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
EOF
cat << EOF > init-user-db.sh
#!/bin/sh
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE DATABASE dvdrental;
EOSQL

pg_restore -U postgres -d dvdrental /dvdrental.tar
EOF
cat << EOF > .ignore
data
EOF
docker build . --tag pg
# rm -rf data
docker run -itd -e POSTGRES_PASSWORD=jcc_pass -p 5432:5432 -v ./data:/var/lib/postgresql/data --name postgresql pg
docker exec -it postgresql /bin/sh
lazydocker
PGPASSWORD=jcc_pass psql -h localhost -p 5432 -U postgres -c '\l'
export PGPASSWORD=jcc_pass 
psql -h localhost -p 5432 -U postgres -d dvdrental
docker pull dpage/pgadmin4:latest
docker run --name pgadmin-jcc -p 5051:80 -e "PGADMIN_DEFAULT_EMAIL=jack@chidley.org" -e "PGADMIN_DEFAULT_PASSWORD=jack_pass" -d dpage/pgadmin4
# need to use this address with pg4admin
docker inspect postgresql | grep "IPAddress"
```

```aichat
> convert postgres datatypes to rust sqlx
When converting PostgreSQL data types to Rust using the `sqlx` library, you'll typically map PostgreSQL types to Rust types that `sqlx` supports. Below are some common PostgreSQL data types and how they can be mapped to Rust types with `sqlx`:

1. **PostgreSQL `INTEGER`, `SMALLINT`, `BIGINT`**
   - Rust: `i32`, `i16`, `i64`

2. **PostgreSQL `SERIAL`, `SMALLSERIAL`, `BIGSERIAL`**
   - Rust: These are normally mapped as `i32`, `i16`, `i64`.

3. **PostgreSQL `REAL`, `DOUBLE PRECISION`**
   - Rust: `f32`, `f64`

4. **PostgreSQL `NUMERIC`, `DECIMAL`**
   - Rust: `Decimal` from `rust_decimal` crate or through the `sqlx::types::BigDecimal`

5. **PostgreSQL `BOOLEAN`**
   - Rust: `bool`

6. **PostgreSQL `CHAR`, `VARCHAR`, `TEXT`**
   - Rust: `String`

7. **PostgreSQL `BYTEA`**
   - Rust: `Vec<u8>`

8. **PostgreSQL `DATE`, `TIME`, `TIMESTAMP`, `TIMESTAMPTZ`**
   - Rust: `chrono::NaiveDate`, `chrono::NaiveTime`, `chrono::NaiveDateTime`, `chrono::DateTime<Utc>`

   Note: You need to include the `chrono` crate in your `Cargo.toml` to handle date and time types effectively.

9. **PostgreSQL `UUID`**
   - Rust: `uuid::Uuid`

   Note: Ensure the `uuid` crate is added to your dependencies.

10. **PostgreSQL `JSON`, `JSONB`**
    - Rust: `serde_json::Value`

    Note: Ensure the `serde` and `serde_json` crates are included in your project.

11. **PostgreSQL `ARRAY`**
    - Rust: `Vec<T>` where `T` is the Rust type equivalent of the PostgreSQL array element type.

12. **PostgreSQL `ENUM`**
    - Rust: You usually define an `enum` in Rust with `#[derive(sqlx::Type)]` to map it to/from a SQL ENUM.

To ensure proper mapping and use in your Rust application, you should include the necessary crate features and dependencies in your `Cargo.toml` file, such as `sqlx`, `chrono`, `serde`, `serde_json`, and `uuid`, if they are not already included.

Here's a sample snippet for your `Cargo.toml` file:

[dependencies]
sqlx = { version = "0.6", features = ["runtime-tokio-rustls", "postgres", "chrono", "uuid", "json"] }
chrono = { version = "0.4", features = ["serde"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
uuid = { version = "1.0", features = ["serde", "v4"] }

These mappings and configurations will help you work effectively with PostgreSQL data types in your Rust applications using `sqlx`.
```

## Links

- [PostgreSQL: Tutorials & Other Resources](https://www.postgresql.org/docs/online-resources/)
- [PostgreSQL SELECT](https://neon.tech/postgresql/postgresql-tutorial/postgresql-select)
- [PostgreSQL Primer for Busy People · Zaiste Programming](https://zaiste.net/posts/postgresql-primer-for-busy-people/)
- [dhamaniasad/awesome-postgres: A curated list of awesome PostgreSQL software, libraries, tools and resources, inspired by awesome-mysql](https://github.com/dhamaniasad/awesome-postgres)
- [postgres - Rust](https://docs.rs/postgres/latest/postgres/index.html)
- [PostgreSQL database with Rust: basic how to - TMS Developer Blog](https://tms-dev-blog.com/postgresql-database-with-rust-how-to/)
- [How to create a backend API with Rust and Postgres - LogRocket Blog](https://blog.logrocket.com/create-backend-api-with-rust-postgres/)
- [Getting Started with Diesel](https://diesel.rs/guides/getting-started)
- [launchbadge/sqlx: 🧰 The Rust SQL Toolkit. An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.](https://github.com/launchbadge/sqlx/tree/main)
- [sqlx/sqlx-cli/README.md at main · launchbadge/sqlx](https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md#enable-building-in-offline-mode-with-query)
- [allan2/dotenvy: A well-maintained fork of the dotenv crate](https://github.com/allan2/dotenvy)
- [Choosing a Rust Database Crate in 2023: Diesel, SQLx, or Tokio-Postgres?](https://rust-trends.com/posts/database-crates-diesel-sqlx-tokio-postgress/)
- [Interacting with databases in Rust using Diesel vs. SQLx - LogRocket Blog](https://blog.logrocket.com/interacting-databases-rust-diesel-vs-sqlx/)

## Links

<!-- markdownlint-disable MD034 -->
* https://example.com
<!-- markdownlint-enable MD034 -->

