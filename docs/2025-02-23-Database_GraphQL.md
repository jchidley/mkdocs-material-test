---
date: "2025-02-23"
title: "Database and GraphQL"
tags:
  - database
  - postgresql
  - graphql
  - rust
  - docker
llm_assisted: true
---
<!-- markdownlint-disable MD025 -->
# Database and GraphQL
<!-- markdownlint-enable MD025 -->

## Introduction

Open source choices seem to be between MySQL, PostgresQL and SQLite. I am leaning twoards both SQLite and PostgresQL because they have vector extensions (useful for storing and searching LLM type data).

There are plenty of database offerings for rust with sqlx and libsql / Turso being my currently preferred. Whist libsql / Turso support vector stuff that variant isn't supported by SQLx at the moment.

For getting data from websites, it seems as if we have REST, GraphQL and gRPC, with REST and GraphQL being the most well used.

# Database

- [PostgreSQL SELECT](https://neon.tech/postgresql/postgresql-tutorial/postgresql-select) — A PostgreSQL tutorial explaining the SELECT statement syntax and usage, covering how to query data from single columns, multiple columns, and all c...
- [PostgreSQL Primer for Busy People ¬∑ Zaiste Programming](https://zaiste.net/posts/postgresql-primer-for-busy-people/) — A comprehensive PostgreSQL quick-reference guide covering installation, user/role management, database operations, table manipulation, and common S...
- [launchbadge/sqlx: üß∞ The Rust SQL Toolkit. An async, pure Rust SQL crate featuring compile-time checked queries without a DSL. Supports PostgreSQL, MySQL, and SQLite.](https://github.com/launchbadge/sqlx/tree/main) — SQLx is an async, pure Rust SQL toolkit featuring compile-time checked queries without a DSL, supporting PostgreSQL, MySQL, and SQLite databases.
- [Introduction - Turso](https://docs.turso.tech/sdk/introduction) — Turso provides official SDKs for connecting to local SQLite files or remote Turso Cloud databases across multiple languages (TypeScript/JS, Rust, G...
- [libSQL | ü¶úÔ∏èüîó Langchain](https://js.langchain.com/docs/integrations/vectorstores/libsql/)
- [Getting unknown database public error while trying to convert PostgreSQL database backup to sqlite ¬∑ Issue #8 ¬∑ caiiiycuk/postgresql-to-sqlite](https://github.com/caiiiycuk/postgresql-to-sqlite/issues/8) — A user reports an 'unknown database public' error when using pg2sqlite to convert a PostgreSQL backup to SQLite, caused by the tool not handling Po...
- [Rust SQLx basics with SQLite: super easy how to - TMS DEV](https://tms-dev-blog.com/rust-sqlx-basics-with-sqlite/#:~:text=In%20this%20tutorial%2C%20we%20will%20learn%20the%20basics,and%20do%20SQL%20operations%20on%20it%20with%20SQLx.) — A tutorial covering the basics of using the SQLx crate with Rust and SQLite, including database creation, table operations, queries, and migrations.

# GraphQL

- [octocrab - Rust](https://docs.rs/octocrab/latest/octocrab/index.html) — Octocrab is a Rust library providing a modern, extensible GitHub API client with both a strongly-typed semantic API covering actions, issues, pulls...
- [octocrab/examples/graphql_issues.rs at main ¬∑ XAMPPRocky/octocrab](https://github.com/XAMPPRocky/octocrab/blob/main/examples/graphql_issues.rs) — This is a GitHub page for octocrab, a Rust library for interacting with the GitHub API, specifically showing an example file for GraphQL issues que...
- [Forming calls with GraphQL - GitHub Docs](https://docs.github.com/en/graphql/guides/forming-calls-with-graphql) — GitHub documentation explaining how to authenticate and make calls to GitHub's GraphQL API, including authentication methods (personal access token...
- [Thinking in Graphs | GraphQL](https://graphql.org/learn/thinking-in-graphs/) — This GraphQL documentation page explains how to model business domains as graphs, emphasizing the importance of creating intuitive shared naming co...
- [Quickstart - Juniper Book](https://graphql-rust.github.io/juniper/quickstart.html) — Juniper is a Rust library for building GraphQL servers using a code-first approach, allowing developers to expose Rust structs and enums as GraphQL...
- [How to create a GraphQL server in Rust - LogRocket Blog](https://blog.logrocket.com/how-to-create-a-graphql-server-in-rust/) — A tutorial on building a GraphQL server using Rust, covering setup and implementation of GraphQL APIs in the Rust programming language.
- [How To Build Powerful GraphQL Servers With Rust - ExpertBeacon](https://expertbeacon.com/how-to-build-powerful-graphql-servers-with-rust/) — A comprehensive tutorial on building GraphQL servers using Rust, covering the advantages of Rust (performance, reliability, type safety) and how to...
- [How to Build a Powerful GraphQL API with Rust](https://oliverjumpertz.com/blog/how-to-build-a-powerful-graphql-api-with-rust/) — A comprehensive tutorial on building a production-ready GraphQL API using Rust, covering project setup, web server creation with Axum, GraphQL inte...

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
   ```bash
   docker inspect my-postgres | grep "IPAddress"
   ```

   If you've mapped the container port to a host port, you can see the mapping with:
   ```bash
   docker port my-postgres
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

- [PostgreSQL with Docker Setup](https://www.baeldung.com/ops/postgresql-docker-setup) — A tutorial explaining how to set up PostgreSQL using Docker, covering pulling the official postgres image, running containers with environment vari...
- [Quick reference from the Docker Postgres Community for the official image](https://github.com/docker-library/docs/blob/master/postgres/README.md) — Official Docker documentation repository for the PostgreSQL container image, providing setup instructions and configuration guidance for running Po...
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

- [PostgreSQL: Tutorials & Other Resources](https://www.postgresql.org/docs/online-resources/) — PostgreSQL's official tutorials and resources page listing external learning materials including encyclopedias, tutorials, interactive exercises, a...
- [dhamaniasad/awesome-postgres: A curated list of awesome PostgreSQL software, libraries, tools and resources, inspired by awesome-mysql](https://github.com/dhamaniasad/awesome-postgres) — A curated GitHub repository listing PostgreSQL software, libraries, tools and resources organized into categories including high-availability, back...
- [postgres - Rust](https://docs.rs/postgres/latest/postgres/index.html)
- [PostgreSQL database with Rust: basic how to - TMS Developer Blog](https://tms-dev-blog.com/postgresql-database-with-rust-how-to/) — A tutorial demonstrating how to connect to and manage a PostgreSQL database using Rust, covering Docker setup, database connections, table creation...
- [How to create a backend API with Rust and Postgres - LogRocket Blog](https://blog.logrocket.com/create-backend-api-with-rust-postgres/) — A tutorial demonstrating how to build a backend API using Rust with the Actix-web framework and PostgreSQL database via Diesel ORM, though commente...
- [Getting Started with Diesel](https://diesel.rs/guides/getting-started) — A tutorial guide for setting up Diesel, a Rust ORM and query builder, covering project initialization, CLI installation, database configuration for...
- [sqlx/sqlx-cli/README.md at main ¬∑ launchbadge/sqlx](https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md#enable-building-in-offline-mode-with-query)
- [allan2/dotenvy: A well-maintained fork of the dotenv crate](https://github.com/allan2/dotenvy) — dotenvy is a well-maintained Rust crate fork of dotenv that loads environment variables from .env files, offering both environment-modifying and no...
- [Choosing a Rust Database Crate in 2023: Diesel, SQLx, or Tokio-Postgres?](https://rust-trends.com/posts/database-crates-diesel-sqlx-tokio-postgress/) — A comparison guide for Rust developers choosing between three database crates—Diesel (ORM), SQLx (async SQL toolkit with compile-time verification)...
- [Interacting with databases in Rust using Diesel vs. SQLx - LogRocket Blog](https://blog.logrocket.com/interacting-databases-rust-diesel-vs-sqlx/) — This article compares Diesel and SQLx, two popular Rust libraries for database interactions, helping developers choose between an ORM-style approac...
