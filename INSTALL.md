# Server Setup and Initial configs for Project 8

### User and Directory Creation
```sh
sudo adduser vinushan
password: password
sudo mkdir /vinushan
sudo chown vinushan:vinushan /vinushan
cd /vinushan
sudo su - vinushan
mkdir installs
mkdir apps
mkdir installs
mkdir support
mkdir -p data/db
```

### Install Python 3.5.2
```sh
sudo yum install libssl-dev openssl
cd /vinushan/installs
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
tar xzvf Python-3.5.2.tgz
cd Python-3.5.2
./configure
make
sudo make altinstall
```

### Install Postgres 12.3
```sh
sudo adduser postgres
cd /vinushan/installs
password: password
wget https://ftp.postgresql.org/pub/source/v12.3/postgresql-12.3.tar.gz
tar zxvf postgresql-12.3.tar.gz
cd postgresql-12.3
./configure --prefix=/vinushan/installs/postgresql-12.3
make
make check
make install
cd /vinushan/data/db/
mkdir psql
sudo chown postgres:postgres psql
su - postgres
/vinushan/installs/postgresql-12.3/bin/initdb -D /vinushan/data/db/psql/
```

### Postgres 12.3 commands
Start Server
```sh
su - postgres
/vinushan/installs/postgresql-12.3/bin/postgres -D /vinushan/data/db/psql/
```
Use PSQL interface
```sh
/vinushan/installs/postgresql-12.3/bin/psql -U postgres
```