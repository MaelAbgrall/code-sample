# Elixir

Elixir is based on Erlang VM (BEAM) developed in 2012 by José Valim

there is two file type in elixir:

- exs: interpreted files, good for trying / unit tests

- ex: compiled code

there is multiple way to use it in command line

- iex: python like interactive mode

- elixir to run exs

- elixirc to compile


# File structure:
```
project
  |
  |-- ebin : compiled bytecode
  |
  |-- lib : contain elixir code (.ex files)
  |
  |-- tes : tests (usually .exs files)
```
 
Elixir is divided in multiple sub projects around one bigger project (an Umbrella app)
this is micro services.
example for a ecommerce:

```
Project
  |
  |-- ui app (store front)
  |    |-- code
  |    |-- code
  |
  |-- admin app (dashboard)
  |    |-- code
  |    |-- code
  |    |-- etc
  |
  |-- api (api layer for machines to interact with)
  |    |-- etc
  |
  |-- DB (bottom level database access layer)
  |    |-- etc
  |
  |-- Inventory app (business logic related to querying and updating inventory)
  |    |-- etc
  |
  |-- uploads (handling file upload like images)
  |    |-- etc
  |
  |-- transactions (charging customers, interacting with the payment gateway)
  |    |-- etc
```

to see the dependencies of your project, you can run the following command:
```shell
mix app.tree --exclude logger --exclude elixir
```
it will show this tree, were ==> will indicate in which order the otp app will be started

```
==> uploads
uploads
==> db
db
==> checkout
checkout
└── db
==> inventory
inventory
└── db
==> transactions
transactions
└── db
==> api
api
└── inventory
    └── db
==> ui
ui
├── transactions
│   └── db
├── inventory
│   └── db
└── checkout
    └── db
==> admin
admin
├── uploads
└── inventory
    └── db
```

[source](https://www.amberbit.com/blog/2017/11/21/structuring-elixir-projects/)

[]